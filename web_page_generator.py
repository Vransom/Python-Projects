import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.geometry("{}x{}".format(600,200))
        self.master.title("Web Page Generator")

        self.varCustom=StringVar()

        #label for custom text box
        self.label=tk.Label(self.master, text="Insert custom text or select the Default HTML button:")
        self.label.grid(row=0, padx=(10,0), pady=(10,10))

        #custom text box entry
        self.entry=tk.Entry(self.master, text=self.varCustom)
        self.entry.grid(row=1, columnspan=3, padx=(10,0), pady=(10,10), sticky=W+E)

        #button for default
        self.btn=Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, padx=(10,10), pady=(10,10))

        #button for custom text submission
        self.btn=Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customText)
        self.btn.grid(row=2, column=2, padx=(10,10), pady=(10,10))


    def defaultHTML(self):
        htmlText="Stay tuned for our amazing summer sale!"
        htmlFile=open("index.html", "w")
        htmlContent="<html>\n<body>\n<h1>" +htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customText(self):
        text=self.varCustom.get()
        htmlFile2=open("index.html", "w")
        htmlContent2="<html>\n<body>\n<h1>" + text + "</h1>\n</body>\n</html>"
        htmlFile2.write(htmlContent2)
        htmlFile2.close()
        webbrowser.open_new_tab("index.html")
        

if __name__=="__main__":
    root=tk.Tk()
    App=ParentWindow(root)
    root.mainloop()

    
