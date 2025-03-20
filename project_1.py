import numpy as np
import matplotlib.pyplot as plt

t_continuous = np.linspace(0, 4 * np.pi, 1000)
y_continuous = np.cos(t_continuous)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(t_continuous, y_continuous)
plt.title('连续余弦信号')
plt.xlabel('时间 (t)')
plt.ylabel('幅度')
plt.grid(True)

t_discrete = np.arange(0, 10)
y_discrete = np.heaviside(t_discrete - 3, 1)

plt.subplot(1, 2, 2)
plt.stem(t_discrete, y_discrete)
plt.title('离散阶跃信号')
plt.xlabel('时间 (n)')
plt.ylabel('幅度')
plt.grid(True)

plt.tight_layout()
plt.show()
    