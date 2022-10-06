import tkinter
window = tkinter.Tk()
window.title("My GUI")
window.configure(background="white") 
T = tkinter.Text(window, height=2, width=30) 
T.grid() 
T.insert(tkinter.END, 'Have a great day\n') 
window.mainloop()