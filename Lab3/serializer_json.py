import DariasSerializer153501.canstants
from DariasSerializer153501 import canstants
from DariasSerializer153501.my_serializer import my_deserializer, my_serializer
import regex


class serialiser_JSON:
    def dumps(self, objet):
        return self.convert_t_str(my_serializer(objet))

    def dump(self, objet, file):
        file.write(self.dumps(objet))

    def convert_t_str(self, val):
        if isinstance(val, str):
            return '"' + val.replace("\\", "\\\\").replace('"', "\"").replace("'", "\'") + '"'

        elif isinstance(val, (int, float, complex)):
            return str(val)

        elif isinstance(val, bool):
            if val:
                return "true"
            else:
                return "false"

        elif isinstance(val, list):
            return "[" + ", ".join([self.convert_t_str(value) for value in val]) + "]"

        if isinstance(val, dict):
            return "{" + ", ".join([f"{self.convert_t_str(key)}: {self.convert_t_str(v)}" for key, v in val.items()]) + "}"

    def loads(self,string):
        return my_deserializer(self.convert_to_expression(string))

    def load(self, file):
        return self.loads(file.read())

    def convert_to_expression(self, string):######################
        string = string.strip() #уберет пробелы на конце и начале

        copya = regex.fullmatch(canstants.INT_REGULAR, string)
        if copya:
            return int(copya.group(0))#полное совпадение

        copya = regex.fullmatch(canstants.FLOAT_REGULAR, string)
        if (copya):
            return float(copya.group(0))

        copya = regex.fullmatch(canstants.BOOL_REGULAR, string)
        if copya:
            return copya.group(0)=="true"

        copya = regex.fullmatch(canstants.STR_REGULAR, string)
        if copya:
            res = copya.group(0)
            res = res.replace("\\\\","\\").\
                replace(r"\"", '"').\
                replace(r"\'", "'")
            return res[1:-1]

        copya = regex.fullmatch(canstants.NONE_REGULAR, string)
        if (copya):
            return None

        if string.startswith("[") and string.endswith("]"):
            string = string[1:-1]
            all_sovpad = regex.findall(canstants.VALUE_REGULAR, string)
            return [self.convert_to_expression(match[0]) for match in all_sovpad]

        if (string.startswith("{") and string.endswith("}")):
            string = string[1:-1]
            all_sovpad = regex.findall(canstants.VALUE_REGULAR, string)
            return {self.convert_to_expression(all_sovpad[i][0]): self.convert_to_expression(all_sovpad[i + 1][0])
                    for i in range(0, len(all_sovpad), 2)}





