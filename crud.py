comidas = []

def show_comidas():
    for comida in comidas:
        print(f"comidas { comida }")

def add_comida(comida):
    comidas.append(comida)
    

def del_comida(comida):
    try: 
        comidas.remove(comida) 
    except Exception:
        print("no se encontro en la lista")


text_menu = ''' 
elige una opcion
    1 - Agregar Comida
    2 - Eliminar Comida 
    3 - Mostrar Comida
    4 - Salir 
'''

while True:
    choice_user = int (input(text_menu))
    if choice_user == 1:
        comida = input("Escribe una comida: ")
        add_comida (comida)
    elif choice_user == 2:
        comida = input("escribe una comida para eliminar: ")
        del_comida (comida)
    elif choice_user ==3:
        show_comidas()
    elif choice_user == 4:
        break
    else:
        print ("Escribe bien carajo  :/")






