import tkinter
window = tkinter.Tk()
window.title("My GUI")
window.configure(background="pink") 
window.geometry("300x50") 
label = tkinter.Label(window, text = "Please enter your text", 
font = ('Verdana',14), bg='pink')
label.grid(row=1, column=0)
entry = tkinter.Entry(fg="black", bg="white", width=50)
entry.grid(row=0, column=0)
window.mainloop()
text_input = entry.get()
print(text_input)