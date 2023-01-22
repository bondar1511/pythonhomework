# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc




path = r'14.01\text1.txt'
path1 = r'14.01\text.txt'
with open(path,'r') as data:
    str = data.read().split()
print(str)

def rle_encode(data):
    encoding = ''
    count = 1
    if not data:
         return ''
    for char in data:
        if char != str:
            if str:
                encoding+=str(count)+ str
                count = 1
                str = char
            else:
                count+=1
        else:
            encoding+=str(count)+ str
    return encoding
    

with open(path1,'w') as data:
    encoding = data.write().sprit()
print(encoding)

with open(path1,'r') as data:
    str = data.read().split()
print(str)
def  rle_decode(data):
    count = ''
    for char in data:
        if char.isdigit():
            count+=char
        else:
            str += char*int(count)
    return str
with open(path,'w') as data:
  str = data.write().split()
print(str)


