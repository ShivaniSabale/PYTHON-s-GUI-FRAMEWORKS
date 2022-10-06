import tkinter
window = tkinter.Tk()
window.title("My GUI")
window.configure(background="white") 
scale = tkinter.Scale(window, from_=0, to=50) 
scale.grid() 
scale2 = tkinter.Scale(window, from_=0, to=100, orient=tkinter.HORIZONTAL) 
scale2.grid() 
window.mainloop()