#Python Ver:    3.11.5
#
#Author:        Victoria Ransom
#
#Purpose:       Phonebook demo demonstrating OOP, Tkinter GUI Module,
#               using Tkinter Parent and Child Relationships

from tkinter import *
from tkinter import messagebox
import tkinter as tk


#importing other modules so we have access to them
import phonebook_gui
import phonebook_func

#Frame is the Tkinter frame class that our own class will ineherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #Define our master frame configuration
        self.master=master
        self.master.minsize(500,300) #(Height, width)
        self.master.maxsize(500,300)
        #This CenterWindow methhod will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        #This protocol method is a tkinter built-in method to catch if
        #the user clicks the upper coener, "X" on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda:phonebook_func.ask_quit(self))
        arg=self.master

        #load in the GUI widgets from a seperate module,
        #keeping our code compartmentalized and clutter-free
        phonebook_gui.load_gui(self)

if __name__=="__main__":
    root=tk.Tk()
    App=ParentWindow(root)
    root.mainloop()

                    
