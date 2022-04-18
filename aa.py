# PROJECT START
import sys
import tkinter as tk
from tkinter import *
import urllib.request
import webbrowser
from functools import partial
from tkinter import Tk, StringVar, ttk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


##################################################################################################


root = Tk()

root.title('ALL-TOGETHER CONVERTER  BY RAHUL KUMAR')
#root.wm_iconbitmap("/home/rahul/PycharmProjects/pythonProject/1.jpg")
root.geometry("550x484")

# width, height
root.minsize(430,400)

# width, height
root.maxsize(700,500)

# set the window color
root.configure(bg='powderblue')
labelfont = ('arial', 56, 'bold')
l = Label(root, bg="black" , fg= 'red',relief='raised', borderwidth=3, text='ALL-TOGETHER CONVERTER', font=("comicsense ", 20, "bold"), justify=CENTER)
l.pack( side=TOP, fill="x", padx=54, pady=5)


# Quit Button start


widget = Button(None, text="QUIT", bg="black", fg="red", font=("Arial", 14, "bold"), relief=RAISED, bd=5,
                justify=CENTER, highlightbackground="red", overrelief=GROOVE, activebackground="green",
                activeforeground="blue", command=root.destroy).place(x=410, y=422)

# Quit Button end


# Notepad start


def Edit():
    def newFile():
        global file
        root.title("Rahul- Notepad")
        file = None
        TextArea.delete(1.0, END)

    def openFile():
        global file
        file = askopenfilename(defaultextension=".txt",
                               filetypes=[("All Files", "*.*"),
                                          ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + " - Notepad")
            TextArea.delete(1.0, END)
            f = open(file, "r")
            TextArea.insert(1.0, f.read())
            f.close()

    def saveFile():
        global file
        if file == None:
            file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                     filetypes=[("All Files", "*.*"),
                                                ("Text Documents", "*.txt")])
            if file == "":
                file = None

            else:
                # Save as a new file

                f = open(file, "w")
                f.write(TextArea.get(1.0, END))
                f.close()

                root.title(os.path.basename(file) + " - Notepad")
                print("File Saved")
        else:
            # Save the file

            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

    def quitApp():
        root.destroy()

    def cut():
        TextArea.event_generate(("<>"))

    def copy():
        TextArea.event_generate(("<>"))

    def paste():
        TextArea.event_generate(("<>"))

    def about():
        showinfo("Notepad", " Notepad Created by Rahul Kumar \n  MCA (01111404419) \n Bhai parmanand institute of businesss studies")

    if __name__ == '__main__':

        # Basic tkinter setup

        root = Tk()
        root.title("Rahul - Notepad")

        # root.wm_iconbitmap("1.png")

        root.geometry("644x788")

        # Add TextArea
        TextArea = Text(root, font="lucida 13")
        file = None
        TextArea.pack(expand=True, fill=BOTH)

        # Lets create a menubar
        MenuBar = Menu(root)

        # File Menu Starts
        FileMenu = Menu(MenuBar, tearoff=0)

        # To open new file
        FileMenu.add_command(label="New", command=newFile)

        # To Open already existing file
        FileMenu.add_command(label="Open", command=openFile)

        # To save the current file

        FileMenu.add_command(label="Save", command=saveFile)
        FileMenu.add_separator()
        FileMenu.add_command(label="Exit", command=quitApp)
        MenuBar.add_cascade(label="File", menu=FileMenu)
        # File Menu ends

        # Edit Menu Starts

        EditMenu = Menu(MenuBar, tearoff=0)

        # To give a feature of cut, copy and paste

        EditMenu.add_command(label="Cut", command=cut)
        EditMenu.add_command(label="Copy", command=copy)
        EditMenu.add_command(label="Paste", command=paste)

        MenuBar.add_cascade(label="Edit", menu=EditMenu, command=quitApp)

        # Edit Menu Ends

        # Help Menu Starts

        HelpMenu = Menu(MenuBar, tearoff=0)
        HelpMenu.add_command(label="About Notepad", command=about)
        MenuBar.add_cascade(label="Help", menu=HelpMenu)

        # Help Menu Ends

        # Exits Menu

        Exitsmenu = Menu(MenuBar, tearoff=0)
        Exitsmenu.add_command(label="Exit", command=quitApp)
        MenuBar.add_cascade(label="Exits", menu=Exitsmenu, command=quitApp)

       # Exits Menu End

        root.config(menu=MenuBar)

        # Adding Scrollbar using rules from Tkinter

        Scroll = Scrollbar(TextArea)
        Scroll.pack(side=RIGHT, fill=Y)
        Scroll.config(command=TextArea.yview)
        TextArea.config(yscrollcommand=Scroll.set)

        root.mainloop()


# Notepad End


# Calculator Start


def calculator():


    def iCalc(source, side):
        storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
        storeObj.pack(side=side, expand=YES, fill=BOTH)
        return storeObj

    def button(source, side, text, command=None):
        storeObj = Button(source, text=text, command=command)
        storeObj.pack(side=side, expand=YES, fill=BOTH)
        return storeObj

    class app(Frame):
        def __init__(self):
            Frame.__init__(self)
            self.option_add('*Font', 'arial 20 bold')
            self.pack(expand=YES, fill=BOTH)
            self.master.title('Rahul Calculator')

            display = StringVar()
            Entry(self, relief=RIDGE, textvariable=display,
                  justify='right'
                  , bd=30, bg="powder blue").pack(side=TOP,
                                                  expand=YES, fill=BOTH)

            for clearButton in (["C"]):
                erase = iCalc(self, TOP)
                for ichar in clearButton:
                    button(erase, LEFT, ichar, lambda
                        storeObj=display, q=ichar: storeObj.set(''))

            for numButton in ("789/", "456*", "123-", "0.+"):
                FunctionNum = iCalc(self, TOP)
                for iEquals in numButton:
                    button(FunctionNum, LEFT, iEquals, lambda
                        storeObj=display, q=iEquals: storeObj
                           .set(storeObj.get() + q))

            EqualButton = iCalc(self, TOP)
            for iEquals in "=":
                if iEquals == '=':
                    btniEquals = button(EqualButton, LEFT, iEquals)
                    btniEquals.bind('<ButtonRelease-1>', lambda e, s=self,
                                                                storeObj=display: s.calc(storeObj), '+')


                else:
                    btniEquals = button(EqualButton, LEFT, iEquals,
                                        lambda storeObj=display, s=' %s ' % iEquals: storeObj.set
                                        (storeObj.get() + s))

        def calc(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("ERROR")

    if __name__ == '__main__':
        app().mainloop()


# Calculator End



# Currency Converter strat


def CurrencyConverter():

    import requests

    import tkinter as tk
    from tkinter import ttk

    class RealTimeCurrencyConverter():
        def __init__(self, url):
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']

        def convert(self, from_currency, to_currency, amount):
            initial_amount = amount
            if from_currency != 'USD':
                amount = amount / self.currencies[from_currency]

                # limiting the precision to 4 decimal places

            amount = round(amount * self.currencies[to_currency], 4)
            return amount

    class App(tk.Tk):

        def __init__(self, converter):
            tk.Tk.__init__(self)
            self.title = ('Currency Converter')
            self.currency_converter = converter

            self.geometry("600x300")
            self.configure(bg="hot pink")

            # Label
            self.intro_label = Label(self, text='Welcome to Real Time Currency Convertor', fg='blue', relief=tk.RAISED,
                                     justify=tk.CENTER, borderwidth=3)
            self.intro_label.config(font=('Manrope', 15, 'bold'))

            self.date_label = Label(self,
                                    text=f"1 Indian Rupee equals = {self.currency_converter.convert('INR', 'USD', 1)} USD \n Date : {self.currency_converter.data['date']}",
                                    relief=tk.GROOVE, borderwidth=2)

            self.intro_label.place(x=40, y=5)
            self.date_label.place(x=150, y=50)

            # Entry box
            valid = (self.register(self.restrictNumberOnly), '%d', '%P')
            self.amount_field = Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER, validate='key',
                                      validatecommand=valid)
            self.converted_amount_field_label = Label(self, text='', fg='black', bg='white', relief=tk.RIDGE,
                                                      justify=tk.CENTER, width=18, borderwidth=3)

            # dropdown
            self.from_currency_variable = StringVar(self)
            self.from_currency_variable.set("INR")  # default value
            self.to_currency_variable = StringVar(self)
            self.to_currency_variable.set("USD")  # default value

            font = ("Manrope", 12, "bold")
            self.option_add('*TCombobox*Listbox.font', font)
            self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,
                                                       values=list(self.currency_converter.currencies.keys()),
                                                       font=font,
                                                       state='readonly', width=15, justify=tk.CENTER)
            self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,
                                                     values=list(self.currency_converter.currencies.keys()), font=font,
                                                     state='readonly', width=13, justify=tk.CENTER)

            # placing
            self.from_currency_dropdown.place(x=30, y=120)
            self.amount_field.place(x=30, y=150)
            self.to_currency_dropdown.place(x=340, y=120)
            self.converted_amount_field_label.place(x=340, y=150)

            # Convert button
            self.convert_button = Button(self, text="Convert", fg="black", command=self.perform)
            self.convert_button.config(font=('Manrope', 12, 'bold'))
            self.convert_button.place(x=225, y=135)

        def perform(self):
            amount = float(self.amount_field.get())
            from_curr = self.from_currency_variable.get()
            to_curr = self.to_currency_variable.get()

            converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
            converted_amount = round(converted_amount, 2)

            self.converted_amount_field_label.config(text=str(converted_amount))

        def restrictNumberOnly(self, action, string):
            regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
            result = regex.match(string)
            return string == "" or (string.count('.') <= 1 and result is not None)

    if __name__ == '__main__':
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        converter = RealTimeCurrencyConverter(url)
        App(converter)
        mainloop()



# End Currency Converter



# Weight Converter




def WeightConverter():
    # factors to multiply to a value to convert from the following units to meters(m)
    factors = {'kg': 1000, 'hg': 100, 'dg': 10, 'g': 1, 'deg': 0.1, 'cg': 0.01, 'mg': 0.001}
    ids = {"Kilogram": 'kg', "Hectagram": 'hg', "Decagram": 'dg', "Decigram": 'deg', "Kilogram": 'kg', "gram": 'g',
           "centigram": 'cg', "milligram": 'mg'}

    # function to convert from a given unit to another
    def convert(amt, frm, to):
        if frm != 'g':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def callback():
        try:
            amt = float(in_field.get())
        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    # initiate window
    root = Toplevel()
    root.title("Weight Converter")

    # initiate frame
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label(mainframe, text="Weight Converter", font=("Arial", 12, "bold"), justify=CENTER).grid(column=1,
                                                                                                            row=1)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    # Add input field
    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
    in_field.grid(row=1, column=2, sticky=(W, E))

    # Add drop-down for input unit
    in_select = OptionMenu(mainframe, in_unit, "Kilogram", "Hectagram", "Decagram", "gram", "Decigram", "Centigram",
                           "Milligram").grid(column=3, row=1, sticky=W)

    # Add output field and drop-down
    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "Kilogram", "Hectagram", "Decagram", "gram", "Decigram", "Centigram",
                           "Milligram").grid(column=3, row=3, sticky=W)

    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    in_field.focus()



# End Weight Converter



# Area Converter start


def AreaConverter():
    wind = Toplevel()
    wind.minsize(width=400, height=150)
    wind.maxsize(width=400, height=150)

    meterFactor = {'square meter': 1, 'square km': 1000000, 'square rood': 1011.7141056, 'square cm': 0.0001,
                   'square foot': 0.09290304,
                   'square inch': 0.00064516, 'square mile': 2589988.110336, 'milimeter': 0.000001,
                   'square rod': 25.29285264,
                   'square yard': 0.83612736, 'square township': 93239571.9721, 'square acre': 4046.8564224,
                   'square are': 100,
                   'square barn': 1e-28, 'square hectare': 10000, 'square homestead': 647497.027584}

    def convert(x, fromUnit, toUnit):
        if fromVar.get() in meterFactor.keys() and toVar.get() in meterFactor.keys():
            resultxt.delete(0, END)
            result = (float(str(x)) * meterFactor[fromUnit]) / (meterFactor[toUnit])
            resultxt.insert(0, str(result))

    titleLabel = Label(wind, text="Area Converter", font=("Arial", 12, "bold"), justify=CENTER).grid(column=1, row=1)

    e = Entry(wind)
    e.grid(row=1, column=2)
    values = list(meterFactor.keys())

    fromVar = StringVar(wind)
    toVar = StringVar(wind)
    fromVar.set("From Unit")
    toVar.set("To Unit")

    fromOption = OptionMenu(wind, fromVar, *values, command=lambda y: convert(e.get(), fromVar.get(), toVar.get()))
    fromOption.grid(row=1, column=3)

    toLabel = Label(wind, text="To : ", font="Arial").grid(row=2, column=2)
    toOption = OptionMenu(wind, toVar, *values, command=lambda x: convert(e.get(), fromVar.get(), toVar.get()))
    toOption.grid(row=3, column=3)

    resultxt = Entry(wind)
    resultxt.grid(row=3, column=2)


# End Area Converter


# Length Converter start



def LengthConverter():
    
    # factors to multiply to a value to convert from the following units to meters(m)
    factors = {'nmi': 1852, 'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'inch': 0.0254, 'km': 1000, 'm': 1, 'cm': 0.01,
               'mm': 0.001}
    ids = {"Nautical Miles": 'nmi', "Miles": 'mi', "Yards": 'yd', "Feet": 'ft', "Inches": 'inch', "Kilometers": 'km',
           "meters": 'm', "centimeters": 'cm', "millileters": 'mm'}

    # function to convert from a given unit to another
    def convert(amt, frm, to):
        if frm != 'm':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def callback():
        try:
            amt = float(in_field.get())
        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    # initiate window
    root = Toplevel()
    root.title("Length Converter")


    # initiate frame
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label(mainframe, text="Length Converter", font=("Arial", 12, "bold"), justify=CENTER).grid(column=1,
                                                                                                            row=1)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    # Add input field
    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
    in_field.grid(row=1, column=2, sticky=(W, E))

    # Add drop-down for input unit
    in_select = OptionMenu(mainframe, in_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers",
                           "meters", "centimeters", "millileters").grid(column=3, row=1, sticky=W)

    # Add output field and drop-down
    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers",
                           "meters", "centimeters", "millileters").grid(column=3, row=3, sticky=W)

    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    in_field.focus()


# End Length converter


# Temperature Converter start



def TemperatureConverter():
    def convert():
        celTemp = celTempVar.get()
        fahTemp = fahTempVar.get()

        if celTempVar.get() != 0.0:
            celToFah = (celTemp * 9 / 5 + 32)
            fahTempVar.set(celToFah)

        elif fahTempVar.get() != 0.0:
            fahToCel = ((fahTemp - 32) * (5 / 9))
            celTempVar.set(fahToCel)

    def reset():
        top = Toplevel(padx=50, pady=50)
        top.grid()
        message = Label(top, text="Reset Complete")
        button = Button(top, text="OK", command=top.destroy)

        message.grid(row=0, padx=5, pady=5)
        button.grid(row=1, ipadx=10, ipady=10, padx=5, pady=5)

        fahTempVar.set(int(0))
        celTempVar.set(int(0))

    top = Toplevel()
    top.title("Temperature Converter")


    ###MAIN###

    celTempVar = IntVar()
    celTempVar.set(int(0))
    fahTempVar = IntVar()
    fahTempVar.set(int(0))
    titleLabel = Label(top, text="Temperature Converter", font=("Arial", 12, "bold"), justify=CENTER).grid(column=1,
                                                                                                           row=1)

    celLabel = Label(top, text="Celcius: ", font=("Arial", 16), fg="red")
    celLabel.grid(row=2, column=1, pady=10, sticky=NW)

    fahLabel = Label(top, text="Fahrenheit: ", font=("Arial", 16), fg="blue")
    fahLabel.grid(row=3, column=1, pady=10, sticky=NW)

    celEntry = Entry(top, width=10, bd=5, textvariable=celTempVar)
    celEntry.grid(row=2, column=1, pady=10, sticky=NW, padx=125)

    fahEntry = Entry(top, width=10, bd=5, textvariable=fahTempVar)
    fahEntry.grid(row=3, column=1, pady=10, sticky=NW, padx=125)

    convertButton = Button(top, text="Convert", font=("Arial", 8, "bold"), relief=RAISED, bd=5, justify=CENTER,
                           highlightbackground="red", overrelief=GROOVE, activebackground="hotpink",
                           activeforeground="blue", command=convert)
    convertButton.grid(row=4, column=1, ipady=8, ipadx=12, pady=5, sticky=NW, padx=55)

    resetButton = Button(top, text="Reset", font=("Arial", 8, "bold"), relief=RAISED, bd=5, justify=CENTER,
                         highlightbackground="red", overrelief=GROOVE, activebackground="orange",
                         activeforeground="blue", command=reset)
    resetButton.grid(row=4, column=2, ipady=8, ipadx=12, pady=5, sticky=NW)


# End Temperature Converter


####################################################################################################


# TEMPERATURE CONVERTER


widget = Button(root, text="Temperature converter", bg="black", fg="red", font=("Arial", 14, "bold"), relief=RAISED,
                bd=5, justify=CENTER, highlightbackground="red", overrelief=GROOVE, activebackground="silver",
                activeforeground="blue", command=TemperatureConverter).place(x=50, y=120)


# Length Converter


widget = Button(root, text="Length Converter", bg="black", fg="red", font=("Arial", 14, "bold"), relief=RAISED, bd=5,
                justify=CENTER, highlightbackground="red", overrelief=GROOVE, activebackground="orange",
                activeforeground="blue", command=LengthConverter).place(x=50, y=180)

# Area Converter


widget = Button(root, text="Area Converter", bg="black", fg="red", font=("Arial", 14, "bold"), relief=RAISED, bd=5,
                justify=CENTER, highlightbackground="red", overrelief=GROOVE, activebackground="yellow",
                activeforeground="blue", command=AreaConverter).place(x=50, y=240)



# Currency Converter


widget = Button(root, text="Calculator", bg="black", fg="red", font=("Arial", 14, "bold"), relief=RAISED, bd=5,
                justify=CENTER, highlightbackground="red", overrelief=GROOVE, activebackground="sky blue",
                activeforeground="blue", command=calculator).place(x=50, y=60)



# Weight Converter


widget = Button(root, text="Weight Converter", bg="black", fg="red", font=("Arial", 14, "bold"), relief=RAISED, bd=5,
                justify=CENTER, highlightbackground="red", overrelief=GROOVE, activebackground="magenta",
                activeforeground="blue", command=WeightConverter).place(x=50, y=300)


# Notepad Editor


widget = Button(root, text="Notepad Editor", bg="black", fg="red", font=("Arial", 15, "bold"), relief=RAISED, bd=5,
                justify=CENTER, highlightbackground="red", overrelief=GROOVE, activebackground="pink",
               activeforeground="blue", command=Edit).place(x=50, y=340, rely=0.05)


# caculator Editor


widget = Button(root, text="Currency converter", bg="black", fg="red", font=("Arial", 15, "bold"), relief=RAISED, bd=5,
                justify=CENTER, highlightbackground="red", overrelief=GROOVE, activebackground="cyan",
               activeforeground="blue", command=CurrencyConverter).place(x=50, y=407, rely=0.05)


root.mainloop()

# PROJECT END