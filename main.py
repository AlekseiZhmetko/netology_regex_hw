from pprint import pprint
import csv
import re

if __name__ == "__main__":

  with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

  pattern = r"(\+7|8)\s?\(?(\d{3})\)?\s?-?(\d{3})\s?-?(\d{2})\s?-?(\d{2})(\s?)(?:(\(?)(([а-яА-Яa-zA-Z.]*\)?)\s+?(\d*)(\)?))?)"
  replacement = r"+7(\2)\3-\4-\5\6\9\10"

  cont_dict = {}
  dict_to_merge = {}

  for i in contacts_list:
    name = ' '.join(i[0:3]).split(' ')
    del name[3:]
    i[0:3] = name[0:3]
    i[5] = re.sub(pattern, replacement, i[5])
    a = i[0] + ' ' + i[1]
    b = i[2:]
    i_dict = {a: b}
    # print(i_dict)
    for k, v in i_dict.items():
      if k not in cont_dict.keys():
        cont_dict.update(i_dict)
      else:
        dict_to_merge.update(i_dict)

  # print()
  # print('Выводим cont_dict')
  # pprint(cont_dict)
  # print()
  # print('Выводим dict_to_merge')
  # pprint(dict_to_merge)

  for k, v in dict_to_merge.items():
    for k1, v1 in cont_dict.items():
      if k == k1:
        merged_data = [x or y for x, y in zip(v1, v)]
        cont_dict[k1] = merged_data

  # print()
  # print('Выводим после слияния')
  # pprint(cont_dict)

  clean_contacts_list = []

  for k, v in cont_dict.items():
    a = k.split() + v
    b = [','.join(a)]
    clean_contacts_list.append(b)

  # pprint(clean_contacts_list)

with open("phonebook.csv", "w", encoding='utf-8', newline='') as f:
  datawriter = csv.writer(f)
  datawriter.writerows(clean_contacts_list)