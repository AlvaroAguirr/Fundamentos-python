#ciclos


#while Exp_ booleana


i=1 
num =7

while i <=10:
    print(f"{num }* {i} = {num * i}")
    i +=1

else:( "termina el ciclo")


# ciclo for 
#permite reccorer iterables
# iterable -> objeto que se puede recorrer
# for item in iterable:

my_string= "hola a todos"
for letter in my_string:
    print(letter, end =', ')
print()

my_list =["uno", "dos", "tres", "cuatro"]
for item in my_list:
    print(item, end= ", ")
    print()

#funciones range()
#range (end)
for i in range (10):
    print(i, end=", ")
print()

#range (start, end)

for i in range(10,20):
    print(i, end=", ")
print()

#range (start, end, step)
for i in range(10,100, 10):
    print(i, end=", ")
print()
