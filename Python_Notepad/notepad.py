import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        
        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(expand=1, fill="both")

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)

        self.edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            self.text_area.delete(1.0, tk.END)
            with open(file, "r") as f:
                self.text_area.insert(tk.INSERT, f.read())

    def save_file(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            with open(file, "w") as f:
                f.write(self.text_area.get(1.0, tk.END))

    def exit_app(self):
        self.root.destroy()

    def cut_text(self):
        self.copy_text()
        self.text_area.delete("sel.first", "sel.last")

    def copy_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.text_area.selection_get())

    def paste_text(self):
        self.text_area.insert(tk.INSERT, self.root.clipboard_get())

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()