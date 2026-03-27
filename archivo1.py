from itertools import count


print("Hola mundo, escrito desde python y el cual será actualizado en git-hub") #un simple print

listaNumber1  = [1,2,3,4,5,6,7,8,9,10] # una cadena de numeros
contador = 0 # contador para saber el numero que toca
for number in listaNumber1: # ciclo para mostrar los numeros
    print(f"{contador}: numero ingresado: {number}")
    contador = contador + 1 # incrementa el contador

print("Este es un print escrito desde GitHub") # imprime una linea de texto

if(len(listaNumber1) <= 10):
    print("su lista tiene 10 o menos numeros")
else:
    print("su lista tiene mas de 10 numeros")