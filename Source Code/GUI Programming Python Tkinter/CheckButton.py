import tkinter
window = tkinter.Tk()
window.title("My GUI")
window.configure(background="white") 
window.geometry("210x150") 
label = tkinter.Label(window, text = "Please choose your food", 
 font = ('Verdana',12), bg='white')
label.grid(row=0, column=0, pady=20)
Check_button1 = tkinter.Checkbutton(window, width = 15,text= "Burger", 
 font = ('Verdana',12), bg='white')
Check_button1.grid(row=1, column=0)
Check_button2 = tkinter.Checkbutton(window, width = 15,text= "Pizza", 
font = ('Verdana',12), bg='white')
Check_button2.grid(row=2, column=0)
window.mainloop()
