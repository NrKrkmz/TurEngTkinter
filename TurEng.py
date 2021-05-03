import tkinter as tk
import ast
from tkinter import *
from tkinter import messagebox


# ----------------------------------------------------------

inputWindow = tk.Tk()
inputWindow.title( "WORD ADD WINDOW" )

inputWindow.geometry("320x300")

frame = tk.Frame(inputWindow, bg='cyan')
frame.pack(side="bottom", fill='both', expand='no')

turkishLabel = Label(inputWindow,width=20,height=3,text="TURKISH WORD   :" , font="Times 10 bold")
turkishLabel.place(x=5 ,y=26)

englishLabel = Label(inputWindow,width=20,height=3,text="ENGLISH WORD    :" , font="Times 10 bold")
englishLabel.place(x=5,y=66)

turkishExLabel = Label(inputWindow,width=20,height=3,text="TURKISH EXAMP   :" , font="Times 10 bold")
turkishExLabel.place(x=5 ,y=106)

englishExLabel = Label(inputWindow,width=20,height=3,text="ENGLISH EXAMP    :" , font="Times 10 bold")
englishExLabel.place(x=5,y=146)

lastLabel = Label(inputWindow,width=40,height=3,text="www.frknyldz.com" , font="Times 10 bold")
lastLabel.place(x=17 ,y=260)

turkish_edit = Entry(inputWindow,width=15)
turkish_edit.place(x=150,y=40)
turkish_edit.config(font="bold")
turkish_edit.insert(END,"")

english_edit = Entry(inputWindow, width=15)
english_edit.place(x=150,y=80)
english_edit.config(font="bold")
english_edit.insert(END,"")

turkishEx_edit = Entry(inputWindow,width=15)
turkishEx_edit.place(x=150,y=120)
turkishEx_edit.config(font="bold")
turkishEx_edit.insert(END,"")

englishEx_edit = Entry(inputWindow, width=15)
englishEx_edit.place(x=150,y=160)
englishEx_edit.config(font="bold")
englishEx_edit.insert(END,"")

kelime_Eng = turkish_edit.get() 
kelime_Tur = english_edit.get()
cumle_Eng = englishEx_edit.get()
cumle_Tur = turkishEx_edit.get()

# ----------------------------------------------------------

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

# Ana fonksiyon
def mainFunction():
    kelime_Eng = turkish_edit.get() 
    kelime_Tur = english_edit.get()
    cumle_Eng = englishEx_edit.get()
    cumle_Tur = turkishEx_edit.get()

    kelime = Ezber(kelime_Eng, kelime_Tur, cumle_Eng, cumle_Tur)
    kelime.save()
    kelime.listele()

    tk.messagebox.showinfo(" NEW WORD ADDED !! \r\n", kelime_Eng + ' ---> '+ kelime_Tur + '\n\n' + cumle_Eng + '\n' + cumle_Tur)


# Kelime Ekle Butonu
controlButton = Button(inputWindow,text="ADD WORD",width=26,command=mainFunction)
controlButton.config(font="bold")
controlButton.place(x=15,y=230)

inputWindow.mainloop()
