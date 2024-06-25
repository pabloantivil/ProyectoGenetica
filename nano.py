import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

seed = 19680801 
np.random.seed(seed)
print("semilla:", seed)
NPob = 10
NCicles = 10
Poblacion = []
nGen = 10
npasos = 50
Asesinatos = 0
Map_x = 10
Map_y = 10
Map = np.full((Map_x, Map_y), False)

class individuo:
    def __init__(self,genes=[],position=[0,0]) -> None:
        self.genes = genes
        self.pasos = 0
        self.is_live = True
        self.position = self.ini_position()
    
        # self asesino (true o false)

        # [n, s, e, o, ne, no, se, so, asesino]
        # [1, 1, 0, 1, 0 , 1,   0,  1,     0  ]
        #self.gen()
    
        if len(self.genes) == 0:
            self.generar_genes()
        else:
            self.mutar()
    
    def ini_position(self):
            Pos_x = np.random.randint(0, Map_x-1)
            Pos_y = np.random.randint(0, 2)
            if not Map[Pos_x, Pos_y] :
                self.position = [Pos_x, Pos_y]
                Map[Pos_x, Pos_y] = True
                return ([Pos_x, Pos_y])
            else: 
               return self.ini_position()
    #javier
    def generar_genes(self):
        #generear los genes de el individuo
        self.genes = [np.random.randint(0,2) for _ in range(9)]
        
    
    #javier 
    def mutar(self):
        # puedes cambiar los gene segun 
        prob_mutacion = 0.3  
        
        if np.random.uniform() <= prob_mutacion:
            index = np.random.randint(9)
            self.genes[index] = np.random.uniform()
            self.genes = self.normalizar(self.genes)

    
    def normalizar(vec):
        normalizado = []
        x = sum(vec)
        for i in vec:
            normalizado.append(i/x)
        return normalizado

    #coto
    def move(self):
        mov = np.random.randint(len(self.genes)-1)# 8,1 OCHOYUNO
        if self.genes[mov] == 1 :
            self.position=posicionar(mov , self.position.copy(), self.genes[8])

    def getColor():
       # suma = [0.2, 0.2, 0.1, 0.6, 0.4, 0.4, , so]
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
    Poblacion.sort(key=lambda sujeto: sujeto.pasos)

def probabilidades(individuos):
    p = 0.3
    for i, individuo in enumerate(individuos):
        probabilidad = p * (1 - p) ** i
        individuo.seleccion = probabilidad

def seleccion(poblacion):
    poblacion.sort(key=lambda sujeto: sujeto.pasos)
    
    probabilidades(poblacion)
    
    sel = []
    while len(sel) < 2:
        for individuo in poblacion:
            if random.random() < individuo.seleccion:
                sel.append(individuo)
            if len(sel) == 2:
                break
            
    c1, c2 = sel[0], sel[1]
    return c1, c2

#benja
def rellenar_Poblacion(): 
    dif = NPob - len(Poblacion) 
    if dif > 0 :
        for i in range(dif):
            x = individuo()
            Poblacion.append(x)
            Map[x.position[0]][x.position[1]] = True
#carlo
def init_Poblacion():
    global Poblacion , Map_x
    if NPob <= (Map_x*2-5):
        for x in range(NPob):
            i = individuo()
            Poblacion.append(i)
            Map[i.position[0]][i.position[1]] = True
    
def asalvo(pos):
    if pos[1] == Map_y-1 :
        return True
    else:
        return False
def colision(pos):
    index_indi = 0
    for a in Poblacion:
        if a.position[0] == pos[0] and a.position[1] == pos[1]:
            return True , index_indi  
        index_indi +=1                          
    return False ,index_indi

# coto

def posicionar(posm,posicion,a):
    global Asesinatos
    ori = posicion.copy()
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
        posicion[0]+=1 ; posicion[1]-=1; 
    if posicion[0]>=0 and posicion[1]>=0 and posicion[0]<Map_x and posicion[1] < Map_y:
        colisiono , indexcol = colision(posicion)
        if colisiono:
            if a == 1:
                Map[Poblacion[indexcol].position[0],Poblacion[indexcol].position[1]] = False
                Poblacion.pop(indexcol)
                Asesinatos +=1
                return posicion
            else:
                return ori
        else :
            return posicion
    else: 
        return ori

gen = 0
pasos = 0

def terminados():
    salvados = []
    conmuertos = 0
    llegaron = 0
    for p in Poblacion:
        if asalvo(p.position):
            p.position = p.ini_position()
            salvados.append(p)
            llegaron += 1
        else:
            conmuertos+=1
    return salvados , conmuertos ,llegaron


# Función de inicialización para la animación
def init():
    print("generacion 0")
    im.set_data(Map)
    return [im]

# Función de animación que se ejecutará en cada cuadro
def animate(i):
    global pasos, npasos,gen,Poblacion,Asesinatos
    if pasos == npasos:
        Poblacion ,muertos,ganadores = terminados()
        #Escribir codigo de cruza 

        #Rellenar poblacion
        rellenar_Poblacion()
        Map.fill(False)
        gen += 1 
        pasos = 0
        print("Ganadores : ",ganadores)
        print("Muertos por no llegas : " , muertos)
        print("Asesinatos : ",Asesinatos)
        print("generacion N°",gen)
        #Reinicio asesinatos
        Asesinatos = 0
    else:
        for indi in Poblacion :
            Map[indi.position[0],indi.position[1]] = False
            #Logica al revez de asalvo 
            if not asalvo(indi.position):
                indi.move()
            Map[indi.position[0],indi.position[1]] = True

    im.set_data(Map)
    pasos += 1
    return [im]

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(8, 8))  
plt.subplots_adjust(wspace=0.5)

im = ax1.imshow(Map, cmap='Reds', interpolation='nearest')
plt.colorbar(im, ax=ax1)
ax1.set_title('Posiciones finales de generacion')
ax1.axis('off')
init_Poblacion()
ax1.grid(color = 'black', linestyle = '--', linewidth = 0.5)
ani = animation.FuncAnimation(fig, animate, frames=nGen * npasos, init_func=init, blit=True)

#ax2.plot(gen, [:nGen], color='red', label='Muertos')
ax2.set_xlabel('Generaciones')
ax2.set_ylabel('Cantidad')
ax2.set_title('Muertos por Generación')

#ax3.plot(gen, Asesinatos[:nGen], color='blue', label='Asesinados')
ax3.set_xlabel('Generaciones')
ax3.set_ylabel('Cantidad')
ax3.set_title('Asesinados por Generación')

#ax4.plot(gen, [:nGen], color='green', label='Ganadores')
ax4.set_xlabel('Generaciones')
ax4.set_ylabel('Cantidad')
ax4.set_title('Ganadores por Generación')

plt.tight_layout()
plt.show()

