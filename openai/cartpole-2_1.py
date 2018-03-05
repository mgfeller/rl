import gym

def run_episode(env):  
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

env = gym.make('CartPole-v0')

for episode in range(10):
    run_episode(env)
