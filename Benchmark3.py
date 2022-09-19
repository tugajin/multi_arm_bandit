from epsilon_greedy import epsilon_greedy
from upper_confidence_bound import UCB, UCB2
from softmax import softmax
from ordinal import ordinal
from Arm import Arm, Arms, OversightGoodArm, GoodArm
import numpy as np

TRYNUM = 10**6
LIST_SIZE = 1000

def is_end(arms):
    try_num_list = []
    for i, arm in enumerate(arms.arms):
        try_num_list.append(arm.try_num)
        if type(arm) == type(OversightGoodArm()) or type(arm) == type(GoodArm()):
            index = i
            break
    correct_try_num = try_num_list[index]
    try_num_list[index] = 0
    max_try_num = max(try_num_list)
    return (correct_try_num - max_try_num > 1000)

def epsilon_greedy_history(p=0.3):
    return [test_epsilon_greedy(p) for i in range(LIST_SIZE)]

def test_epsilon_greedy(p=0.3):
    arms = Arms()
    for t in range(TRYNUM):
        epsilon_greedy(arms, 1, p)
        if is_end(arms):
            return t
    return TRYNUM

def softmax_history():
    return [test_softmax() for i in range(LIST_SIZE)]

def test_softmax():
    arms = Arms()
    for t in range(TRYNUM):
        softmax(arms=arms, T=1)
        if is_end(arms):
            return t
    return TRYNUM

def ucb_history(c=1):
    return [test_ucb(c) for i in range(LIST_SIZE)]

def test_ucb(c=1):
    arms = Arms()
    for t in range(TRYNUM):
        UCB2(arms=arms, n=t+1, c=c)
        if is_end(arms):
            return t
    return TRYNUM

def ordinal_history(p=0.6):
    return [test_ordinal(p) for i in range(LIST_SIZE)]

def test_ordinal(p=0.6):
    arms = Arms()
    for t in range(TRYNUM):
        ordinal(arms=arms, T=1, p=p)
        if is_end(arms):
            return t
    return TRYNUM

def out_benchmark(array):
    print('\t Avg: {}, Std: {}, Max: {}, Min: {}, Median: {}'.format(np.average(array), np.std(array), np.max(array), np.min(array), np.median(array)))


if __name__ == "__main__":
    print("eplison0.1:",end="")
    out_benchmark(epsilon_greedy_history(0.1))
    print("eplison0.2:",end="")
    out_benchmark(epsilon_greedy_history(0.2))
    print("eplison0.3:",end="")
    out_benchmark(epsilon_greedy_history(0.3))
    print("eplison0.4:",end="")
    out_benchmark(epsilon_greedy_history(0.4))
    print("eplison0.5:",end="")
    out_benchmark(epsilon_greedy_history(0.5))
    print("eplison0.6:",end="")
    out_benchmark(epsilon_greedy_history(0.6))
    print("eplison0.7:",end="")
    out_benchmark(epsilon_greedy_history(0.7))
    print("eplison0.8:",end="")
    out_benchmark(epsilon_greedy_history(0.8))
    print("eplison0.9:",end="")
    out_benchmark(epsilon_greedy_history(0.9))
    print("softmax:",end="")
    out_benchmark(softmax_history())
    print("ucb10  :",end="")
    out_benchmark(ucb_history(10))
    print("ucb20  :",end="")
    out_benchmark(ucb_history(20))
    print("ucb25  :",end="")
    out_benchmark(ucb_history(25))
    print("ucb40  :",end="")
    out_benchmark(ucb_history(40))
    print("ucb60  :",end="")
    out_benchmark(ucb_history(60))
    print("ucb80  :",end="")
    out_benchmark(ucb_history(80))
    print("ordinal06:",end="")
    out_benchmark(ordinal_history(0.6))
    print("ordinal07:",end="")
    out_benchmark(ordinal_history(0.7))
    print("ordinal08:",end="")
    out_benchmark(ordinal_history(0.8))
    print("ordinal09:",end="")
    out_benchmark(ordinal_history(0.9))