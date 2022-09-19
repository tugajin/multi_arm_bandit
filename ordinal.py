from numpy.random import binomial, randint
from Arm import Arms, Arm

def ordinal(arms, T, p=0.6):
    reward = 0
    for i in range(1, T+1):
        arms.sort(lambda arm: (arm.reward))
        length = len(arms.arms)
        for i in range(len(arms.arms)):
            prob = ((p * (length - i - 1)+1) / (length-i))
            if binomial(n=1, p=prob) == 1:
                index = i
                reward += arms.arms[index].play()
                break
    return reward

if __name__ == "__main__":
    arms = Arms()
    print(ordinal(arms=arms, T=10**4))
    print(arms)
