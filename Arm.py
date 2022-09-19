import numpy as np

# 腕クラス
# p: 成功確率
WIN_VALUE = 1
LOSE_VALUE = -WIN_VALUE

class Arm:
    def __init__(self):
        self.try_num = 1
        self.reward = 0.0
        self.sum_reward = 0.0
        self.find_resolved_flag = False
        self.reward_history = []

    def play(self):
        self.try_num += 1
        reward = self.decide_reward()
        self.reward = reward
        self.sum_reward += reward
        self.update_info(reward)
        return reward

    def update_info(self, reward):
        self.find_resolved_flag = (abs(reward) == WIN_VALUE)
        self.reward_history.append(reward)
        if len(self.reward_history) > 1000:
            self.reward_history.pop()

    def decide_reward(self):
        r = np.random.rand()
        if np.random.binomial(1, 0.5) == 1:
            r *= -1
        return r
    def __str__(self):
        string = 'try:' + str(self.try_num) + ' reward:' + \
            str(self.reward) + ' sum_reward:' + str(self.sum_reward) + " flag:" + str(self.find_resolved_flag) + ' class:' + \
            self.__class__.__name__
        return string

class Arm2(Arm):
    def decide_reward(self):
        r = np.random.rand()
        if np.random.binomial(1, 0.2) == 1:
            r *= -1
        return r

class GoodArm(Arm):
    def __init__(self):
        super().__init__()
    def update_info(self, reward):
        pass
    def decide_reward(self):
        if np.random.binomial(1, 0.2) == 1:
            r = 0.9
        else:
            r = 0
        return r
class OversightGoodArm(Arm):
    def __init__(self):
        super().__init__()
    def update_info(self, reward):
        pass
    def decide_reward(self):
        if self.find_resolved_flag:
            r = 0.999
        elif np.random.binomial(1, 0.001) == 1:
            r = 0.999
            self.find_resolved_flag = True
        else:
            r = -0.999
        return r

class AllGoodArm(Arm):
    def decide_reward(self):
        r = (0.99 + (np.random.rand()/10))
        return r

class OversightBadArm(Arm):
    def update_info(self, reward):
        pass
    def decide_reward(self):
        if self.find_resolved_flag:
            r = -0.999
        elif np.random.binomial(1, 0.0001) == 1:
            r = -0.999
            self.find_resolved_flag = True
        else:
            r = 0.5 + (np.random.rand() / 3)
        return r

class AllBadArm(Arm):
    def decide_reward(self):
        r = -(0.89 + (np.random.rand()/10))
        return r


# 腕リストクラス
class Arms:
    def __init__(self):
        self.arms = [AllBadArm() for i in range(5)]
        #self.arms.append(OversightGoodArm())
        self.arms.append(GoodArm())
        
        #self.arms = [Arm() for i in range(4)]
        #self.arms.append(Arm2())
        #self.arms = [OversightBadArm() for i in range(4)]
        #self.arms.append(OversightGoodArm())
        
        #self.arms = [Arm() for i in range(4)]
        #self.arms.insert(0,OversightBadArm())
        #self.arms.append(OversightGoodArm())
    
    def __str__(self):
        string = ''
        for i, arm in enumerate(self.arms):
            string += str(i) + ":" + arm.__str__() + "\n"
        return string
    def sort(self, f):
        self.arms.sort(key=f, reverse=True)
    
    def diff(self, try_num):
        ans = np.zeros(len(self.arms))
        for i, arm in enumerate(self.arms):
            if type(arm) == type(OversightGoodArm()):
                index = i
                break
        ans[index] = try_num
        #print(ans)
        pred = np.array([arm.try_num for arm in self.arms])
        #print(pred)
        #print((pred-ans)**2)
        return np.sqrt(np.sum((pred - ans)**2))

if __name__ == '__main__':
    f = lambda arm: (arm.sum_reward/(arm.try_num+1))
    arms = Arms()
    arms.sort(f)
    print(arms)

