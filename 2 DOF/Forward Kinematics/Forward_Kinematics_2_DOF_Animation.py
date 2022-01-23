# LIBRARIES

import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# LINK LENGTHS

a1=a2=2.0

# JOINT ANGLES

T1=np.deg2rad(45)
#T2=0

x0=0
y0=0


increment=0.1

angles = np.arange(0,pi/2+increment,increment)


X1 = np.zeros(len(angles))
Y1 = np.zeros(len(angles)) 
X2 = np.zeros(len(angles)) 
Y2 = np.zeros(len(angles))



for ind1,T2 in enumerate(angles, start=0):
    
    x1=a1*cos(T1)
    y1=a1*sin(T1)

    x2=a1*cos(T1)+a2*cos(T1+T2)
    y2=a1*sin(T1)+a2*sin(T1+T2)
    
    X1[ind1] = x1 
    Y1[ind1] = y1
    X2[ind1] = x2
    Y2[ind1] = y2 
    
print("x1  ")
print(x2)
print("x2  ")
print(y2)
   


# set up the figure and subplot
fig = plt.figure()
fig.canvas.set_window_title('Matplotlib Animation')
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-4,4), ylim=(-2,6))
ax.grid()
ax.set_title('2-DOF animation')
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
line, = ax.plot([], [], 'o-', lw=5, color='#de2d26')

# initialization function
def init():
    line.set_data([], [])
    return line,

# animation function
def animate(i):
    x_points = [0, X1[i], X2[i]]
    y_points = [0, Y1[i], Y2[i]]

    line.set_data(x_points, y_points)
    return line,

# call the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(X1), interval=100, blit=True, repeat=False)
## to save animation, uncomment the line below:
## ani.save('offset_piston_motion_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

#show the animation
plt.show()
