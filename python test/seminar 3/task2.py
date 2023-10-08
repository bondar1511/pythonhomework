# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, 
# а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.



def function_key(**kwargs):
 y_dict= {}
 y_dict = kwargs
 return {v if v.__hash__ is not None else str(v):k for k,v in y_dict.items()}

print(function_key(name="Anna",surname="Bondar",age=35, Citi= "Saratov", profession= "lawyer"))

