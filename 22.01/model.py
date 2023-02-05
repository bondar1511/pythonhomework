
list = ''
list = list.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').split()
list = []
def get_list():
  global list
  return list

def calculate():
  i = 0
  while i < (len(list)):
      if list[i]=='*':
        list[i-1] = int(list[i-1])*int(list[i+1])
        del list[i]
        del list[i]
        i+=1  
        list[i] 
      return list  
      

  i=0
  while i < (len(list)):  
      if list[i]=='/':
        list[i-1] = int(list[i-1])/int(list[i+1])
        del list[i]
        del list[i]
        i+=1
        return list
     

  while'+' in list or '-' in list:
       i=0
       while i < (len(list)):
        if list[i]=='+':
         list[i-1] = int(list[i-1])+int(list[i+1])
         del list[i]
         del list[i]
        elif list[i]=='-':
          list[i-1] = int(list[i-1])-int(list[i+1])
          del list[i]
          del list[i]
          i+=1     
        return list[0]



