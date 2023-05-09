from my_serializer import my_deserializer, my_serializer
import regex


class serialiser_XML:
    def dumps(self, objet):
        return self.convert_to_str(my_serializer(objet))

    def dump(self, objet, file):
        file.write(self.dumps(objet))

    def convert_to_str(self, obj):
        if isinstance(obj, (int, float, bool, complex)):
            return self._create_elem(type(obj).__name__, str(obj))

        if (isinstance(obj, str)):
            value = self._change_symbol(obj)
            return self._create_elem("str", value)

        if (isinstance(obj, list)):
            value = "".join([self.convert_to_str(v) for v in obj])
            return self._create_elem("list", value)

        if (isinstance(obj, dict)):
            value = "".join([f"{self.convert_to_str(k)}\
                                {self.convert_to_str(v)}" \
                             for k, v in obj.items()])
            return self._create_elem("dict", value)

        if (not obj):
            return self._create_elem("NoneType", "None")