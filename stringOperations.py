from os.path import join
import csv
import numpy as np
from jpype import JClass, JString, getDefaultJVMPath, shutdownJVM, startJVM

"""from nlpPreparation import bigrams"""


class stringOperationsStart():
    #Bu cümle default olarak başlar class çağırıldığında içeriği değiştirilir.
    ZEMBEREK_PATH: str = join('..', 'bin', 'zemberek-full.jar')
    startJVM(
        getDefaultJVMPath(),
        '-ea',
        f'-Djava.class.path={ZEMBEREK_PATH}',
        convertStrings=False
    )
    sentenceThatWillBeChanged = "baslangic"
    #sentenceThatWontBeChangedButNormalized = "baslangic"
    #opening classes
    TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
    TurkishTokenizer: JClass = JClass('zemberek.tokenization.TurkishTokenizer')
    Paths: JClass = JClass('java.nio.file.Paths')
    TurkishSentenceNormalizer: JClass = JClass(
        'zemberek.normalization.TurkishSentenceNormalizer'
    )

    normalizer = TurkishSentenceNormalizer(
        TurkishMorphology.createWithDefaults(),
        Paths.get(
            join('..', 'data', 'normalization')
        ),
        Paths.get(
            join('..', 'data', 'lm', 'lm.2gram.slm')
        )
    )


    tokenizer: TurkishTokenizer = TurkishTokenizer.DEFAULT

    #morfoloji baslangic

    TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
    AnalysisFormatters: JClass = JClass(
        'zemberek.morphology.analysis.AnalysisFormatters'
    )
    WordAnalysis: JClass = JClass('zemberek.morphology.analysis.WordAnalysis')

    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

    #morfoloji bitis

    def _init_(self, str):

        self.sentenceThatWillBeChanged = str
        self.sentenceThatWontBeChangedButNormalized = str

    def stringiDegis(self,str):
        self.sentenceThatWillBeChanged = str
    def normalize(self):

        #normalizer


        deneme = self.normalizer.normalize(JString(self.sentenceThatWillBeChanged))
        self.sentenceThatWillBeChanged = str(deneme)
        self.sentenceThatWontBeChangedButNormalized = str(deneme)

        return self.sentenceThatWillBeChanged


    def tokenize(self, cumle):
        kelimeler = []

        inp: str = cumle

        for i, token in enumerate(self.tokenizer.tokenizeToStrings(
                JString(inp)
        )):
            kelimeler.append(str(token))


        return kelimeler
    def negatifler(self,arr):
        with open('../files/negative.csv', encoding="utf8") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            data = [row for row in csv.reader(csvfile)]
            count = 0
            for i in arr:
                for row in data:
                    if i == str(row[0]):
                        i = "(-)" + i
                        arr[count] = i
                count = count + 1
        return arr

    def pozitifler(self, arr):
        with open('../files/positive.csv', encoding="utf8") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            data = [row for row in csv.reader(csvfile)]
            count = 0
            for i in arr:
                for row in data:
                    # print(str(row[0]))
                    if i == str(row[0]):
                        i = "(+)" + i
                        arr[count] = i
                count = count + 1
        return arr

    def morfoloji(self, arr):


        word: str = 'etmiyorum'
        count = 0
        for i in arr:
            word: str = i

            results: JClass = self.morphology.analyze(JString(word))


            if "+neg" in str(results):
                i = "NOT_" + i
                arr[count] = i
            elif ":Neg" in str(results):
                i = "NOT_" + i
                arr[count] = i
            count = count + 1

    def zamanveBaglacIceriyorMu(self, arr):
        count = 0
        for word in arr:
            if word == "ay":
                word += "_zaman"
                arr[count] = word
            elif word == "hafta":
                word += "_zaman"
                arr[count] = word
            elif word == "gün":
                word += "_zaman"
                arr[count] = word
            elif word == "yıl":
                word += "_zaman"
                arr[count] = word
            elif word == "dakika":
                word += "_zaman"
                arr[count] = word
            elif word == "saniye":
                word += "_zaman"
            elif word == "fakat":
                word += "_baglac"
                arr[count] = word
            elif word == "lakin":
                word += "_baglac"
                arr[count] = word
            elif word == "ama":
                word += "_baglac"
                arr[count] = word
            elif word == "ancak":
                word += "_baglac"
                arr[count] = word
            elif word == "yalnız":
                word += "_baglac"
                arr[count] = word

            count = count + 1


    def olumsuzSayisi(self, arr):
        count = 0
        for word in arr:
            if "(-)" in word :
                count = count + 1
        return count
    def olumluSayisi(self, arr):
        count = 0
        for word in arr:
            if "(+)" in word :
                count = count + 1
        return count

    def baglacSayisi(self, arr):
        count = 0
        for word in arr:
            if "_baglac" in word:
                count = count + 1
        return count

    def notSayisi(self, arr):
        count = 0
        for word in arr:
            if "NOT_" in word:
                count = count + 1
        return count

    def zamanIceriyorMu(self, arr):

        for word in arr:
            if "_zaman" in word:
                return 1

        return 0
    def bigramToplamlari(self, arr):
        obj = bigrams.Bigrams()
        count = 0
        bigramToplamlari = 0
        for word in arr:
            if "(-)" in word :
                word = word[3:]
                if count > 0:
                    bigramToplamlari = bigramToplamlari + obj.calculate_bigram(arr[count-1] ,arr[count])
                elif count == 0:
                    bigramToplamlari = bigramToplamlari + obj.calculate_bigram("", arr[count])
            elif "(+)" in word :
                word = word[3:]
                if count > 0:
                    bigramToplamlari = bigramToplamlari + obj.calculate_bigram(arr[count-1] ,arr[count])
                elif count == 0:
                    bigramToplamlari = bigramToplamlari + obj.calculate_bigram("", arr[count])

            count = count + 1
        return bigramToplamlari

    def kapat(self):
        shutdownJVM()