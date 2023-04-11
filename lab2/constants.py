from enum import Enum
constantes = (
        r'Mr\.', r'Mrs\.', r'Dr\.', r'St\.',  r'Lt\.', r'sq\.', r'Rep\.', r'B\.A\.', r'Ph\.D\.',
        r'etc\.', r'exp\.',  r'ex\.', r'e\.g\.', r'vs\.',  r'P\.S\.', r'ft\.', r'kg\.', r'lbs\.', r'in\.', r'sec\.', r'g\.', r'cm\.',
        r'Jan\.', r'Feb\.', r'Mar\.', r'Apr\.', r'Jn\.', r'Jl\.', r'Aug\.', r'Sep\.', r'Oct\.', r'Now\.', r'Dec\.',
        r'Mon\.', r'Tue\.', r'Wed\.', r'Th\.', r'Fr\.', r'Sat\.', r'Sn\.', r'p\.m\.')
PATH = "/home/dari/PycharmProjects/Lab2IGI/Filiki/"

ADD = "add"
REMOVE = "remove"
FIND = "find"
GREP = "grep"
LIST = "list"
LOAD = "load"
SWITCH = "switch"
EXIT = "exit"
HELP="help"
YES = "y"
NO = "n"
HELP_COMMANDS = "add *smth* :  add new text in container\n\
remove *smth* : delete text from container\n\
find *smth* : if we have element in container we will show it\n\
list : show all text from container\n\
grep <regular> : check the text by regex\n\
switch : switches to another person\n\
load : load container from file\n"


#REGULARS
#delete ... in sentenses
delete_3_points = r'\.{3,}\S'
delete_random_3_points = r'[\n\s{2,}]\.'
double_signs = r'[\?\!|.]{2,}'
end_sentenses = r', \"[\w\d\s,\'!?.]*[.]\"'
end_sentenses_sign = r', \"[\w\d\s,\'?!.]*[?!]\"'
start_sentenses = r'\"[\w\d\s,\']*\",'
start_sentenses_sign = r'\"[\w\d\s,\'!?.]*\",'
full_sentenses = r'\"[\w\d\s,\'!?.]*[.]\"'
full_sentenses_sign = r'\"[\w\d\s,\'!?.]*[?!]\"'

find_sign = r"[\.!?]"
find_non_declare = r"[!?]"
check_numbers = r"[+-]{0,1}(\d+)*[.,]{0,1}((\d+[eE][+-]{0,1}\d+[\s|\d])|\d+)"
signs = r"[?\.!',\"\^\*\/\#\+\-\=\(\)]"
name_check = r"[?!#$\"/\\\s]+"