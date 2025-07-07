import matplotlib.pyplot as plt
import numpy as np

# 기본 상수
G = 6.67430e-11  # 만유인력 상수 (m^3 kg^-1 s^-2)
M = 5.972e24     # 지구 질량 (kg)
R = 6.371e6      # 지구 반지름 (m)

# 시뮬레이션 시간 설정
dt = 1           # 시간 간격 (초)
T = 100000         # 전체 시뮬레이션 시간 (초)

# 테스트할 초기 속도들
initial_speeds = [1000, 3000, 7500, 10000]
colors = ['red', 'green', 'blue', 'purple']

# 궤도 시뮬레이션 함수
def simulate_orbit(vy0):
    x, y = R + 500000, 0  # 지표면에서 500km 상공
    vx, vy = 0, vy0
    xs, ys = [], []
    for _ in range(T):
        r = np.sqrt(x**2 + y**2)
        if r < R:
            break  # 지표면 충돌
        a = -G * M / r**3
        ax = a * x
        ay = a * y
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        xs.append(x)
        ys.append(y)
    return xs, ys

# 시각화
plt.figure(figsize=(8, 8))
earth = plt.Circle((0, 0), R, color='blue', alpha=0.5, label='Earth')
plt.gca().add_patch(earth)

for speed, color in zip(initial_speeds, colors):
    xs, ys = simulate_orbit(speed)
    plt.plot(xs, ys, label=f'{speed} m/s', color=color)

plt.title('Satellite Orbit Simulation with Various Initial Speeds')
plt.xlabel('x (1000Km)')
plt.ylabel('y (1000Km)')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
