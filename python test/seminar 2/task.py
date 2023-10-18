# from collections import Counter
# import re
# def frequent_words(text):
#     text = re.findall(r'\w+', text.lower())
#     counter = Counter(text)
#     frequent = counter.most_common(10)

#     return (frequent)
# text = input()
# res  = frequent_words(text)
# print(res)

def fill_backpack(things, max_weight):
     def recursive_fill(remaining_stuff, remaining_weight, current_backpack):
        if remaining_weight < 0:
             return []
        if not remaining_things:
             return [current_backpack]

        results = []
        item, weight = remaining_things[0]
        remaining_things = remaining_things[1:]
        results.extend(recursive_fill(remaining_things, remaining_weight - weight, current_backpack + [(item, weight)]))
        results.extend(recursive_fill(remaining_things, remaining_weight, current_backpack))

        return results
  initial_backpack = []
  all_options = recursive_fill(list(things.items()), max_weight, initial_backpack)
  return all_options
things = {}
max_weight = 1.0
result = fill_backpack(things, max_weight)
print(result)

# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
def get_file_info(path):
    dir_path, full_filename = path.rsplit("/", 1)
    name, file_ext = full_filename.split(".", 1)
    
    return dir_path, name, f".{file_ext}"


file_path = "C:/Users/User/Documents/example.txt"
directory, filename, file_extension = get_file_info(file_path)
my_tuple = (directory, filename, file_extension)
print(my_tuple)
