print('       **bienvenidos a la calculadora de genaro**')
#empezar el ciclo completo
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
    #determina la operacion a realizar
    operacion = int(input("""        ingresa el numero de la operacion que quieres realizar o
        presiona 0 para salir: """))
    #si presionan 0 rompen el ciclo
    if operacion == 0:
        break
    #solicita las cantidades a operar
    uno = int(input("introduce el primer numero: "))
    dos = int(input("introduce el segundo numero: "))
    #funciones que ejecutan las operaciones
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
   #comparan la operacion seleccionada
    elif operacion == 1:
        suma(uno, dos)
        
    elif operacion == 2:
        resta(uno, dos)
    
    elif operacion == 3:
        multiplicacion(uno, dos)
        
    elif operacion == 4:
        division(uno, dos)
        
    #terminar o volver a iniciar el ciclo
    opcion = input("deseas continuar? ")
    
    if opcion != "si" :
        print("hasta luego")
        break
    



   
