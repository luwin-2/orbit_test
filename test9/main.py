import matplotlib.pyplot as plt
import numpy as np

# 기본 상수
G = 6.67430e-11  # 만유인력 상수 (m^3 kg^-1 s^-2)
M = 5.972e24  # 지구 질량 (kg)
R = 6.371e6  # 지구 반지름 (m)

# 시간 설정
dt = 1  # 시간 간격 (초)
T = 60000  # 전체 시뮬레이션 시간 (초)

# 초기 조건
x0 = R + 500000  # 지표면에서 500km 위 (m)
y0 = 0
vx0 = 0
vy0 = 11200  # 초기 속도 (m/s), 궤도 진입 시도

# 위치와 속도 초기화
x, y = x0, y0
vx, vy = vx0, vy0

# 궤도 기록용 리스트
xs, ys = [], []

for _ in range(T):
    r = np.sqrt(x ** 2 + y ** 2)
    if r < R:
        break  # 지표면에 충돌

    # 중력 가속도
    a = -G * M / r ** 3
    ax = a * x
    ay = a * y

    # 속도 갱신
    vx += ax * dt
    vy += ay * dt

    # 위치 갱신
    x += vx * dt
    y += vy * dt

    # 기록
    xs.append(x)
    ys.append(y)

# 시각화
plt.figure(figsize=(6, 6))
earth = plt.Circle((0, 0), R, color='blue', alpha=0.5)
plt.gca().add_patch(earth)
plt.plot(xs, ys, label='Trajectory')
plt.title('Satellite Orbit Simulation')
plt.xlabel('x (1000Km)')
plt.ylabel('y (1000Km)')
plt.axis('equal')
plt.legend()
plt.grid(True)
plt.show()
