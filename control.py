# Make a PD controller
# Diego, 17/10/2026

class Controller:
    def __init__(self, kp:float = 0.15, kd:float = 0.6):
        self.kp = kp
        self.kd = kd

    def compute_control(self, reference: float, observation:float):
        error = reference - observation

        action = self.kp * error