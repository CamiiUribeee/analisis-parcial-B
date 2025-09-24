# comparación de T(n)1 con T(n)3

def funcion1_T(n):
    return 5*n**2+10*n

def funcion2_T(n):
    return 0.01*n**3

for n in range(2,1_000_000):
    T1=funcion1_T(n)
    T2=funcion2_T(n)

    if T1<T2:
        print(f"El cruce se da en n igual a {n}")
        break

for n in [10,100,1000,10000, 1_000_000]:
    T1=funcion1_T(n)
    T2=funcion2_T(n)

    if T1<T2:
        mejor="Función 1"
    else: 
        mejor="Función 2"
    print(f"para n igual a {n} el mejor es {mejor}")

# Conclusión: la mejor función es la Función 1 