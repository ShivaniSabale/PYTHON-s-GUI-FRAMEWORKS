import tkinter
window = tkinter.Tk()
window.title("My GUI")
window.configure(background="white") 
window.geometry("100x100") 
canva = tkinter.Canvas(window, width=80, height=80) 
canva.grid() 
canvas_height=20
canvas_width=200
y = int(canvas_height / 2) 
canva.create_line(0, y, canvas_width, y ) 
window.mainloop()