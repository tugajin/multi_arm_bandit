from Arm import Arm, Arms
import math

def __get_score(arm, t, c):
    ucb = math.sqrt(2*math.log(t) / (arm.try_num))
    return (arm.sum_reward / arm.try_num) + c * ucb

def UCB(arms, T, c=1):
    reward = 0

    for i in range(1, T+1):
        scores = [__get_score(arm, i, c) for arm in arms.arms]
        max_score_index = scores.index(max(scores))
        reward += arms.arms[max_score_index].play()
    return reward

def UCB2(arms, n, c=1):
    reward = 0
    scores = [__get_score(arm, n, c) for arm in arms.arms]
    max_score_index = scores.index(max(scores))
    reward += arms.arms[max_score_index].play()
    return reward
if __name__=="__main__":
    arms = Arms()
    print(UCB(arms=arms, T=10,c=25))
    print(arms)