import tkinter
window = tkinter.Tk()
window.title("My GUI")
window.configure(background="white") 
window.geometry("210x150") 
label = tkinter.Label(window, text = "Please choose your food", 
font = ('Verdana',12), bg='pink')
label.grid(row=0, column=0, pady=20)
Radio_button1 = tkinter.Radiobutton(window, width = 15,text= "Burger", 
font = ('Verdana',12), bg='pink', value = 0)
Radio_button1.grid(row=1, column=0)
Radio_button2 = tkinter.Radiobutton(window, width = 15,text = "Pizza", 
font = ('Verdana',12), bg='pink', 
value = 1)
Radio_button2.grid(row=2, column=0)
window.mainloop()