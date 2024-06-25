import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

seed = 19680801 
np.random.seed(seed)
print("semilla:", seed)
NPob = 15 #Numero de poblacion
Poblacion = []
nGen = 50 #Numero de generaciones
npasos = 100 #Numero de pasos maximos que puedendar
Asesinatos = 0
Map_x = 10
Map_y = 25
Map = np.full((Map_x, Map_y,3),255)

# Para almacenar datos de las gráficas
muertes_por_generacion = []
asesinatos_por_generacion = []
ganadores_por_generacion = []

class individuo:
    def __init__(self,genes=[],position=[0,0]) -> None:
        self.genes = genes
        self.pasos = 0
        self.is_live = True
    
        # self asesino (true o false)

        # [n, s, e, o, ne, no, se, so, asesino]
        # [1, 1, 1, 1, 1 , 1,   1,  1,     1  ]
        #self.gen()

        if len(self.genes) == 0:
            self.generar_genes()
        else:
            self.mutar()
        self.color = self.getColor()
        self.position = self.ini_position()
        
            
    def ini_position(self):
            Pos_x = np.random.randint(0, Map_x-1)
            Pos_y = np.random.randint(0, 2)
            if np.array_equal( Map[Pos_x, Pos_y], np.array([255,255,255])):
                self.position = [Pos_x, Pos_y]
                Map[Pos_x, Pos_y] = self.color
                return ([Pos_x, Pos_y])
            else: 
               return self.ini_position()
    #javier
    def generar_genes(self):
        #generear los genes de el individuo
        self.genes = np.random.randint(0,10,size=9)
        self.genes[8]=0
        self.genes = self.genes / self.genes.sum()
        #Probabilidad de asesino 
        pasesino = [0.8,0.2]
        self.genes[8] = np.random.choice([0,1],p=pasesino)
        
    
    #javier 
    def mutar(self):
        # puedes cambiar los gene segun 
        prob_mutacion = 0.3  
        
        if np.random.uniform() <= prob_mutacion:
            index = np.random.randint(9)
            self.genes[index] = np.random.uniform()
            self.genes = self.normalizar(self.genes)

    
    def normalizar(self,vec):
        normalizado = []
        x = sum(vec)
        for i in vec:
            normalizado.append(i/x)
        return normalizado

    #coto
    def move(self):
        mov = np.random.choice(range(8),p=self.genes[:8])
           
        self.pasos +=1
        self.position=posicionar(mov , self.position.copy(), self.genes[8])

    def getColor(self):
    # Ponderaciones para los colores RGB según las direcciones
        ponderaciones = [-0.1, -0.1, -0.2, 0.6, -0.15, 0.2, -0.15, 0.2]
        # Calcular la suma ponderada de los genes y las ponderaciones
        suma = sum(ponderaciones[x] * self.genes[x] for x in range(len(ponderaciones)))
        # Asegurarse de que suma esté en el rango [-1, 1]
        suma = max(-1, min(suma, 1))
        # Mapear la suma al rango de 0 a 255 para los colores RGB
        if suma > 0:
            color_value = int(suma * 255)  # Para valores positivos
            # Ajustar intensidad según la dirección
            if self.genes[3] == 1:  # oeste
                color_value = min(color_value + 50, 255)  # Incrementar el canal azul para oeste
            if self.genes[5] == 1:  # noroeste
                color_value = min(color_value + 70, 255)  # Incrementar el canal azul más para noroeste
            if self.genes[7] == 1:  # suroeste
                color_value = min(color_value + 70, 255)  # Incrementar el canal azul más para suroeste
            return (color_value, 0, 0)
        else:
            color_value = int(-suma * 255)  # Para valores negativos
            # Ajustar intensidad según la dirección
            if self.genes[3] == 1:  # oeste
                color_value = min(color_value + 50, 255)  # Incrementar el canal rojo para oeste
            if self.genes[5] == 1:  # noroeste
                color_value = min(color_value + 70, 255)  # Incrementar el canal rojo más para noroeste
            if self.genes[7] == 1:  # suroeste
                color_value = min(color_value + 70, 255)  # Incrementar el canal rojo más para suroeste

            return (0, 0, color_value)

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
    
    # Activamos mutar
    ch_1.mutar()
    ch_2.mutar()

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

def seleccion():
    global Poblacion
    fitness()
    
    probabilidades(Poblacion)
    
    sel = []
    while len(sel) < 2:
        for individuo in Poblacion:
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
            Map[x.position[0]][x.position[1]] = x.color
#carlo
def init_Poblacion():
    global Poblacion , Map_x
    if NPob <= (Map_x*2-5):
        for x in range(NPob):
            i = individuo()
            Poblacion.append(i)
            Map[i.position[0]][i.position[1]] = i.color
    else:
        print("Poblacion demaciado grande")
    
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
                Map[Poblacion[indexcol].position[0],Poblacion[indexcol].position[1]] = np.array([255,255,255])
                Poblacion.pop(indexcol)
                Asesinatos +=1
                return posicion
            else:
                return ori
        else :
            return posicion
    else: 
        return ori

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
    return salvados, conmuertos, llegaron


# Función de inicialización para la animación
def init():
    print("generacion 0")
    im.set_data(Map)
    return [im]

# Función de animación que se ejecutará en cada cuadro
def animate(i):
    global pasos,npasos,gen,Poblacion,Asesinatos

    if pasos == npasos:
        Poblacion ,muertos,ganadores = terminados()
        muertes_por_generacion.append(muertos)
        asesinatos_por_generacion.append(Asesinatos)
        ganadores_por_generacion.append(ganadores)
        #Escribir codigo de cruza 
        if len(Poblacion) > 1:
            c1, c2 = seleccion(Poblacion)
            h1, h2 = cruce(c1, c2)
            Poblacion.append(h1)
            Poblacion.append(h2)
        #Rellenar poblacion
        rellenar_Poblacion()
        Map.fill(255)
        gen += 1 
        pasos = 0
        print("Ganadores: ",ganadores)
        print("Muertos por no llegar: ", muertos)
        print("Asesinatos: ",Asesinatos)
        print("generacion N°",gen)
        #Reinicio asesinatos
        Asesinatos = 0
    else:
        for indi in Poblacion :
            Map[indi.position[0],indi.position[1]] = np.array([255,255,255])
            #Logica al revez de asalvo 
            if not asalvo(indi.position):
                indi.move()
            Map[indi.position[0],indi.position[1]] = indi.color

    im.set_data(Map)
    pasos += 1
    ax2.clear()
    ax3.clear()
    ax4.clear()

    ax2.plot(muertes_por_generacion, label='Muertes')
    ax2.set_xlabel('Generaciones')
    ax2.set_ylabel('Cantidad')
    ax2.set_title('Muertos por Generación')
    ax2.set_xlim([1,nGen])
    ax2.set_ylim([0,NPob])


    ax3.plot(asesinatos_por_generacion, label='Asesinatos')
    ax3.set_xlabel('Generaciones')
    ax3.set_ylabel('Cantidad')
    ax3.set_title('Asesinados por Generación')
    ax3.set_xlim([1,nGen])
    ax3.set_ylim([0,NPob])

    ax4.plot(ganadores_por_generacion, label='Ganadores')
    ax4.set_xlabel('Generaciones')
    ax4.set_ylabel('Cantidad')
    ax4.set_title('Ganadores por Generación')
    ax4.set_xlim([1,nGen])
    ax4.set_ylim([0,NPob])
    plt.tight_layout(pad=1.0)

    ax1.set_title(f'Generación {gen}, Iteración {pasos}')
    return [im]

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(8, 8), gridspec_kw={'height_ratios': [3, 1, 1, 1]})  
im = ax1.imshow(Map, cmap='Reds', interpolation='nearest')
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')  # En Windows
#Permite la cuadricula de movimiento para los individuos (tiles)
ax1.set_xticks(np.arange(-0.5, Map.shape[1], 1), minor=True)
ax1.set_yticks(np.arange(-0.5, Map.shape[0], 1), minor=True)
ax1.grid(which='minor', color='gray', linestyle='-', linewidth=1)
ax1.tick_params(which='minor', size=0)
ax1.axis('on')

init_Poblacion()
gen = 1
pasos = 0

ani = animation.FuncAnimation(fig, animate, frames=nGen * npasos, init_func=init, interval=0.00000000001, blit=False)

plt.tight_layout()
plt.subplots_adjust(hspace=0.5)
plt.show()

