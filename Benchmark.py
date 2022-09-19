from thompson_sampling import thompson_sampling
from epsilon_greedy import epsilon_greedy
from upper_confidence_bound import UCB
from softmax import softmax
from ordinal import ordinal
from Arm import Arm, Arms
import numpy as np

TRYNUM = 10**3

def simulate_eg(epsilon):
    arms = Arms()
    return epsilon_greedy(arms=arms, T=TRYNUM, epsilon=epsilon)

def simulate_ucb():
    arms = Arms()
    return UCB(arms=arms, T=TRYNUM)

def simulate_softmax():
    arms = Arms()
    return softmax(arms=arms, T=TRYNUM)

def simulate_ordinal(p):
    arms = Arms()
    return ordinal(arms=arms, T=TRYNUM, p=p)

# def simulate_ts():
#     arms = Arms()
#     return thompson_sampling(arms=arms, T=TRYNUM)

def __out_benchmark(array):
    print('\t Avg: {}, Std: {}, Max: {}, Min: {}'.format(np.average(array), np.std(array), np.max(array), np.min(array)))


if __name__ == "__main__":
    loop_cnt = 1000
    eg_01_reward_hist = []
    eg_1_reward_hist = []
    eg_3_reward_hist = []
    eg_5_reward_hist = []
    eg_7_reward_hist = []
    eg_9_reward_hist = []
    ucb_reward_hist = []
    sm_reward_hist = []
    or_1_reward_hist = []
    or_3_reward_hist = []
    or_5_reward_hist = []
    or_7_reward_hist = []
    or_9_reward_hist = []
    #ts_reward_hist = []
    for i in range(loop_cnt):
        eg_01_reward_hist.append(simulate_eg(0.01))
        eg_1_reward_hist.append(simulate_eg(0.1))
        eg_3_reward_hist.append(simulate_eg(0.3))
        eg_5_reward_hist.append(simulate_eg(0.5))
        eg_7_reward_hist.append(simulate_eg(0.7))
        eg_9_reward_hist.append(simulate_eg(0.9))
        ucb_reward_hist.append(simulate_ucb())
        sm_reward_hist.append(simulate_softmax())
        or_1_reward_hist.append(simulate_ordinal(0.1))
        or_3_reward_hist.append(simulate_ordinal(0.3))
        or_5_reward_hist.append(simulate_ordinal(0.5))
        or_7_reward_hist.append(simulate_ordinal(0.7))
        or_9_reward_hist.append(simulate_ordinal(0.9))
        #ts_reward_hist.append(simulate_ts())

    print('Epsilon-greedy_0.01')
    __out_benchmark(eg_01_reward_hist)
    print('Epsilon-greedy_0.1')
    __out_benchmark(eg_1_reward_hist)
    print('Epsilon-greedy_0.3')
    __out_benchmark(eg_3_reward_hist)
    print('Epsilon-greedy_0.5')
    __out_benchmark(eg_5_reward_hist)
    print('Epsilon-greedy_0.7')
    __out_benchmark(eg_7_reward_hist)
    print('Epsilon-greedy_0.9')
    __out_benchmark(eg_9_reward_hist)
    print('UCB')
    __out_benchmark(ucb_reward_hist)
    print('SoftMax')
    __out_benchmark(sm_reward_hist)
    print('ordinal_0.1')
    __out_benchmark(or_1_reward_hist)
    print('ordinal_0.3')
    __out_benchmark(or_3_reward_hist)
    print('ordinal_0.5')
    __out_benchmark(or_5_reward_hist)
    print('ordinal_0.7')
    __out_benchmark(or_7_reward_hist)
    print('ordinal_0.9')
    __out_benchmark(or_9_reward_hist)

    #print('Thompson sampling')
    #__out_benchmark(ts_reward_hist)