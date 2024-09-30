# Problema 1
divisibles = [i for i in range(1500, 2701) if i % 7 == 0 and i % 5 == 0]
print(divisibles)

# Problema 2
for i in range(1, 6):
    print('* ' * i)
for i in range(4, 0, -1):
    print('* ' * i)

# Problema 3
numeros = []
while input("Desea ingresar un número? (SI/NO): ").lower() == "si":
    num = int(input("Ingrese el número: "))
    numeros.append(num)
pares = len([n for n in numeros if n % 2 == 0])
impares = len(numeros) - pares
print("Números ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)

# Problema 4
alumnos = []
n = int(input("Ingrese la cantidad de alumnos: "))
for _ in range(n):
    nombre = input("Nombre del alumno: ")
    notas = [int(input(f"Nota {i+1}: ")) for i in range(3)]
    alumnos.append({"Alumno": nombre, "Notas": notas})
for alumno in alumnos:
    print(alumno)

# Problema 5
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
suma_primos = sum([i for i in range(100) if es_primo(i)])
print(suma_primos)

# Problema 6
a, b = 0, 1
while a <= 50:
    print(a, end=' ')
    a, b = b, a + b
print()

# Problema 7
def es_perfecto(n):
    return sum([i for i in range(1, n) if n % i == 0]) == n
perfectos = [i for i in range(1, 1000) if es_perfecto(i)]
print(perfectos)

# Problema 8
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
print(factorial(int(input("Ingrese un número para el factorial: "))))

# Problema 9
cadena = input("Ingrese una cadena de texto: ")
sin_vocales = ''.join([c for c in cadena if c.lower() not in "aeiou"])
print(sin_vocales)

# Problema 10
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
fecha = input("Ingrese una fecha (MM/DD/AAAA o Mes Día, AAAA): ")

if '/' in fecha:
    mes, dia, anio = map(int, fecha.split('/'))
else:
    mes_nombre, dia_anio = fecha.split(' ', 1)
    mes = meses.index(mes_nombre) + 1
    dia, anio = map(int, dia_anio.replace(',', '').split())
print(f"{anio}-{mes:02}-{dia:02}")
