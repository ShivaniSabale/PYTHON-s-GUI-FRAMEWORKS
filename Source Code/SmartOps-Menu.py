import tkinter
import tk_tools
window = tkinter.Tk()
# create the dropdown and grid
som = tk_tools.SmartOptionMenu(window, ['one', 'two', 'three'])
som.grid()
# define a callback function that retrieves
# the currently selected option
def callback():
 print(som.get())
# add the callback function to the dropdown
som.add_callback(callback)
window.mainloop()
