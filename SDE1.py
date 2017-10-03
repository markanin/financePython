import numpy as np
import matplotlib.pyplot as plt

t_0 = 0
t_F = 8
length = 4000 # number of datapoints along t-axis
theta = 1.0
mu_A = 1.0
mu_B = 1.5
sigma1 = 0.0
sigma2 = 0.1
sigma3 = 0.5

t = np.linspace(t_0,t_F,length)
dt = np.mean(np.diff(t))

y1 = np.zeros(length)
y2 = np.zeros(length)
y3 = np.zeros(length)

y0 = 0

noise = np.random.normal(loc=0.0,scale=1.0,size=length)*np.sqrt(dt)

for i in range(1,length):
    if i < length/2:
        mu = mu_A
    else:
        mu = mu_B

    y1[i] = y1[i - 1] + theta*(mu-y1[i - 1]) * dt + sigma1 * noise[i]
    y2[i] = y2[i - 1] + theta*(mu-y2[i - 1]) * dt + sigma2 * noise[i]
    y3[i] = y3[i - 1] + theta*(mu-y3[i - 1]) * dt + sigma3 * noise[i]

plt.plot(t, y1, label='sigma=%.1f' % sigma1)
plt.plot(t, y2, label='sigma=%.1f' % sigma2)
plt.plot(t, y3, label='sigma=%.1f' % sigma3)
plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.vlines(4, 0, 2) # indicate the point where mu switches from mu_A to mu_B
plt.title('Test Ornstein–Uhlenbeck process')
plt.grid()
plt.show()

