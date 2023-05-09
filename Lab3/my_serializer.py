import re
import inspect
import types
from canstants import CODE_ATTRIBUTES,BASIC_COLLECTION,DEFAULT_TYPES

def my_serializer(objet):
    serial = dict()
    obj_type = type(objet)

    def return_basic_type():
        return re.search(r"\'(\w+)\'"), str(obj_type)[1]#не берем скобки, берем слово
    if isinstance(objet,(str, int, bool, float, complex)):
        serial["TYPE"] = return_basic_type()
        serial["VALUE"] = objet

    elif (isinstance(objet,(tuple, list, set, frozenset, bytes, bytearray))):
        serial["TYPE"] = return_basic_type()
        serial["VALUE"] = [my_serializer(serialised_objet) for serialised_objet in objet]

    elif isinstance(objet, dict):
        serial["TYPE"] = return_basic_type()
        serial["VALUE"] = [my_serializer([key,val]) for (key,val) in objet.items()]

    elif inspect.isfunction(objet):
        serial["TYPE"] = "function"
        serial["VALUE"] = serialize_function(objet)

    elif inspect.iscode(objet):
        serial["TYPE"] = "code"
        arguments = dict()
        for key,val in inspect.getmembers(objet):
            if key in CODE_ATTRIBUTES : arguments[key]=my_serializer(val)
        serial["VALUE"] = arguments
    elif isinstance(objet, types.CellType):
        serial["TYPE"] = "cell"
        serial["VALUE"] = my_serializer(objet.cell_contents)

    elif inspect.isclass(objet):
        serial["TYPE"] = "class"
        serial["VALUE"] = serialize_class(objet)#################

    elif not objet:
        serial["TYPE"] = "NoneType"
        serial["VALUE"] = "Null"

    else:
        serial["TYPE"] = "object"
        serial["VALUE"] = serialize_object(objet)##################

def serialize_function(function, clas = None):
    if not inspect.isfunction(function):
        return

    serialize_value_function = dict()

    serialize_value_function["__name__"] = function.__name__
    serialize_value_function["__globals"] =  return_globals(function, clas)
    serialize_value_function["__closure__"] = my_serializer(function.__closure__) if function.__closure__ else my_serializer(tuple())

    arguments = dict()

    for key,val in inspect.getmembers(function.__code__):
        if key in CODE_ATTRIBUTES : arguments[key]=my_serializer(val)

    serialize_value_function["__code__"] = arguments

    return serialize_value_function

def return_globals(function, clas = None):
    globs = dict()

    for glob_variable in function.__code__.co_names:# проверка на подключаемые модули MAth. sin
        if glob_variable in function.__globals__:
            if isinstance(function.__globals__[glob_variable], types.ModuleType):
                globs["module "+glob_variable] = my_serializer(function.__globals__[glob_variable].__name__)

            elif inspect.isclass(function.__globals__[glob_variable]):#функция с родителем но если использует класс не родительский
                if (clas and function.__globals__[glob_variable]!=clas) or not clas:
                    globs[glob_variable] = my_serializer(function.__globals__[glob_variable])

            elif glob_variable!=function.__code__.co_names:#для рекурсии
                globs[glob_variable] = my_serializer(function.__globals__[glob_variable])

            else:
                globs[glob_variable] = my_serializer(function.__name__)

            return globs

def serialize_class(objet):
    serial = dict()

    serial["__name__"] = my_serializer(objet.__name__)

    for mem in objet.__dict__:
        member = [mem, objet.__dict__[mem]]#пара ключ значение

        if (member[0] in ("__name__", "__base__",
                          "__basicsize__", "__dictoffset__", "__class__") or
                type(member[1]) in (
                        types.WrapperDescriptorType,
                        types.MethodDescriptorType,
                        types.BuiltinFunctionType,
                        types.GetSetDescriptorType,
                        types.MappingProxyType
                )):
            continue
        if isinstance(objet.__dict__[member[0]], staticmethod):
            serial[member[0]] = {"type" : "staticmethod",
                              "value" : {"type" : "function",
                                         "value": serialize_function(member[1].__func__, objet)}}
        elif (isinstance(objet.__dict__[member[0]], classmethod)):
            serial[member[0]] = {"type" : "classmethod",
                              "value" : {"type" : "function",
                                         "value": serialize_function(member[1].__func__, objet)}}
        elif (inspect.ismethod(member[1])):
            serial[member[0]] = serialize_function(member[1].__func__, objet)

        elif inspect.isfunction(member[1]):
            serial[member[0]] = {"type" : "function", "value": serialize_function(member[1], objet)}

        else:
            serial[member[0]] = my_serializer(member[1])

    serial["__bases__"] ={"type" : "tuple", "value" :
                            [my_serializer(base) for base in objet.__bases__ if base != object]}
    return serial


def serialize_object(objet):#для чего это пример
    serial = dict()
    serial["__class__"] = my_serializer(objet._class__)
    members = dict()
    for key, val in inspect.getmembers(objet):
        if key.startswith("__") or inspect.isfunction(val) or inspect.ismethod(val):
            continue
        members[key]=my_serializer(val)

    serial["__members__"]=members
    return serial

def my_deserializer(objet : dict):

    if objet["TYPE"] in DEFAULT_TYPES:
        return return_type(objet["TYPE"], objet["VALUE"])

    elif objet["TYPE"] in BASIC_COLLECTION:
        return return_collection(objet["TYPE"], objet["VALUE"])

    elif objet["TYPE"] =="dict":
        return dict(return_collection("list", objet["VALUE"]))

    elif objet["TYPE"] =="function":
        return deserialize_function(objet["VALUE"])

    elif objet["TYPE"] == "code":
        code = objet["VALUE"]
        return types.CodeType(my_deserializer(code["co_argcount"]),
                              my_deserializer(code["co_posonlyargcount"]),
                              my_deserializer(code["co_kwonlyargcount"]),
                              my_deserializer(code["co_nlocals"]),
                              my_deserializer(code["co_stacksize"]),
                              my_deserializer(code["co_flags"]),
                              my_deserializer(code["co_code"]),
                              my_deserializer(code["co_consts"]),
                              my_deserializer(code["co_names"]),
                              my_deserializer(code["co_varnames"]),
                              my_deserializer(code["co_filename"]),
                              my_deserializer(code["co_name"]),
                              #my_deserializer(code["co_qualname"]),
                              my_deserializer(code["co_firstlineno"]),
                              my_deserializer(code["co_lnotab"]),
                              #my_deserializer(code["co_exeptiontable"]),
                              my_deserializer(code["co_freevars"]),
                              my_deserializer(code["co_cellvars"]))

    elif objet["TYPE"] =="cell":
        return types.CellType(my_deserializer(objet["VALUE"]))

    elif objet["TYPE"] =="class":
        return deserialize_class(objet["VALUE"])

    elif objet["TYPE"] =="staticmethod":
        return staticmethod(my_deserializer(objet["VALUE"]))

    elif objet["TYPE"] =="staticmethod":
        return classmethod(my_deserializer(objet["VALUE"]))

    elif objet["TYPE"] =="object":
        return deserialize_object(objet["VALUE"])



def return_type(_type, objet):#почеу не нравится последняя
    if (_type == "int"):
        return int(objet)
    elif (_type == "float"):
        return float(objet)
    elif (_type == "complex"):
        return complex(objet)
    elif (_type == "str"):
        return str(objet)
    elif (_type == "bool"):
        return bool(objet)

def return_collection(_type, objet):
    if _type == "list":
        return list(my_deserializer(o) for o in objet)
    elif _type == "tuple":
        return tuple(my_deserializer(o) for o in objet)
    elif _type == "set":
        return set(my_deserializer(o) for o in objet)
    elif _type == "frozenset":
        return frozenset(my_deserializer(o) for o in objet)
    elif _type == "bytearray":
        return bytearray(my_deserializer(o) for o in objet)
    elif _type == "bytes":
        return bytes(my_deserializer(o) for o in objet)

def deserialize_function(objet):##########################
    code = objet["__code__"]
    globs = objet["__globals__"]
    closures = objet["__closure__"]
    res_globs = dict()

    for key in objet["__globals__"]:
        if ("module" in key):
            res_globs[globs[key]["VALUE"]] = __import__(globs[key]["VALUE"])

        elif (globs[key] != objet["__name__"]):
            res_globs[key] = my_serializer(globs[key])

    closure = tuple(my_deserializer(closures))

    codeType = types.CodeType(my_deserializer(code["co_argcount"]),
                              my_deserializer(code["co_posonlyargcount"]),
                              my_deserializer(code["co_kwonlyargcount"]),
                              my_deserializer(code["co_nlocals"]),
                              my_deserializer(code["co_stacksize"]),
                              my_deserializer(code["co_flags"]),
                              my_deserializer(code["co_code"]),
                              my_deserializer(code["co_consts"]),
                              my_deserializer(code["co_names"]),
                              my_deserializer(code["co_varnames"]),
                              my_deserializer(code["co_filename"]),
                              my_deserializer(code["co_name"]),
                              # my_deserializer(code["co_qualname"]),
                              my_deserializer(code["co_firstlineno"]),
                              my_deserializer(code["co_lnotab"]),
                              # my_deserializer(code["co_exeptiontable"]),
                              my_deserializer(code["co_freevars"]),
                              my_deserializer(code["co_cellvars"]))

    funcRes = types.FunctionType(code=codeType, globals=res_globs, closure=closure)
    funcRes.__globals__.update({funcRes.__name__: funcRes})

    return funcRes

def deserialize_class(objet):# почему не нравится 266

    bases = my_serializer(objet["__bases__"])
    members = dict()

    for member, value in objet.items():
        members[member] = my_deserializer(value)

    clas = type(my_deserializer(objet["__name__"]), bases, members)

    # чтоб не было бесконечной рекурсии метода и класса
    for k, member in members.items():
        if (inspect.isfunction(member)):
            member.__globals__.update({clas.__name__: clas})
        elif isinstance(member, (staticmethod, classmethod)):
            member.__func__.__globals__.update({clas.__name__: clas})
    return clas


def deserialize_object(obj):
    clas = my_deserializer(obj["__class__"])
    members = dict()

    for k, v in obj["__members__"].items():
        members[k] = my_deserializer(v)

    res = object.__new__(clas)
    res.__dict__ = members

    return res








