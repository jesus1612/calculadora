print('       **bienvenidos a la calculadora de genaro**')

while True:
    print('''
        ---------------------------------------------
        estas son las operaciones que puedes realizar
        1- suma
        ---------
        2- resta
        ---------
        3- multiplicacion
        ---------
        4- division
         ''')
    operacion = int(input("""        ingresa el numero de la operacion que quieres realizar o
        presiona 0 para salir: """))
    if operacion == 0:
        break
    
    uno = int(input("introduce el primer numero: "))
    dos = int(input("introduce el segundo numero: "))

    def suma(primero, segundo):
        resultado = primero + segundo
        print("el resultado es ", resultado)

    def resta(primero, segundo):
        resultado = primero - segundo
        print("el resultado es ", resultado)

    def multiplicacion(primero, segundo):
        resultado = primero * segundo
        print("el resultado es ", resultado)
    
    def division(primero, segundo):
        resultado = primero / segundo
        print("el resultado es", resultado)
    
    if operacion < 1 or operacion > 4:
        print("""------esa opción no esta en mis posibilidades :(--------
                 ------vuelve a intentarlo
                    """)
    elif operacion == 1:
        suma(uno, dos)
        
    elif operacion == 2:
        resta(uno, dos)
    
    elif operacion == 3:
        multiplicacion(uno, dos)
        
    elif operacion == 4:
        division(uno, dos)
        
    
    opcion = input("deseas continuar? ")
    
    if opcion != "si" :
        print("hasta luego")
        break
    



   
