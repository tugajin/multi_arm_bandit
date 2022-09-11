from numpy.random import binomial

# 腕クラス
# p: 成功確率
class Arm:
    def __init__(self, p):
        self._p = p
        self.success = 0
        self.fail = 0

    def play(self):
        result = binomial(n=1, p=self._p)
        if result == 1:
            self.success += 1
        else:
            self.fail += 1
        return result

# 腕リストクラス
class Arms:
    def __init__(self):
        self.arms = [Arm(0.3) for i in range(4)]
        self.arms.append(Arm(0.5))