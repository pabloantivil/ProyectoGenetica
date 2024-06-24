import random
import numpy as np

NPob = 10 
SEED = 12
NCicles = 2
Poblacion = []
MAP = [[]]
nGen = 10
nPasos = 10
Asesinatos = 0

class individuo:
    def __init__(self,genes=[],position=[0,0]) -> None:
        self.genes = genes
        self.pasos = 0
        self.is_live = True
        self.position = position
        # self asesino (true o false)

        # [n, s, e, o, ne, no, se, so, asesino]
        # [1, 1, 0, 1, 0 , 1,   0,  1,     0  ]
        #self.gen()

        if len(self.genes) == 0:
            self.generar_genes()
        else:
            self.mutar()
        
    #javier
    def generar_genes(self):
        #generear los genes de el individuo
        genes = self.normalizar([np.random.uniform() for _ in range(9)])
        return genes
    
    #javier 
    def mutar(self):
        # puedes cambiar los gene segun 
        prob_mutacion = 0.1  
# 
        if np.random.uniform() <= prob_mutacion:
            index = np.random.randint(9)
            self.genes[index] = np.random.uniform()
            self.genes = self.normalizar(self.genes)
        pass
    
    def normalizar(vec):
        normalizado = []
        x = sum(vec)
        for i in vec:
            normalizado.append(i/x)
        return normalizado

    
    
    #coto
    def move(self):
        mov = np.random.randint(len(self.genes))
        if self.genes[mov] == 1 :
            self.position=posicionar(mov , self.position, self.genes[8])


# pablo 
def cruce(c1, c2):
    # Dividir c1 y c2 en dos partes
    long_gen = len(c1.genes)
    p_cruce = long_gen // 2
    
    c1_1 = c1.genes[:p_cruce]
    c1_2 = c1.genes[p_cruce:]
    
    c2_1 = c2.genes[:p_cruce]
    c2_2 = c2.genes[p_cruce:]
    
    # Cruce 
    ch_1 = c1_1 + c2_2
    ch_2 = c2_1 + c1_2
    
    # Crear nuevos individuos
    ch_1 = individuo(genes=ch_1)
    ch_2 = individuo(genes=ch_2)
    
    return ch_1, ch_2

#benja
def fitness():
    #Se ordena de Menor a mayor segun los pasos que dan 
    Poblacion.sort(key=lambda sujeto: sujeto.pasos)

#pablo Funcion de seleccion que devuelve los dos mejores individuos por su fitness 
def seleccion(Poblacion_ordenada):
    c1 = Poblacion_ordenada[0]
    c2 = Poblacion_ordenada[1]
    return c1, c2

#benja
def rellenar_Poblacion(): 
    dif = -NPob - len(Poblacion) 
    if dif > 0 :
        for i in range(dif):
            Poblacion.append(individuo.generar_genes())

#carlo
def init_Poblacion():
    for x in range(NPob):
        i = individuo(position=[x,0])
        Poblacion.append(i)
        MAP[x][0] = i
    

def colision(pos):
    index_indi = 0
    for a in Poblacion:
        if a.position[0] == pos[0] and a.position[1] == pos[1]:
            return True , index_indi  
        index_indi +=1                          
    return False

# coto
"""MAP = [[0,X,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
"""

def posicionar(posm,posicion,a):
        # [n, s, e, o, ne, no, se, so, asesino]
    if posm == 0 :
        #n
        posicion[0]-=1
    elif posm == 1:
        #s
        posicion[0]+=1
    elif posm == 2:
        #e
        posicion[1]+=1   
    elif posm == 3:
        #o
        posicion[1]-=1
    elif posm == 4:
        #ne
        posicion[1]+=1 ; posicion[0]-=1
    elif posm == 5:
        #no
        posicion[0]-=1 ; posicion[1]-=1
    elif posm == 6:
        #se
        posicion[0]+=1 ; posicion[1]+=1
    elif posm == 7:
        #so
        posicion[0]+=1 ; posicion[0]-=1; 
    
    if posicion[0]>=0 and posicion[1]>=0 and posicion[0]<=len(MAP) and posicion[1] <= len(MAP):
        colisiono , indexcol = colision(posicion)
        if colisiono:
            if a == 1:
                Poblacion.pop(indexcol)
                Asesinatos +=1
                return posicion
        else :
            return posicion

def main():
    gen = 1
    while(gen <= nGen ):
        while():
            pass
        pass

    pass


