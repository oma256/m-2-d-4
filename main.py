"""
1) Задача
Посчитать количество одинаковых элементов в списке
Дан список целых чисел. Посчитать, сколько раз в нем встречается каждое число.
Например, если дан список [1, 1, 3, 2, 1, 3, 4], то в нем число 1 встречается 
три раза, число 3 - два раза, числа 2 и 4 - по одному разу.
"""

# class MyList:

#     def __init__(self, num_list) -> None:
#         self.num_list = num_list
    
#     def get_num_rep_count(self):
#         result = {}

#         for num in self.num_list:
#             if num in result:
#                 result[num] += 1
#             else:
#                 result[num] = 1

        
#         for k, v in result.items():
#             print(f'Число {k} встречается {v}')

#     def __str__(self) -> str:
#         return f'Объект список: {self.num_list}'

# my_list = MyList([1, 1, 3, 2, 1, 3, 4])
# my_list.get_num_rep_count()
# print(my_list)


"""
2) Задача
В строке заменить пробелы символом *
В строке заменить пробелы звездочкой. Если встречается подряд несколько 
пробелов, то их следует заменить одним знаком "*", пробелы в начале и конце 
строки удалить.
"""

# class Star:

#     def __init__(self, text) -> None:
#         self.text = text
    
#     def replace_space_to_star(self):
#         result = ''
#         for t in self.text.strip().split():
#             result += t
#             result += '*'

#         print(result[:-1])

# star = Star('   Hello  Wor   ld!   ')
# star.replace_space_to_star()


"""
3) Задача
Напишите программу, которая принимает имя файла и выводит его расширение. 
Если расширение у файла определить невозможно, выбросите исключение.
"""

# import os


# class Path:
#     def __init__(self, path) -> None:
#         self.path = path

#     def get_files_ext(self):
#         for name in os.listdir(path=self.path):
#             if os.path.isfile(os.path.join(self.path, name)):
#                 if name.split('.')[-1] in ('pdf', 'txt', 'epub'):
#                     print(f"{name.split('.')[0]} - " 
#                           f"расширение {name.split('.')[-1]}")


# path = Path('/Users/oma/Desktop')
# path.get_files_ext()


"""
Задача 4
Сложите цифры целого числа 35732
"""

class Number:
    def __init__(self, number) -> None:
        self.number = number

    def get_num_sum(self):
        result = 0
        for n in str(self.number):
            result += int(n)
        
        return result


number = Number(number=35732)
print(number.get_num_sum())
