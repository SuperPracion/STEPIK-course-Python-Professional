from functools import partial


def send_email(name, email_address, text):
    return f'В письме для {name} на адрес {email_address} сказано следующее: {text}'


to_Timur = partial(send_email, 'timyrik20@beegeek.ru', text='123')
send_an_invitation = partial(send_email, text='Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....')

print(to_Timur('когда курс?'))