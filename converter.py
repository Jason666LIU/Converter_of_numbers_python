# David Omrai, 27.12.2017
# Converter, from arabic number to romannumber and from roman number to arabic number in range from 1 to 3999
from tkinter import *

class Convector():
    def __init__(self):
        self.number = ""
        self.roman = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        self.arabic = {"I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}
        self.numbers = [1, 5, 10, 50, 100, 500, 1000]
        self.output = ""
        self.root = Tk()
        self.root.configure(background="#191919")
        self.root.wm_title("Convector")
        self.root.minsize(250, 125)
        self.text = Label(self.root, text="Insert arabic or roman number", font = "fixedsys 9", bg="#191919", fg="#ffffff")
        self.text.pack()
        def sendIt(): # function used by button, also sending input to function whichOne
            self.number = self.inNum.get()
            self.whichOne()
        self.inNum = Entry(self.root)
        self.inNum.pack()
        self.inNum.focus_set()
        Button(self.root, text="Get", command = sendIt, font="system 8 bold", bg="#19aa19", fg="#ffffff").pack(side = TOP, padx= 6, pady= 6)
        self.outtext = Label(self.root, text="Output", font="system 9", bg="#191919", fg="#ffffff")
        self.outtext.pack()
        self.value = Label(self.root, text="...", font="system 19", bg="#191919", fg="#2dff21")
        self.value.pack()
        self.root.mainloop()
    def whichOne(self): # This function choose according to input where should it be send
        try:
            if self.number[0] in self.arabic:
                self.doArabic()
            elif int(self.number[0]) not in self.arabic:
                self.kv = len(self.number)-1
                self.doRoman()
        except:
            self.value.config(text="Error")    
    def doRoman(self): # function which convert arabic number to roman number
        if int(self.number) in self.roman:
            self.output = self.roman[int(self.number)]
        else:
            for i in range(0, len(self.number)):
                self.num = int(self.number[i])*10**self.kv
                self.kv -= 1
                if self.num in self.roman:
                    self.output += self.roman[self.num]
                else:
                    for h in range(0, len(self.numbers)-1):
                        if self.num < self.numbers[h+1] and self.num > self.numbers[h] and h % 2 == 0:
                            while self.num > 0:
                                self.output += self.roman[self.numbers[h]]
                                self.num -= self.numbers[h]
                        elif self.num < self.numbers[h+1] and self.num > self.numbers[h] and h % 2 == 1:
                            self.output += self.roman[self.numbers[h]]
                            self.num -= self.numbers[h]
                            while self.num > 0:
                                self.output += self.roman[self.numbers[h-1]]
                                self.num -= self.numbers[h-1]
                        
                        elif self.num > max(self.numbers):
                            while self.num > 0:
                                self.output += self.roman[self.numbers[len(self.numbers)-1]]
                                self.num -= self.numbers[len(self.numbers)-1]
        self.printMe()
    def doDel(self, turn): # this function convert str to list, delete number from list and then convert beck to str
        for i in range(turn):
            self.number = list(self.number)
            self.number[i] = ""
        return "".join(list(self.number))
    def doArabic(self): # function which convert roman number to arabic number
        self.output = 0
        while len("".join(list(self.number))) != 0:
            if len(self.number) == 1:
                self.output += self.arabic[str(self.number[0])]
                self.number = self.doDel(1)
            elif int(self.arabic[self.number[0]]) < int(self.arabic[self.number[1]]):
                self.output += self.arabic[str(self.number[0]+self.number[1])]
                self.number = self.number = self.doDel(2)
            elif self.number[0] in self.arabic:
                self.output += self.arabic[str(self.number[0])]
                self.number = self.doDel(1)
        self.printMe()
    def printMe(self): # output
        self.value.config(text=self.output)
        self.output = ""
Convector()



