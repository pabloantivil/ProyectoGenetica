import random

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

        # [n, s, e, o, ne, no, se, so, asesino]
        # [1, 1, 1, 1, 1,  1,   1,   1,     1]/24
        #self.gen()

        if len(self.genes) == 0:
            self.generar_genes()
        else:
            self.mutar()
        
    #javier
    def generar_genes(self):
        #generear los genes de el individuo
        pass
    
    #javier 
    def mutar(self):
        # puedes cambiar los gene segun 
        pass

    #coto
    def move(self):
        #muevete CTM
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
def fitness(poblacion):
    #ordenar  poblacion y eliminar penkas
    pass

#pablo Implementa un mecanismo de selección que favorece a los individuos que realizan menos movimientos para llegar al borde seleccionado.
def seleccion(poblacion_ordenada):
    #retornar dos indivduos segun pasos
    pass

#bejna
def rellenar_poblacion(): 
    #rellenar
    pass

#carlo
def init_poblacion():
    #generar poblacion
    pass



# coto
def posisionar():
    # dar posisiones iniciales
    pass


#
def main():
    gen = 1
    while(gen <= nGen ):
        while():
            pass
        pass

    pass


