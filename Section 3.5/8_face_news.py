from datetime import *


def choose_plural(amount, declensions):
    out_res = f'{amount} {declensions[2]}'

    dict_value = {0: [1, 21, 41, 61, 31, 51, 71, 91],
                  1: [2, 3, 4, 22, 23, 24, 42, 43, 44, 62, 63, 64, 82, 83, 84, 32, 33, 34, 52, 53, 54, 72, 73, 74, 92,
                      93, 94]}

    for key, value in dict_value.items():
        if amount % 100 in value:
            out_res = f'{amount} {declensions[key]}'

    return out_res


declensions = {0: ("день", "дня", "дней"), 1: ("час", "часа", "часов"), 2: ("минута", "минуты", "минут")}
today_is = datetime.strptime(input(), '%d.%m.%Y %H:%M')
date_of_course = datetime(year=2022, month=11, day=8, hour=12, minute=0)


if today_is < date_of_course:
    time_left = date_of_course - today_is
    stay_times = [time_left.days, time_left.seconds // 60 // 60, time_left.seconds % 60]

    break_flag = 0
    for time in range(3):

        if break_flag == 2:
            break

        if stay_times[time] != 0:
            if break_flag != 0:
                print(' и ', end='')
            print(choose_plural(stay_times[time], declensions[time]))
            break_flag += 1

else:
    print('Курс уже вышел!')
