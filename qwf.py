import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

# Raumgitter
L = 2*np.pi
N = 60
x = np.linspace(0, L, N)
y = np.linspace(0, L, N)
X, Y = np.meshgrid(x, y)

# --- Wellenspezifikation ---------------------------------------------------
kx, ky = 1, 2   # for simplicity change these
c      = 1.0
ωx, ωy = c*kx, c*ky

def amplitude(t):
    Z  = np.sin(kx*X - ωx*t) + np.sin(ky*Y - ωy*t)
    Z[0, :], Z[-1, :], Z[:, 0], Z[:, -1] = 0, 0, 0, 0   # feste Ränder
    return Z

# --- Abbildung & erstes Surface -------------------------------------------
fig = plt.figure(figsize=(6, 4))
ax  = fig.add_subplot(111, projection='3d')
ax.set_zlim(-2, 2)
surf = [ax.plot_surface(X, Y, amplitude(0), cmap='viridis', linewidth=0)]

def update(frame):
    surf[0].remove()
    z = amplitude(frame*0.05)
    surf[0] = ax.plot_surface(X, Y, z, cmap='viridis', linewidth=0)
    return surf

ani = animation.FuncAnimation(fig, update,
                              frames=200, interval=30, blit=False)

plt.show()

ani.save('wave.gif', writer=animation.PillowWriter(fps=30))
