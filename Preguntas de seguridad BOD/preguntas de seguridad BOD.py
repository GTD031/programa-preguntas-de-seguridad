print("Programa para saber las respuestas de las preguntas de seguridad del banco BOD")
## Uso de un diccionario y una lista
preguntasBOD=['Cual es el nombre de tu primer sobrino?','Cual es el nombre de su mama?','En que ciudad nació usted?','Cual es el mes de cumpleaños de su mamá?','Cual es la marca de su primer vehiculo?','Cual es el nombre de su mascota?'] 
respuestaBOD={1:'carlos',2:'Maria',3:'micasadeloschorros',4:'Enero',5:'Ford',6:'Cleo'}
while True:
    print("Las preguntas de seguridad del BOD son las siguientes: ")
    for k in range(6):
        print(str(k+1)+')'+preguntasBOD[k])
    try:
        print("Por favor, siga los siguientes pasos:")
        print("a)Verifique la pregunta de seguridad que le piden en la página BOD")
        print("b)Busca la pregunta en el menu de arriba y revise el numero correspondiente")
        print("c)Coloque el número de la pregunta a continuacion para saber la respuesta")
        k=int(input("Introduzca el número de la pregunta:"))
    except:
        print("Valor inadmisible. Debe ser un número entero comprendido entre 1 y 6")
        continue
    if k in [1,2,3,4,5,6]:
        print("La respuesta es: "+respuestaBOD[k])
    else:
        print("Valor Erroneo: Debe ser algún número que corresponde a las preguntas de seguridad ya mencionadas")

    i=input("Tiene alguna duda sobre otra pregunta de seguridad? Presione S desea volver al menu principal de preguntas de seguridad, N si desea finalizar: ")
    i=i.upper()
    while i!='S' and i!='N':
        i=input("Valor Erroneo: Seleccione 'S' si desea continuar y 'N' si desea finalizar: ")
        i=i.upper()
    if i=='N':
        break

print("Ha finalizado el programa.")

