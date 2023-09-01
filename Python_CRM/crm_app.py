import tkinter as tk
from tkinter import ttk, messagebox
import database
import os

if "RUN_WITHOUT_GUI" not in os.environ:
    root = tk.Tk()
    # ... rest of GUI code

class CRMApp:

    def __init__(self, root):
        self.root = root
        self.root.title("CRM App")

        # Create Entry Fields
        self.first_name_var = tk.StringVar()
        ttk.Label(root, text="First Name").grid(row=0, column=0)
        ttk.Entry(root, textvariable=self.first_name_var).grid(row=0, column=1)

        self.last_name_var = tk.StringVar()
        ttk.Label(root, text="Last Name").grid(row=1, column=0)
        ttk.Entry(root, textvariable=self.last_name_var).grid(row=1, column=1)

        self.company_var = tk.StringVar()
        ttk.Label(root, text="Company").grid(row=2, column=0)
        ttk.Entry(root, textvariable=self.company_var).grid(row=2, column=1)

        self.email_var = tk.StringVar()
        ttk.Label(root, text="Email Address").grid(row=3, column=0)
        ttk.Entry(root, textvariable=self.email_var).grid(row=3, column=1)

        self.phone_var = tk.StringVar()
        ttk.Label(root, text="Phone Number").grid(row=4, column=0)
        ttk.Entry(root, textvariable=self.phone_var).grid(row=4, column=1)

        self.has_website_var = tk.StringVar()
        ttk.Label(root, text="Has Website? (yes/no)").grid(row=5, column=0)
        ttk.Entry(root, textvariable=self.has_website_var).grid(row=5, column=1)

        # Button to add contact
        ttk.Button(root, text="Add Contact", command=self.add_contact).grid(row=6, column=0, columnspan=2)

        # Button to display contacts
        ttk.Button(root, text="Display Contacts", command=self.display_contacts).grid(row=7, column=0, columnspan=2)

        # Text widget to display the contacts
        self.contacts_text = tk.Text(root, width=50, height=10)
        self.contacts_text.grid(row=8, column=0, columnspan=2)
        self.contacts_text.config(state=tk.DISABLED)  # Initially set to read-only

    def add_contact(self):
        contact = (
            self.first_name_var.get(),
            self.last_name_var.get(),
            self.company_var.get(),
            self.email_var.get(),
            self.phone_var.get(),
            self.has_website_var.get().lower()
        )

        if self.has_website_var.get().lower() not in ['yes', 'no']:
            messagebox.showerror("Error", "Has Website? field must be 'yes' or 'no'")
            return

        conn = database.create_connection()
        database.add_contact(conn, contact)
        conn.close()
        messagebox.showinfo("Success", "Contact added successfully!")

        # Clear the fields after successful addition
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.company_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.has_website_var.set("")

    def display_contacts(self):
        conn = database.create_connection()
        contacts = database.get_all_contacts(conn)
        conn.close()

        # Clear the text widget and make it editable
        self.contacts_text.config(state=tk.NORMAL)
        self.contacts_text.delete(1.0, tk.END)

        # Display each contact in the text widget
        for contact in contacts:
            self.contacts_text.insert(tk.END, f"First Name: {contact[1]}\n")
            self.contacts_text.insert(tk.END, f"Last Name: {contact[2]}\n")
            self.contacts_text.insert(tk.END, f"Company: {contact[3]}\n")
            self.contacts_text.insert(tk.END, f"Email: {contact[4]}\n")
            self.contacts_text.insert(tk.END, f"Phone: {contact[5]}\n")
            self.contacts_text.insert(tk.END, f"Has Website: {contact[6]}\n")
            self.contacts_text.insert(tk.END, '-'*40 + '\n')  # Separator

        # Set the text widget back to read-only after displaying contacts
        self.contacts_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = CRMApp(root)
    root.mainloop()
