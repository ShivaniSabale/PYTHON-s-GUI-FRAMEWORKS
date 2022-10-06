import tkinter
window = tkinter.Tk()
window.title("My GUI")
window.configure(background="pink") 
window.geometry("100x50") 
label = tkinter.Label(window, text = "Hello world",
font = ('Verdana',14), bg ="orange")
label.grid(row=0, column=0)
window.mainloop()