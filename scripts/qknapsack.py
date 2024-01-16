import sys
import numpy as np
import gurobipy as gp
from gurobipy import GRB

def qknapsack(datafile):
    with open(datafile, 'r') as file: linhas = file.readlines()

    # remove linha vazia inicial e elimina os "\n" de cada linha
    linhas = [a.strip() for a in linhas] 

    # ler o tamanho da instancia
    n = int(linhas[0]) 

    # ler a diagonal da matriz
    d = np.fromstring(linhas[1], dtype=int, sep = ' ') 

    # define a matriz
    p = np.zeros((n,n), dtype=int) 

    # preenche a diagonal
    for i in range(n): 
        p[i][i] = d[i]

    # preenche o resto da matriz
    for i in range(n-1): 
        linha = np.fromstring(linhas[i+2], dtype=int, sep = ' ')
        for j in range(n-(i+1)):
            p[i][j+i+1] = linha[j]
            p[j+i+1][i] = p[i][j+i+1]

    # ler a capacidade
    c = int(linhas[n+2]) 

    # ler os pesos
    w = np.fromstring(linhas[n+3], dtype=int, sep = ' ') 

    #cria o modelo
    m = gp.Model("qknapsack") 

    x = []
    for j in range(0, n):
        x.append(m.addVar(vtype=GRB.BINARY,name="x_{}".format(j+1)))

    obj = 0 
    for i in range(0, n):
        obj += p[i][i] * x[i]
        for j in range(i+1, n):
            obj += p[i][j] * x[i] * x[j]

    m.setObjective(obj, GRB.MAXIMIZE)

    constr = 0
    for j in range(0, n):
        constr += (w[j] * x[j])
    m.addConstr(constr <= c)

    #m.write("qknapsack.lp")

    m.optimize()

    #time, lower bound, upper bound, gap, qtd nodes
    print('Obj: %g' % obj.getValue())

if __name__ == "__main__":
    datafile = "instances/100/100_25_1.txt"

    if len(sys.argv) < 2:
        print("Default data file : " + datafile)
    else:
        datafile = sys.argv[1]

    qknapsack(datafile)
