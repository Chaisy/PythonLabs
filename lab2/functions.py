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


