# 5/02/2024


# class definition to hold the window and interface widgets for processing
from tkinter import *

from tkinter.font import Font # for font creation

from tkinter import messagebox # for our exit

class TestAvg_GUI:
    #constructor to create the user interface
    def __init__(self):
        # create the window and set the title
        self.__mainWindow = Tk()
        self.__mainWindow.title('Test Average')
        self.__mainWindow.geometry('320x200') #W*H
        self.__mainWindow.configure(bg = 'Black')

        # create plain and bold Helvetica 12 point font
        self.Helv12 = Font(family = 'Helvetica', size = 12, weight = 'normal')
        self.Helv12b = Font(family = 'Helvetica', size = 12, weight = 'bold')

        # test1 --> first row
        # create objects
        self.__test1Label = Label(self.__mainWindow,
         font = self.Helv12,
        text = 'enter the score for test1:',
        bg = 'Black', fg = 'SpringGreen3' )
        self.__test1TextBox = Entry(self.__mainWindow, width = 10,
                                    font = self.Helv12,
                                      justify = CENTER
                                    )
        # place objects in window grid
        self.__test1Label.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.__test1TextBox.grid(row = 0, column = 1, padx = 5, pady = 5)
        
        # test2 --> second row
        # create objects
        self.__test2Label = Label(self.__mainWindow,
                                  font = self.Helv12,
                                    text = 'enter the score for test2:',
                                    fg = 'SpringGreen3',
                                    bg = 'Black')
        self.__test2TextBox = Entry(self.__mainWindow, width = 10, 
                                    font = self.Helv12,
                                    justify = CENTER)
        # place objects in window grid
        self.__test2Label.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.__test2TextBox.grid(row = 1, column = 1, padx = 5, pady = 5)
  
        # test3 --> Third row
        # create objects
        self.__test3Label = Label(self.__mainWindow, 
                                  font = self.Helv12 ,
                                  text = 'enter the score for test3:',
                                  fg = 'SpringGreen3',
                                  bg = 'Black')
        self.__test3TextBox = Entry(self.__mainWindow, width = 10,
                                    font = self.Helv12,
                                      justify = CENTER)
        # place objects in window grid
        self.__test3Label.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.__test3TextBox.grid(row = 2, column = 1, padx = 5, pady = 5)


        # create labels and place in grid
        self.__resultLabel = Label(self.__mainWindow,
                                   font = self.Helv12b,
                                     text = 'Average:',
                                     bg = 'Black', fg = 'Grey')
        self.__averageLabel = Label(self.__mainWindow, width =10, relief = 'groove',
                                    font = self.Helv12b,
                                      justify = CENTER)
       # create objects in window grid
        self.__resultLabel.grid(row = 3, column = 0)
        self.__averageLabel.grid(row = 3, column = 1)

        # create buttons and place in grid
        self.__calcButton = Button(self.__mainWindow,
                                   font = self.Helv12b,
                                     text = 'Calculate average', fg = 'SpringGreen3', 
                                     bg = 'Black',
                                     command = self.calcButtonClick)
        self.__exitButton = Button(self.__mainWindow,
                                   font = self.Helv12b,
                                     text = 'Exit', fg = 'SpringGreen3', bg = 'Black',
                                     command = self.exitButtonClick)
        self.__calcButton.grid(row = 4, column = 0)
        self.__exitButton.grid(row = 4, column = 1)

        self.__mainWindow.mainloop()
    # method to calculate and display average
    def calcButtonClick(self):
        test1 = float(self.__test1TextBox.get())
        test2 = float(self.__test2TextBox.get())
        test3 = float(self.__test3TextBox.get())

        average = (test1 + test2 + test3) / 3

        self.__averageLabel.configure(text = format(average, '.2f'))

    # methon to confirm user exut
    def exitButtonClick(self):
        response = messagebox.askyesno('Exit confirmation', 
                                       'Are you sure you want to exit?')
        if response == True:
            self.__mainWindow.destroy()

        


# main module to start program
def main():
    myTestAvg = TestAvg_GUI()

main()

