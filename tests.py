import core
from connection import server_conn
import pandas as pd
from classes import Trx

import socket




print(server_conn('list_users', verbose=True))

#
#
# trx = Trx(creditor_id=0)
# trx.equal_split([0,1,2])
# #
# #
# core.balance_overview()

# server_conn('reset_databases')