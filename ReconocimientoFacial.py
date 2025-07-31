import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

#CREAR BASE DE DATOS
ruta = "Empleados"
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

#CARGAR LISTA DE NOMBRES SIN .JPG
for nombre in lista_empleados:
    imagen_actual = cv2.imread(f"{ruta}\{nombre}")
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print(nombres_empleados)

#CODIFICAR IMAGENES
def codificar(imagenes):

    #CREAR UNA LISTA NUEVA
    lista_codificada = []

    #PASAR TODAS LAS IMAGENES A RGB
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)

        #CODIFICAR
        codificado = fr.face_encodings(imagen)[0]

        #AGREGAR A LA LISTA
        lista_codificada.append(codificado)

    #DEVOVER LISTA CODIFICADA
    return lista_codificada

#REGISTRAR LOS INGRESOS
def registrar_ingresos(persona):
    f = open("registro.csv","r+")
    lista_datos = f.readline()
    nombre_registro = []
    for linea in lista_datos:
        ingreso = linea.split(",")
        nombre_registro.append(ingreso[0])

    if persona not in nombre_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime("%H:%M:%S")
        f.writelines(f"\n{persona}, {string_ahora}")



lista_empleados_codificada = codificar(mis_imagenes)

#TOMAR UNA IMAGEN DE CAMARA WEB
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#LEER IMAGEN DE LA CAMARA
exito,imagen = captura.read()

if not exito:
    print("no se pudo tomar la captura")
else:
    #RECONOCER CARA EN CAPTURA
    cara_captura = fr.face_locations(imagen)

    #CODIFICAR CARA CAPTURADA
    cara_captura_codificada = fr.face_encodings(imagen,cara_captura)

    #BUSCAR COINCIDENCIA
    for caracodif, caraubic in zip(cara_captura_codificada,cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada,caracodif)
        distancias = fr.face_distance(lista_empleados_codificada,caracodif)

        print(distancias)

        indice_coincidencia = numpy.argmin(distancias)

        #MOSTRAR COINCIDENCIAS SI LAS HAY
        if distancias[indice_coincidencia] > 0.6:
            print("No coincide con ninguno de nuestros empleados")

        else:

            #BUSCAR EL NOMBRE DE EMPLEADO ENCONTRADO
            nombre = nombres_empleados[indice_coincidencia]

            #DIBUJAR RECTANGULO Y ESCRIBIR TEXTO EN IMAGEN
            y1,x2,y2,x1 = caraubic
            cv2.rectangle(imagen, (x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(imagen,(x1, y2 - 35), (x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(imagen,nombre, (x1 + 6 , y2 -6),cv2.FONT_ITALIC,1,(255,255,255),2)

            registrar_ingresos(nombre)
            
            #MOSTRAR LA IMAGEN OBTENIDA
            cv2.imshow("Imagen Web",imagen)

            #MENTENER VENTANA ABIERTA
            cv2.waitKey(0)
