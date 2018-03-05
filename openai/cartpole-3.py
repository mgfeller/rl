import gym
import numpy as np

env = gym.make('CartPole-v0')

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

bestparams = None  
bestreward = 0  
for episode in range(100):  
    parameters = np.random.rand(4) * 2 - 1
    reward = run_episode(env,parameters)
    print("episode %2d: reward = %d" % (episode+1, reward))
    if reward > bestreward:
        bestreward = reward
        bestparams = parameters
        # considered solved if the agent lasts 200 timesteps
        if reward == 200:
            break
