class Controller():
    def __init__(self):
        self.rpmCurve = [
        (50, 20),
        (60, 40),
        (70, 60),
        (80, 80),
        (120, 100)]
        
        self.tempLimit = 3
        self.alpha_up = 0.7
        self.alpha_down = 0.2
        self.lastRPM = None
        

    def setRPM(self, cpuTemperature):
        for temp, rpm in self.rpmCurve:
            if cpuTemperature <= temp:
                return rpm
        return 100

    def smoothRPM(self, targetRPM):
        if self.lastRPM is None:
            self.lastRPM = float(targetRPM)
            return targetRPM

        if abs(targetRPM - self.lastRPM) < 2:
            return int(self.lastRPM)

        if targetRPM > self.lastRPM:
            alpha = self.alpha_up
        else:
            alpha = self.alpha_down

        smoothed = (
            alpha * targetRPM + (1 - alpha) * self.lastRPM
        )

        self.lastRPM = smoothed
        return int(smoothed)