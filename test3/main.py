import matplotlib.pyplot as plt
import numpy as np

# 상수
G = 6.67430e-11       # 만유인력 상수 (m^3 kg^-1 s^-2)
M = 5.972e24          # 지구 질량 (kg)
R = 6.371e6           # 지구 반지름 (m)
rho0 = 1.225          # 해수면 공기 밀도 (kg/m^3)
H = 8500              # 대기 밀도 감소 고도 스케일 (m)
Cd = 0.47             # 공기 저항 계수 (구체 기준)
A = np.pi * (0.1**2)  # 대포알의 단면적 (지름 0.2m 가정)
m = 10.0              # 대포알 질량 (kg)

# 시뮬레이션 파라미터
dt = 0.1              # 시간 간격 (초)
T = 1000              # 총 시뮬레이션 시간 (초)
steps = int(T / dt)

# 실험 1: 공기 저항 포함한 수평 발사
x1, y1 = 0, R + 10000
vx1, vy1 = 20000, 0
xs1, ys1, speeds1 = [], [], []

for _ in range(steps):
    r = np.sqrt(x1**2 + y1**2)
    if r <= R:
        break
    a_grav = -G * M / r**3
    ax_g = a_grav * x1
    ay_g = a_grav * y1
    altitude = r - R
    rho = rho0 * np.exp(-altitude / H)
    v = np.sqrt(vx1**2 + vy1**2)
    F_drag = 0.5 * rho * Cd * A * v**2
    ax_d = -F_drag * vx1 / (v * m)
    ay_d = -F_drag * vy1 / (v * m)
    ax = ax_g + ax_d
    ay = ay_g + ay_d
    vx1 += ax * dt
    vy1 += ay * dt
    x1 += vx1 * dt
    y1 += vy1 * dt
    xs1.append(x1)
    ys1.append(y1)
    speeds1.append(np.sqrt(vx1**2 + vy1**2))

# 실험 2: 진짜 지구 궤도를 도는 이상적인 위성 (공기저항 X)
x2, y2 = R + 500000, 0
r2 = np.sqrt(x2**2 + y2**2)
vx2, vy2 = 0, np.sqrt(G * M / r2)
xs2, ys2, speeds2 = [], [], []

for _ in range(steps):
    r = np.sqrt(x2**2 + y2**2)
    a_grav = -G * M / r**3
    ax_g = a_grav * x2
    ay_g = a_grav * y2
    vx2 += ax_g * dt
    vy2 += ay_g * dt
    x2 += vx2 * dt
    y2 += vy2 * dt
    xs2.append(x2)
    ys2.append(y2)
    speeds2.append(np.sqrt(vx2**2 + vy2**2))

# 시각화: 궤도
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(np.array(xs1)/1000, (np.array(ys1) - R)/1000, label='With Air Resistance')
plt.plot(np.array(xs2)/1000, (np.array(ys2) - R)/1000, label='Ideal Orbit')
plt.axhline(0, color='blue', linestyle='--', label='Earth Surface')
plt.xlabel('Horizontal Distance (km)')
plt.ylabel('Altitude (km)')
plt.title('Trajectory Comparison')
plt.legend()
plt.grid(True)

# 시각화: 속도 그래프
plt.subplot(1, 2, 2)
plt.plot(np.arange(len(speeds1)) * dt, speeds1, label='With Air Resistance')
plt.plot(np.arange(len(speeds2)) * dt, speeds2, label='Ideal Orbit')
plt.xlabel('Time (s)')
plt.ylabel('Speed (m/s)')
plt.title('Speed Over Time')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
