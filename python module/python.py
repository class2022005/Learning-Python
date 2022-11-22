#!/usr/bin/env python3
# #lst.insert(x,entry) #inserts a new entry
# #lst.pop() #erases the last entry in the list
# #del lst[1] #erases specific index entry
# variable = "Test"
# variable.upper() #prints it upper case
# variable.lower() #prints variable lower case
# print() #prints
# #'' string ''
# #' string '
# #'''string''' 
# liist = ['test',1,33.2,'Complex Sentences',[12,32.2,'test']] #mutable
# t = (variable,'variable',44.3, 44, True,['otherTest',1]) #last item of the tuple can be changed because it is a list
# #.clear() # clears a list

# #convert list to tuple
# Fist = [1, 2, 3, 4, 5]
# tupleList = tuple(Fist)
# #convert tuple to list
# listList = list(Fist)

# #* #multiplication
# #/ #division
# #// #division, returns integer number
# #** #exponent
# #% #modulus, returns remainder
# #+ #sum
# #- #subtraction
# #formatting strings
# var1 = "Kevin"
# var2 = "Nivek"
# "hello {}, how are you {}".format(var1,var2)
# "hello {1}, how are you {0}".format(var1,var2)
# list() # lists every single character separatelly
# var1.split() # lists every word by itself
# var1.split(' ') #splits at every space, or whatever is set to
# #replace last variable of a list
# root = 'root:x:0:0::/root:/etc/bash'
# root.split(':')
# listName = root.split(':')#lst.insert(x,entry) #inserts a new entry
# #lst.pop() #erases the last entry in the list
# #del lst[1] #erases specific index entry
# variable = "Test"
# variable.upper() #prints it upper case
# variable.lower() #prints variable lower case
# print() #prints
# #'' string ''
# #' string '
# #'''string''' 
# liist = ['test',1,33.2,'Complex Sentences',[12,32.2,'test']] #mutable
# t = (variable,'variable',44.3, 44, True,['otherTest',1]) #last item of the tuple can be changed because it is a list
# #.clear() # clears a list

# #convert list to tuple
# Fist = [1, 2, 3, 4, 5]
# tupleList = tuple(Fist)
# #convert tuple to list
# listList = list(Fist)

# #* #multiplication
# #/ #division
# #// #division, returns integer number
# #** #exponent
# #% #modulus, returns remainder
# #+ #sum
# #- #subtraction
# #formatting strings
# var1 = "Kevin"
# var2 = "Nivek"
# "hello {}, how are you {}".format(var1,var2)
# "hello {1}, how are you {0}".format(var1,var2)
# list() # lists every single character separatelly
# var1.split() # lists every word by itself
# var1.split(' ') #splits at every space, or whatever is set to
# #replace last variable of a list
# root = 'root:x:0:0::/root:/etc/bash'
# root.split(':')
# listName = root.split(':')
# listName[-1] = 'newValue'
# ':'.join(listName) #puts the list back together with the determined delimiter :
# #you can also split tuples
# coolInput = input('Give me something cool')
# a = 'apple'
# b = 'banana'
# c = 'carrot'

# print(a,b,c,sep='PYTHON')
# print(a,b,c,sep='\n')
# print(a,b,c,sep='CYBER',end='WARRIORS\n')

# filePointer = '/etc/passwd'
# filePointer.flush() #flushes the memory
# filePointer.writelines() #writes from file
# filePointer.close() #closes file
# filePointer.open() #open files
# filePointer.write() #writes stuff
# filePointer.read() #reads a file
# filePointer.rename(current, new_name) #renames a file

# with open('/etc/passwd') as fi, open('passwd.txt', 'w') as fo: #file in (reads the /file/path, file out gives the output of /file/path on the new file
#     for line in fi:
#         # line.replace('/bin/bash\n', '/bin/fsh/\n')
#         tmp = line.split(':')
#         tmp[-1] = '/bin/fish\n'
#         fo.write(':'.join(tmp))

# print(*lst)#lst.insert(x,entry) #inserts a new entry
# #lst.pop() #erases the last entry in the list
# #del lst[1] #erases specific index entry
# variable = "Test"
# variable.upper() #prints it upper case
# variable.lower() #prints variable lower case
# print() #prints
# #'' string ''
# #' string '
# #'''string''' 
# liist = ['test',1,33.2,'Complex Sentences',[12,32.2,'test']] #mutable
# t = (variable,'variable',44.3, 44, True,['otherTest',1]) #last item of the tuple can be changed because it is a list
# #.clear() # clears a list

# #convert list to tuple
# Fist = [1, 2, 3, 4, 5]
# tupleList = tuple(Fist)
# #convert tuple to list
# listList = list(Fist)

# #* #multiplication
# #/ #division
# #// #division, returns integer number
# #** #exponent
# #% #modulus, returns remainder
# #+ #sum
# #- #subtraction
# #formatting strings
# var1 = "Kevin"
# var2 = "Nivek"
# "hello {}, how are you {}".format(var1,var2)
# "hello {1}, how are you {0}".format(var1,var2)
# list() # lists every single character separatelly
# var1.split() # lists every word by itself
# var1.split(' ') #splits at every space, or whatever is set to
# #replace last variable of a list
# root = 'root:x:0:0::/root:/etc/bash'
# root.split(':')
# listName = root.split(':')
# listName[-1] = 'newValue'
# ':'.join(listName) #puts the list back together with the determined delimiter :
# #you can also split tuples
# coolInput = input('Give me something cool')
# a = 'apple'
# b = 'banana'
# c = 'carrot'

# print(a,b,c,sep='PYTHON')
# print(a,b,c,sep='\n')
# print(a,b,c,sep='CYBER',end='WARRIORS\n')

# filePointer = '/etc/passwd'
# filePointer.flush() #flushes the memory
# filePointer.writelines() #writes from file
# filePointer.close() #closes file
# filePointer.open() #open files
# filePointer.write() #writes stuff
# filePointer.read() #reads a file
# filePointer.rename(current, new_name) #renames a file

# with open('/etc/passwd') as fi, open('passwd.txt', 'w') as fo: #file in (reads the /file/path, file out gives the output of /file/path on the new file
#     for line in fi:
#         # line.replace('/bin/bash\n', '/bin/fsh/\n')
#         tmp = line.split(':')
#         tmp[-1] = '/bin/fish\n'
#         fo.write(':'.join(tmp))

# print(*lst)
# doSum(*arg) #will add up all elements in arg list

# dosum(*[int(num for num in lst)]) #will iterate 'numbers' for 'number' in 'list'. so it will do (for example) 10 times the number of 'numbers' in the list

# d: {'a':10, 'b':20, 'c':30, 'd':40}
# dosum(d) 
# doSum(*arg) #will add up all elements in arg list

# dosum(*[int(num for num in lst)]) #will iterate 'numbers' for 'number' in 'list'. so it will do (for example) 10 times the number of 'numbers' in the list

# d: {'a':10, 'b':20, 'c':30, 'd':40}
# dosum(d) imiter :
# #you can also split tuples
# coolInput = input('Give me something cool')
# a = 'apple'
# b = 'banana'
# c = 'carrot'

# print(a,b,c,sep='PYTHON')
# print(a,b,c,sep='\n')
# print(a,b,c,sep='CYBER',end='WARRIORS\n')

# filePointer = '/etc/passwd'
# filePointer.flush() #flushes the memory
# filePointer.writelines() #writes from file
# filePointer.close() #closes file
# filePointer.open() #open files
# filePointer.write() #writes stuff
# filePointer.read() #reads a file
# filePointer.rename(current, new_name) #renames a file

# with open('/etc/passwd') as fi, open('passwd.txt', 'w') as fo: #file in (reads the /file/path, file out gives the output of /file/path on the new file
#     for line in fi:
#         # line.replace('/bin/bash\n', '/bin/fsh/\n')
#         tmp = line.split(':')
#         tmp[-1] = '/bin/fish\n'
#         fo.write(':'.join(tmp))

# print(*lst)
# doSum(*arg) #will add up all elements in arg list

# dosum(*[int(num for num in lst)]) #will iterate 'numbers' for 'number' in 'list'. so it will do (for example) 10 times the number of 'numbers' in the list

# d: {'a':10, 'b':20, 'c':30, 'd':40}
# dosum(d) #in order to unpack a library into a function, we MUST match the variable names as to the library.

s = {1,2,3,4,5,3,3,2,2,4,5,5,3,3,3}
set(s)

# lambda is an "on demand, one liner functions" that may not appear again in the program

#encoding data with XOR

message = b"my hidden message"

def simple_xor(data):
    ct = bytearray()
    for index in range(len(data)):
        ct.append(data[index] ^ 1)
    return ct

if __name__ == "__main__":
    print(f'Simple XOR message:\n{message}')
    xor_simple_CT = simple_xor(message)
    print(f'\nSimple XOR CT:\n{xor_simple_CT}')
    print(f'Simple XOR message returned to original state:\n{simple_xor(xor_simple_CT)}')