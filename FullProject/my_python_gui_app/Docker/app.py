import tkinter as tk

def on_submit():
    label.config(text=f"Hello, {name_var.get()}!")

app = tk.Tk()
app.title("My GUI App")

name_var = tk.StringVar()
entry = tk.Entry(app, textvariable=name_var)
entry.pack()

button = tk.Button(app, text="Submit", command=on_submit)
button.pack()

label = tk.Label(app, text="")
label.pack()

app.mainloop()
