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


