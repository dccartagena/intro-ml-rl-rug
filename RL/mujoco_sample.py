import gymnasium as gym
import mujoco

env = gym.make('Ant-v2')

action_space = env.action_space
obs_space = env.observation_space

obs = env.reset()

random_action = env.action_space.sample()

new_obs, reward, done, info = env.step(random_action)

# env.render()
# env.close()