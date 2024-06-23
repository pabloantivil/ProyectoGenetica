import random
import numpy as np

NPob = 10 
SEED = 12
NCicles = 2
POBLACION = []
MAP = [[]]
nGen = 10
nPasos = 10


class individuo:
    def __init__(self,genes=[],position=[0,0]) -> None:
        self.genes = genes
        self.pasos = 0
        self.is_live = True
        self.position = position
        # self asesino (true o false)

        self.direcciones = {0: 'n', 1: 's', 2: 'e', 3: 'o', 4: 'ne', 5: 'no', 6: 'se', 7: 'so', 8: 'asesino'}
        # [n, s, e, o, ne, no, se, so, asesino]
        #self.gen()

        if len(self.genes) == 0:
            self.generar_genes()
        else:
            self.mutar()
        
    #javier
    def generar_genes(self):
        #generear los genes de el individuo
        genes = self.normalizar([np.random.uniform() for _ in range(8)])
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
        #muevete CTM
        direccion = self.direcciones[np.random.choice(9, p=self.genes)]
        nueva_pos = posicionar(self.position, direccion)
        #retornar poss
        pass



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
    POBLACION.sort(key=lambda sujeto: sujeto.pasos)

#pablo Funcion de seleccion que devuelve los dos mejores individuos por su fitness 
def seleccion(poblacion_ordenada):
    c1 = poblacion_ordenada[0]
    c2 = poblacion_ordenada[1]
    return c1, c2

#benja
def rellenar_poblacion(): 
    dif = -NPob - len(POBLACION) 
    if dif > 0 :
        for i in range(dif):
            POBLACION.append(individuo.generar_genes())

#carlo
def init_poblacion():
    #generar poblacion
    pass

                                     

# coto
def posicionar(posicion, direccion, valorX, valorY):
    # Función para actualizar la posición según la dirección
    if direccion == 'n':
        return (posicion[0], max(0, posicion[1] - 1))
    elif direccion == 's':
        return (posicion[0], min(valorY, posicion[1] + 1))
    elif direccion == 'e':
        return (min(valorX, posicion[0] + 1), posicion[1])
    elif direccion == 'o':
        return (max(0, posicion[0] - 1), posicion[1])
    elif direccion == 'ne':
        return (min(valorX, posicion[0] + 1), max(0, posicion[1] - 1))
    elif direccion == 'no':
        return (max(0, posicion[0] - 1), max(0, posicion[1] - 1))
    elif direccion == 'se':
        return (min(valorX, posicion[0] + 1), min(valorY, posicion[1] + 1))
    elif direccion == 'so':
        return (max(0, posicion[0] - 1), min(valorY, posicion[1] + 1))
    elif direccion == 'asesino':
        return posicion


#
def main():
    gen = 1
    while(gen <= nGen ):
        while():
            pass
        pass

    pass


