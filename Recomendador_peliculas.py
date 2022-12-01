import pandas as pd  # libreria necesaria para el tratamiento del dato
import re  # libreria empleada para el uso de expresiones regulares
import sys  # estas dos ultimas creadas para un manejador de señales
import signal


def handler_signal(signal, frame):  # funcion de salida controlada
    print("\n\n Interrupcion del programa, saliendo del prograama de manera controlada y ordenada")
    sys.exit(1)


# Ctrl + C, en caso de introducirlo por teclado saldremos del programa
signal.signal(signal.SIGINT, handler_signal)


def extract():  # Vamos a trabajar con el dataset y quedarnos con lo que queremos eliminaremos una serie de columnas
    csv = pd.read_csv('imdb_top_1000.csv')
    return csv


def transform(csv):
    # eliminamos la palabra min de duracion para qiue solo tenga caracteres numericos utilizando regex
    # eliminaremos las columnas de nuestro dataset que no vayamos a emplear
    csv["Runtime"] = csv["Runtime"].replace({'min': ''}, regex=True)
    csv = csv.drop(['Poster_Link'], axis=1)
    csv = csv.drop(['Certificate'], axis=1)
    csv = csv.drop(['Gross'], axis=1)
    csv = csv.drop(['No_of_Votes'], axis=1)
    csv = csv.drop(['Meta_score'], axis=1)
    lista_listas = csv.to_numpy().tolist()
    return lista_listas


def transformar_lista_string(lista):
    string = ""
    for i in lista:
        string += str(i) + ","
    return string


def recomendiones_regex(lista_listas, datos_pelicula):
    # nuestra lista de recomendaods en 0
    recomendados = []
    lista_coincidencias = []
    valor = 0
    for i in range(len(lista_listas)):  # vamos a recorrer las peliculas
        contador_coincidencias = 0
        for j in datos_pelicula:  # vamos a encontrar las peliculas que más incidencias tengan con aquello que el ususario introduzca por pantalla
            j = str(j)
            lista_a_string = transformar_lista_string(lista_listas[i])
            # empleamos findall para buscarlas
            a = re.findall(j, lista_a_string)
            if len(a) > 0:
                contador_coincidencias += 1
        if contador_coincidencias > valor:
            valor = contador_coincidencias
            recomendados.append(lista_listas[i][0])
            recomendados.append(lista_listas[i][5])
    return recomendados  # devolvemos la lista de pelis recomendadas


def usuario():
    # le vamos a preguntar al usuario que caracteristicas quiere que tenga su pelicula
    # para despues crrar una lista con dichas caracteristicas y hacer un findall para
    # encontrar con que pelis tiene mas coincidencias y devolver dicha peli
    print("En caso de no queres ninguno de estos campos responda no")
    datos_pelicula = []
    genero = input("Select the genre of the movie:")
    duracion = input(
        "seleccione el tiempo que desea que dure la pelicula: ")
    actores_directores = input("Desea algun actor o director en particular: ")
    año_pelicula = input("Año de la pelicula, maarque un año:")
    datos_pelicula.append(genero)
    datos_pelicula.append(duracion)
    datos_pelicula.append(actores_directores)
    datos_pelicula.append(año_pelicula)
    return datos_pelicula


if __name__ == "__main__":
    datos_pelicula = usuario()
    csv = extract()
    lista_listas = transform(csv)
    recomendados = recomendiones_regex(lista_listas, datos_pelicula)
    print(recomendados)
