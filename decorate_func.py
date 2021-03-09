# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'


# def log_errors(func):
#     def surogate(*args):
#         try:
#             res = func(*args)
#             return res
#         except Exception as exc:
#             file_name = 'function_errors.log'
#             with open(file_name, mode='a', encoding='utf8') as file:
#                 print(f'Ловим ошибку - {exc}.')
#                 file.write(f'Имя функции - {func.__name__} Параметры функции - {args} Ошибка - {type(exc)} Текст ошибки - {exc}\n')
#
#     return surogate




# Проверить работу на следующих функциях
# @log_errors
# def perky(param):
#     return param / 0
# # res = perky(3)
# # print(res)
# #
# @log_errors
# def check_line(line):
#     name, email, age = line.split(' ')
#     if not name.isalpha():
#         raise ValueError("it's not a name")
#     if '@' not in email or '.' not in email:
#         raise ValueError("it's not a email")
#     if not 10 <= int(age) <= 99:
#         raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
# for line in lines:
#     try:
#         check_line(line)
#     except Exception as exc:
#         print(f'Invalid format: {exc}')



# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass

def log_error(file):
    def log_errors(func):
        def surogate(*args):
            file_name = file
            try:
                res = func(*args)
                return res
            except Exception as exc:

                with open(file_name, mode='a', encoding='utf8') as ffile:
                    print(f'Ловим ошибку - {exc}.')
                    ffile.write(f'Имя функции - {func.__name__} Параметры функции - {args} Ошибка - {type(exc)} Текст ошибки - {exc}\n')

        return surogate
    return log_errors

@log_error(file='new_function_errors.log')
def perky(param):
    return param / 0

res = perky(3)
print(res)