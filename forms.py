import tkinter as tk
from classes import User
from tkinter import messagebox
global f_name_out_label, l_name_out_label, debt_out_label, receivables_out_label


class WindowUserOverview:
    def __init__(self):
        # Creating windows
        self.user_overview = tk.Tk()

        # Creating and placing elements
        # labels
        self.username_label = tk.Label(self.user_overview, text='Usename:')
        self.username_label.grid(row=0, column=0, pady=10)

        self.f_name_label = tk.Label(self.user_overview, text='First name:')
        self.f_name_label.grid(row=2, column=0, sticky=tk.W)

        self.l_name_label = tk.Label(self.user_overview, text='Last name:')
        self.l_name_label.grid(row=3, column=0, sticky=tk.W)

        self.user_debt_label = tk.Label(self.user_overview, text='Debt:')
        self.user_debt_label.grid(row=4, column=0, sticky=tk.W)

        self.user_receivables_label = tk.Label(self.user_overview, text='Receivables:')
        self.user_receivables_label.grid(row=5, column=0, sticky=tk.W)

        # buttons
        self.load_user_button = tk.Button(self.user_overview, text='Load', width=10,
                                          command=self.load_user_button_click)
        self.load_user_button.grid(row=0, column=2, padx=10)

        # entry
        self.username_entry = tk.Entry(self.user_overview)
        self.username_entry.grid(row=0, column=1)

        self.user_overview.mainloop()

    def load_user_button_click(self):
        global f_name_out_label, l_name_out_label, debt_out_label, receivables_out_label

        user = User(username=self.username_entry.get())
        user.load(offer_to_create=False)

        if user.user_id == -1:
            messagebox.showwarning('Error', 'User not found')
            try:
                f_name_out_label.destroy()
                l_name_out_label.destroy()
                debt_out_label.destroy()
                receivables_out_label.destroy()
            except NameError:
                pass

        else:
            try:
                f_name_out_label.destroy()
                l_name_out_label.destroy()
                debt_out_label.destroy()
                receivables_out_label.destroy()
            except NameError:
                pass

            f_name_out_label = tk.Label(self.user_overview, text=user.f_name)
            f_name_out_label.grid(row=2, column=1)

            l_name_out_label = tk.Label(self.user_overview, text=user.l_name)
            l_name_out_label.grid(row=3, column=1)

            balance = user.balance()

            debt_out_label = tk.Label(self.user_overview, text=balance[0])
            debt_out_label.grid(row=4, column=1)

            receivables_out_label = tk.Label(self.user_overview, text=balance[1])
            receivables_out_label.grid(row=5, column=1)


class NewTRX:
    def __init__(self):
        # creating main window
        self.insert_trx_window = tk.Tk()

        # creating frames
        self.input_frame = tk.LabelFrame(self.insert_trx_window, padx=5, pady=3)
        self.input_frame.grid(row=0,column=0)

        self.button_frame = tk.LabelFrame(self.insert_trx_window, padx=5, pady=5)
        self.button_frame.grid(row=2, column=1)

        # Creating and placing elements
        # labels
        self.name_label = tk.Label(self.input_frame, text='Name')
        self.name_label.grid(row=0, column=0, padx=5, pady=5)

        self.date_label = tk.Label(self.input_frame, text='Date')
        self.date_label.grid(row=1, column=0, padx=5, pady=5)

        self.volume_label = tk.Label(self.input_frame, text='Volume')
        self.volume_label.grid(row=2, column=0, padx=5, pady=5)

        self.creditor_label = tk.Label(self.input_frame, text='Creditor')
        self.creditor_label.grid(row=3, column=0, padx=5, pady=5)

        # entry
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.grid(row=0, column=1)

        self.date_entry = tk.Entry(self.input_frame)
        self.date_entry.grid(row=1, column=1)

        self.volume_entry = tk.Entry(self.input_frame)
        self.volume_entry.grid(row=2, column=1)

        self.creditor_entry = tk.Entry(self.input_frame)
        self.creditor_entry.grid(row=3, column=1)

        self.insert_trx_window.mainloop()
