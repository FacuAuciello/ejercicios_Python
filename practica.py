#PRACTICANDO PARCIAL
#Ejercicios faciles
#--------------------------------------------------------------------------------------------  
#Pedir un número y decir si es mayor, menor o igual a 0.

#numeroUsuario = int (input("Ingresa un numero: "))

#if numeroUsuario > 0:
#    print (f"{numeroUsuario} es mayor que 0")
#elif numeroUsuario < 0:
#    print (f"{numeroUsuario} es menor que 0")
#elif numeroUsuario == 0:
#    print ("El numero ingresado es igual 0")
#--------------------------------------------------------------------------------------------  
#ingresar una edad y mostrar si la persona es mayor de edad (18 años o más).

#mayorDeEdad = 18
#edadPersona = int (input("Ingresa tu edad: "))

#if edadPersona > mayorDeEdad:
#    print ("Sos mayor de edad")
#elif edadPersona == mayorDeEdad:
#    print ("18. Mayor edad")
#else:
#    print ("Sos menor de edad")
#--------------------------------------------------------------------------------------------  
#Mostrar los números del 1 al 10 usando un while.

#contador = 1
#while contador <= 10:
#    print ("Numeros: ", contador)
#    contador = contador + 1
#--------------------------------------------------------------------------------------------  
#Pedir un número y mostrar su tabla de multiplicar hasta el 10

#contador = 0
#numeroIngresado = int (input("Ingresa un numero: "))

#while contador < 10:
#    contador = contador + 1
#    resultado = contador * numeroIngresado
#    print (numeroIngresado, " X ", contador, " = ", resultado )
#--------------------------------------------------------------------------------------------  
#Pedir dos números y mostrar el mayor.

#num1 = int (input("Ingresa un numero: "))
#num2 = int (input("Ingresa otro numero: "))

#if num1 > num2:
#    print (f"{num1} es mayor que {num2}")
#elif num1 < num2:
#    print (f"{num1} es menor que {num2}")
#else:
#    print (f"{num1} = {num2}")
#--------------------------------------------------------------------------------------------  
#Contar del 10 al 1 (de manera descendente) usando un for

#for numeros in range (10, 0, -1):
#    print (numeros)
#--------------------------------------------------------------------------------------------  
#Crear una lista con los números del 1 al 5 e imprimirla

#listaNumeros = [1, 2, 3, 4, 5]
#print (listaNumeros)
#--------------------------------------------------------------------------------------------  
#EJERCICIOS INTERMEDIOS
#Pedir números al usuario hasta que ingrese un número negativo, y luego mostrar la suma total.

#usuarioNumeros = 0
#sumaTotal = 0
#usuarioNumeros = int (input("Ingresa un numero: ")) #Si se cumple ingresa

#while usuarioNumeros >= 0:
#    sumaTotal = sumaTotal + usuarioNumeros
#    usuarioNumeros = int (input("Ingresa un numero: "))

#print ("La suma total es de:", sumaTotal)
#--------------------------------------------------------------------------------------------  
#Leer 5 números y guardar sólo los números pares en una lista. Mostrar la lista final.

#listaNumeros = []

#for numeros in range (1,6,1):
#    numeros = int (input("Ingresa un numero: "))
#    if numeros % 2 == 0:
#        listaNumeros.append(numeros)

#print (listaNumeros)
#--------------------------------------------------------------------------------------------  
#Dada una lista, mostrar cuántos elementos mayores a 10 contiene.

#numeros = [5, 3, 10, 20, 35]
#contador = 0

#for numero in numeros: #Recorriendo la lista
#    if numero > 10:
#        contador = contador + 1

#print (f"La lista tiene {contador} numeros mayores a 10")
#--------------------------------------------------------------------------------------------  
#Pedir 10 nombres al usuario y guardar solo los que tengan más de 5 letras

#guardarNombres = []

#for nombres in range (1,11,1):
#    nombres = str (input("Ingresa un nombre: "))
    
#    if len(nombres) > 5:
#        guardarNombres.append(nombres)
        
#print (guardarNombres)
#--------------------------------------------------------------------------------------------  
#Crear un programa que recorra una lista de números y cuente cuántos son pares y cuántos impares.

#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#contadorPar = 0
#contadorImpar = 0

#for numeros in (lista):
#    if numeros % 2 == 0:
#        contadorPar = contadorPar + 1
#    else:
#        contadorImpar = contadorImpar + 1

#print (f"Numeros pares: {contadorPar}")
#print (f"Numeros impares {contadorImpar}")
#--------------------------------------------------------------------------------------------        
#Leer 5 números y mostrar el máximo y el mínimo de la lista.

#lista = []

#for numeros in range (1,6,1):
#    numeros = int (input("Ingresa un numero: "))
#    lista.append(numeros)

#print ("Numero maximo: ",max(lista)) #directamente en el print para sacar el max y el min
#print ("Numero minimo: ",min(lista))
#-------------------------------------------------------------------------------------------- 

#Pedir palabras hasta que el usuario ingrese "salir", luego mostrar todas las palabras juntas en una lista

#palabras = []

#usuarioEntrada = str (input("Ingresa una palabra: "))
#while usuarioEntrada != "salir":
#    usuarioEntrada = str (input("Ingresa una palabra: "))
    
#    if usuarioEntrada != "salir":
#        palabras.append(usuarioEntrada)
#    elif usuarioEntrada == "salir":
#        print ("Hasta luego")

#print ("Palabras ingresadas: ", palabras)
#-------------------------------------------------------------------------------------------- 

#EJERCICIOS AVANZANDOS
#Pedir 10 números y crear dos listas: una con los números mayores a 50 y otra con los números menores o iguales a 50.

#listaMayores50 = []
#listaMenores50 = []

#for numeros in range (1,11,1):
#    numeros = int (input("Ingresa un numero: "))

#    if numeros > 50:
#        listaMayores50.append(numeros)
#    elif numeros <= 50:
#        listaMenores50.append(numeros)

#print (f"Lista mayores: {listaMayores50}")
#print (f"Lista menores: {listaMenores50}")
#--------------------------------------------------------------------------------------------

#Crear una lista de números aleatorios entre 1 y 100 (usar random.randint) y luego ordenarla de menor a mayor.
#import random #importo la libreria para los numeros random

#numerosRandom = []

#for numeros in range (1,11,1):
#    numerosRandom.append(random.randint(1, 100)) #aplico los numeros random con random.randint
#    numerosRandom.sort() #el sort es para ordenar de menor a mayor

#print (numerosRandom)
#--------------------------------------------------------------------------------------------

#Pedir un número y verificar si ese número está en una lista ya definida

#numeros = [1, 5, 112, 28]

#usuarioNumero = int (input ("Ingresa un numero: "))

#if usuarioNumero in numeros:
#        print (f"El numero {usuarioNumero} esta dentro de la lista")
#else:
#        print (f"El numero {usuarioNumero} no esta dentro de la lista")  
#--------------------------------------------------------------------------------------------

#Dada una lista de palabras, crear otra lista que contenga sólo las palabras que empiecen con vocal

#palabras = ["argentina", "valor", "elefante", "oidos", "caca", "programacion"]
#listaVocales = []
#vocales = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

#for i in palabras:
#    if i[0] in vocales:
#        listaVocales.append(i)

#print(listaVocales)
#--------------------------------------------------------------------------------------------

#Simular un carrito de compras: el usuario puede agregar productos a una 
#lista hasta que escriba "terminar", luego mostrar el carrito final y la cantidad de productos.

#listaCompras = []
#usuarioCompras = ""
#acumuladorProductos = 0

#usuarioCompras = str (input("Ingresar producto al carrito: "))
#while usuarioCompras != "terminar":
#    listaCompras.append(usuarioCompras)
#    acumuladorProductos = acumuladorProductos + 1
#    usuarioCompras = str (input("Ingresar producto al carrito: "))

#print ("Carrito final: ", listaCompras)
#print ("Cantidad de productos: ", acumuladorProductos)
#--------------------------------------------------------------------------------------------


#Estructuras secuenciales (1 a 5)
#1)Conversor de temperaturas: Pedí una temperatura en °C y convertí a °F y °K. 
# Mostrá ambas conversiones.

#temperaturaC = int (input("Ingresa una temperatura en °C: "))

#temperaturaF = (temperaturaC * 9/5) + 32
#temperaturaK = temperaturaC + 273.15

#print (f"{temperaturaC} °C")
#print (f"{temperaturaF} °F")
#print (f"{temperaturaK} °K")
#--------------------------------------------------------------------------------------------


#2)Área y perímetro de figuras: Pedí al usuario una figura (círculo, cuadrado, triángulo) y calculá su área y perímetro.

#figura = str (input("Ingresa una figura: "))

#if figura == "circulo":
#    radio = float (input("Ingresa el radio: "))
#    area = 3.14 * radio ** 2
#    perimetro = 2 * 3.14 * radio
#    print (f"circulo: Area {area} Perimetro {perimetro}")
#elif figura == "cuadrado":
#    lado = float (input("Ingresa un lado: "))
#    area = lado * lado
#    perimetro = 4 * lado
#    print (f"cuadrado: Area {area} Perimetro {perimetro}")
#elif figura == "triangulo":
#    base = float (input("Ingresa su base: "))
#    altura = float (input("Ingresa su altura: "))
#    lado1 = float (input("Ingresa un lado: "))
#    lado2 = float (input("Ingresa un lado: "))
#    lado3 = float (input("Ingresa un lado: "))
#    area = (base * altura)/2
#    perimetro = lado1 + lado2 + lado3
#    print (f"triangulo: Area {area} Perimetro {perimetro}")
#else:
#    print ("Figura no valida")
#--------------------------------------------------------------------------------------------

#3)Promedio con decimales: Pedí 3 notas con coma y mostrale al usuario el promedio con dos decimales.
#infoNotas = (input("Ingresa tus notas con coma si es necesario (Apreta enter para continuar)"))
#nota1 = float (input("Nota uno: "))
#nota2 = float (input("Nota dos: "))
#nota3 = float (input("Nota tres: "))

#promedio = (nota1 + nota2 + nota3) //3

#print (f"Promedio: {promedio}")
#--------------------------------------------------------------------------------------------

#4)Descuento aplicado: Pedí precio y porcentaje de descuento, y mostrale el precio final.

#precio = int (input("Ingresa el precio del producto: "))
#porcentajeProducto = int (input("Ingresa el descuento que dice la etiqueta (10%, 20%, 30%): "))

#if porcentajeProducto == 30:
#    precioFinal = precio * (1 - porcentajeProducto /100)
#    print (f"Precio final: {precioFinal}")
#elif porcentajeProducto == 20:
#    precioFinal = precio * (1 - porcentajeProducto /100)
#    print (f"Precio final: {precioFinal}")
#elif porcentajeProducto == 10:
#    precioFinal = precio * (1 - porcentajeProducto /100)
#    print (f"Precio final: {precioFinal}")
#else:
#    print ("Ingresa un porcentaje correcto")
#--------------------------------------------------------------------------------------------

#5)Suma de cifras: Pedí un número de 3 cifras y mostrale la suma de sus cifras (usá int(str(...)[i]) o divisiones).

#numeroUsuario = int (input("Ingresa un numero de tres cifras: "))

#centena = numeroUsuario // 100
#decena = (numeroUsuario // 10) % 10
#unidad = numeroUsuario % 10

#print (f"{numeroUsuario} = {centena} + {decena} + {unidad}")
#--------------------------------------------------------------------------------------------

#Condicionales (6 a 10)
#Par, impar o cero: Pedí un número y decí si es par, impar o cero.

#numeroUsuario = int (input("Ingresa un numero: "))

#if numeroUsuario == 0:
#    print (f"{numeroUsuario} es CERO")
#elif numeroUsuario % 2 == 0:
#    print (f"{numeroUsuario} es PAR")
#else:
#    print (f"{numeroUsuario} es IMPAR")
#--------------------------------------------------------------------------------------------

#7)Mayor y menor de tres: Pedí tres números y decí cuál es el mayor y cuál el menor (sin usar max() ni min()).

#numero1 = int (input("Ingresa un numero: "))
#numero2 = int (input("Ingresa un numero: "))
#numero3 = int (input("Ingresa un numero: "))

#if numero1 > numero2 and numero1 > numero3:
#    print (f"{numero1} es MAYOR que {numero2} y {numero3}")
#elif numero2 > numero1 and numero2 > numero3:
#    print (f"{numero2} es MAYOR que {numero1} y {numero3}")
#elif numero3 > numero1 and numero3 > numero2:
#    print (f"{numero3} es MAYOR que {numero1} y {numero2}")
#--------------------------------------------------------------------------------------------

#8)Evaluador de contraseñas: Compará la contraseña ingresada con una predefinida y permití solo 3 intentos.

#password = "LebronJames"
#intentos = 0
#intentosMaximos = 3

#while intentos < intentosMaximos:
#    claveIngresada = str (input("Ingresa la clave: "))
    
#    if claveIngresada == password:
#        print ("Password correcta. Ingresando...")
#        break
#    else:
#        intentos = intentos + 1
#        print ("Password incorrecto.")

#if intentos == intentosMaximos:
#    print ("Alcanzaste el limite maximo de intentos. Vuelva mas tarde")
#--------------------------------------------------------------------------------------------

#9)Números iguales o distintos: Pedí dos números y mostrale si son iguales, o cuál es mayor y cuál es menor.

#Try intenta ejecutar el codigo y si hay un error (ingresar una letra) salta al bloque except
#Se usa cada vez que el codigo pueda fallar por algo que no controle directamente
#Usar Cada vez que el codigo depende de algo externo, como un usuario que se equivoque.
#try:
#    num1 = int (input("Ingresa el primer numero: "))
#    num2 = int (input("Ingresa el segundo numero: "))

#    if num1 == num2:
#        print (f"{num1} = {num2}")
#    elif num1 > num2:
#        print (f"{num1} es mayor que {num2}")
#    else:
#        print (f"{num1} es menor que {num2}")
#except:
#    print ("Error. Ingresa un numero.")
#--------------------------------------------------------------------------------------------

#10)Aprobado o desaprobado con condiciones: Si el promedio de 3 notas es mayor a 6, aprobado. 
# Pero si alguna es menor a 4, desaprobado igual.
#try:
#    nota1 = int(input("Ingresa la primer nota: "))
#    nota2 = int(input("Ingresa la segunda nota: "))
#    nota3 = int(input("Ingresa la tercer nota: "))

#    promedio = (nota1 + nota2 + nota3)/3

#    if nota1 <= 4 or nota2 <= 4 or nota3 <= 4:
#        print ("Estas DESAPROBADO (Una o mas notas son 4)")
#    elif promedio >= 6:
#        print ("Estas APROBADO")
#except:
#    print ("ERROR. Ingresa un numero.")
#--------------------------------------------------------------------------------------------

#Estructuras repetitivas (11 a 15)
#11) Sumar hasta un número: Pedí un número N y sumá todos los números del 1 al N.

#numero = int (input("Ingresa un numero: "))
#suma = 0

#for i in range (1,numero + 1,1):
#    suma = suma + i

#print (suma)
#--------------------------------------------------------------------------------------------

#12)Contador de pares e impares: Pedí 10 números y contá cuántos son pares y cuántos impares.

#contadorPares = 0
#contadorImpares = 0

#for i in range (1,11,1):
#    numeros = int (input("Ingresa un numero: "))

#    if numeros % 2 == 0:
#        contadorPares = contadorPares + 1
#    else:
#        contadorImpares = contadorImpares + 1

#print (f"Total numeros PARES: {contadorPares}")
#print (f"Total numeros IMPARES: {contadorImpares}")
#--------------------------------------------------------------------------------------------

#13)promedio hasta 'salir': El usuario ingresa notas hasta que escribe "salir". Mostrá el promedio.

#suma = 0
#cantidadNotas = 0

#ingresarNota = input("Ingresa una nota: ")
#while ingresarNota != "Salir":
    
#    ingresarNota = input("Ingresa una nota: ")
#    suma = suma + ingresarNota 
#   promedio = suma / cantidadNotas
    
#print (f"Promedio: {promedio}")
#--------------------------------------------------------------------------------------------

#LISTAS
#14)#Buscar un elemento: Pedí al usuario una lista de palabras y una palabra a buscar. Decí si está en la lista.

#lista = []

#for i in range (1,6,1):
#    palabrasLista = str (input("Ingresa palabras para una lista: "))
#    lista.append(palabrasLista)

#busquedaPalabra = str (input("Ingresa una palabra a buscar dentro de la lista: "))

#if busquedaPalabra in lista:
#    print(f"{busquedaPalabra} esta en la lista")
#else:
#    print (f"{busquedaPalabra} no esta en la lista")
#--------------------------------------------------------------------------------------------

#UTN EJERCICIOS COMPLEMENTARIOS
#Dada una lista de palabras, realizar las siguientes acciones:
#Mostrar cuántas palabras tienen exactamente 7 letras.
#Crear una nueva lista con las palabras que terminan en "o" o en "a".
#Preguntar al usuario una sílaba (por ejemplo, “ar”) y mostrar todas las palabras que la contengan.
#Mostrar la palabra más larga de la lista.
#palabras = ["computadora", "teclado", "pantalla", "ratón", "código", "memoria", "proceso"]

#palabras = ["computadora", "teclado", "pantalla", "raton", "codigo", "memoria", "proceso"]
#contador = 0

#for palabra in palabras: #No hace falta numeros porque ya recorro IN palabras
#    if len(palabra) == 7:
#        contador = contador + 1

#print (f"Cantidad de palabras con 7 letras: {contador}")

#terminanOyA = []

#for terminaciones in palabras:
#    if terminaciones.endswith("a") or terminaciones.endswith("o"):
#        terminanOyA.append(terminaciones)

#print (f"Lista actualizada de palabras que terminan en A/O: {terminanOyA}")

#palabraLarga = max(palabras, key=len)

#print (f"La palabra mas larga de la lista es: {palabraLarga}")
#-------------------------------------------------------------------------------------

#Carga de nombres y búsqueda de repetidos
#Crear un programa que:
#Pida al usuario ingresar nombres hasta que escriba "FIN".
#Agregue los nombres a una lista.
#Luego del ingreso:
#Mostrar cuántos nombres se ingresaron.
#Mostrar los que tienen más de 5 letras.
#Decir si hay nombres repetidos.

#lista = []
#contador = 0

#nombres = str (input("Ingresa nombres: (Si escribis FIN se cierra el programa)"))
#while nombres.lower() != "fin":
#    lista.append(nombres)
#    contador = contador + 1
#    nombres = str (input("Ingresa nombres: (Si escribis FIN se cierra el programa)"))

#print (f"Nombres ingresados: {lista}")

#for nombre in lista:
#    if len(nombre) > 5:
#        print (f"Nombres con mas de 5 letras: {nombre}")

#repetidos = []

#for nombre in lista:
#    if lista.count(nombre) > 1 and nombre not in repetidos:
#        repetidos.append(nombre)

#if repetidos:
#    print("Nombres repetidos:", repetidos)
#else:
#    print("No hay nombres repetidos.")
#-------------------------------------------------------------------------------------

#Lista de compras editable
#Crear un programa que:
#Permita al usuario agregar productos a una lista hasta que escriba "listo".
#Luego, mostrar la lista numerada.
#Preguntar si quiere quitar algún producto y, si sí, permitirlo hasta que escriba "no".
#Mostrar la lista final con un mensaje tipo: "Lista preparada para ir al súper."

#Creaste lista y parate listo
#productos = []
#contador = 0

#usuarioAgregar = str (input("Ingresa un producto - ('listo' para dejar de ingresar):"))
#while usuarioAgregar.lower() != "listo":
#    productos.append(usuarioAgregar)
#    contador = contador + 1
#    usuarioAgregar = str (input("Ingresa un producto - ('listo' para dejar de ingresar):"))

#mostrasdo la lista enumerada
#indice = 1
#for producto in productos:
#    print (f"{indice}){producto}")
#    indice = indice + 1

#Si el usuario quiere quitar un producto o no. Eliminar si asi desea.
#preguntaUsuario = str (input("Queres quitar algun producto: (S/N)"))

#if preguntaUsuario.lower() == "s":
#    productoEliminar = str (input("Ingresa producto a eliminar de la lista: "))
#    if productoEliminar in productos:
#        productos.remove(productoEliminar)
#        print(f"{productoEliminar} fue eliminado de la lista")
#elif preguntaUsuario == "n":
#    print(f"Lista preparada para ir al super: {productos}")
#else:
#    print ("El producto no esta en la lista")
#-------------------------------------------------------------------------------------

#Lista de edades y promedio
#Pedí al usuario 5 edades, guardalas en una lista y mostrá el promedio. 
#Luego, decí cuántos son mayores de edad.

#Lista y pedido de edades. Actualiza lista.
#edades = []

#for recorrer in range (1,6,1):
#    ingresoEdades = int (input("Ingresa una edad: "))
#    edades.append(ingresoEdades)

#Promedio de edades
#promedioEdades = sum(edades) / 5

#Mayor edad, contador y for para ver cuanta cantidad son mayor de edad
#mayorDeEdad = 18
#contador = 0

#for edad in edades:
#    if edad >= mayorDeEdad:
#        contador = contador + 1

#print (f"Edades ingresadas: {edades}")
#print (f"Promedio de edades ingresadas: {promedioEdades}")
#print (f"Mayores de edad: {contador}")
#-------------------------------------------------------------------------------------

#Validador de DNI
#Pedí un número de DNI y validá que tenga entre 7 y 8 cifras. Si no es válido, pedilo de nuevo hasta que lo sea.

#pedirDNI = (input("Ingresa tu DNI: "))
#while len(pedirDNI) != 8:
#    print ("DNI INVALIDO. Debes ingresar 8 numeros")
#    pedirDNI = (input("Ingresa tu DNI: "))
    
#print ("DNI VALIDO")  
#-------------------------------------------------------------------------------------

#Validar fecha de nacimiento
#Pedí el día, mes de nacimiento y anio. Valida si es correcto o no

#ingresoNacimiento = (input("Ingresa tu fecha de nacimiento (Todo junto sin espacios): ")) 

#dia = ingresoNacimiento[0:2]
#mes = ingresoNacimiento[2:4]
#anio = ingresoNacimiento[4:8]

#print(f"{dia}/{mes}/{anio}")

#while len(ingresoNacimiento) != 8:
#    print ("ERROR. Ingresa 8 numeros")
#    ingresoNacimiento = (input("Ingresa tu fecha de nacimiento (Todo junto sin espacios): "))

#validacion = input (f"{ingresoNacimiento} es correcto? Responde S/N: ")

#if validacion.lower() == "s":
#    print ("Fecha de nacimiento ingresada")
#elif validacion.lower() == "n":

    #while validacion.lower() != "s":
#        ingresoNacimiento = (input("Ingresa de nuevo la fecha: "))
#        dia = ingresoNacimiento[0:2]
#        mes = ingresoNacimiento[2:4]
#        anio = ingresoNacimiento[4:8]
#        print(f"{dia}/{mes}/{anio}")
        
#        validacion = input (f"{ingresoNacimiento} es correcto? Responde S/N: ")
#        if validacion.lower() == "s":
#            print ("Fecha de nacimiento ingresada")
#-------------------------------------------------------------------------------------

#Funciones
#Simulador de pase libre. Recibe edad y si tiene documento. Si tiene más de 65 o menos de 10, y tiene documento

#def paseLibre (edad, tieneDocumento):
#    if tieneDocumento:
#        pregunta = str(input("Tenes el documento? RESPONDE Si/No"))
#        if pregunta.lower() == "si":
#            tieneDocumento = True
#            print("Documento VERIFICADO")
#            if edad >= 65 or edad <= 10:
#                print ("PASE LIBRE")
#            else:
#                print ("NO tiene edad para PASE LIBRE")
#        else:
#            print ("Documento NO VERIFICADO. Sin importar la edad debera abonar.")
#        
#edad = int(input("Ingresar edad: "))
#tieneDocumento = True

#paseLibre(edad, tieneDocumento)
#-------------------------------------------------------------------------------------

#Control de stock. Recibe dos números y devuelve el stock restante. 
#Si el resultado es menor a 0, devuelve "Error: stock insuficiente".

#def actualizarStock (stockActual, vendidos):
#    print(stockActual - vendidos)
#    if (stockActual - vendidos) <= 0:
#        print ("STOCK INSUFICIENTE")

#stockActual = int(input("Ingresa el numero de stock actual de productos: "))
#vendidos = int(input("Ingresa el numero de productos vendidos: "))

#actualizarStock(stockActual, vendidos)
#-------------------------------------------------------------------------------------
#Practicando variables

#Solicitá al usuario su nombre, apellido, edad y ciudad de residencia

#nombre = "lebron"
#apellido = "james"
#edad = 38
#ciudad = "Los angeles"

#print(f"Hola, mi nombre es {nombre} {apellido}, tengo {edad} anios y vivo en la ciudad de {ciudad}")

#Pedile al usuario un número entero. Convertilo a string y mostrá el tipo de dato antes y después de la conversión.

#ingresa_numero = int(input("Ingresa un numero: "))

#print(type(ingresa_numero))
#ingresa_numero = str(ingresa_numero)
#print(type(ingresa_numero))

#Pedile al usuario una frase y mostrá cuántos caracteres tiene (usá len())

#usuario_frase = input("Ingresa una frase: ")
#print(len(usuario_frase))

#Declarar 4 variables en una sola línea: nombre, apellido, alias, edad. Luego imprimilas en un mensaje

#nombre, apellido, alias, edad = "Kobe", "Bryant", "BLACK-MAMBA", 40
#print(f"Soy {nombre} {apellido}, me dicen {alias} y mi edad es {edad}")

#inicializá una variable con un tipo de dato (por ejemplo, string), luego asignale un valor de otro tipo (por ejemplo, bool, int, float). Mostrá su valor y su tipo en cada paso.

#valor = "hola"
#print(type(valor))

#valor = 2
#print(type(valor))

#valor = 2.5
#print(type(valor))

#valor = True
#print(type(valor))
#-------------------------------------------------------------------------------------
# Operadores Aritméticos

#Pedile al usuario dos números enteros y calculalos

#a = int(input("Ingresa un numero"))
#b = int(input("Ingresa un numero"))

#suma = a + b
#print(suma)
#resta = a - b
#print(resta)
#multiplicacion = a * b
#print(multiplicacion)
#division = a / b
#print (division)

#Pedile al usuario dos números y decile si el primero es múltiplo del segundo usando el operador módulo (%).

#a = int(input("Ingresa un numero"))
#b = int(input("Ingresa un numero"))

#if a % b == 0:
#    print(f"{a} es multiplo de {b}")
#else:
#    print("No es multiplo")

#Pedile dos palabras al usuario y decile cuál tiene más letras. Si tienen la misma longitud, avisale también.

#palabra1 = str(input("Ingresa una palabra: "))
#palabra2 = str(input("Ingresa una palabra: "))

#if len(palabra1) > len(palabra2):
#    print(f"{palabra1} tiene mas letras que {palabra2}")
#elif len(palabra2) > len(palabra1):
#    print(f"{palabra2} tiene mas letras que {palabra1}")
#else:
#    print("Ambas tienen la misma cantidad de letras")

#pedile al usuario una palabra y un número. Mostrá la palabra repetida 2 elevado a ese número de veces.

#palabra = str(input("Ingresa una palabra: "))
#numero = int(input("Ingresa un numero: "))

#print(palabra * (2**numero))

#Pedile tres números al usuario: A, B y C. Mostrá en pantalla si se cumple la siguiente condición lógica

#a = input("ingresa un numero: ")
#b = input("ingresa un numero: ")
#c = input("ingresa un numero: ")

#if (a > b and b > c) or (c == a):
#    print(f"A={a}, B={b}, C={c}: Se cumple")
#else:
#    print(f"A={a}, B={b}, C={c}: No se cumple")
#-------------------------------------------------------------------------------------

#Pedile una palabra al usuario y decile cuántas veces aparece la letra "a"

#palabra = str(input("Ingresa una palabra: "))

#print(palabra.count("o"))
#otra opcion
#cantidad = palabra.count("o")
#print(f'La letra "o" aparece {cantidad} veces') #comillas simples y dobles

#Pedile al usuario su nombre y mostralo escrito al revés usando slicing

#nombre = input("Ingresa tu nombre: ")

#nombre_al_reves = nombre[::-1]
#print(nombre_al_reves)

#Pedile un dato al usuario y mostrá si es un número o no usando .isnumeric()

#dato = input("Ingresa un dato: ")

#print(dato.isnumeric()) Pedile una frase al usuario. Mostrá: Las primeras 3 letras. La frase con salto de línea. La frase con tabulación

#palabra = input("Ingresa una palabra: ")

#tres_primeras = palabra[0:3]
#print(f"Primeras 3 letras {tres_primeras}")

#salto_linea = "string con\nsalto de linea"
#print(salto_linea)

#frase_tabulacion = "\tstring con tabulacion"
#print(frase_tabulacion)
#-------------------------------------------------------------------------------------

### Lists ###

#Pedile al usuario que ingrese 5 números enteros y guardalos en una lista. Luego imprimí la lista completa y cuántos elementos tiene.

#a, b, c, d, e = 1, 2, 3, 4, 5

#lista = []
#lista.append(a)
#lista.append(b)
#lista.append(c)
#lista.append(d)
#lista.append(e)
#print(f'La lista tiene {len(lista)} elementos')

#accede a elemenos de una lista fija. El primero, el del medio y el ultimo

#colores = ["rojo", "azul", "amarillo", "violeta", "blanco"]

#print(colores[0])
#print(colores[2])
#print(colores[4])

#Pedile al usuario que ingrese 4 números. Después preguntale qué número quiere buscar y decile cuántas veces aparece en la lista.

#a = input("Ingresa un numero: ")
#b = input("Ingresa un numero: ")
#c = input("Ingresa un numero: ")
#d = input("Ingresa un numero: ")

#lista = [a, b, c, d]

#busqueda = input("Que numero queres buscar de los que ingreaste: ")

#if busqueda in lista:
#    cantidad = lista.count(busqueda)
#    print(f"El numero {busqueda} aparece {cantidad} veces.")
#else:
#    print("El numero no se encuentra entre los ingresados.")

#Actualiza elementos de la lista. Reemplaza la segunda fruta por una que el usuario indique

#frutas = ["manzana", "banana", "frutillas", "mandarinas"]

#usuario = str(input("Ingresa una fruta que quiera actualizar: "))
#frutas[1] = usuario
#print(frutas)

#Pedile al usuario qué nombre quiere eliminar y usá .remove() para quitarlo. Mostrá la lista actualizada

#frutas = ["manzana", "banana", "frutillas", "mandarinas"]

#busqueda = str(input("Que fruta queres eliminar de los que ingreaste: "))

#if busqueda in frutas:
#    frutas.remove(busqueda)
#    print(frutas)
#else:
#    print("Ingresa una fruta que se encuentre en la lista")

#Creá una lista con los días de la semana, sin incluir "miércoles". Insertalo en la posición correcta y mostrá la lista completa.

#dias = ["Lunes", "martes", "jueves", "viernes"]

#dias.insert(2,"miercoles")
#print(dias)

#Ordenala de menor a mayor, Después invertí el orden (de mayor a menor). Mostrá ambas listas

#numeros = [4, 1, 7, 3, 9]

#numeros.sort()
#print(numeros)
#numeros.reverse()
#print(numeros)

#Creá una sublista con los elementos del índice 1 al 3 (inclusive el 1, exclusivo el 3). Copiá la lista original, vaciá la original con .clear(), y mostrá ambas.

#nombres = ["Luna", "Sol", "Estrella", "Nube", "Cielo"]

#print(nombres[0:3])
#nombres_copia = nombres.copy()
#nombres.clear()

#print(f"Lista original: {nombres}")
#print(f"Lista copiada: {nombres_copia}")
#-------------------------------------------------------------------------------------

### Tuples ###

#Creá una tupla con 3 datos tuyos: nombre, edad, y ciudad. Mostrá la tupla y su tipo

#mi_tupla = "gordo", 23, "mdp"
#print(type(mi_tupla))

#Mostrá el primer y el último elemento usando índices positivos y negativos

#datos = ("Facu", 25, "Rosario", "Argentina")

#print(datos[0])
#print(datos[-1])

#Mostrá:Cuántas veces aparece "rojo". En qué índice aparece "amarillo"

#colores = ("rojo", "azul", "verde", "rojo", "amarillo", "rojo")

#print(f"El color rojo aparece {colores.count('rojo')} veces y {colores.count('amarillo')} veces")

#Creá dos tuplas con 3 números cada una. Concatenalas en una nueva tupla y mostrá la suma de todos los números.

#tupla1 = (1,2,3)
#tupla2 = (4,5,6)

#suma_tuplas = tupla1 + tupla2
#print(suma_tuplas)
#suma_total = sum(suma_tuplas)
#print(suma_total)

#Modificar una tupla (con conversión)Convertila a lista, cambiá la ciudad por otra, agregá un alias y volvela a convertir a tupla.

#datos = ("Facu", 25, "Brasil")

#datos = list(datos)
#datos.append("Torales")
#print(type(datos))
#datos = tuple(datos)
#print(type(datos))
#-------------------------------------------------------------------------------------

### Sets ###

#Crear un set sin repetidos. Pedile al usuario que ingrese 5 palabras, algunas repetidas. Guardalas en un set y mostrá cuántas palabras únicas ingresó.

#a = str(input("Ingresa una palabra: "))
#b = str(input("Ingresa una palabra: "))
#c = str(input("Ingresa una palabra: "))
#d = str(input("Ingresa una palabra: "))
#e = str(input("Ingresa una palabra: "))

#mi_set = {a, b, c, d, e}
#print(f"Ingresaste {len(mi_set)} palabras unicas ")

#Buscar si una palabra existe. Con un set de frutas predefinido, preguntale al usuario si quiere saber si cierta fruta está o no.

#frutas = {"banana", "manzana", "pera", "naranja"}

#que_fruta = str(input("Que fruta buscas?: "))
#if que_fruta in frutas:
#    print(f"{que_fruta} esta dentro del set de frutas")
#else:
#    print(f"{que_fruta} no se encuentra dentro del set de frutas")

#Eliminar elementos duplicados de una lista. Dada una lista con elementos repetidos, convertí la lista en set para eliminar duplicados y luego volvé a convertirla en lista

#numeros = [1, 2, 2, 2, 3, 3, 4, 5, 6, 6]

#numeros = set(numeros)
#print(type(numeros))
#print(numeros)

#numeros = list(numeros)
#print(type(numeros))
#print(numeros)

#Unión de dos sets. Creá dos sets de lenguajes que conocés y querés aprender. Unilos y mostrá el resultado sin duplicados.

#conozco = {"python", "html", "javascript"}
#quiero_aprender = {"java", "rust", "c++", "kotlin", "flutter"}

#union_sets = conozco.union(quiero_aprender)
#print(union_sets)

#Con los mismos sets del ejercicio anterior, mostrá los lenguajes que querés aprender pero todavía no sabés

#conozco = {"python", "html", "javascript"}
#quiero_aprender = {"java", "rust", "c++", "kotlin", "flutter"}

#union_sets = conozco.union(quiero_aprender)
#print(union_sets.difference(conozco))

#-------------------------------------------------------------------------------------

### Dictionaries ###

#Crear un diccionario con tus datos. Creá un diccionario llamado persona con estas claves:"nombre""edad""ciudad"

#mi_diccionario = {"Nombre": "Agustin", "Apellido": "Lopez", "Edad": 28}
#otra forma
#mi_diccionario = {
#    "Nombre": "Agustin",
#    "Apellido": "Lopez",
#    "Edad": 28
#}
#print(mi_diccionario)

#Agregar y actualizar datos.Usando el diccionario anterior (persona): Agregale una nueva clave "profesion" con el valor "Estudiante".Cambiá el valor de "edad" por uno nuevo.Mostrá el diccionario actualizado.

#mi_diccionario = {
#    "Nombre": "Agustin",
#    "Apellido": "Lopez",
#    "Edad": 28
#}

#mi_diccionario["Profesion"] = "Carpintero"
#mi_diccionario["Edad"] = 41
#print(mi_diccionario)

#Contar cuántas claves tiene. Creá un diccionario con al menos 5 claves. Mostrá cuántas claves tiene y luego mostrá solo las claves y solo los valores por separado.

#autos_GT3 = {
#    1:"Mercedes",
#    2:"BMW",
#    3:"Mclaren",
#    4:"Audi",
#    5:"Ferrari"
#}

#print(f"Tiene {len(autos_GT3)} claves")
#print(autos_GT3.keys())
#print(autos_GT3.values())

#Eliminar una clave de un diccionario. Usá del para eliminar la clave "profesion" del diccionario persona y mostrale al usuario cómo quedó el diccionario.

#mi_diccionario = {
#    "Nombre": "Agustin",
#    "Apellido": "Lopez",
#    "Edad": 28,
#    "Profesion":"Carpintero"
#}

#del mi_diccionario["Profesion"]
#print(mi_diccionario)

#Crear un nuevo diccionario desde una lista de claves. Creá una lista con estas claves: ["nombre", "edad", "email"]. Luego usá fromkeys para crear un nuevo diccionario con esas claves y todos los valores iguales a "Desconocido". Mostralo.

#lista = ["nombre", "edad", "email"]
#diccionario = dict.fromkeys(lista, "default")
#print(diccionario)
#-------------------------------------------------------------------------------------

### Conditionals ### ciclos/Loops/bucles

#contador while

#contador = 0
#while contador < 10:
#    contador += 1
#    print(contador)

#Contar pares e impares. Pedile al usuario 6 números y contá cuántos son pares y cuántos impares

#contador_pares = 0
#contador_impares = 0

#for numeros in range(6):
#    usuario_ingreso = int(input("Ingresa un numero: "))
#    if usuario_ingreso % 2 == 0:
#        contador_pares +=1
#    else:
#        contador_impares +=1
#print(f"PARES: {contador_pares}. IMPARES: {contador_impares}")

#Pedile al usuario números uno por uno hasta que ingrese 0. Mostrá la suma total.

#acumulador = 0
#ingreso_numeros = int(input("Ingresa un numero: "))
#while ingreso_numeros != 0:
#    ingreso_numeros = int(input("Ingresa un numero: "))
#    acumulador += ingreso_numeros
#print(acumulador)
#-------------------------------------------------------------------------------------

### Functions ###

#def saludo():
#    print("Hola chaval")

#saludo()

#Creá una función llamada multiplicar_dos_numeros(a, b) que reciba dos números y muestre el resultado

#def multiplicar_dos_numeros(a, b):
#    print(f"El resultado es {a * b}")

#multiplicar_dos_numeros(3, 3)

#Creá una función promedio(lista) que reciba una lista de números y devuelva el promedio.

#lista = [9,8,7]

#def lista_numeros(lista):
#    promedio = sum(lista) / len(lista)
#    return promedio

#resultado = lista_numeros(lista)
#print(f"El promedio es: {resultado}")

#Función con parámetro por defecto. Creá una función presentarse(nombre, ciudad="desconocida") que imprima un mensaje

#def presentarse(nombre, ciudad="desconocido"):
#    print(f"Hola soy {nombre} y mi ciudad es {ciudad}")

#presentarse("facu")

#Función con cantidad variable de textos. Creá una función listar_palabras(*palabras) que reciba cualquier cantidad de palabras y las imprima una por una en mayúsculas, con su número de orden

#def listar_palabras(*palabras):
#    for j, palabra in enumerate(palabras, start=1):
#        print(f"{j}. {palabra.upper()}")

#listar_palabras("python", "hola", "clase")

#-------------------------------------------------------------------------------------

### Classes ###

#Clase Perro simple

#class perro:
#    def __init__(self, nombre):
#        self.nombre = f"{nombre} esta ladrando"

#perro_nombre = perro("Larry")
#print(perro_nombre.nombre)

#Creá una clase Auto que tenga: un atributo modelo, un atributo velocidad (arranca en 0), un método acelerar() que aumente la velocidad en 10, un método frenar() que baje la velocidad en 5

#class auto:
#    def __init__(self, modelo):
#        self.modelo = modelo
#        self.velocidad = 0
    
#    def acelerar(self):
#        self.velocidad += 10
#        print(f"{self.modelo} esta aumentando la velocidad. Velocidad actual: {self.velocidad}km")

#    def frenar(self):
#        if self.velocidad >= 5:
#            self.velocidad -= 5
#        else:
#            self.velocidad = 0
#        print(f"{self.modelo} freno. Velocidad actual: {self.velocidad}km")

#mi_auto = auto("BMW")  
#mi_auto.acelerar()  
#mi_auto.frenar()    

#lase CuentaBancaria con propiedad privada
#Creá una clase CuentaBancaria que tenga:un atributo privado __saldo, un método depositar(monto), un método retirar(monto), un método ver_saldo() que muestre el saldo actual. Asegurate de que no se pueda acceder directamente a __saldo desde afuera.

#class cuentaBancaria:
#    def __init__(self):
#        self.__saldo = 20000
    
#    def depositar(self, monto):
#        self.__saldo += monto
#        print(f"{monto} fue depositado correctamente")
    
#    def retirar(self, monto):
#        if monto <= self.__saldo:
#            resta = self.__saldo - monto
#            print(f"Retiraste {resta}")
#        else:
#            print("Fondos insuficientes")

#    def ver_saldo(self):
#        print(f"El saldo actual es de {self.__saldo}")

#mi_cuenta = cuentaBancaria()
#mi_cuenta.ver_saldo()
#mi_cuenta.depositar(500)
#mi_cuenta.retirar(2000)
#mi_cuenta.ver_saldo()

#Clase Alumno con método promedio
#Creá una clase Alumno que reciba:nombre, una lista de notas. Agregá un método calcular_promedio() que devuelva el promedio de sus notas.

#class Alumno:
#    def __init__(self, nombre, notas):
#        self.nombre = nombre
#        self.notas = notas
        
    
#    def calcular_promedio(self):
#        promedio = sum(self.notas) / len(self.notas)
#        return promedio

#mi_alumno = Alumno("Facu", [8,6,10])
#print(f"Nombre: {mi_alumno.nombre}")
#print(f"Promedio: {mi_alumno.calcular_promedio()}")

#-------------------------------------------------------------------------------------

# +funciones y class

#Nivel 1
#1)Función de saludo personalizado
#Crear una función saludar(nombre) que reciba un nombre e imprima: "Hola, [nombre]!".

#2)Función que calcule el doble
#Crear una función doble(numero) que retorne el doble del número ingresado.

#3)Clase Persona con atributos simples
#Crear una clase Persona que tenga un atributo nombre y una función presentarse() que imprima "Hola, me llamo [nombre]".

#1)
#def saludar(nombre):
#    print(f"hola {nombre}")

#saludar("Marisa")

#2)
#def doble(numero):
#    return numero * 2

#print(doble(2)) #si quiero ver como funciona, es correcto print, llamado y parametro

#3)
#class Persona:
#    def __init__(self, nombre):
#        self.nombre = nombre

#    def presentarse(self):
#        print(f"Hola, me llamo {self.nombre}")

#mi_persona = Persona("Carlos")
#mi_persona.presentarse()

#Nivel 2
#1)Función que calcule el promedio de una lista
#Crear una función calcular_promedio(lista) que reciba una lista de números y retorne el promedio.

#2)Clase Producto con precio e IVA.
#Crear una clase Producto con atributos nombre y precio. Agregar un método precio_con_iva() que retorne el precio más el 21% de IVA.

#3)Clase Alumno con notas.
#Crear una clase Alumno con atributos nombre y notas (lista). Agregar un método calcular_promedio() que devuelva el promedio de las notas.

#1)
#def calcular_promedio(lista):
#    promedio = sum(lista) / len(lista)
#    return promedio

#print(calcular_promedio([8, 9, 6, 8]))

#2)
#class Producto:
#    def __init__(self, nombre, precio):
#        self.nombre = nombre
#        self.precio = precio

#    def precio_con_iva(self):
#        calcular_iva = self.precio * 1.21 #iva en argentina es del 21%
#        return calcular_iva

#mi_producto = Producto("Placa de video", 500000)
#print(mi_producto.nombre)
#print(mi_producto.precio)
#print(mi_producto.precio_con_iva())

#3)
#class Alumno:
#    def __init__(self, nombre, notas):
#        self.nombre = nombre
#        self.notas = notas
    
#    def calcular_promedio(self):
#        promedio = sum(self.notas) / len(self.notas)
#        return promedio

#mi_alumno = Alumno("Nombre", [8, 6, 10, 10])
#print(mi_alumno.calcular_promedio())

#Nivel 3
#1)Clase CuentaBancaria con depósitos y extracciones. Crear una clase CuentaBancaria con un atributo saldo. 
#Agregar métodos depositar(monto) y retirar(monto) que actualicen el saldo. Agregar un método ver_saldo().

#2)Función que reciba una lista de objetos Alumno y retorne el promedio general de todos.
#Crear varios alumnos, guardarlos en una lista y crear una función promedio_general(alumnos) que calcule el promedio total de todos.

#3)Clase Rectángulo con área y perímetro. Crear una clase Rectangulo que reciba base y altura como atributos. 
#Agregar métodos area() y perimetro().

#4)Simulador de carrera simple con autos. Crear una clase Auto con atributos modelo y velocidad, y métodos acelerar() y frenar(). 
#Crear una función que simule una carrera entre 2 autos llamando varias veces a acelerar() y mostrando cuál llega primero a cierta velocidad.

#1)
#class cuentaBancaria():
#    def __init__(self, saldo):
#        self.saldo = saldo

#    def depositar(self, monto):
#        self.saldo += monto
#        print(f"Ingresaste {monto}. Nuevo saldo: {self.saldo}")

#    def retirar(self, monto):
#        if monto <= self.saldo:
#            self.saldo -= monto
#            print(f"Retiraste {monto}. Nuevo saldo: {self.saldo}")
#        else:
#            print("Fondos insuficientes")

#    def ver_saldo(self):
#        print(f"Tu saldo actual es de: {self.saldo}")

#mi_cuenta_bancaria = cuentaBancaria(100000)
#mi_cuenta_bancaria.depositar(10000)
#mi_cuenta_bancaria.retirar(50000)
#mi_cuenta_bancaria.ver_saldo()

#2)
#class Alumno:
#    def __init__(self, notas):
#        self.notas = notas

#    def calcular_promedio(self):
#        return sum(self.notas) / len(self.notas)

#primer_alumno = Alumno([2, 6, 8, 7])
#segundo_alumno = Alumno([4, 4, 6, 9])
#tercero_alumno = Alumno([8, 8, 7, 9])
#cuarto_alumno = Alumno([10, 10, 9, 9])

#todos_los_alumnos = [primer_alumno, segundo_alumno, tercero_alumno, cuarto_alumno]

#def promedio_general(todos_los_alumnos):
#    suma_total = 0 #acumulando los promedios individuales
#    cantidad_alumnos = 0 
    
#    for alumno in todos_los_alumnos:
#        promedio_individual = alumno.calcular_promedio()
#        suma_total += promedio_individual
#        cantidad_alumnos += 1

#    promedio_general = suma_total / cantidad_alumnos
#    return promedio_general

#print(promedio_general(todos_los_alumnos))

#3)Clase Rectángulo con área y perímetro. Crear una clase Rectangulo que reciba base y altura como atributos. 
#Agregar métodos area() y perimetro().
#-------------------------------------------------------------------------------------

#exception hadling

#Objetivo: Pedir al usuario su edad y asegurarte de que sea un número entero positivo.
#Consigna: Pedí al usuario su edad. 
#Si ingresa texto o un número negativo, mostrá un mensaje de error y pedile de nuevo hasta que lo haga bien. 
# Luego imprimí "Edad registrada: X años".


#while True:
#        try:
#            numero = int(input("Ingresa tu edad: "))
#            if numero > 0:
#                print(f"Tu edad es {numero}")
#                break
#            else:
#                print("La edad debe ser mayor a 0")
#        except:
#            print("No podes ingresar texto ni numeros negativos o con coma\nINTENTALO DE NUEVO")

#Objetivo: Usar un menú y asegurarte de que el usuario elija una opción válida.

#def menu():
#    opciones = int(input(("1)Saludar\n2)Mostrar numero favorito\n3)Salir\nElegi una opcion: ")))
#    return opciones

#def elegir_numero_fav():
#    decir_numero = int(input("Cual es el numero favorito de tu hermano?: "))
#    return decir_numero

#def chau():
#    print("Chau")

#numero_fav = 7

#while True:
#    try:
#        opciones_menu = menu()
#        if opciones_menu == 1:
#            print("Hola")
#        elif opciones_menu == 2:
#            while True:
#                try:
#                    opciones_menu = elegir_numero_fav()
#                    if numero_fav == opciones_menu:
#                        print(f"El {numero_fav} es correcto")
#                        break
#                    else:
#                        print("No es el numero favorito de tu hermano. INTENTALO DE NUEVO")
#                except:
#                    print("Ingresa solo un numero")
#        elif opciones_menu == 3:
#            chau()
#            break
#    except:
#        print("Ingresa las opciones correspondientes")
#-------------------------------------------------------------------------------------

#ejercicio validar pin. El usuario debe ingresar un PIN de 4 dígitos. Si se equivoca, debe volver a intentarlo hasta que sea correcto.

#pin = 1020
#pin_valido = True

#while pin_valido:
#    ingresar_pin = int(input("Ingresa el pin: "))
#    if ingresar_pin == pin:
#        print("El pin es correcto. Accediendo...")
#        pin_valido = False
#    else:
#        print("Intenta de nuevo")
#-------------------------------------------------------------------------------------

#edabit

#Escriba una función que tome un número entero minutos y lo convierta a segundos. 
# Ejemplos convert(5) ➞ 300

#def conversion(minutos):
#    return minutos * 60
    
#print(conversion(minutos=5))

#Escriba una función que convierta horas segundos.

#def horas_en_segundos(horas):
#    return horas * 3600

#print(horas_en_segundos(horas=3))

#Dado un polígono regular de n lados n, devuelve la suma total de los ángulos internos (en grados).
#n siempre será mayor que 2.
#La fórmula (n - 2) x 180 da la suma de todas las medidas de los ángulos de un polígono de n lados.

#def suma_poligonos(n):
#    return (n - 2) * 180

#print(suma_poligonos(6))

#Crea una función que reciba una lista de números y devuelva el primer elemento.

#lista = [1,2,3]

#def recibiendo_lista(lista):
#    return lista[0]

#print(recibiendo_lista(lista))

#Crea una función que reciba tres números: cantidad de partidos ganados, empatados y perdidos.
#Ganado = 3 puntos. Empatado = 1 punto. Perdido = 0 puntos. Devolvé el total de puntos.



#def recibiendo_tres_numeros(ganado, empate, perdido):
#    ganados = ganado * 3
#    empatados = empate * 1
    
#    suma_total = ganados + empatados 
#    return suma_total

#print(recibiendo_tres_numeros(6,3,0))

#Consigna: Dado un número de gallinas, vacas y cerdos, 
#devolvé la cantidad total de patas (cada gallina tiene 2 patas, cada vaca y cerdo tiene 4)

#def cantidad_patas(gallinas, vacas, cerdos): 
#    galli = gallinas * 2
#    vak = vacas * 4
#    crdos = cerdos * 4
#    suma_patas_total = galli + vak + crdos
#    return suma_patas_total #otra forma directa return gallinas * 2 + vacas * 4 + cerdos * 4

#print(cantidad_patas(10,5,5))

#Escribí una función que reciba una cadena (string) que representa un número y devolvé ese número como entero.
#def cadena_a_entero(text):
#    return int(text)

#print(cadena_a_entero(5))

#Consigna:#Crea una función que reciba dos argumentos y 
#devuelva True si son iguales, o False si no lo son.

#def iguales_o_no(a,b):
#    return a==b 

#print(iguales_o_no(5,4))

#def adjetivo_en_verbo(frase):
#    palabras = frase.split()
#    return palabras

#print(adjetivo_en_verbo("Hola estoy corriendo"))

#Dada una lista de números, devolvé el número más grande.

#lista = [1,10,100,500,20,3]

#def el_mas_grande(lista):
#    return min(lista)

#print(el_mas_grande(lista))

#Arreglá una función que solo debe devolver True si el número recibido es 7.
#era esto XD

#def devolver_siete(numero):
#    return numero == 7

#print(devolver_siete(7))

#Hice esto
#def devolver_siete():
#    bandera = True
#    while bandera:
#        numero = int(input("Ingresa un numero: "))
#        if numero == 7:
#            print("Correcto")
#            bandera = False
#        else:
#            print("No ingresaste el numero correcto")

#devolver_siete()

#Diferencia entre el máximo y el mínimo en una lista

#lista1 = [10, 4, 1, 4, -10, -50, 32, 21]
#lista2 = [44, 32, 86, 19]

#def devolver_diferencia(lista1, lista2):
#    return max(lista1) - min(lista2)

#print(devolver_diferencia(lista1,lista2))

