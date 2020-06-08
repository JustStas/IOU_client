import pandas as pd
import datetime
from classes import Trx, IOU, User
from connection import server_conn
from paths import trx_log_path, users_db_path


#
# def create_dbs():
#     trx_log = pd.DataFrame(columns=['trx_id', 'IOU_id', 'creditor_id', 'debtor_id', 'currency', 'amount', 'date'],
#                            data=[[0, 0, 0, 0, 'RUB', 0.00, datetime.datetime.now()]])
#     users_db = pd.DataFrame(columns=['user_id', 'f_name', 'l_name'],
#                             data=[[0, 'Stanislav', 'Nosulenko'],
#                                   [1, 'Oleg', 'Cock'],
#                                   [2, 'Andrey', 'BigBelly']])
#     trx_log.to_hdf(trx_log_path, key='df')
#     users_db.to_hdf(users_db_path, key='df')


def balance_overview(user_ids=-1):
    if user_ids == -1:
        user_ids = []
    elif isinstance(user_ids, list):
        pass
    elif isinstance(user_ids, int):
        user_ids = [user_ids]
    else:
        print('Wrong input')
        return
    users = server_conn('list_users')
    counterpart_ids = users.to_list()
    if not user_ids:
        user_ids = counterpart_ids

    for user_id in user_ids:
        print('=' * 50)
        user1 = User(user_id=user_id)
        user1.load()
        user1.describe()
        user1_balance = user1.balance()
        print('Accumulated debt:', user1_balance[0], 'RUB')
        print('Accumulated receivables:', user1_balance[1], 'RUB')

        remaining_users = [i for i in counterpart_ids if i != user1.user_id]

        for counterpart_id in remaining_users:
            user2 = User(user_id=counterpart_id)
            counterpart_balance = user1.balance(counterpart_id=user2.user_id)
            debt_to_counterpart = counterpart_balance[0]
            receivables_from_counterpart = counterpart_balance[1]
            if debt_to_counterpart != 0 or receivables_from_counterpart != 0:
                user2.load()
                user2.describe()
                print('-' * 20)
                print('Debt to {0}: {1} RUB:'.format(user2.f_name, debt_to_counterpart))
                print('Receivables from {0}: {1} RUB'.format(user2.f_name, receivables_from_counterpart))

# create_dbs()
# i_trx = Trx()
# i_trx.equal_split(debtors=[1, 2, 3])
