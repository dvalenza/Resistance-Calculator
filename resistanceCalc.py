#Resistance Calculator 
#
#By David Valenza
#
#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import Tk, W, E , RIGHT, END
from ttk import Frame, Button, Label, Style
from ttk import Entry


class ResistanceCalc(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        
        self.parent = parent
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Resistor Calculator")
        
        Style().configure("TButton", padding=(0, 5, 0, 5), 
            font='serif 10')
        
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        self.columnconfigure(4, pad=3)        
        self.columnconfigure(5, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.rowconfigure(6, pad=3)
        self.rowconfigure(7, pad=3)
        self.rowconfigure(8, pad=3)
        self.rowconfigure(9, pad=3)
        self.rowconfigure(10, pad=3)
        self.rowconfigure(11, pad=3)
        self.rowconfigure(12, pad=3)


        entry = Entry(self)
        entry.grid(row=0, columnspan=4, sticky=W+E)
        global resistance
        resistance=""
        def ringOne(number):
            entry.delete(0, END)
            entry.insert(0, str(number))
            global resistance
            resistance = resistance + str(number)
        def ringTwo(number):
            ent=str(number)
            entry.insert(END, str(number))
            global resistance
            resistance = resistance + str(number)
        def ringThree(number): 
            ent=str(number)
            entry.insert(END, str(number))
            global resistance
            resistance = resistance + str(number)
        def ringFour(number):
            global resistance
            entry.delete(0, END)
            for x in range (0, number):
               resistance = resistance + "0"
            ent = "Resistance is: " + resistance
            entry.insert(END,ent)
            resistance = ""
        def cls():
            global resistance
            resistance = ""
            entry.delete(0, END)
            entry.insert(0,"Please Select ring colors")
               
        entry.insert(0,"Please Select ring colors")
        entry.config(justify=RIGHT)

        black = Button(self, text="Black", command=lambda: ringOne(0))
        black.grid(row=2, column=0)
        brown = Button(self, text="Brown", command=lambda: ringOne(1))
        brown.grid(row=3, column=0)
        red = Button(self, text = "Red", command=lambda: ringOne(2))
        red.grid(row=4, column=0)    
        orange = Button(self, text="Orange", command=lambda: ringOne(3))
        orange.grid(row=5, column=0)        
        yellow = Button(self, text="Yellow", command=lambda: ringOne(4))
        yellow.grid(row=6, column=0)        
        green = Button(self, text="Green", command=lambda: ringOne(5))
        green.grid(row=7, column=0)         
        blue = Button(self, text="Blue", command=lambda: ringOne(6))
        blue.grid(row=8, column=0) 
        violet = Button(self, text="Violet", command=lambda: ringOne(7))
        violet.grid(row=9, column=0) 
        grey = Button(self, text = "Grey", command=lambda: ringOne(8))
        grey.grid(row=10, column = 0)
        white = Button(self, text="White", command=lambda: ringOne(9))
        white.grid(row=11,column = 0)

        black2 = Button(self, text="Black", command=lambda: ringTwo(0))
        black2.grid(row=2, column=1)
        brown2 = Button(self, text="Brown", command=lambda: ringTwo(1))
        brown2.grid(row=3, column=1)
        red2 = Button(self, text = "Red", command=lambda: ringTwo(2))
        red2.grid(row=4, column=1)    
        orange2 = Button(self, text="Orange", command=lambda: ringTwo(3))
        orange2.grid(row=5, column=1)        
        yellow2 = Button(self, text="Yellow", command=lambda: ringTwo(4))
        yellow2.grid(row=6, column=1)        
        green2 = Button(self, text="Green", command=lambda: ringTwo(5))
        green2.grid(row=7, column=1)         
        blue2 = Button(self, text="Blue", command=lambda: ringTwo(6))
        blue2.grid(row=8, column=1) 
        violet2 = Button(self, text="Violet", command=lambda: ringTwo(7))
        violet2.grid(row=9, column=1) 
        grey2 = Button(self, text = "Grey", command=lambda: ringTwo(8))
        grey2.grid(row=10, column = 1)
        white2 = Button(self, text="White", command=lambda: ringTwo(9))
        white2.grid(row=11,column = 1)

        
        black3 = Button(self, text="Black", command=lambda: ringThree(0))
        black3.grid(row=2, column=2)
        brown3 = Button(self, text="Brown", command=lambda: ringThree(1))
        brown3.grid(row=3, column=2)
        red3 = Button(self, text = "Red", command=lambda: ringThree(2))
        red3.grid(row=4, column=2)    
        orange3 = Button(self, text="Orange", command=lambda: ringThree(3))
        orange3.grid(row=5, column=2)        
        yellow3 = Button(self, text="Yellow", command=lambda: ringThree(4))
        yellow3.grid(row=6, column=2)        
        green3 = Button(self, text="Green", command=lambda: ringThree(5))
        green3.grid(row=7, column=2)         
        blue3 = Button(self, text="Blue", command=lambda: ringThree(6))
        blue3.grid(row=8, column=2) 
        violet3 = Button(self, text="Violet", command=lambda: ringThree(7))
        violet3.grid(row=9, column=2) 
        grey3 = Button(self, text = "Grey", command=lambda: ringThree(8))
        grey3.grid(row=10, column = 2)
        white3 = Button(self, text="White", command=lambda: ringThree(9))
        white3.grid(row=11,column = 2)

        black4 = Button(self, text="Black", command=lambda: ringFour(0))
        black4.grid(row=2, column=3)
        brown4 = Button(self, text="Brown", command=lambda: ringFour(1))
        brown4.grid(row=3, column=3)
        red4 = Button(self, text = "Red", command=lambda: ringFour(2))
        red4.grid(row=4, column=3)    
        orange4 = Button(self, text="Orange", command=lambda: ringFour(3))
        orange4.grid(row=5, column=3)        
        yellow4 = Button(self, text="Yellow", command=lambda: ringFour(4))
        yellow4.grid(row=6, column=3)        
        green4 = Button(self, text="Green", command=lambda: ringFour(5))
        green4.grid(row=7, column=3)         
        blue4 = Button(self, text="Blue", command=lambda: ringFour(6))
        blue4.grid(row=8, column=3) 
        violet4 = Button(self, text="Violet", command=lambda: ringFour(7))
        violet4.grid(row=9, column=3) 
        grey4 = Button(self, text = "Grey", command=lambda: ringFour(8))
        grey4.grid(row=10, column = 3)
        white4 = Button(self, text="White", command=lambda: ringFour(9))
        white4.grid(row=11,column = 3)
        
        i=0
        labels = "Ring 1", "Ring 2", "Ring 3", "Multiplier"
        for label in labels:
          label1 = Label(self, text=label)
          label1.grid(row=1, column = i)
          i+=1
          
        clear = Button(self, text = "Clear", command = lambda: cls())
        clear.grid(row=12, columnspan=4, sticky=W+E)

        self.pack()
         

def main():
  
    root = Tk()
    app = ResistanceCalc(root)
    root.mainloop()  


if __name__ == '__main__':
    main() 
