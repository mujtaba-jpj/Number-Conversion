from conversion.bin_conversion import *
from conversion.dec_conversion import *
from conversion.hex_conversion import *
from conversion.octal_conversion import *
from tkinter import messagebox
from tkinter import *
from tkinter import ttk 

window = Tk()
window.resizable(width=FALSE,height=FALSE)
window.geometry("700x500")

options = [
    "Binary",
    "Decimal",
    "Hexadecimal",
    "Octal"
]

def convert():
    convert_from = combo1.get()
    convert_to = combo2.get()
    conversion_num = entry1.get()

    if convert_from == "Binary":
        if convert_to == "Decimal":
            ans = bin_dec(conversion_num)
            result.config(text=ans)
        elif convert_to == "Hexadecimal":
            ans = bin_hex(conversion_num)
            result.config(text=ans)
        elif convert_to == "Octal":
            ans = bin_oct(conversion_num)
            result.config(text=ans)

    elif convert_from == "Decimal":

        if convert_to == "Binary":

            ans = dec_bin(conversion_num)
            result.config(text=ans)

        elif convert_to == "Hexadecimal":
            ans = dec_hex(conversion_num)
            result.config(text=ans)

        elif convert_to == "Octal":
            ans = dec_oct(conversion_num)
            result.config(text=ans)

    elif convert_from == "Hexadecimal":

        if convert_to == "Binary":
            ans = hex_bin(conversion_num)
            result.config(text=ans)

        elif convert_to == "Decimal":
            ans = hex_dec(conversion_num)
            result.config(text=ans)

        elif convert_to == "Octal":
            ans = hex_oct(conversion_num)
            result.config(text=ans)

    elif convert_from == "Octal":

        if convert_to == "Binary":
            ans = oct_bin(conversion_num)
            result.config(text=ans)

        elif convert_to == "Hexadecimal":
            ans = oct_hex(conversion_num)
            result.config(text=ans)

        elif convert_to == "Decimal":
            ans = oct_dec(conversion_num)
            result.config(text=ans)
    else:
        messagebox.showerror('Python Error', 'Error: This is an Error Message!')


#heading
heading = Label(window,text="Number Conversion",font=("Calibri",25))
heading.pack(anchor="center",ipady="75")

#dropdown entry box #1
combo1 = ttk.Combobox(window,values=options,state="readonly",font = ("Courier",11))
combo1.current(0) #Default Value
combo1.place(x=60,y=300)
entry1 = int
entry1 = Entry(window,font = ("Arial",11),borderwidth=3)
entry1.insert(0,"Enter num")
entry1.place(x=95,y=325)

#dropdown entry box #2
combo2 = ttk.Combobox(window,values=options,state="readonly",font = ("Courier",11))
combo2.current(1) #Default Value
combo2.place(x=450,y=300)
result = Label(window,font = ("Arial",11,"bold"),borderwidth=5,text='',bg="white",relief=RAISED)
result.place(x=450,y=325)


convert = Button(window,text="Convert!",command=convert,font = ("Comic Sans",16),bg="#545c58",activebackground="#7d827f")
convert.place(x=310,y=300)

if __name__ == "__main__":
    window.mainloop()


