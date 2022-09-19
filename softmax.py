from numpy.random import binomial, randint
from Arm import Arms, Arm
import numpy as np

def softmax(arms, T):
    reward = 0
    for i in range(1, T+1):
        softmax_list = [ np.exp((arm.sum_reward/(arm.try_num+1))) for arm in arms.arms]
        sumv = sum(softmax_list)
        softmax_list /= sumv
        index = np.random.choice(len(softmax_list),p=softmax_list)
        reward += arms.arms[index].play()
    return reward

if __name__ == "__main__":
    arms = Arms()
    print(softmax(arms=arms, T=10**4))
    print(arms)
