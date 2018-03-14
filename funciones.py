num = 30
if num >= 0 and num <= 100:
    print("este numero esta en el rango")
else:
    print("No esta en rango")

if 0<= num <=100:
    print("este numero esta en el rango")
else:
    print("No esta en rango")
# -------------------- Compresion de listas ----------------------------------
lista = []
for letra in "satanas":
    lista.append(letra)
print(lista)

lista2 = [letra for letra in "satanas"] #comprension de listas
print(lista2)

lista3 = [numero**2 for numero in range(0,11)] #eleva al cuadrado los 10 primeros numeros
print(lista3)

lista4 = [numero for numero in range(0,11) if numero % 2 == 0] #solo números pares
print(lista4)

lista5 = [numero**2 for numero in range(0,11) if numero % 2 == 0] #solo números pares y al cuadrado
print(lista5)

lista6 = [numero for numero in [numero**2 for numero in range(0,11) if numero % 2 == 0]] #igual
print(lista6)

# ------------------ Funciones sin nombre (lambda) ---------------------------
def Doble(num):
    resultado = num * 2
    return resultado
print(Doble(2))

Doblar = lambda num:num*2 #funcion en una sola línea para calculos sencillos y rápidos
print(Doblar(2))

Par = lambda num:num%2==0
print(Par(2))

Revertir = lambda cadena:cadena[::-1] #imprime la cadena al revés
print(Revertir("hola"))

Sumar = lambda x,y:x+y
print(Sumar(8,9))

def MultiploCinco(numero):
    if numero % 5 == 0:
        return True
    else:
        return False

# ------- filtros -------
lista_numero = range(0,20)
lista_multiplo = list(filter(lambda x:x%5==0,lista_numero)) #filtra datos con la condicion que le indicamos
print(lista_multiplo)

print(list(filter(MultiploCinco,lista_numero)))

# --- filtros con objetos -------
class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{} de {} años".format(self.nombre,self.edad)

personas = [Persona("Juan",35),Persona("Pepe",36),Persona("Alberto",17)] #carga lista de personas
menores = filter(lambda Persona:Persona.edad>18,personas) #filtra por edad
for menor in menores:
    print(menor)










