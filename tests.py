import core
from connection import server_conn
import pandas as pd
from classes import Trx, User
from pprint import pprint as pp
from forms import WindowUserOverview, NewTRX
from paths import users_db_path

import socket



#
# print(max(server_conn('list_users')))
#
#
# i=0
# while True:
#     i+=1
#     trx = Trx(creditor_id=1)
#     trx.equal_split([0,1,2])
#     print(i)
# #
# #

#def print_users():
#    users = pd.read_hdf(users_db_path, key='df')
#    print(users)

# # trx.describe()
# user_pair = {'debtor_id': 0, 'creditor_id': 1}
# receivables = server_conn('amount_check', user_pair)
# print(receivables)

# user1 = User(user_id=1)
# user2 = User(user_id=0)
#
# print(user1.balance(counterpart_id=user2.user_id))

# user = User(user_id=9)
# user.load()
# user.describe(short=False)
# core.balance_overview([0,1])
#print_users()
WindowUserOverview()
# NewTRX()
# print(server_conn('list_trx'))