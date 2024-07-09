import tkinter as tk

window=tk.Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)


my_label=tk.Label(text="My first lable", font=("Arial",24,"bold"))
my_label.pack()


def button_clicked():
    print("Button clicked.")
    new_text=input.get()
    my_label.config(text=new_text)

button=tk.Button(text="click me", command=button_clicked)
button.pack()


input=tk.Entry(width=20)
input.pack()
print(input.pack())



window.mainloop()