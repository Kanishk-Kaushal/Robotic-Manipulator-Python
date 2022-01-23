# LIBRARIES

import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# LINK LENTGHS

a1 = input("Enter Length for Link 1: \n")
a2 = input("Enter Length for Link 2: \n")

increment = 0.1

# END EFFECTOR POSITION ARRAY

Y = float(input("Enter Desired Y Coordinate: \n"))
X_0 = float(input("Enter Desired X Coordiante: \n"))

#Y = 0.0
X = np.arange(0,X_0+increment,increment)


X1 = np.zeros(len(X))
Y1 = np.zeros(len(X)) 
X2 = np.zeros(len(X)) 
Y2 = np.zeros(len(X))

for ind1,x in enumerate(X, start=0):

  
    r = sqrt(x**2+Y**2)
    phi1 = np.arctan(Y/x)
    phi2 = np.arccos((r**2+float(a1)**2-float(a2)**2)/(2*r*float(a1)))
    phi3 = np.arccos((float(a1)**2+float(a2)**2-r**2)/(2*float(a1)*float(a2)))

    # JOINT ANGLES

    T2 = pi-phi3
    T1 = phi1-phi2

    '''

    print("Joint Angle 1: \n ")
    print(T1)
    print("Joint Angle 2: \n ")
    print(T2)
    
    '''
    
    x1 = float(a1)*cos(T1)
    y1 = float(a1)*sin(T1)

    x2 = float(a1)*cos(T1)+float(a2)*cos(T1+T2)
    y2 = float(a1)*sin(T1)+float(a2)*sin(T1+T2)

    X1[ind1] = x1 
    Y1[ind1] = y1
    X2[ind1] = x2
    Y2[ind1] = y2 

# ANIMATION

fig = plt.figure()
fig.canvas.set_window_title('Matplotlib Animation')
ax = fig.add_subplot(111, aspect='equal', autoscale_on=True, xlim=(-5,5), ylim=(-5,5))
ax.grid()
ax.set_title('2-DOF animation')
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
line, = ax.plot([], [], '-', lw = 3, color='#de2d26')

# INITIALIZATION FUNCTION

def init():
    line.set_data([], [])
    return line,

# ANIMATION FUNCTION

def animate(i):
    x_points = [0, X1[i], X2[i]]
    y_points = [0, Y1[i], Y2[i]]

    line.set_data(x_points, y_points)
    return line,

# CALL THE ANIMATION

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(X1), interval=100, blit=True, repeat=False)


# SHOW THE ANIMATION

plt.show()
    
