from numpy.random import beta
from Arm import Arms, Arm

def thompson_sampling(arms, T):
    reward = 0
    for i in range(1, T+1):
        rand_gened_params = [beta(a=arm.success+1, b=arm.fail+1) for arm in arms.arms]
        max_index = rand_gened_params.index(max(rand_gened_params))
        reward += arms.arms[max_index].play()
    return reward

if __name__ == "__main__":
    arms = Arms()
    thompson_sampling(arms=arms, T=10**3)
