import tkinter
window = tkinter.Tk()
window.title("My GUI")
window.configure(background="pink") 
window.geometry("200x100") 
button = tkinter.Button(window, text = "Click me", 
 font = ('Verdana',14), bg ="white", state= 
tkinter.NORMAL)
button.grid(row=0, column=0)
window.mainloop()