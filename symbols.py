
start_1, start_2, start_3 = '{', '(', '['
finish_1, finish_2, finish_3 = '}', ')', ']'
start_symbols = [start_1, start_2, start_3]
finish_symbols = [finish_1, finish_2, finish_3]
string = '[({}())]'
# if string.count(start_1) == string.count(finish_1) and string.count(start_2) == string.count(finish_2) and string.count(start_3) == string.count(finish_3):
#     print('OK')
# else:
#     print('NOK')

symbol = string[0]
