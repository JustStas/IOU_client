import tkinter as tk
import pandas as pd
from paths import users_db_path
from tkinter import messagebox


users_df = pd.read_hdf(users_db_path, key='df')
global f_name_out_label, l_name_out_label, debt_out_label, receivables_out_label


def load_user_button_click():
    global f_name_out_label, l_name_out_label, debt_out_label, receivables_out_label
    try:
        user_id = user_id_entry.get()
        user_line = users_df.loc[users_df['user_id'] == user_id]

        f_name_out_label = tk.Label(user_overview, text=user_line['f_name'].iloc[0])
        f_name_out_label.grid(row=2, column=1)

        l_name_out_label = tk.Label(user_overview, text=user_line['l_name'].iloc[0])
        l_name_out_label.grid(row=3, column=1)

        debt_out_label = tk.Label(user_overview, text=user_line['debt'].iloc[0])
        debt_out_label.grid(row=4, column=1)

        receivables_out_label = tk.Label(user_overview, text=user_line['receivables'].iloc[0])
        receivables_out_label.grid(row=5, column=1)
    except IndexError:
        messagebox.showwarning('Error', 'No such user exists')
        f_name_out_label.destroy()
        l_name_out_label.destroy()
        debt_out_label.destroy()
        receivables_out_label.destroy()


# Creating windows
user_overview = tk.Tk()
#new_trx = tk.Tk()

# Creating and placing elements
# labels
user_id_label = tk.Label(user_overview, text='User ID:')
user_id_label.grid(row=0, column=0, pady=10)

f_name_label = tk.Label(user_overview, text='First name:')
f_name_label.grid(row=2, column=0, sticky=tk.W)

l_name_label = tk.Label(user_overview, text='Last name:')
l_name_label.grid(row=3, column=0, sticky=tk.W)

user_debt_label = tk.Label(user_overview, text='Debt:')
user_debt_label.grid(row=4, column=0, sticky=tk.W)

user_receivables_label = tk.Label(user_overview, text='Receivables:')
user_receivables_label.grid(row=5, column=0, sticky=tk.W)

# buttons
load_user_button = tk.Button(user_overview, text='Load', width=10, command=load_user_button_click)
load_user_button.grid(row=0, column=2, padx=10)

# entry
user_id_entry = tk.Entry(user_overview)
user_id_entry.grid(row=0, column=1)



user_overview.mainloop()