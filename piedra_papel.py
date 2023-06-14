#Elecion de maquina
import random

num_rand = random.randint(1,3)
if num_rand==1:
    choice_maq ='piedra'
elif num_rand==2:
    choice_maq ='papel'
else:
    choice_maq ='tijeras'


# Eleccion usuario

choice_text = '''
Escribe una opcion:
    piedra
    papel
    tijeras
 '''
choice_user = input(choice_text)
#Imprime eleccion 
print("usuario elige:", choice_user)
print("maquina elige:", choice_maq)

#Define ganador 
if choice_user == choice_maq:
    print("Es un empate")
else:
    if choice_user == 'piedra' and choice_maq== 'papel':
        print("gana la maquina")
    elif choice_user == 'piedra' and choice_maq== 'tijeras':
        print("gana usuario!")
    elif choice_user == 'papel' and choice_maq== 'piedra':
        print("gana usuario!")
    elif choice_user == 'papel' and choice_maq== 'tijeras':
        print("gana la maquina!")
    elif choice_user == 'tijeras' and choice_maq== 'piedra':
        print("gana la maquina!")
    elif choice_user == 'tijeras' and choice_maq== 'papel':
        print("gana usuario!")
    else:
        print("escribe bien Usuario")
