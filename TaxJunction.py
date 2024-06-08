##Author: Aidan Lewis
##Date: 5/8/24
##Assignment: Lab 11 event handling
##Filename: TaxJunction.py
##Desc: This is a graphical user interface program that calculates the assessed value and property tax off of an entered value

from tkinter import *
from tkinter.font import Font
from tkinter import messagebox


class TJ_GUI:
    def __init__(self):
        self.__mainWindow = Tk()
        self.__mainWindow.title('Tax Junction')
        self.__mainWindow.geometry('400x180')
        self.__mainWindow.configure(bg = 'Gold3')


    # get the value of property from the user
        self.__valueLabel = Label(self.__mainWindow, 
            text = """Property value in $:""",
             fg = 'Black', bg = 'Gold3')
        self.__valueBox = Entry(self.__mainWindow,
                              justify = CENTER,
                              width = 20,
                              bg = 'white', fg = 'Black')
        self.__valueLabel.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.__valueBox.grid(row = 1, column = 1, padx = 10, pady = 10)
       # assessment value label and box
        self.__avLabel = Label(self.__mainWindow,
                           text ="Assessment Value:",
                           bg = 'Gold3', fg = 'Black')
        self.__avBox = Label(self.__mainWindow,
                        justify = CENTER,
                        width = 10)
        self.__avLabel.grid(row= 2, column=1 ,padx=10,pady=10)
        self.__avBox.grid(row= 2, column=2 ,padx=10,pady=10)
        
        self.__ptLabel = Label(self.__mainWindow,
                               text = 'Property Tax:',
                               bg ='Gold3', fg='Black')
        self.__ptBox = Label(self.__mainWindow,
                             justify = CENTER,
                             width = 10)
        self.__ptLabel.grid(row=3 ,column=1 ,padx= 10,pady= 10)
        self.__ptBox.grid(row=3,column=2 ,padx= 10,pady= 10)
        
        self.__calcButton = Button(self.__mainWindow,
                                   text = "Calculate!",
                                   bg = 'green',
                                   command = self.calcButtonClick)
        self.__calcButton.grid(row=2,column=0,padx=10,pady=10)

        self.__exitButton = Button(self.__mainWindow,
                                   text = 'Exit',
                                   bg = 'Black',
                                  width = 5,
                                  fg ='White',
                                  command = self.exitButtonClick)
        self.__exitButton.grid(row =3,column=0,padx=10,pady=10)


        
        self.__mainWindow.mainloop()

    def calcButtonClick(self):
        value = float(self.__valueBox.get())
        asconstant = float(0.60)
        ptconstant = float(0.64)
        AV = (value * asconstant)
        pttempcalc = (AV / 100)
        PT = (pttempcalc * ptconstant)
        self.__avBox.configure(text = format(AV, '.2f'))
        self.__ptBox.configure(text = format(PT, '.2f'))

    def exitButtonClick(self):
        resp = messagebox.askyesno("Do you want to exit?",
                                   "Are you sure?")
        if resp == True:
            self.__mainWindow.destroy()




def main():
    Tax = TJ_GUI()

main()
