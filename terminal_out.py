import gym
import numpy as np
import time

env = gym.make('FrozenLake-v0')
env.reset()

for i_episode in range(15):
    env.render()
    env.step(env.action_space.sample())
    time.sleep(0.2)