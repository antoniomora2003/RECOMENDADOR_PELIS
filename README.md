# RECOMENDADOR_PELIS
En este repo realizaremos nuestro recomendador de películas empleando de nuevo una dinámica de ETL, nos importamos las librerías de pandas(tratamiento de csv y dataframes), re(librería de expresiones regulares, para buscar en dataframes), y sis y signal para realizar un manejador de señales. 

Emplearemos un csv inicial de Imdb, que contiene las 1000 mejores películas, vamos a recomendar algo conocido y famoso. Mediante el empleo de pandas realizaremos la extracción y transformación del dato quedándonos solo con aquellas columnas del dataframe que nos interesen. Le vamos a preguntar al usuario por las características que quiera que su película tenga, una vez obtenemos esa información, emplearemos Regex para encontrar las películas con mas incidencias con las peticiones de mi usuario y las devolvemos, junto con su descripción.

