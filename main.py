"""
1) Задача
Посчитать количество одинаковых элементов в списке
Дан список целых чисел. Посчитать, сколько раз в нем встречается каждое число.
Например, если дан список [1, 1, 3, 2, 1, 3, 4], то в нем число 1 встречается 
три раза, число 3 - два раза, числа 2 и 4 - по одному разу.
"""

class MyList:

    def __init__(self, num_list) -> None:
        self.num_list = num_list
    
    def get_num_rep_count(self):
        result = {}

        for num in self.num_list:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1

        
        for k, v in result.items():
            print(f'Число {k} встречается {v}')

    def __str__(self) -> str:
        return f'Объект список: {self.num_list}'

my_list = MyList([1, 1, 3, 2, 1, 3, 4])
my_list.get_num_rep_count()
print(my_list)
