# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#

file_name = 'events.txt'
file_exit='file_exit.txt'
file = open(file_name, mode='r', encoding='utf8')
file_exit = open(file_exit, mode='w', encoding='utf8')

content_list = []

for line in file.readlines():
    if 'NOK' in line:
        content = line[0:17:] + ']'
        content_list.append(content)


for content in sorted(set(content_list)):
    file_exit.write((content) + ' ' + str(content_list.count(content)))
    file_exit.write('\n')
file.close()
file_exit.close()