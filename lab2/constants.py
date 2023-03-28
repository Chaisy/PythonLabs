K=10
constantes = (
        r'Mr\.', r'Mrs\.', r'Dr\.', r'St\.',  r'Lt\.', r'sq\.', r'Rep\.', r'B\.A\.', r'Ph\.D\.',
        r'etc\.', r'exp\.',  r'ex\.', r'e\.g\.', r'vs\.',  r'P\.S\.', r'ft\.', r'kg\.', r'lbs\.', r'in\.', r'sec\.', r'g\.', r'cm\.',
        r'Jan\.', r'Feb\.', r'Mar\.', r'Apr\.', r'Jn\.', r'Jl\.', r'Aug\.', r'Sep\.', r'Oct\.', r'Now\.', r'Dec\.',
        r'Mon\.', r'Tue\.', r'Wed\.', r'Th\.', r'Fr\.', r'Sat\.', r'Sn\.', r'p\.m\.')


ADD = "add"
REMOVE = "remove"
FIND = "find"
GREP = "grep"
LIST = "list"
LOAD = "load"
SWITCH = "switch"
HELP = "help"
EXIT = "exit"
PATH = "/home/dari/PycharmProjects/Lab2IGI/Filiki/"
YES = "y"
NO = "n"
HELP_INFO = "help"
HELP_COMMANDS = "add *smth* :  add new text in container\n\
remove *smth* : delete text from container\n\
find *smth* : if we have element in container we will show it\n\
list : show all text from container\n\
grep <regular> : check the text by regex\n\
switch : switches to another person\n\
load : load container from file\n"