import re
from constants import constantes, delete_3_points, delete_random_3_points, double_signs, end_sentenses, \
    end_sentenses_sign, start_sentenses, start_sentenses_sign, full_sentenses, full_sentenses_sign, \
    find_sign, find_non_declare, check_numbers, signs, name_check
from container import Container,UsersAndContainers
from constants import ADD,NO,YES,LIST,LOAD,HELP_COMMANDS,HELP, PATH, EXIT, REMOVE, SWITCH, GREP, FIND


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
        # print(YES)
        if inp != "y" and inp != "n":
            print("You enter something wrong, try again\n")
        elif inp == "y":
            N = getNumber(input("Enter a number: "))
            K = getNumber(input("Enter a number: "))
            n_grams_list = Top_n_grams(text, int(N), int(K))
            print(f"top-{K} :  {N}-grams in the text:")
            for n_gram in n_grams_list:
                print(n_gram)
            break
        else:
            N = 4
            K = 10
            n_grams_list = Top_n_grams(text, int(N), int(K))
            print(f"top-{K} repeated {N}-grams in the text:")
            for n_gram in n_grams_list:
                print(n_gram)
            break

def Top_n_grams(text, n, k):

    text = text.lower()

    text = re.sub(r':', ' ', text)
    words = show_only_words(text)
    print(words)
    n_grams = dict()
    print(n_grams)
    # here we get our ngram
    for i in range(len(words) - n + 1):
        ngram = " ".join(words[i: i + n])
        # for situation, if ngram were founded earlier
        if (ngram in n_grams):
            n_grams[ngram] += 1
        else:
            n_grams[ngram] = 1
    print(n_grams)

    return sorted(n_grams.items(), key=lambda x: x[1], reverse=True)[:k]


def ContainersStart():
    input_str = " "
    username_conteiners = UsersAndContainers()
    active_container = Container()

    print("Please enter your name: ")
    active_user = username_check(input())
    username_conteiners.add_user(active_user)

    print("Do you want load?")
    if(save_changes(input())):
        active_container.load(username_conteiners.find_user(active_user))


    while (input_str != EXIT):
        input_str = input()
        if (input_str.isspace() or input_str == ""):
            print("Incorrect input.Try again: ")
            continue
        opertion = input_str.split()[0]
        if (len(opertion) + 1 < len(input_str)):
            text = input_str[len(opertion) + 1::]
        else:
            text = " "

        if (opertion == ADD):
            active_container.add(text)
        elif (opertion == REMOVE):
            active_container.remove(text)
        elif opertion == FIND:
            print(active_container.find(text))
        elif (opertion == LIST):
            active_container.list()
        elif (opertion == GREP):
            print(active_container.grep(text))
        elif (opertion == HELP):
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
        print(f"&&&***&&&\n")


def username_check(name: str):
    while (re.findall(name_check, name)):
        print(f"Something happend with input. Please, enter again:")
        name = input()
    return name


def save_changes(chs: str):
    while (True):
        if (chs == YES): return True
        if (chs == NO):  return False
        print(f"You wrote something wrong. Try again:")
        chs = input()

def getNumber (a):
    while True:
        if a.isdigit() and int(a)>=0:
            return a
        else:
            return getNumber(input("You should enter positive number: "))
