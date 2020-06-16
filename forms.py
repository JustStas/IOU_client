import tkinter as tk
from classes import User
from tkinter import messagebox
global f_name_out_label, l_name_out_label, debt_out_label, receivables_out_label


class WindowUserOverview: # todo check why text displays incorrectly after multiple pushes of the Load button
    def __init__(self):
        # Creating windows
        self.user_overview = tk.Tk()

        # Creating and placing elements
        # labels
        self.username_label = tk.Label(self.user_overview, text='User ID:')
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
            f_name_out_label.destroy()
            l_name_out_label.destroy()
            debt_out_label.destroy()
            receivables_out_label.destroy()

        else:
            f_name_out_label = tk.Label(self.user_overview, text=user.f_name)
            f_name_out_label.grid(row=2, column=1)

            l_name_out_label = tk.Label(self.user_overview, text=user.l_name)
            l_name_out_label.grid(row=3, column=1)

            balance = user.balance()

            debt_out_label = tk.Label(self.user_overview, text=balance[0])
            debt_out_label.grid(row=4, column=1)

            receivables_out_label = tk.Label(self.user_overview, text=balance[1])
            receivables_out_label.grid(row=5, column=1)


