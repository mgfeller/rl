import gym
import numpy as np

env = gym.make('CartPole-v0')

# http://kvfrans.com/simple-algoritms-for-solving-cartpole/
# 
# Hill-Climbing 
# Another method of choosing weights is the hill-climbing algorithm. 
# We start with some randomly chosen initial weights. 
# Every episode, add some noise to the weights, 
# and keep the new weights if the agent improves.

def run_episode(env, parameters):  
    observation = env.reset()
    totalreward = 0
    for _ in range(200):
        env.render()
        action = 0 if np.matmul(parameters,observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
    return totalreward

noise_scaling = 0.1  
parameters = np.random.rand(4) * 2 - 1  
bestreward = 0  
for episode in range(100):  
    newparams = parameters + (np.random.rand(4) * 2 - 1)*noise_scaling
    reward = run_episode(env,newparams)
    print("episode %2d: reward = %d" % (episode+1, reward))
    if reward > bestreward:
        bestreward = reward
        parameters = newparams
        if reward == 200:
            break
