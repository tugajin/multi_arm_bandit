from epsilon_greedy import epsilon_greedy
from upper_confidence_bound import UCB
from softmax import softmax
from ordinal import ordinal
from Arm import Arm, Arms
import numpy as np

TRYNUM = 10**6

if __name__ == "__main__":
    print("epsilon_greedy 0.1")
    arms = Arms()
    print(epsilon_greedy(arms=arms, T=TRYNUM, epsilon=0.1))
    print("diff:",arms.diff(TRYNUM))
    arms.sort(lambda arm: (arm.try_num))
    print(arms)

    print("epsilon_greedy 0.2")
    arms = Arms()
    print(epsilon_greedy(arms=arms, T=TRYNUM, epsilon=0.2))
    print("diff:",arms.diff(TRYNUM))
    arms.sort(lambda arm: (arm.try_num))
    print(arms)

    print("epsilon_greedy 0.3")
    arms = Arms()
    print(epsilon_greedy(arms=arms, T=TRYNUM, epsilon=0.3))
    print("diff:",arms.diff(TRYNUM))
    arms.sort(lambda arm: (arm.try_num))
    print(arms)

    print("ordinal 0.6")
    arms = Arms()
    print(ordinal(arms=arms, T=TRYNUM, p=0.6))
    print("diff:",arms.diff(TRYNUM))
    arms.sort(lambda arm: (arm.try_num))
    print(arms)

    print("ordinal 0.7")
    arms = Arms()
    print(ordinal(arms=arms, T=TRYNUM, p=0.7))
    print("diff:",arms.diff(TRYNUM))
    arms.sort(lambda arm: (arm.try_num))
    print(arms)

    print("ordinal 0.8")
    arms = Arms()
    print(ordinal(arms=arms, T=TRYNUM, p=0.8))
    print("diff:",arms.diff(TRYNUM))
    arms.sort(lambda arm: (arm.try_num))
    print(arms)

    print("softmax")
    arms = Arms()
    print(softmax(arms=arms, T=TRYNUM))
    print("diff:",arms.diff(TRYNUM))
    arms.sort(lambda arm: (arm.try_num))
    print(arms)

    print("ucb1")
    arms = Arms()
    print(UCB(arms=arms, T=TRYNUM,c=1))
    print("diff:",arms.diff(TRYNUM))
    arms.sort(lambda arm: (arm.try_num))
    print(arms)

    print("ucb10")
    arms = Arms()
    print(UCB(arms=arms, T=TRYNUM,c=10))
    print("diff:",arms.diff(TRYNUM))
    arms.sort(lambda arm: (arm.try_num))
    print(arms)


    print("ucb12")
    arms = Arms()
    print(UCB(arms=arms, T=TRYNUM,c=12))
    print("diff:",arms.diff(TRYNUM))
    arms.sort(lambda arm: (arm.try_num))
    print(arms)

    print("ucb25")
    arms = Arms()
    print(UCB(arms=arms, T=TRYNUM,c=25))
    print("diff:",arms.diff(TRYNUM))
    arms.sort(lambda arm: (arm.try_num))
    print(arms)

    print("ucb50")
    arms = Arms()
    print(UCB(arms=arms, T=TRYNUM,c=50))
    print("diff:",arms.diff(TRYNUM))
    arms.sort(lambda arm: (arm.try_num))
    print(arms)

    print("ucb100")
    arms = Arms()
    print(UCB(arms=arms, T=TRYNUM,c=100))
    print("diff:",arms.diff(TRYNUM))
    arms.sort(lambda arm: (arm.try_num))
    print(arms)
