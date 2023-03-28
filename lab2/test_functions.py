from unittest import TestCase

from functions import correctText, counting, show_only_words,  non_declar, Len_sent, Len_word, Top_n_grams

class Test_correct_text1(TestCase):
    def test_correct_text(self):

            text = "she dont want, \"no!\""
            assert correctText(text) == "she dont want END?"

class Test_correct_text2(TestCase):
    def test_correct_text(self):
        text = "\"of cource\", my mum."
        print(correctText(text))
        assert correctText(text) == "START, my mum."


class Test_correct_text3(TestCase):
    def test_correct_text(self):
        text = "\"Faster!\", shouted one step-sister."
        assert correctText(text) == "START? shouted one step-sister."

class Test_correct_text4(TestCase):
    def test_correct_text(self):
        text = "but i dont want...........?"
        print(correctText(text))
        assert correctText(text) == "but i dont want?"

class Test_correct_text5(TestCase):
    def test_correct_text(self):
        text = "but, what about me?!?!?      ..."
        print(correctText(text))
        assert correctText(text) == "but, what about me?     "


class Test_counting(TestCase):
    def test_counting1(self):
        text = "car. so many?!?!?! how did you can...?"
        print(counting(text))
        assert counting(text) == 3

class Test_counting(TestCase):
    def test_counting2(self):
        text = "At Cinderella’s house, she now had extra work to do.  She had to make two brand-new gowns for her step-sisters. " \
               "\"Faster!\", shouted one step-sister."
        print(counting(text))
        assert counting(text) == 3

class Test_counting(TestCase):
    def test_counting3(self):
        text = "\"Faster!\", shouted one step-sister. \"You call that a dress?\""
        print(counting(text))
        assert counting(text) == 2

class Test_counting(TestCase):
    def test_counting4(self):
        text = "oooooooooooooooooo."
        print(counting(text))
        assert counting(text) == 1

class Test_counting(TestCase):
    def test_counting5(self):
        text = ""
        print(counting(text))
        assert counting(text) == 0


class Test_nonDeclare(TestCase):
    def test_non_declar1(self):
        text = "At Cinderella’s house, she now had extra work to do.  She had to make two brand-new gowns for her " \
               "step-sisters.\"Faster!\", shouted one step-sister. \"You call that a dress?\""
        print(non_declar(text))
        assert non_declar(text) == 1

class Test_nonDeclare(TestCase):
    def test_non_declar2(self):
        text = "aaa. AAAAAA! AAAAAAAAA? AAAAAAAAAA!??!"
        print(non_declar(text))
        assert non_declar(text) == 3

class Test_nonDeclare(TestCase):
    def test_non_declar3(self):
        text = "aaaaaaa. dddddddddd. ffffffffffffff..?"
        print(non_declar(text))
        assert non_declar(text) == 1

class Test_show_only_words(TestCase):
    def test_show_only_words1(self):
        text = "aaaaaaa. dddddddddd. ffffffffffffff..?"
        print(show_only_words(text))
        assert show_only_words(text) == ['aaaaaaa', 'dddddddddd', 'ffffffffffffff']


class Test_show_only_words(TestCase):
    def test_show_only_words2(self):
        text = "show snow 2e34 234 adda. hphphp."
        print(show_only_words(text))
        assert show_only_words(text) == ['show', 'snow', 'adda', 'hphphp']

class Test_show_only_words(TestCase):
    def test_show_only_words3(self):
        text = "aaa! !!!!!!!!! AAAAAAAA!?!? AA...!    ..."
        print(show_only_words(text))
        assert show_only_words(text) == ['aaa', 'AAAAAAAA', 'AA']


class Test_len_sent(TestCase):
    def test_len_sent1(self):
        text = "aa. bb. cc. ee."
        print(Len_sent(text))
        assert Len_sent(text) == 2


class Test_len_sent(TestCase):
    def test_len_sent2(self):
        text = "dddddddd? hhhhhhh."
        print(Len_sent(text))  # 16/8
        assert Len_sent(text) == 8


class Test_len_sent(TestCase):
    def test_len_sent3(self):
        text = "????"
        print(Len_sent(text))
        assert Len_sent(text) == 0

class Test_len_word(TestCase):
    def test_len_word(self):
        text = "aa. bb. cc. dd. ee. ff."
        assert Len_word(text) == 2

class Test_len_word(TestCase):
    def test_len_word2(self):
        text = "whar 3? what. so 23e-765... so??? so soo"
        print(Len_word(text))
        assert Len_word(text) == 3


class Test_top_n_grams(TestCase):
    def test_top_n_grams1(self):
        text = ""
        print(Top_n_grams(text))
        assert Top_n_grams(text) == []

class Test_top_n_grams(TestCase):
    def test_top_n_grams2(self):
        text = "so i dont. so i. so i. dadad"
        print(Top_n_grams(text, n=3))
        assert Top_n_grams(text,n=3) == [('so i dont', 1), ('i dont so', 1), ('dont so i', 1), ('so i so', 1), ('i so i', 1), ('so i dadad', 1)]

class Test_top_n_grams(TestCase):
    def test_top_n_grams3(self):
        text = "aaa bbb ccc aaa bbb ccc"
        print(Top_n_grams(text, n=2))
        assert Top_n_grams(text, n=2) == [('aaa bbb', 1), ('bbb ccc', 1), ('ccc aaa', 1)]
