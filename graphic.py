import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Número de generaciones y tamaño de la cuadrícula
num_generations = 100
grid_size = (30, 30)

# Generación de datos de prueba (booleanos)
gens = np.random.rand(num_generations, *grid_size) > 0.5

fig, ax = plt.subplots(figsize=(8, 8))

# Configuración de la animación

im = ax.imshow(gens[0], cmap='Reds', interpolation='nearest')
plt.colorbar(im, ax=ax)
ax.set_title('Posiciones finales de generacion')
ax.axis('off')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

# Función de inicialización para la animación
def init():
    im.set_data(gens[0])
    return [im]

# Función de animación que se ejecutará en cada cuadro
def animate(i):
    im.set_data(gens[i])
    return [im]


# Crea la animación usando las funciones anteriores
ani = animation.FuncAnimation(fig, animate, frames=num_generations, init_func=init, blit=True)
plt.show()
