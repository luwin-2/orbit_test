import matplotlib.pyplot as plt
import numpy as np

# 물리 상수
G = 6.67430e-11     # 만유인력 상수
M = 5.972e24        # 지구 질량
R = 6.371e6         # 지구 반지름
rho0 = 1.225        # 해수면에서의 공기 밀도 (kg/m^3)
H = 8500            # 대기 밀도 감소 scale height (m)
Cd = 0.47           # 구체의 항력 계수
A = 0.01            # 단면적 (m^2)
mass = 10           # 질량 (kg)

# 시간 설정
dt = 1
T = 200000

# 초기 조건: 10km 위, 대각선 발사
x0 = R + 80000      # 80km 고도
y0 = 0
vx0 = 0
vy0 = 10000           # 약간 높은 속도

x, y = x0, y0
vx, vy = vx0, vy0

# 기록 리스트
xs, ys, speeds = [], [], []

for _ in range(T):
    r = np.sqrt(x**2 + y**2)
    if r < R:
        break  # 충돌

    # 중력
    a_grav = -G * M / r**3
    ax_grav = a_grav * x
    ay_grav = a_grav * y

    # 고도에 따른 공기 밀도
    altitude = r - R
    rho = rho0 * np.exp(-altitude / H)

    # 속도 및 단위 벡터
    v = np.sqrt(vx**2 + vy**2)
    if v == 0:
        ax_drag, ay_drag = 0, 0
    else:
        drag_force = 0.5 * rho * v**2 * Cd * A
        ax_drag = -drag_force * vx / v / mass
        ay_drag = -drag_force * vy / v / mass

    # 가속도 총합
    ax = ax_grav + ax_drag
    ay = ay_grav + ay_drag

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

# 시각화
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 궤도 시각화
earth = plt.Circle((0, 0), R, color='blue', alpha=0.5, label='Earth')
ax1.add_patch(earth)
ax1.plot(xs, ys, label='Trajectory with Air Drag', color='red')
ax1.set_title('Trajectory with Air Drag (from 80km)')
ax1.set_xlabel('x (m)')
ax1.set_ylabel('y (m)')
ax1.set_aspect('equal')
ax1.legend()
ax1.grid(True)

# 속도 시각화
time = np.arange(len(speeds)) * dt
ax2.plot(time, speeds, label='Speed with Drag', color='purple')
ax2.set_title('Speed Over Time with Air Drag')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Speed (m/s)')
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()
