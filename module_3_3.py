def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(a = 1, b = 'строка', c = True)
print_params(c = True)
print_params(a = 1, c = True)
print_params()
print_params(a = 1, b = 25, c = True)
print_params(a = 1, b = 25, c = [1,2,3])

values_list = [False, 3, 'ok']
values_dict = {'a':False, 'b':3, 'c':'ok'}

def print_params(*values_list, **values_dict):
    print(*values_list)
    print(values_dict)

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print(*values_list_2)

print_params(*values_list_2, 42)

