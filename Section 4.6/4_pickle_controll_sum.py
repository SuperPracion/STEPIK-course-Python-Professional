import pickle


def comparison_control_sum(file_name, control_sum):
    with open(file_name, 'rb') as file:
        objects = pickle.load(file)
        lst = [num for num in objects if type(num) == int] or [0]

        if type(objects) == list:
            return (max(lst) * min(lst)) == control_sum
        else:
            return (sum(lst)) == control_sum


file_name = input()
control_sum = int(input())

print('Контрольные суммы совпадают' if comparison_control_sum(file_name, control_sum) else 'Контрольные суммы не совпадают')