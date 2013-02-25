import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

# gamma und gammap
t = np.arange(0.0, 2.0, 0.01)
n = np.size(t)
s = np.sin(2*np.pi*t)
s2 = np.cos(2*np.pi*t)

line, = ax.plot(t, s, lw=1, color='k')
line2, = ax.plot(t, s2, lw=1, color='k', linestyle='--')

plotn=3*n/5
ax.annotate('$\gamma$', xy=(t[plotn], s[plotn]), xytext=(t[plotn]+0.2, s[plotn]+0.5),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )
plotn=n/2
ax.annotate('$\dot{\gamma}$', xy=(t[plotn], s2[plotn]), xytext=(t[plotn]-0.2, s2[plotn]+0.5),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )
ax.set_ylim(-2,2)
frame = plt.gca()
frame.axes.get_xaxis().set_ticks([])
frame.axes.get_yaxis().set_ticks([])
plt.xlabel('t')
plt.ylabel('Auslenkung und Scherung')
fig.show()
fig.set_size_inches((15,5),forward=True)
fig.savefig("SchwingungsmodiA")

# Antwort
fig = plt.figure()
ax = fig.add_subplot(111)

s = np.sin(2*np.pi*t)
s2 = np.cos(2*np.pi*t)
s3 = np.sin(2*np.pi*t+np.pi/4)

line, = ax.plot(t, s, lw=1, color='k')
line2, = ax.plot(t, s2, lw=1, color='k', linestyle='--')
line3, = ax.plot(t, s3, lw=1, color='b')

plotn=3*n/5
ax.annotate('Elastisch', xy=(t[plotn], s[plotn]), xytext=(t[plotn]+0.2, s[plotn]+0.5),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )
plotn=n/2
ax.annotate('Viskos', xy=(t[plotn], s2[plotn]), xytext=(t[plotn]-0.2, s2[plotn]+0.5),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )

plotn=n/3
ax.annotate('Viskoelastisch', xy=(t[plotn], s3[plotn]), xytext=(t[plotn]-0.4, s3[plotn]-0.8), color = 'b',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )

ax.set_ylim(-2,2)
frame = plt.gca()
frame.axes.get_xaxis().set_ticks([])
frame.axes.get_yaxis().set_ticks([])
plt.xlabel('t')
plt.ylabel('Widerstand')
plt.show()
fig.set_size_inches((15,5),forward=True)
fig.savefig("SchwingungsmodiB")
