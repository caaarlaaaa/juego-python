import random


lista_palabras = ['perro', 'actor', 'tigre', 'leona', 'manos', 'nariz', 'vivir', 'juego', 'reloj', 'mango', 'pulpo', "zorro","huevo","zorra"+]
    
palabra= random.choice(lista_palabras)
print(lista_palabras)
    
#Si no aciertas 
ganar= False 

#Itentos 
for i in range(0,5):
        
    intento= input("dime una palabra.")
    if intento == palabra:        
        ganar = True  
        break
       
#Cuando acierta
if ganar == True: 
    print("¡Lo has adivinado!")
else:
    print("¡Has perdido")




