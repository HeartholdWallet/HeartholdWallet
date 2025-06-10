

class SequenceForecaster:
    def __init__(self, data):
        self.data = data

    def linear_projection(self, steps=5):
        if len(self.data) < 2:
            return []
        delta = self.data[-1] - self.data[-2]
        return [self.data[-1] + delta * (i+1) for i in range(steps)]

    def rolling_average(self, window=3):
        if len(self.data) < window:
            return []
        return [sum(self.data[i:i+window])/window for i in range(len(self.data)-window+1)]

    def gradient(self):
        return [self.data[i+1] - self.data[i] for i in range(len(self.data)-1)]

    def classify_trend(self):
        grad = self.gradient()
        if all(g > 0 for g in grad):
            return 'uptrend'
        elif all(g < 0 for g in grad):
            return 'downtrend'
        else:
            return 'mixed'

    def trend_strength(self):
        grad = self.gradient()
        return sum(abs(g) for g in grad) / len(grad) if grad else 0
