# 多自由度(MDOF)转换为单自由度(SDOF)程序 (Program to convert MDOF to SDOF)

## 1 等效条件
(1) SDOD位移与MDOF顶层位移、速度、加速度相等  
(2) SDOF与MDOF的底部剪力相等  
(3) SDOF与MDOF的底部弯矩相等  
(4) SDOF与MDOF的周期相等

## 2 参数定义
## 2.1 MODF参数
| 参数 | 含义 |
| ---- | --- |
| $T$ | 周期 |
| $\Delta_i$ | 第$i$层位移 |
| $m_i$ | 第$i$层质量 |
| $h_i$ | 第$i$层标高(楼层至地面距离) |
| $w_i$ | 第$i$层竖向重力荷载 |
| $V_{base}$ | 底部剪力 |
| $M_{base}$ | 底部弯矩 |
## 2.2 SODF参数
| 参数 | 含义 |
| ---- | --- |
| $T$ | 周期 |
| $\Delta$ | 位移 |
| $m$ | 质量 |
| $h$ | 标高 |
| $w$ | 竖向重力荷载 |
| $V_{base}$ | 底部剪力 |
| $M_{base}$ | 底部弯矩 |
| $k$ | 初始刚度 |

注：SDOF中，$T$、$V_{base}$、$M_{base}$的含义与数值均与MDOF相同
## 3 转换公式
(1) SDOF位移：
$$
\Delta = \frac{\sum_{i=1}^n m_i \Delta_i^2}{\sum_{i=1}^n m_i \Delta_i}
$$
(2) SDOF质量：
$$
m = \sum_{i=1}^n \frac{m_i\Delta_i}{\Delta}
$$
(3) SDOF高度：
$$
h = \frac{\sum_{i=1}^n m_i \Delta_i h_i}{\sum_{i=1}^n m_i \Delta_i}
$$
(4) SDOF初始刚度：
$$
k = \frac{4\pi^2m}{T^2}
$$
(5) SDOF竖向重力荷载：
$$
w = \frac{\sum_{i=1}^n w_i \Delta_i \times \sum_{i=1}^n m_i \Delta_i}{\sum_{i=1}^n m_i \Delta_i^2}
$$
