import tkinter as tk
from tkinter import filedialog, messagebox
import os
from hasher import HashData


class MainApp(tk.Frame):
    """Main GUI"""

    _root_title = 'Google AdWords Customer Match Hasher 0.1'
    _DIR = os.environ['PWD']

    userinput = None
    hashed_data = None

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title(self._root_title)

        self.create_widgets()

    def create_widgets(self):
        """Main layout and widgets"""
        self.info_input = tk.Label(self)
        self.info_input['text'] = 'Paste emails, one per line and click "Encrypt" to see results below:'
        self.info_input['pady'] = 10
        self.info_input.grid(row=0, columnspan=3)

        self.input = tk.Text(self)
        self.input['height'] = 10
        self.input.grid(row=1, columnspan=3)

        self.info_output = tk.Label(self)
        self.info_output['text'] = 'Encrypted mails:'
        self.info_output['pady'] = 10
        self.info_output.grid(row=2, columnspan=3)

        self.output = tk.Text(self)
        self.output['height'] = 10
        self.output.grid(row=3, columnspan=3)

        self.btn_submit = tk.Button(self)
        self.btn_submit['text'] = 'Encrypt'
        self.btn_submit['command'] = self.hash_input
        self.btn_submit.grid(row=4, column=0)

        self.btn_save_as = tk.Button(self)
        self.btn_save_as['text'] = 'Save to file'
        self.btn_save_as['command'] = self.save_to_file
        self.btn_save_as.grid(row=4, column=1)

        self.btn_quit = tk.Button(self)
        self.btn_quit['text'] = 'Quit'
        self.btn_quit['command'] = self.master.destroy
        self.btn_quit.grid(row=4, column=2)


    def create_error_box(self, message):
        """Display errors for user"""
        messagebox.showerror("Error", message)

    def save_to_file(self):
        tk.filedialog.asksaveasfilename(
            initialdir=self._DIR,
            title='emails',
        )

    def hash_input(self):
        """Hash mails from self.input"""
        input_text = self.input.get('1.0', tk.END)
        email_list = HashData(input_text.splitlines())

        try:
            email_list.validate_email()
            self.hashed_data = list(email_list.encrypt())

            self.output.delete('1.0', tk.END) # purge output before writing
            self.output.insert('1.0', '\n'.join(self.hashed_data))

        except ValueError as e:
            self.create_error_box(e)




