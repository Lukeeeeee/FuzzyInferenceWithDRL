import gc

from src import *

gc.enable()

ENV_NAME = 'InvertedPendulum-v1'
EPISODES = 100000
TEST = 10

def main():
    env = Environment(name=ENV_NAME)
    agent = DDPGController(env)

    for episode in range(EPISODES):
        state = env.reset()
        for step in range(env.timestep_limit):
            action = agent.noise_action(state)
            next_state, reward, done = env.step(action)
            agent.perceive(state, action, reward, next_state, done)
            state = next_state
            if done:
                break
        if episode % 100 == 0 and episode > 0:
            total_reward = 0.0
            for i in range(TEST):
                stat = env.reset()
                for j in range(env.timestep_limit):
                    action = agent.action(state)
                    state, reward, done = env.step(action)
                    total_reward += reward
                    if done:
                        break
            ave_reward = total_reward / TEST
            print ('episode: ', episode, 'Evaluation Average Reward:', ave_reward)

if __name__ == '__main__':
    main()
