class WordsFinder:
    def __init__(self, *args):
        self.file_names = args
        self.all_words = {}

    def remove_(self, string):
        trans_table = {ord(",") : None, ord('.') : None, ord('=') : None, ord('!') : None, ord('?') : None, ord(';') : None, ord(':') : None, ord('-') : None}
        return string.translate(trans_table)
    def get_all_words(self):
        for i in self.file_names:
            with open(i, encoding = 'utf-8') as text:
                list_ = text.read()
                j = 0
                while j < len(list_):
                    k = list_.lower()
                    k = self.remove_(k)
                    k = k.split()

                    j += 1
                #print(k)
            self.all_words[i] = k
            return self.all_words

    def find(self, word):
        dict_ = {}
        k = str.lower(word)
        i = self.get_all_words()
        for name, words in i.items():
            m = 1
            for j in words:
                if k == j:
                    dict_[name] = m
                else:
                    m += 1
                    continue
                return dict_

    def count(self, word):
        count_ = {}
        k = str.lower(word)
        i = self.get_all_words()
        for name, words in i.items():
            m = 1
            for j in words:
                if k == j:
                    count_[name] = m
                    m += 1
                    continue
                else:
                    continue
            return count_






finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder1 = WordsFinder('Rudyard Kipling - If.txt',)

print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))


finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

