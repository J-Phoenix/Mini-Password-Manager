import tkinter as tk
from tkinter import messagebox, simpledialog
from manager.manager import PasswordManager

def run_app():
    root = tk.Tk()
    root.title("Mini Password Manager")
    app = PasswordManagerGUI(root)
    root.mainloop()

class PasswordManagerGUI:
    def __init__(self, root):
        self.root = root
        self.manager = None

        self.frame = tk.Frame(root, padx=20, pady=20)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Mini Password Manager", font=("Arial", 14))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.unlock_btn = tk.Button(self.frame, text="Unlock", command=self.unlock_store, width=20)
        self.unlock_btn.grid(row=1, column=0, columnspan=2, pady=5)

        self.add_btn = tk.Button(self.frame, text="Add Credential", command=self.add_credential, state="disabled", width=20)
        self.add_btn.grid(row=2, column=0, pady=5)

        self.view_btn = tk.Button(self.frame, text="View Credential", command=self.view_credential, state="disabled", width=20)
        self.view_btn.grid(row=2, column=1, pady=5)

        self.list_btn = tk.Button(self.frame, text="List Sites", command=self.list_sites, state="disabled", width=20)
        self.list_btn.grid(row=3, column=0, columnspan=2, pady=5)

    def unlock_store(self):
        master = simpledialog.askstring("Unlock", "Enter Master Password:", show="*")
        if not master:
            return
        try:
            self.manager = PasswordManager(master)
        except ValueError:
            messagebox.showerror("Error", "Wrong master password.")
            return

        self.add_btn.config(state="normal")
        self.view_btn.config(state="normal")
        self.list_btn.config(state="normal")
        messagebox.showinfo("Unlocked", "Store unlocked successfully!")

    def add_credential(self):
        site = simpledialog.askstring("Add", "Enter Site Name:")
        if not site: return
        user = simpledialog.askstring("Add", f"Username for {site}:")
        pwd = simpledialog.askstring("Add", f"Password for {site}:", show="*")
        if not user or not pwd: return
        self.manager.add_credential(site, user, pwd)
        messagebox.showinfo("Saved", f"Credential for {site} saved.")

    def view_credential(self):
        site = simpledialog.askstring("View", "Enter Site Name:")
        if not site: return
        entry = self.manager.get_credential(site)
        if not entry:
            messagebox.showerror("Not Found", f"No entry for {site}.")
            return
        messagebox.showinfo("Credential", f"Site: {site}\nUsername: {entry['username']}\nPassword: {entry['password']}")

    def list_sites(self):
        sites = self.manager.list_sites()
        if not sites:
            messagebox.showinfo("Empty", "No sites stored yet.")
            return
        messagebox.showinfo("Sites", "\n".join(sites))
