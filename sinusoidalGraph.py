import matplotlib.pyplot as plt
import numpy as np

class SinusoidalGraph:

    def __init__(self, _amplitude=1, _frequency=1, _phase=0, _x_range=(0, 2*np.pi), color = 'red'):
        self.amplitude = _amplitude
        self.frequency = _frequency
        self.phase = _phase
        self.x_range = _x_range
        self.color = color

    def plot(self):
        x = np.arange(self.x_range[0], self.x_range[1], 0.1)
        y = np.sin(x*self.frequency -self.phase) * self.amplitude
        plt.plot(x, y, color=self.color)



