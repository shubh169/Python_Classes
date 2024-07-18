import tkinter

window=tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500,350)

# Create a label.
my_label=tkinter.Label(text="I Am A Lable",font=("Arial",25,"bold"))
my_label.pack(side="top")




window.mainloop()