def likes(names):
    out_message = ''

    match len(names) if len(names) - 1 < 4 else 4:
        case 0: out_message = 'Никто не оценил данную запись'
        case 1: out_message = f'{names[0]} оценил(а) данную запись'
        case 2: out_message = f'{names[0]} и {names[1]} оценили данную запись'
        case 3: out_message = f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
        case 4: out_message = f'{names[0]}, {names[1]} и {len(names) - 2} других оценили данную запись'

    return out_message

print(likes(['Тимур', 'Артур']))