import matplotlib.pyplot as plt
import numpy as np

# 기본 상수
G = 6.67430e-11  # 만유인력 상수 (m^3 kg^-1 s^-2)
M = 5.972e24     # 지구 질량 (kg)
R = 6.371e6      # 지구 반지름 (m)

# 시간 설정
dt = 1           # 시간 간격 (초)
T = 6000         # 전체 시뮬레이션 시간 (초)

# 초기 조건
x0 = R + 500000  # 지표면에서 5000km 위 (m)
y0 = 0
vx0 = 0
vy0 = 7600       # 초기 속도 (m/s), 궤도 진입 시도

# 위치와 속도 초기화
x, y = x0, y0
vx, vy = vx0, vy0

# 궤도 기록용 리스트
xs, ys, speeds = [], [], []

for _ in range(T):
    r = np.sqrt(x**2 + y**2)
    if r < R:
        break  # 지표면에 충돌

    # 중력 가속도
    a = -G * M / r**3
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
    speeds.append(np.sqrt(vx**2 + vy**2))

# 시각화: 궤도와 속도 그래프
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 궤도 시각화
earth = plt.Circle((0, 0), R, color='blue', alpha=0.5, label='Earth')
ax1.add_patch(earth)
ax1.plot(xs, ys, label='Trajectory', color='orange')
ax1.set_title('Satellite Orbit Simulation')
ax1.set_xlabel('x (m)')
ax1.set_ylabel('y (m)')
ax1.set_aspect('equal')
ax1.legend()
ax1.grid(True)

# 속도 시각화
time = np.arange(len(speeds)) * dt
ax2.plot(time, speeds, label='Speed (m/s)', color='green')
ax2.set_title('Speed Over Time')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Speed (m/s)')
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()
