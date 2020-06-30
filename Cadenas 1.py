#VARIABLES QUE ALMACENAN TEXTO strings(str) SE ENCUENTRA ENTRE COMILLAS

#ASIGNACION
Mensaje="Hola"
Mensaje += "_"
Mensaje += "Mundo"
print(Mensaje)

#CONCATENACION
Mensaje = "Hola"
Espacio = "_"
Nombre = "Mundo"
print(Mensaje + Espacio + Nombre)

#AUTOMATICAMENTE DETECTA CUANDO SE QUIERE SUMAR O CONCATENAR
Numero_1 = 2
Numero_2 = 1
Resultado = Numero_1 + Numero_2

#CONVERTIR A STRING
Resultado = str(Resultado)

#NO PUEDE IMPRIMIR STRING E INT SE DEBE CONVERTIR
print("Resultado:" + Resultado)

#BUSQUEDA
Mensaje = "Hola Mundo"
#BUSCA LA POSICION DE LA CADENA INICIA DESDE 0
Buscar_subcadena = Mensaje.find("Mundo")
print(Buscar_subcadena)

#EXTRACCION
Mensaje = "Hola Mundo"
#PRIMER NUMERO: POCISION INICIAL DESDE DONDE QUEREMOS EXTRAER LA PORCION DE CADENA
#SEGUNDO NUMERO: POCICION FINAL PARA DELIMITAR HASTA QUE PUNTO QUEREMOS EXTRAER LA POSICION DE CADENA
Extraer_subcadena = Mensaje[1:8]
print(Extraer_subcadena)

#COMPARACION
Mensaje_1 = "Hola"
Mensaje_2 = "Hola"
print(Mensaje_1 ==Mensaje_2) 
