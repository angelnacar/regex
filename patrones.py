# ---- Expresiones regulares  ------
import re
cadena = "la vida es dura y larga"
re.search("larga",cadena)
#print(re.search("larga",cadena))
encontrar = re.search("larga",cadena)
#print(encontrar.start()) #posicion donde encuentra la coincidencia
#print(encontrar.end()) #posicion donde termina la coincidencia
#print(encontrar.span()) #donde empieza y termina
cadena = "hola adios amigos del metal hola satan os quiero de verdad"
resultado = re.findall("hola",cadena) #encuentra todas las coincidencias
#print(resultado)
resultado2 = re.findall("hola|adios|amigos",cadena) #encuentra varias palabras a la vez
#print(resultado2)
cadena = "hla hola hoola hooola hooooola"
def Busqueda(patrones,texto):
    for patron in patrones:
        print(re.findall(patron,texto))

patrones = ["ho","ho*","ho*la","hu*la"] #saca todos los que haya
#Busqueda(patrones,cadena)
patrones2 = ["ho*","ho+"] #solo saca coincidencia exacta  *--> Like +--> =
#Busqueda(patrones2,cadena)
patrones3 = ["ho*","ho+","ho?","ho?la"] #?que empieze por h
#Busqueda(patrones3,cadena)
patrones4 = ["ho{0}la","ho{1}la","ho{2}la"] #sacame las palabras que coincidan el numero de repeticiones de o
#Busqueda(patrones4,cadena)
patrones5 = ["ho{0,2}la","ho{1,2}la","ho{2,4}la"] #sacame las palabras que tenga de 0 a 2 oes, de 1 a 2 y ...
#Busqueda(patrones5,cadena)
texto = "hala hela hila hola hula"
patrones6 = ["h[ou]la","h[ai]la"] #muestra las palabras que contenga las letras que se encuentra dentro de los corchetes
#Busqueda(patrones6,texto)
texto2 = "hala heela hiiila hoooola huuuuuuuula"
patrones7 = ["h[ae]la","h[ae]*la","h[io]{3,9}la"]
#Busqueda(patrones7,texto2)
texto3 = "hola hela hila hola hula"
patrones8 = ["h[o]la","h[^i]la"]
#Busqueda(patrones,texto3)

#-------------- Selección por códigos ----------------
texto = "Python es un lenguaje que nació e€ 1921"
patrones9 = [r"\d+",r"\D+",r"\s",r"\S+",r"\w+",r"\W+"] #saca lo numérico, saca lo no numérico, saca espacios en blanco, saca sin espacios en blanco, saca sin espacios en blanco y sin caracteres espciales, sa
Busqueda(patrones9,texto)

#https://www.python-course.eu/python3_course.php

