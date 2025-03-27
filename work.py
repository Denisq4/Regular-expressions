from pprint import pprint
import csv
import re
#+7 (495) 913-11-11 (доб. 0792)

PATTERN = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
PATTERN_PHONE_SUB = r'7(\2)-\3-\4-\5\6\7'

with open('phonebook_raw.csv', 'r', encoding='utf-8') as f:
    start_list = csv.reader(f, delimiter=",")
    info_list = list(start_list)

filter_list = list()

for item in info_list:
    fio = ' '.join(item[:3]).split(' ')
    number_ordering = re.sub(PATTERN, PATTERN_PHONE_SUB, item[5])
    new_list = [fio[0], fio[1], fio[2], item[3], item[4], number_ordering, item[6]]
    filter_list.append(new_list)

result = list()

for ready in filter_list:
    last_name = ready[0]
    first_name = ready[1]
    for new_ready in filter_list:
        new_last_name = new_ready[0]
        new_first_name = new_ready[1]
        if last_name == new_last_name and first_name == new_first_name:
            if ready[2] == '':
                ready[2] = new_ready[2]
            if ready[3] == '':
                ready[3] = new_ready[3]
            if ready[4] == '':
                ready[4] = new_ready[4]
            if ready[5] == '':
                ready[5] = new_ready[5]
            if ready[6] == '':
                ready[6] = new_ready[6]
for i in filter_list:
    if i not in result:
        result.append(i)


with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result)
