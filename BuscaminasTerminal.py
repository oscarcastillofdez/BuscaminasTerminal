import random
import sys
import CasillaTerminal as casillaTerminal

def inicio() -> list:
#Iniciar las dimensiones y minas
    columnas = input("\tNumero de columnas:")
    filas = input("\tNumero de filas:")
    n_minas = input("\tNumero de minas:")
    try:
        columnas = int(columnas)
        filas = int(filas)
        n_minas = int(n_minas)
    except:
        print("\tError: solo numeros enteros en la entrada\n\tPresione enter para cerrar")
        input()
        exit()

    if (n_minas > columnas*filas*3/4):
        print("\tError: demasiadas minas\n\tPresione enter para cerrar")
        input()
        exit()
    
    return [filas, columnas, n_minas]

def crearMatriz(filas, columnas) -> list:
    #Crear la matriz
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            x = casillaTerminal.casilla()
            fila.append(x)
        matriz.append(fila)
    return matriz

def pedirPosición(filas, columnas) -> list:
    #Pedir primer casilla a mostrar 
    x = input("\tFila a seleccionar:")
    y = input ("\tColumna a seleccionar:")
    try:
        x = int(x)
        y = int(y)
    except:
        print("\tError: solo numeros enteros en la entrada\n\tPresione enter para cerrar")
        input()
        exit()
    if (x > filas or y > columnas):
        print("\tError: solo numeros enteros en la entrada\n\tPresione enter para cerrar")
        input()
        exit()
    pos = [x,y]
    return pos

def imprimirMatriz(filas, columnas, matriz):
    #Imprime la matriz
    print("\t\t\t ",end="")
    for i in range(columnas):
    	if i+1 < 10:
    		print(str(i+1) + "   ",end="")
    	else:
    		print(str(i+1) + "  ",end="")
    print("")
    for i in range(filas):
        print("\t\t"+ str(i+1) + "\t",end="")
        for j in range(columnas):
            matriz[i][j].print()
        print("")

def valorMatriz(filas, columnas, matriz) -> int:
    #Consigue el valor de la matriz
    n = 0
    for i in range(filas):
        for j in range(columnas):
            n = n + matriz[i][j].getVal()
    return n

def crearMinas(filas,columnas, n_minas, primer) -> list:
    #Calcular la posicion de las minas
    minas = []
    for i in range(n_minas):
        pos = [random.randint(1,filas),random.randint(1,columnas)]
        while(minas.count(pos)==1 or pos == primer):
            pos = [random.randint(1,filas),random.randint(1,columnas)]
        minas.append(pos)
    return minas

def calcularMatriz(filas, columnas, matriz, minas) -> list:
#Calcular los valores de la matriz
    for i in range(len(minas)):
        (x,y) = minas[i]
        matriz[x-1][y-1].convertirMina()
        for j in range(x-1, x+2):
            if (j >= 1 and j <= filas):
                for k in range(y-1,y+2):
                    if (k >= 1 and k <= columnas):
                        cas = matriz[j-1][k-1]
                        cas.aumentarVal()
    return matriz

def mostrarCasilla(filas, columnas, matriz, pos, val) -> list:
#Mostrar esa casilla
    fin = True
    (x,y) = pos
    res = matriz[x-1][y-1].mostrar()
    if (res == -1):
        fin = False
    else:
        if (res == 0):
            for j in range(x-1, x+2):
                if (j >= 1 and j <= filas):
                    for k in range(y-1,y+2):
                        if (k >= 1 and k <= columnas):
                            (val,fin) = mostrarCasilla(filas, columnas, matriz, (j,k), val)
        else:
            if (res > 0):
                val = val - res
    if (val <= 0):
        fin = False 
    return (val,fin)


def main() -> int:
    (filas, columnas, n_minas) = inicio()
    matriz = crearMatriz(filas, columnas)
    imprimirMatriz(filas, columnas, matriz)
    pos = pedirPosición(filas, columnas)
    minas = crearMinas(filas, columnas, n_minas, pos)
    matriz = calcularMatriz(filas, columnas, matriz, minas)
    val = valorMatriz(filas, columnas, matriz)
    (val,fin) = mostrarCasilla(filas, columnas, matriz, pos, val)
    while(fin):
        imprimirMatriz(filas, columnas, matriz)
        pos = pedirPosición(filas, columnas)
        (val,fin) = mostrarCasilla(filas, columnas, matriz, pos, val)
    imprimirMatriz(filas, columnas, matriz)
    input()
    return 0

if __name__ == '__main__':
    sys.exit(main())
