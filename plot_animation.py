import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


frameheight = 480
framewidth  = 640

def data_gen(t=0):
    cnt = 0
    while cnt < (640*480+640*480/2)/16 :
        cnt += 1
        t += 0.1
        #yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
        yield t,cnt


def init():
    framewidth = 640 
    frameheight = 480
    ax.set_ylim(0, framewidth)
    ax.set_xlim(0, frameheight)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
plt.title('MALI GPU Frame Buffer Rendering')
xdata, ydata = [], []


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
                              repeat=False, init_func=init)
plt.show()