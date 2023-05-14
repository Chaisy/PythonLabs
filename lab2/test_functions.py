from unittest import TestCase

from functions import correctText, counting, show_only_words,  non_declar, Len_sent, Len_word, Top_n_grams

class Test_correct_text1(TestCase):
    def test_correct_text(self):

            text = "she dont want, \"no!\""
            assert correctText(text) == "she dont want END?"

    def test_correct_text1(self):
        text = "\"of cource\", my mum."
        print(correctText(text))
        assert correctText(text) == "START, my mum."




    def test_correct_text3(self):
        text = "but i dont want...........??"
        print(correctText(text))
        assert correctText(text) == "but i dont want?"

    def test_correct_text4(self):
        text = "but, what about me?!?!?"
        print(correctText(text))
        assert correctText(text) == "but, what about me?"


    def test_counting1(self):
        text = "car. so many?!?!?! how did you can."
        print(counting(text))
        assert counting(text) == 3

    def test_counting2(self):
        text = "At Cinderella’s house, she now had extra work to do.  She had to make two brand-new gowns for her step-sisters. " \
               "\"Faster!\", shouted one step-sister."
        print(counting(text))
        assert counting(text) == 3

    def test_counting3(self):
        text = "\"Faster!\", shouted one step-sister. \"You call that a dress?\""
        print(counting(text))
        assert counting(text) == 2

    def test_counting4(self):
        text = "oooooooooooooooooo."
        print(counting(text))
        assert counting(text) == 1

    def test_counting5(self):
        text = ""
        print(counting(text))
        assert counting(text) == 0


    def test_non_declar1(self):
        text = "At Cinderella’s house, she now had extra work to do.  She had to make two brand-new gowns for her " \
               "step-sisters.\"Faster!\", shouted one step-sister. \"You call that a dress?\""
        print(non_declar(text))
        assert non_declar(text) == 1


    def test_non_declar2(self):
        text = "aaa. AAAAAA! AAAAAAAAA? AAAAAAAAAA!??!"
        print(non_declar(text))
        assert non_declar(text) == 3


    def test_non_declar3(self):
        text = "aaaaaaa. dddddddddd. ffffffffffffff..?"
        print(non_declar(text))
        assert non_declar(text) == 1

    def test_show_only_words1(self):
        text = "aaaaaaa. dddddddddd. ffffffffffffff..?"
        print(show_only_words(text))
        assert show_only_words(text) == ['aaaaaaa', 'dddddddddd', 'ffffffffffffff']



    def test_show_only_words2(self):
        text = "show snow 2e34 234 adda. hphphp."
        print(show_only_words(text))
        assert show_only_words(text) == ['show', 'snow', 'adda', 'hphphp']


    def test_show_only_words3(self):
        text = "aaa! !!!!!!!!! AAAAAAAA!?!? AA...!    ..."
        print(show_only_words(text))
        assert show_only_words(text) == ['aaa', 'AAAAAAAA', 'AA']



    def test_len_sent1(self):
        text = "aa. bb. cc. ee."
        print(Len_sent(text))
        assert Len_sent(text) == 2



    def test_len_sent2(self):
        text = "dddddddd? hhhhhhh."
        print(Len_sent(text))  # 16/8
        assert Len_sent(text) == 8



    def test_len_sent3(self):
        text = "????"
        print(Len_sent(text))
        assert Len_sent(text) == 0


    def test_len_word(self):
        text = "aa. bb. cc. dd. ee. ff."
        assert Len_word(text) == 2


    def test_len_word2(self):
        text = "whar 3? what. so 23e-765... so??? so soo"
        print(Len_word(text))
        assert Len_word(text) == 3


    def test_top_n_grams3(self):
        text = "aaa bbb ccc aaa bbb ccc"
        print(Top_n_grams(text, n=2, k=3))
        assert Top_n_grams(text, n=2, k=3) == [('aaa bbb', 1), ('bbb ccc', 1), ('ccc aaa', 1)]
