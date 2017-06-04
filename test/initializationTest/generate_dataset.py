from __future__ import print_function

import json

from ddpgInitializationTest import *

if __name__ == '__main__':
    env = Environment(name="InitialTest", state_dim=100, action_dim=10)

    testInitializer = DDPGInitializaionTest(state_dim=env.state_dim,
                                            action_dim=env.action_dim)
    fuzzy_controller = testInitializer.generate_fuzzy_logic_controller()
    fuzzy_valuer = testInitializer.generate_fuzzy_logic_valuer()

    ddpgController = DDPGController(env)

    ddpgInitializer = DDPGInitializer(ddpg_controller=ddpgController,
                                      fuzzy_logic_controller=fuzzy_controller,
                                      fuzzy_logic_valuer=fuzzy_valuer,
                                      mini_batch_size=100)

    dataset_log = open("../../log/dataset.json", "w")
    json.dump(ddpgInitializer.generate_training_sample_mini_batch(10), dataset_log)