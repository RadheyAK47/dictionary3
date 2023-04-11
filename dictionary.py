from tkinter import*
root=Tk()

root.title("my dictionary")
root.geometry("400x400")

dictionary={
    "tkinter":"It is a gui library of python",
    "mutable":"value that can be changed like a list",
    "immutable":"value that can not be changed like a tuple"
    }

label_mutable=Label(root)
label_immutable=Label(root)
label_tkinter=Label(root)

def mutable():
    label_mutable["text"]=dictionary["mutable"]
    
def immutable():
    label_immutable["text"]=dictionary["immutable"]
    
def tkinter():
    label_tkinter["text"]=dictionary["tkinter"]

btn1=Button(root,text="mutable",command=mutable)
btn2=Button(root,text="immutable",command=immutable)
btn3=Button(root,text="tkinter",command=tkinter)

btn1.place(relx=0.5,rely=0.2,anchor=CENTER)
btn2.place(relx=0.5,rely=0.5,anchor=CENTER)
btn3.place(relx=0.5,rely=0.8,anchor=CENTER)

label_mutable.place(relx=0.5,rely=0.3,anchor=CENTER)
label_immutable.place(relx=0.5,rely=0.6,anchor=CENTER)
label_tkinter.place(relx=0.5,rely=0.9,anchor=CENTER)

root.mainloop()







