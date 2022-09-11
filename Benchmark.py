from thompson_sampling import thompson_sampling
from epsilon_greedy import epsilon_greedy
from upper_confidence_bound import UCB
from Arm import Arm, Arms
import numpy as np

def simulate_eg(epsilon):
    arms = Arms()
    return epsilon_greedy(arms=arms, T=10**3, epsilon=epsilon)

def simulate_ucb():
    arms = Arms()
    return UCB(arms=arms, T=10**3)

def simulate_ts():
    arms = Arms()
    return thompson_sampling(arms=arms, T=10**3)

def __out_benchmark(array):
    print('\t Avg: {}, Std: {}, Max: {}, Min: {}'.format(np.average(array), np.std(array), np.max(array), np.min(array)))


if __name__ == "__main__":
    loop_cnt = 1000
    eg_3_reward_hist = []
    eg_5_reward_hist = []
    eg_7_reward_hist = []
    ucb_reward_hist = []
    ts_reward_hist = []
    for i in range(loop_cnt):
        eg_3_reward_hist.append(simulate_eg(0.3))
        eg_5_reward_hist.append(simulate_eg(0.5))
        eg_7_reward_hist.append(simulate_eg(0.7))
        ucb_reward_hist.append(simulate_ucb())
        ts_reward_hist.append(simulate_ts())

    print('Epsilon-greedy_0.3')
    __out_benchmark(eg_3_reward_hist)
    print('Epsilon-greedy_0.5')
    __out_benchmark(eg_5_reward_hist)
    print('Epsilon-greedy_0.7')
    __out_benchmark(eg_7_reward_hist)
    print('UCB')
    __out_benchmark(ucb_reward_hist)
    print('Thompson sampling')
    __out_benchmark(ts_reward_hist)