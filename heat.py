from numpy import zeros,sin,meshgrid,linspace,empty
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def heat_transf2d(init_cond, time, alpha):

    nrow = init_cond.shape[0]
    ncol = init_cond.shape[1]
    y_t=zeros((nrow,ncol,time))
    t=0

    while t < time-1:
        for x in range(1,ncol-1):
            for y in range(1,nrow-1):
                y_t[x,y,t+1] = y_t[x,y,t] + sin(x/2+y/4)
                + (alpha/10) * (y_t[x+1,y,t] + y_t[x-1,y,t] - 2 * y_t[x,y,t]
                + y_t[x,y+1,t] + y_t[x,y-1,t] - 2 *y_t[x,y,t])  
        #y_t(x,y,t+1)=y_t(x,y,t+1)/max(max(y_t(:,:,t+1)));
        t=t+1

    x = linspace(0, 32, 32)
    y = linspace(0, 32, 32)
    X, Y = meshgrid(x, y)
    z = y_t[:,:,-1]

    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, z, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    plt.show()


init_cond = empty((32,32))
time = 500
alpha = 1

heat_transf2d(init_cond, time, alpha)


