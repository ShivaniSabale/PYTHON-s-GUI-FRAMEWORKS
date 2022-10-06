import tkinter
import tk_tools
def update(y):
 rs.set_value(int(y))
window = tkinter.Tk() #create tkinter window
window.title("Speed control") #give title
window.configure(background="white") #change background color 
window.geometry("120x180") 
scale = tkinter.Scale(window, from_=0, to=100, orient=tkinter.HORIZONTAL, 
command = update) 
scale.grid(row=0, column=0) 
rs = tk_tools.RotaryScale(window, max_value=100.0, size=100, needle_thickness=5, needle_color='black',unit='km/h')
rs.grid(row=1, column=0)
window.mainloop()
