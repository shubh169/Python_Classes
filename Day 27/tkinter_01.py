import tkinter as tk

#Screen Setup.
window=tk.Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)

# How to create a lable.
my_label=tk.Label(text="My first lable", font=("Arial",24,"bold"))
my_label.pack()
# Changing the lable text after creating.
# my_label.config(text="My new text")

def button_clicked():
    print("Button clicked.")
    new_text=input.get()
    my_label.config(text=new_text)

# Create a button.
button=tk.Button(text="click me", command=button_clicked)
button.pack()

#Entry component(how to take a input from user).
input=tk.Entry(width=20)
input.pack()
print(input.pack())



window.mainloop()