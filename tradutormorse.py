import tkinter as tk
import re

'''
msg = input("Texto:\n")
lol = msg.split(" ")
trad = ""
for i in lol:
    
    if i == ".-":
        i = "a"
        trad+=i
    if i == "-...":
        i = "b"
        trad+=i
    if i == "-.-.":
        i = "c"
        trad+=i
    if i == "-..":
        i = "d"
        trad+=i
    if i == ".":
        i = "e"
        trad+=i
    if i == "..-.":
        i = "f"
        trad+=i
    if i == "--.":
        i = "g"
        trad+=i
    if i == "....":
        i = "h"
        trad+=i
    if i == "..":
        i = "i"
        trad+=i
    if i == ".---":
        i = "j"
        trad+=i
    if i == "-.-":
        i = "k"
        trad+=i
    if i == ".-..":
        i = "l"
        trad+=i
    if i == "--":
        i = "m"
        trad+=i
    if i == "-.":
        i = "n"
        trad+=i
    if i == "---":
        i = "o"
        trad+=i
    if i == ".--.":
        i = "p"
        trad+=i
    if i == "--.-":
        i = "q"
        trad+=i
    if i == ".-.":
        i = "r"
        trad+=i
    if i == "...":
        i = "s"
        trad+=i
    if i == "-":
        i = "t"
        trad+=i
    if i == "..-":
        i = "u"
        trad+=i
    if i == "...-":
        i = "v"
        trad+=i
    if i == ".--":
        i = "w"
        trad+=i
    if i == "-..-":
        i = "x"
        trad+=i
    if i == "-.--":
        i = "y"
        trad+=i
    if i == "--..":
        i = "z"
        trad+=i
    if i == "/":
        i = " "
        trad+=i
    

            
    
    
    
    
print("\nTradução: \n")
print(trad)
'''
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.t1 = tk.Text(self)
        self.bt = tk.Button(self,text="Translate", command= self.translate)
        self.t2 = tk.Text(self)
        self.t2.configure(state="normal")
        self.t1.place(x = 0, y = 0, height = 200, width = 400)
        self.bt.place( x= 180 , y=200)
        self.t2.place(x = 0, y = 225, height = 200, width = 400)
        

    def translate(self):
        self.t2.delete(1.0, tk.END)
        
    
        
        if bool(re.search('[a-zA-Z]', self.t1.get(1.0, tk.END))):
            trad = ""
            texto = self.t1.get(1.0, tk.END)
               
            for i in texto:
                
                if i == "a":
                    i = ".- "
                    trad+=i
                if i == "b":
                    i = "-... "
                    trad+=i
                if i == "c":
                    i = "-.-. "
                    trad+=i
                if i == "d":
                    i = "-.. "
                    trad+=i
                if i == "e":
                    i = ". "
                    trad+=i
                if i == "f":
                    i = "..-. "
                    trad+=i
                if i == "g":
                    i = "--. "
                    trad+=i
                if i == "h":
                    i = ".... "
                    trad+=i
                if i == "i":
                    i = ".. "
                    trad+=i
                if i == "j":
                    i = ".--- "
                    trad+=i
                if i == "k":
                    i = "-.- "
                    trad+=i
                if i == "l":
                    i = ".-.. "
                    trad+=i
                if i == "m":
                    i = "-- "
                    trad+=i
                if i == "n":
                    i = "-. "
                    trad+=i
                if i == "o":
                    i = "--- "
                    trad+=i
                if i == "p":
                    i = ".--. "
                    trad+=i
                if i == "q":
                    i = "--.- "
                    trad+=i
                if i == "r":
                    i = ".-. "
                    trad+=i
                if i == "s":
                    i = "... "
                    trad+=i
                if i == "t":
                    i = "- "
                    trad+=i
                if i == "u":
                    i = "..- "
                    trad+=i
                if i == "v":
                    i = "...- "
                    trad+=i
                if i == "w":
                    i = ".-- "
                    trad+=i
                if i == "x":
                    i = "-..- "
                    trad+=i
                if i == "y":
                    i = "-.-- "
                    trad+=i
                if i == "z": 
                    i = "--.. "
                    trad+=i
                if i == " ":
                    i = "/ "
                    trad+=i
            self.t2.insert(1.0, trad)
        else:
            trad = ""
            texto = self.t1.get(1.0, tk.END).split(" ")
            texto[-1] = texto[-1].strip()
            
            for i in texto:
                texto[-1] = texto[-1].strip()
                
                
                if i == ".-":
                    i = "a"
                    trad+=i
                if i == "-...":
                    i = "b"
                    trad+=i
                if i == "-.-.":
                    i = "c"
                    trad+=i
                if i == "-..":
                    i = "d"
                    trad+=i
                if i == ".":
                    i = "e"
                    trad+=i
                if i == "..-.":
                    i = "f"
                    trad+=i
                if i == "--.":
                    i = "g"
                    trad+=i
                if i == "....":
                    i = "h"
                    trad+=i
                if i == "..":
                    i = "i"
                    trad+=i
                if i == ".---":
                    i = "j"
                    trad+=i
                if i == "-.-":
                    i = "k"
                    trad+=i
                if i == ".-..":
                    i = "l"
                    trad+=i
                if i == "--":
                    i = "m"
                    trad+=i
                if i == "-.":
                    i = "n"
                    trad+=i
                if i == "---":
                    i = "o"
                    trad+=i
                if i == ".--.":
                    i = "p"
                    trad+=i
                if i == "--.-":
                    i = "q"
                    trad+=i
                if i == ".-.":
                    i = "r"
                    trad+=i
                if i == "...":
                    i = "s"
                    trad+=i
                if i == "-":
                    i = "t"
                    trad+=i
                if i == "..-":
                    i = "u"
                    trad+=i
                if i == "...-":
                    i = "v"
                    trad+=i
                if i == ".--":
                    i = "w"
                    trad+=i
                if i == "-..-":
                    i = "x"
                    trad+=i
                if i == "-.--":
                    i = "y"
                    trad+=i
                if i == "--..":
                    i = "z"
                    trad+=i
                if i == "/":
                    i = " "
                    trad+=i
            self.t2.insert(1.0, trad)
    


      
        

lol = App()
lol.geometry('400x430')
lol.title("Morse Translator/Encoder")
lol.mainloop()