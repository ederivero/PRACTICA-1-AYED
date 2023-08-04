import random


def generar_cadena(limite):
    cadena = []
    x = 0
    while x < limite:
        cadena.append(random.randint(1,50000))
        x+=1
    
    return cadena

print('{"Cadena de 100":',generar_cadena(100),',')


print('"Cadena de 1000":',generar_cadena(1000),',')


print('"Cadena de 2000":',generar_cadena(2000),',')


print('"Cadena de 3000":',generar_cadena(3000),',')


print('"Cadena de 4000":',generar_cadena(4000),',')


print('"Cadena de 5000":',generar_cadena(5000),',')


print('"Cadena de 6000":',generar_cadena(6000),',')


print('"Cadena de 7000":',generar_cadena(7000),',')


print('"Cadena de 8000":',generar_cadena(8000),',')


print('"Cadena de 9000":',generar_cadena(9000),',')


print('"Cadena de 10000":',generar_cadena(10000),',')


print('"Cadena de 20000":',generar_cadena(20000),',')


print('"Cadena de 30000":',generar_cadena(30000),',')


print('"Cadena de 40000":',generar_cadena(40000),',')


print('"Cadena de 50000":',generar_cadena(50000),'}')



