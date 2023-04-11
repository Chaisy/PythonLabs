import re
from constants import constantes, delete_3_points, delete_random_3_points, double_signs, end_sentenses, \
    end_sentenses_sign, start_sentenses, start_sentenses_sign, full_sentenses, full_sentenses_sign, \
    find_sign, find_non_declare, check_numbers, signs, name_check
from container import Container,UsersAndContainers
from constants import commands


def correctText(text):

    w = re.sub(delete_3_points, '.', text) # delete ... in sentenses AAAAAAAAAAAAAAAAAA
    w = re.sub(delete_random_3_points, '', w) # delete ...
    w = re.sub(double_signs, '?', w) #delete other !??!

    w = re.sub(end_sentenses, ' END.', w)  # change end of sentenses to END.
    w = re.sub(end_sentenses_sign, ' END?', w)  # change end of sentenses to END.
    w = re.sub(start_sentenses, 'START,', w)  # change start of sentenses to START,
    w = re.sub(start_sentenses_sign, 'START', w)  # change start of sentenses to START,
    w = re.sub(full_sentenses, "FULL.", w)
    w = re.sub(full_sentenses_sign, "FULL?", w)

    for i in constantes:
        w = re.sub(i,re.sub(r"\\\.","",i),w)
    print(w)
    return w


def counting(text):
    return len(re.findall(find_sign, correctText(text)))
def non_declar(text):
     return len(re.findall(find_non_declare, correctText(text)))


def show_only_words(text):

     t = re.sub(check_numbers, " ", text)  # check for numbers int, double, with e
     t = re.sub(signs, " ", t)
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


def ngrams_menu(text):
    while True:
        inp = input(f"Do you want enter your personal K and N? Please, enter \"y\" or \"n\": \n")

        if inp != commands.YES and inp != commands.NO:
            print("You enter something wrong, try again\n")
        elif inp == commands.YES:
            N = getNumber(input("Enter a number: "))
            K = getNumber(input("Enter a number: "))
            n_grams_list = Top_n_grams(text, N, K)
            print(f"top-{K} :  {N}-grams in the text:")
            for n_gram in n_grams_list:
                print(n_gram)
            break
        else:
            N = 4
            K = 10
            n_grams_list = Top_n_grams(text, N, K)
            print(f"top-{K} repeated {N}-grams in the text:")
            for n_gram in n_grams_list:
                print(n_gram)
            break

def Top_n_grams(text, n, k):

    text = text.lower()
    words = show_only_words(text)
    n_grams = dict()
    # here we get our ngram
    for i in range(len(words) - n + 1):
        ngram = " ".join(words[i: i + n])
        # for situation, if ngram were founded earlier
        if (i in n_grams):
            n_grams[ngram] += 1
        else:
            n_grams[ngram] = 1

    return sorted(n_grams.items(), key=lambda x: x[1], reverse=True)[:k]


def ContainersStart():
    input_str = " "
    username_conteiners = UsersAndContainers()
    active_container = Container()

    print("Please enter your name: ")
    active_user = username_check(input())
    username_conteiners.add_user(active_user)
    active_container.load(username_conteiners.find_user(active_user))

    while (input_str != commands.EXIT):
        input_str = input()
        opertion = input_str.split()[0]
        if (len(opertion) + 1 < len(input_str)):
            text = input_str[len(opertion) + 1::]
        else:
            text = " "

        if (opertion == commands.ADD):
            active_container.add(text)
        elif (opertion == commands.REMOVE):
            active_container.remove(text)
        elif (opertion == commands.FIND):
            print(active_container.find(text))
        elif (opertion == commands.LIST):
            active_container.list()
        elif (opertion == commands.GREP):
            print(active_container.grep(text))
        elif (opertion == commands.HELP_COMMANDS):
            print(commands.HELP_COMMANDS)
        elif (opertion == commands.LOAD):
            active_container.load(commands.PATH + "Containers/" + text + "\'sContainer.txt")
        elif (opertion == commands.SWITCH):
            print(f"Enter \'y\' if you want to save changes or \'n\' if you dont want: ")
            if (save_changes(input())):
                active_container.save(username_conteiners.find_user(active_user))
            print(f"Please enter your name: ")
            active_user = username_check(input())
            username_conteiners.add_user(active_user)
            del active_container
            active_container = Container()
            active_container.load(username_conteiners.find_user(active_user))
        elif (opertion == commands.EXIT):
            print(f"Enter \'y\' if you want to save changes or \'n\' if you dont want: ")
            if (save_changes(input())):
                active_container.save(username_conteiners.find_user(active_user))
        print(f"***\n")


def username_check(name: str):
    while (re.findall(name_check, name)):
        print(f"Something happend with input. Please, enter again:")
        name = input()
    return name


def save_changes(chs: str):
    while (True):
        if (chs == commands.YES): return True
        if (chs == commands.NO):  return False
        print(f"You wrote something wrong. Try again:")
        chs = input()

def getNumber (a):
    while True:
        if a.isdigit() and a>=0 : return a
        else: return getNumber(input("You should enter positive number: "))
