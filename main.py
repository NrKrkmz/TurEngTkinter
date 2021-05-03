import ast

# Ezber sınıfı olusturuldu
class Ezber:
    def __init__(self, turkce, ingilizce, turkceCumle, ingilizceCumle):
        self.turkce = turkce
        self.ingilizce = ingilizce
        self.turkceCumle = turkceCumle
        self.ingilizceCumle = ingilizceCumle
        self.listLittle = {
            'ingilizcesi': ingilizce,
            'turkcesi': turkce,
            'turkceCumle': turkceCumle,
            'ingilizceCumle': ingilizceCumle 
        }

    def gosterEng(self):
        return self.ingilizce

    def gosterTur(self):
        return self.turkce 

    def gosterTurCumle(self):
        return self.turkceCumle

    def gosterEngCumle(self):
        return self.ingilizceCumle

    def save(self):
        file = open('Kelimelerim', 'a')
        file.writelines(str(self.listLittle) + '$')
        file.close()

    def listele(self):
        print('\n******************************************************\n')

        dosya = open('Kelimelerim', 'r')
        stringFile = dosya.read()
        stringToList = stringFile.split('$')

        for i in range(0, len(stringToList) - 1):
            ezber = stringToList[i] or []

            if len(ezber) > 0:
                kelimeDict = ast.literal_eval(ezber) 
                ingilizceKelime = kelimeDict['ingilizcesi']
                turkceKelime = kelimeDict['turkcesi']
                turkceCumle = kelimeDict['turkceCumle']
                ingilizceCumle = kelimeDict['ingilizceCumle']

                print('----------- WORD - ', i+1 , '-----------\n')

                print('English  = ', ingilizceKelime)
                print('Turkish  = ', turkceKelime)
                print('English Exam = ', ingilizceCumle)
                print('Turkish Exam = ', turkceCumle, '\n\n')

        print('\n******************************************************\n')


def getDataFromUser():
    kelimeler_FromUser = {}

    kelime_Eng = input('-ENG- Kelimeyi Girin : ')
    kelime_Tur = input('-TUR- Türkçe Karşılığını Girin : ')
    cumle_Eng = input('-ENG- İngilizce Cümleyi Girin : ')
    cumle_Tur = input('-TUR- Türkçe Cümleyi Girin : ')


    kelimeler_FromUser = {
        'ingilizcesi': kelime_Eng,
        'turkcesi': kelime_Tur,
        'turkceCumle': cumle_Tur,
        'ingilizceCumle': cumle_Eng 
    }

    return kelimeler_FromUser

def mainFunction():
    kullanıcıKelimeInputs = getDataFromUser()

    kelime = Ezber(kullanıcıKelimeInputs['ingilizcesi'], kullanıcıKelimeInputs['turkcesi'], 
        kullanıcıKelimeInputs['turkceCumle'], kullanıcıKelimeInputs['ingilizceCumle'])

    '''print('\n******************************************************\n' +
           kelime.gosterTur() + ' ---> ' + kelime.gosterEng() + '\n' +
            kelime.gosterTurCumle() + ' ---> ' + kelime.gosterEngCumle() +
         '\n******************************************************\n')
    '''

    kelime.save()
    kelime.listele()

mainFunction()