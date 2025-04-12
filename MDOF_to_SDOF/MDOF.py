from math import pi
import numpy as np


class MDOF():
    def __init__(self,
            period: float,
            mass: list[float],
            height: list[float],
            mode: list[float],
            gravity: list[float] = None
        ):
        """多自由度体系定义

        Args:
            period (float): MDOF周期
            mass (list[float]): 各层质量(从下往上)
            hi (list[float]): 各层的绝对高度(楼层标高)
            phi (list[float]): 振型位移(可不归一化)
            Gi (list[float], optional): 各层所受重力荷载，可不定义
        """
        self.N = len(mass)  # 楼层数
        self.T = period  # 周期
        self.mi = np.array(mass)  # 楼层质量
        self.hi = np.array(height)  # 楼层标高
        self.phi = np.array(mode)  # 振型
        self.Gi = np.array(gravity) if gravity is not None else np.zeros(self.N)  # 竖向荷载
    
    def _get_story_disp(self, top_disp: float) -> np.ndarray:
        """由顶层位移计算各层位移"""
        factor = top_disp / self.phi[-1]
        story_disp = self.phi * factor
        return story_disp  # 二维数组，行数=楼层数，列数=位移数

    def SDOF_disp(self, MDOF_top_disp: float) -> float:
        """由MDOF的顶层位移计算SDOF位移

        Args:
            MDOF_top_disp (float): MDOF顶层位移

        Returns:
            float: SDOF位移
        """
        MDOF_top_disp = np.array(MDOF_top_disp, ndmin=1)
        story_disp = self._get_story_disp(MDOF_top_disp)  # 各层位移
        disp = np.sum(self.mi * story_disp ** 2) / np.sum(self.mi * story_disp)
        return disp

    def SDOF_shear(self, MDOF_Vbase: float) -> float:
        """由MDOF的底部剪力计算SDOF的底部剪力

        Args:
            MDOF_Vbase (float): MDOF的底部剪力

        Returns:
            float: SDOF底部剪力
        """
        return MDOF_Vbase  # SDOF与MDOF的底部剪力相同
    
    def SDOF_moment(self, MDOF_moment: float) -> float:
        """由MDOF的底部弯矩计算SDOF的底部弯矩

        Args:
            MDOF_Vbase (float): MDOF的底部弯矩

        Returns:
            float: SDOF底部弯矩
        """
        return MDOF_moment  # SDOF与MDOF的底部弯矩相同
    
    @property
    def SDOF_mass(self) -> float:
        """SDOF质量"""
        delta = np.sum(self.mi * self.phi ** 2) / np.sum(self.mi * self.phi)
        M = np.sum(self.mi * self.phi) / delta
        return M
    
    @property
    def SDOF_height(self) -> float:
        """SDOF高度"""
        H = np.sum(self.mi * self.phi * self.hi) / np.sum(self.mi * self.phi)
        return H
    
    @property
    def SDOF_initial_stiffness(self) -> float:
        """SDOF初始刚度"""
        k0 = 4 * pi ** 2 * self.SDOF_mass / self.T ** 2
        return k0
    
    @property
    def SDOF_gravity(self) -> float:
        """SDOF竖向荷载"""
        # 根据两种结构在重力荷载下引起的附加弯矩相等来进行计算
        moment = np.sum(self.Gi * self.phi)  # 底部弯矩
        delta = np.sum(self.mi * self.phi ** 2) / np.sum(self.mi * self.phi)  # 等效位移
        return moment / delta

