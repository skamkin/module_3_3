def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    print()
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

list_ = ['Sergey', 234, False]
list_1 = ['Anton', 234]
dict_ = {'c':56}
print_params(*list_)
print_params(*list_1, 65)
print_params(*list_1,**dict_)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
