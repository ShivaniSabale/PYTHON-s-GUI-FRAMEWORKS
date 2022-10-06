import tkinter
window = tkinter.Tk()
window.title("My GUI")
window.configure(background="white") 
window.geometry("100x100") 
ourMessage ='This is our Message'
messageVar = tkinter.Message(window, text = "Hello:") 
messageVar.config(bg='pink') 
messageVar.grid(row =0, column=0 ) 
window.mainloop() 