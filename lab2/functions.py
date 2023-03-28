import re
from  constants  import *
from container import Container,UsersAndContainers


def correctText(text):

    w = re.sub(r'\.{3,}\S', '.', text) # delete ... in sentenses AAAAAAAAAAAAAAAAAA
    w = re.sub(r'[\n\s{2,}]\.', '', w) # delete ...
    w = re.sub(r'[\?\!|.]{2,}', '?', w) #delete other !??!

    w = re.sub(r', \"[\w\d\s,\'!?.]*[.]\"', ' END.', w)  # change end of sentenses to END.
    w = re.sub(r', \"[\w\d\s,\'?!.]*[?!]\"', ' END?', w)  # change end of sentenses to END.
    w = re.sub(r'\"[\w\d\s,\']*\",', 'START,', w)  # change start of sentenses to START,
    w = re.sub(r'\"[\w\d\s,\'!?.]*\",', 'START', w)  # change start of sentenses to START,
    w = re.sub(r'\"[\w\d\s,\'!?.]*[.]\"', "FULL.", w)
    w = re.sub(r'\"[\w\d\s,\'!?.]*[?!]\"', "FULL?", w)

    for i in constantes:
        w = re.sub(i,re.sub(r"\\\.","",i),w)
    print(w)
    return w


def counting(text):
    return len(re.findall(r"[\.!?]", correctText(text)))
def non_declar(text):
     return len(re.findall(r"[!?]", correctText(text)))


def show_only_words(text):

     t = re.sub(r"[+-]{0,1}(\d+)*[.,]{0,1}((\d+[eE][+-]{0,1}\d+[\s|\d])|\d+)", " ", text)  # проверка на числа с e, дробные, целые
     t = re.sub(r"[?\.!',\"\^\*\/\#\+\-\=\(\)]", " ", t)
     # print(t)
     return t.split()


def Len_sent(text):

    countSent = counting(text)
    allSymbols = 0

    for i in show_only_words(text):
        allSymbols += len(i)

    return round(allSymbols / countSent)


def Len_word(text):

    allSymbols = show_only_words(text)
    symbolsInWorld = 0

    for i in allSymbols:
        symbolsInWorld += len(i)

    return round(symbolsInWorld / len(allSymbols))


def Top_n_grams(text, n=4):

    text = text.lower()
    words = show_only_words(text)
    n_grams = dict()

    for i in range(len(words) - n + 1):
        ngram = " ".join(words[i: i + n])

        if (i in n_grams):
            n_grams[ngram] += 1
        else:
            n_grams[ngram] = 1

    return sorted(n_grams.items(), key=lambda x: x[1], reverse=True)


def ContainersStart():
    input_str = " "
    username_conteiners = UsersAndContainers()
    active_container = Container()

    print("Please enter your name: ")
    active_user = username_check(input())
    username_conteiners.add_user(active_user)
    active_container.load(username_conteiners.find_user(active_user))

    while (input_str != EXIT):
        input_str = input()
        opertion = input_str.split()[0]
        if (len(opertion) + 1 < len(input_str)):
            text = input_str[len(opertion) + 1::]
        else:
            text = " "

        if (opertion == ADD):
            active_container.add(text)
        elif (opertion == REMOVE):
            active_container.remove(text)
        elif (opertion == FIND):
            print(active_container.find(text))
        elif (opertion == LIST):
            active_container.list()
        elif (opertion == GREP):
            print(active_container.grep(text))
        elif (opertion == HELP_INFO):
            print(HELP_COMMANDS)
        elif (opertion == LOAD):
            active_container.load(PATH + "Containers/" + text + "\'sContainer.txt")
        elif (opertion == SWITCH):
            print(f"Enter \'y\' if you want to save changes or \'n\' if you dont want: ")
            if (save_changes(input())):
                active_container.save(username_conteiners.find_user(active_user))
            print(f"Please enter your name: ")
            active_user = username_check(input())
            username_conteiners.add_user(active_user)
            del active_container
            active_container = Container()
            active_container.load(username_conteiners.find_user(active_user))
        elif (opertion == EXIT):
            print(f"Enter \'y\' if you want to save changes or \'n\' if you dont want: ")
            if (save_changes(input())):
                active_container.save(username_conteiners.find_user(active_user))
        print(f"***\n")


def username_check(name: str):
    while (re.findall(r"[?!#$\"/\\\s]+", name)):
        print(f"Something happend with input. Please, enter again:")
        name = input()
    return name


def save_changes(chs: str):
    while (True):
        if (chs == YES): return True
        if (chs == NO):  return False
        print(f"You wrote something wrong. Try again:")
        chs = input()
