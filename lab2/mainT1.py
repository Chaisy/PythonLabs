from functions import counting, non_declar, Len_sent, Len_word, Top_n_grams, ngrams_menu

def mainT1():
    with open('text.txt') as file: text = file.read()

    print(text)

    print(f"Amount sentenses:  {counting(text)}")

    print(f"non declarative:  {non_declar(text)}")

    print(f"average length of the sentence in characters (words count only):  {Len_sent(text)}")

    print(f"average length of the word in the text in characters:  {Len_word(text)}")


    print(f"Ngrams:  {ngrams_menu(text)}")



