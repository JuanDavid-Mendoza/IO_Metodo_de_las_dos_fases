from pulp import *
from os import system

while(True):
    system("cls")
    # Definiendo el tipo de problema
    problemType = input("Digite el tipo de problema (min/max): ")
    if(problemType.lower() == "min"):
        problema = LpProblem("Problema", LpMinimize)
    else:
        problema = LpProblem("Problema", LpMaximize)

    # Definiendo las variables
    numVariables = int(input("\nDigite el número de variables del problema: "))
    X=[]
    X.append(0)
    for i in range(1,numVariables+1):
        X.append(LpVariable("X"+str(i), lowBound=0))

    # Definiendo la función objetivo
    print("\nFunción objetivo: ")
    objFunction = 0
    for i in range(1,len(X)):
        objFunction += int(input("Digite el coeficiente de X"+str(i)+": "))*X[i]
    problema += objFunction

    #Definiendo las restricciones
    print("\nRestricciones: ")
    numRestrictions = int(input("Digite el numero de restricciones del problema: "))

    for i in range(numRestrictions):
        restriction = 0
        finalRestriction = 0
        print("\nRestriccion "+str(i+1))
        for j in range(1,len(X)):
            restriction += int(input("Digite el coeficiente de X"+str(j)+": "))*X[j]

        cr = int(input("Digite el coeficiente de la restriccion: "))        
        resSign = input("Digite el simbolo de la restriccion (<=, >=, =): ")
        if(resSign == "<="):
            finalRestriction = restriction + 0*X[1] <= cr
        elif(resSign == ">="):
            finalRestriction = restriction + 0*X[1] >= cr
        elif(resSign == "="):
            finalRestriction = restriction + 0*X[1] == cr

        problema += finalRestriction

    #Imprimiendo el problema por consola
    print("\n.:Problema a resolver:.\n")
    print('Funcion objetivo:')
    print(problema.objective)

    print('\nRestricciones:')
    for res in problema.constraints:
        print(res, ':', problema.constraints[res])
    
    if(input("\n¿Este es el problema que desea Resolver?(s/n)").lower() == 's'):
        break
    else:
        print("Por favor, vuelva a digitar su problema de programación lineal.")

# Imprimiendo la solución (Si se halla una solución factible)
if(problema.solve(PULP_CBC_CMD(msg=False)) == 1):
    print("\nSolución óptima en: ")
    for i in range(1,len(X)):
        print("X"+str(i)+" = "+str(X[i].varValue))
    print("\nCon un valor de Z = "+str(pulp.value(problema.objective))+"\n")
else:
    print("\nNo se encontro una solucion para el problema planteado.\n")
