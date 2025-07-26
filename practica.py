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