from numpy.random import binomial, randint
from Arm import Arms, Arm

def __calc_success_ratio(arm):
    if arm.success + arm.fail == 0:
        return 0
    return arm.success / (arm.success + arm.fail)

def epsilon_greedy(arms, T, epsilon):
    reward = 0
    for i in range(1, T+1):
        if binomial(n=1, p=epsilon) == 1:
            # 探索ステップ : アームを一様ランダムに選ぶ
            index = randint(0, len(arms.arms))
        else:
            # 活用ステップ : 今までで一番成功確率の高いアームを選ぶ
            avgs = [ __calc_success_ratio(arm) for arm in arms.arms]
            index = avgs.index(max(avgs))
        reward += arms.arms[index].play()
    return reward

if __name__ == "__main__":
    arms = Arms()
    epsilon_greedy(arms=arms, T=10**3, epsilon=0.3)