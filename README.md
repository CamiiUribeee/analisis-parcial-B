# Parciales — Análisis de Algoritmos (193502)

Universidad Francisco de Paula Santander Ocaña  
Programa: Ingeniería de Sistemas  
Semestre: V  
Créditos: 3  
Asignatura: **Análisis de Algoritmos** 

---

## Instrucciones generales

- Tiempo máximo: **60 minutos**  
- Cada parcial tiene **4 puntos (25 pts c/u)**  
- Usa Python o pseudocódigo claro.  
- Para comparar funciones, basta con un **`for` + `if`** y reportar el menor `n` que verifica la desigualdad.  
- Justifica con fórmulas y razonamiento.  

---
# Parcial — Versión B

### Punto 1 (25 pts) — Ordena por complejidad
Ordena de menor a mayor las siguientes funciones (asintóticamente).  
Si dos son del mismo orden, indícalo.


![Logo](https://lh3.googleusercontent.com/pw/AP1GczOKbm4PRxvPmIk6xzWEndiZu8Rshw7xbFWnNI3rltL041tyTLuAEoS_afx5V8mtGSJr9FWorLJj02v-8Ga3JJ6YDmsSpBgSFL8ruWN_1OLTVyTerg_9zIomuoPte5JNZIQ_yNwoxVdjH8460tgjJaPO=w128-h290-s-no?authuser=0)

---

### Punto 2 (25 pts) — Identifica y confronta
Asocia cada \(T(n)\) con un algoritmo plausible. Luego compara **dos pares** y encuentra el umbral de `n` con un `for` + `if`.

- T1(n) = 5n^2 + 10n 
- T2(n) = 6n\log2(n) + 300
- T3(n) = 0.01n^3
- T4(n) = 1.5^n 

Algoritmos posibles:  
- Selection/Insertion  
- Mergesort/Heapsort  
- Multiplicación de matrices cúbica  
- Backtracking con poda leve  

---

### Punto 3 (25 pts) — Ejercicio lógico
#### Isaac y los intervalos mágicos

Isaac, convencido de que tiene un talento especial para los números, asegura que puede contar al instante cuántos primos existen en cualquier rango que le propongan sus amigos. Para comprobarlo, ellos le entregan una lista con N pares de números (a,b), y él debe responder de inmediato cuántos números primos hay en cada intervalo. A partir de esta historia, elabora el análisis necesario para resolver el problema y define claramente qué se recibe como entrada, qué se debe producir como salida y qué lógica se requiere para verificar la afirmación de Isaac. 

---

### Punto 4 (25 pts) — Cuestionario

[![Click here!!](https://cf.quizizz.com/img/wayground/brand/plans/logo-basic.png)](https://wayground.com/join?gc=846438)




SOLUCIÓN DE LOS 2 PRIMEROS PUNTOS 

PRIMER PUNTO:
ORDEN DE MENOR A MAYOR -> log2n, n, nlog2n, sqrtnlog2n, n^2, n^(3/2), n^0.99, n^2/log2n, 3^n, 2^(n/2)*n

SEGUNDO PUNTO: 
PARTE 1
Conclusión de la comparación de funciones:
En mi caso, al comparar la función 1 que vendría siendo un Insertion, con la función 2 que es una multiplicación cúbica, resulta conveniente utilizar insertion, puesto que es más rápido al pasarle datos, esto no solo es importante es terminos de eficiencia o eficacia, sino también en el consumo de recursos. El cruce entre ambas funciones se da en n igual a 502.
PARTE 2
Conclusión de la compración de funciones: 
Al comparar el insertion con el backtraking resulta mas conveniente usar Insertion. El cruce se da en n igual a 19 

TERCER PUNTO: 
La complejidad del algoritmo de Isaac para saber cuantos numeros primos hay en in intervalo (a,b), es de O(n) o complejidad lineal




CORRECCIÓN DEL PARCIAL 

PRIMER PUNTO: 

Ordenar las siguientes funciones de **menor a mayor crecimiento**:

1. log₂n  
2. √n·log₂n  
3. n^0.99  
4. n  
5. n·log₂n  
6. n^(3/2)  
7. n²/log₂n  
8. n²  
9. 3ⁿ  
10. 2^(n/2)·n

Orden de menor a mayor: log₂n < n^0.99 < √n·log₂n < n < n·log₂n < n^(3/2) < n²/log₂n < n² < 2^(n/2)·n < 3ⁿ


SEGUNDO PUNTO / PRIMERA PARTE:

Comparación 1: T1(n) vs T3(n). Insertion sort vs Multiplicación cúbica

Conclusiones: El cruce se da aproximadamente en n=502. 
Para valores mayores, Insertion sort (T1) es más eficiente, esto refleja que los algoritmos con complejidad cuadrática escalan mejor que los cúbicos. Insertion es más eficiente en tiempo y recursos a partir de ese punto.

SEGUNDA PARTE: 

Comparación 2: T1(n) vs T4(n). Insertion sort vs Backtracking 

Conclusiones: El punto de cruce se encuentra en n=19. Backtracking se vuelve ineficiente muy rápido, por tanto, a partir de ese valor, Insertion sort tiene un comportamiento mucho más estable y eficiente en tiempo y recursos.


TERCER PUNTO: 

la función esPrimo_T() recorre todos los números desde 2 hasta n, lo que genera una complejidad O(n²) en total (por los dos bucles anidados). 