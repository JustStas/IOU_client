import core
from connection import server_conn
import pandas as pd
from classes import Trx, User

import socket



#
# print(max(server_conn('list_users')))
# server_conn('reset_databases')
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
core.balance_overview([0,1])
