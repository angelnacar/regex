import re
import datetime

fichero = open("amigospython.txt","r")
texto = fichero.read()
fichero.close()
fechas = {"enero":"01","febrero":"02","marzo":"03","abril":"04","mayo":"05","junio":"06","julio":"07","agosto":"08","septiembre":"09","octubre":"10","noviembre":"11","diciembre":"12"}
ayo = datetime.date.today()
patrones = ["LUIS|pedro|Andres",r"\S+\d","enero|mayo|octubre",r'\S+@+\S+[A-Za-z]'] #busca patrones con multiples alternativas, el segundo busca numeros que le precedan al menos un espacio en blanco y el tercero busca @ que le precedan al menos un espacio en blanco y acaben en espacio en blanco y solo pueda contener caracteres del alfabeto

def Busqueda(patrones,texto):
    cadena = []
    for patron in patrones:
        cadena.append(re.findall(patron,texto)) #las coincidencias las va agregando a una lista
    return cadena

ca = [Busqueda(patrones,texto)]
b = [] #creo segunda lista
#al ser una lista de listas, voy agregando cada elemento en una nueva lista
for i in ca:
    for k in i:
        for z in k:
            b.append(z)
print("{} {}-{}-{} {} {}\n{} {}-{} {} {}\n{} {}-{}-{} {}".format(b[0],b[3],fechas.get(b[8]),b[4],b[11],ayo.year-int(b[4]),str(b[1]).upper(),fechas.get(b[9]),b[5],b[-1],ayo.year-int(b[5]),str(b[2]).upper(),b[6],fechas.get(b[10]),b[7],ayo.year-int(b[7])))


