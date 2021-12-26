from tkinter import *
from PIL import Image

def buttonCommand():
    convert()
    root.destroy()

def convert():
    
    #Checvk if the input is a file name
    if(URL.get().endswith(".jpg") or 
    URL.get().endswith(".jpeg") or 
    URL.get().endswith(".jfif") or 
    URL.get().endswith(".pjpeg") or 
    URL.get().endswith(".pjp") or
    URL.get().endswith(".png") or
    URL.get().endswith(".webp") or
    URL.get().endswith(".svg")):

        #Se il nome inserito è un file immagine
        print("Start Convert")

        img = Image.open(URL.get())
        img.save(URL.get() + '.ico')

        print('Convert Image to Icon Complete')

    else:
        #Se il nome inserito è errato
        print("The file name is incorrect")

#Definition for Tkinter
root = Tk()
root.geometry('380x380')
root.title("Image to Icon (write by Simone Zoppelletto)")
root.configure(background='#4d0000')

#URL input (YouTube)
label_URL = Label(root, text="Name of image (in the same directory as this file)", background='#4d0000', foreground="white", padx=10, pady=10).pack()
URL = Entry(root, width = 50)
URL.pack()

#Like Padx, Pady but between Input Label and Button Label
skipLine = Label(root, text="", background='#4d0000', foreground="white").pack()

Button(root, text="Input", command=convert).pack()

#Footer Credits
footer = Label(root, text="Created by Simone Zoppelletto", background='#4d0000', foreground="white", padx=10, pady=10).pack()

root.mainloop()