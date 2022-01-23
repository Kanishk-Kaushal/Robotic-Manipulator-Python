# POINT BEYOND WORKSPACE PROBLEM

# LIBRARIES

import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# LINK LENGTHS

a1 = float(input("Enter Length for Link 1: \n"))
a2 = float(input("Enter Length for Link 2: \n"))

# END EFFECTOR POSITION ARRAY

x_i = float(input("Enter Initial X Coordinate: \n"))
y = float(input("Enter Initial & Desired Y Coordinate: \n"))
X_0 = float(input("Enter Desired X Coordinate: \n"))



# WORKSPACE PROBLEM 

if(((y*y)+(X_0*X_0)) > ((a1+a2)*(a1+a2))):

    X_0 = (a1+a2)*(X_0)/(sqrt((X_0*X_0)+(y*y)))
    y = (a1+a2)*(y)/(sqrt((X_0*X_0)+(y*y)))

else:
    X_0 += 0
    y += 0
    


if(X_0 < x_i):
    increment= -0.05
else:
    increment = 0.05

X = np.arange(x_i,X_0+increment,increment)

X1 = np.zeros(len(X))
Y1 = np.zeros(len(X)) 
X2 = np.zeros(len(X)) 
Y2 = np.zeros(len(X))
R1 = np.zeros(len(X))
R2 = np.zeros(len(X))

# INVERSE KINEMATICS

for ind1,x in enumerate(X, start=0):

    r = sqrt(x**2+y**2)

    # ELBOW UP FOR ACTUAL ARM

    if(X_0 < 0 ):
        phi1 = -np.arccos((a1**2+r**2-a2**2)/(2*a1*r))
        phi2 = np.arctan(y/(x+0.0000001)) + pi
        phi3 = -np.arccos((a1**2+a2**2-r**2)/(2*a1*a2))
    else:
        phi1 = np.arccos((a1**2+r**2-a2**2)/(2*a1*r))
        phi2 = np.arctan(y/(x+0.0000001))
        phi3 = np.arccos((a1**2+a2**2-r**2)/(2*a1*a2))

  
    # JOINT ANGLES

    T1 = phi1 + phi2
    T2 = phi3 - pi

    # FORWARD KINEMATICS

    x1 = a1*cos(T1)
    y1 = a1*sin(T1)

    x2 = a1*cos(T1)+a2*cos((T2+T1))
    y2 = a1*sin(T1)+a2*sin((T2+T1))


    X1[ind1] = x1 
    Y1[ind1] = y1
    X2[ind1] = x2
    Y2[ind1] = y2
    R1[ind1] = sqrt((x1**2)+(y1**2))
    R2[ind1] = sqrt((x2**2)+(y2**2))

    

# SET UP THE FIGURE AND SUBPLOT

print("JOINT ANGLE 1: \n")
print(T1*(180/pi))
print("\n")
print("JOINT ANGLE 2: \n")
print(T2*(-180./pi))
print("\n")

# SIMULATION

fig = plt.figure()
fig.canvas.set_window_title('Matplotlib Animation')
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-4,4), ylim=(-4,4))
ax.grid()
ax.set_title('2-DOF animation')
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
line, = ax.plot([], [], 'o-', lw=5, color='#de2d26')
line1, = ax.plot([], [], '-', lw=2, color='#104E8B' )
plt.plot()


# INITIALIZE FUNCTION

def init():

    line.set_data([], [])
    line1.set_data([], [])
    return line, line1

# ANIMATION FUNCTION 

def animate(i):

    x_points = [0, X1[i], X2[i]]
    y_points = [0, Y1[i], Y2[i]]
    r_points = [0, X2[i], 0]

    line.set_data(x_points, y_points)
    line1.set_data(r_points, y)

    return line , line1

# CALL THE ANIMATION

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(X1), interval=125, blit=True, repeat=False)


# SHOW THE ANIMATION

plt.show()
