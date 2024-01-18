import sys
import numpy as np
import gurobipy as gp
from gurobipy import GRB

from pathlib import Path
import os

def qknapsack(instance):

    with open(instance, 'r') as file: linhas = file.readlines()

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
    model = gp.Model("qkp01") 

    x = []
    for j in range(0, n):
        x.append(model.addVar(vtype=GRB.BINARY, name="x_{}".format(j+1)))
        
    model.Params.TimeLimit = 600
    model.Params.MIPGap = 1.e-6
    model.Params.Threads = 1
    
    # Turn off display
    #gp.setParam('OutputFlag', 0)

    obj = 0 
    for i in range(0, n):
        obj += p[i][i] * x[i]
        for j in range(i+1, n):
            obj += p[i][j] * x[i] * x[j]

    model.setObjective(obj, GRB.MAXIMIZE)

    constr = 0
    for j in range(0, n):
        constr += (w[j] * x[j])
    model.addConstr(constr <= c)

    #model.write("qkp01.lp")

    model.optimize()
    
    status = 0
    if model.status == GRB.OPTIMAL:
        status = 1
 
    lb = model.objBound
    ub = model.objVal
    gap = model.MIPGap
    time = model.Runtime
    nodes = model.NodeCount

    model.dispose()

    #time, lower bound, upper bound, gap, qtd nodes
    #print('Obj: %g' % obj.getValue())
    
    arquivo = open('result.csv','a')
    arquivo.write(
        str(instance)+';'
        +str(round(lb,1))+';'
        +str(round(ub,1))+';'
        +str(round(gap,2))+';'
        +str(round(time,2))+';'
        +str(round(nodes,1))+';'
        +str(round(status,1))+'\n'
    )
    arquivo.close()


if __name__ == "__main__":

	#result_path = Path(f"result/{inst_}")
	
    if len(sys.argv) < 2:
        instance = "instances/100/100_25_1.txt"
        print("Default data file : " + instance)
    else:
        instance = sys.argv[1]

    qknapsack(instance)
