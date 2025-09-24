# Compración de T(n)1 con T(n)4

def funcion1_T(n):
    return 5*n**2+10*n

def funcion2_T(n):
    return 1.5**n


for n in range(2, 1_000_000):
    T1= funcion1_T(n)
    T2= funcion2_T(n)

    if T1<T2:
        print(f"El cruce se da en n igual a {n}")
        break


for n in[10,20,30,40,50]:
    T1= funcion1_T(n)
    T2= funcion2_T(n)

    if T1<T2:
        mejor="Insertion"
    else:
        mejor="Backtraking"
    print(f"Para n igual a {n} resulta mas conveniente usar {mejor}")