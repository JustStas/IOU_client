import pandas as pd
import datetime
from classes import Trx, IOU, User
from connection import server_conn


def balance_overview(user_ids=-1):
    to_print = ''

    if user_ids == -1:
        user_ids = []
    elif isinstance(user_ids, list):
        pass
    elif isinstance(user_ids, int):
        user_ids = [user_ids]
    else:
        to_print += '\nWrong input'
        return
    users = server_conn('list_users')
    counterpart_ids = users.to_list()
    if not user_ids:
        user_ids = counterpart_ids

    for user_id in user_ids:
        to_print += '\n'
        to_print += ('=' * 50)
        user1 = User(user_id=user_id)
        user1.load()
        to_print += '\n'
        to_print += user1.f_name
        user1_balance = user1.balance()
        to_print += '\n'
        to_print += ('Accumulated debt: {0} RUB'.format(user1_balance[0]))
        to_print += '\n'
        to_print += ('Accumulated receivables: {0} RUB'.format(user1_balance[1]))

        remaining_users = [i for i in counterpart_ids if i != user1.user_id]

        for counterpart_id in remaining_users:
            user2 = User(user_id=counterpart_id)
            counterpart_balance = user1.balance(counterpart_id=user2.user_id)
            debt_to_counterpart = counterpart_balance[0]
            receivables_from_counterpart = counterpart_balance[1]
            if debt_to_counterpart != 0 or receivables_from_counterpart != 0:
                user2.load()
                to_print += '\n'
                to_print += ('-' * 20)
                to_print += '\n'
                to_print += ('Debt to {0}: {1} RUB:'.format(user2.f_name, debt_to_counterpart))
                to_print += '\n'
                to_print += ('Receivables from {0}: {1} RUB'.format(user2.f_name, receivables_from_counterpart))
    print(to_print)
    return to_print
