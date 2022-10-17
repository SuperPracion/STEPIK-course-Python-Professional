from datetime import *

def is_correct(day, month, year):
    is_correct_flag = True

    try:
        date(year, month, day)
    except:
        is_correct_flag = False

    return is_correct_flag
