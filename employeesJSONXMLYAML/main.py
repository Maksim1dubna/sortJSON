import json
from operator import itemgetter
def employees_rewrite(sort_type):
    with open('employees.json', "r") as json_file:
        data = json.load(json_file)
        switch = False
        if type(data['employees'][0][sort_type]) is int:
            switch = True
        data['employees'] = sorted(data['employees'], key=lambda x: x[sort_type], reverse=switch)

        with open(f'employees_[{sort_type}]_sorted.json', 'w', encoding='utf-8') as json_file_write:
            json.dump(data, json_file_write, ensure_ascii=False,indent=4)
        return data
print(employees_rewrite('salary'))

