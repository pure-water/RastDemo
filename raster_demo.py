"""
Matplotlib Animation Example

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

#sx=np.array(0:640*480)
#print(sx.shape)
#sy=np.array(0:640*480).T
#print(sy.shape)

#s_tile = np.vstack((sx, sy)).T

#s_tile=np.zeros((20,15))

#for i in range(0,20):
#    for j in range(0,15) :
#        s_tile[i,j] =[i,j]

s_tile = np.array([[0,0],[0,1],[1,0],[1,1],[2,0],[2,1],[3,0],[3,1],[0,2],[1,2],[0,3],[1,3]])
#print(s_tile.shape)

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 640), ylim=(0, 480))
plt.ylim(max(plt.ylim()), min(plt.ylim()))
plt.title("Mali Render Order Demo")

major_ticks = np.arange(0, 640+32, 32)
minor_ticks = np.arange(0, 480+32, 32)
ax.set_xticks(major_ticks)
ax.set_yticks(minor_ticks)


tile_dot, = ax.plot([], [], 'go')

# And a corresponding grid
ax.grid(which='both')

plt.grid(True)

# initialization function: plot the background of each frame
def init():
    tile_dot.set_data([], [])
    return tile_dot,

# animation function.  This is called sequentially
def animate(i):
    #x = np.linspace(0, 2, 1000)
    #y = np.sin(2 * np.pi * (x - 0.01 * i))

    offset = 0.5
    x = s_tile[:i,0]*32 + offset*32
    y = s_tile[:i,1]*32 + offset*32
    tile_dot.set_data(x, y)
    return tile_dot,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=4, interval=600, blit=False)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
