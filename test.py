import random
from main import generate_upgrades

number_list = [1, 2, 3]
number_of_upgrades_shown = random.choice(number_list)
print(f"number of upgrades rolled: {number_of_upgrades_shown}")

chosen_rewards = generate_upgrades(number_of_upgrades_shown)

rewards_descriptions = []

for i, reward_description in enumerate(range(number_of_upgrades_shown)):
    reward_choice_number = (i + 1) - 1
    the_reward = chosen_rewards[reward_choice_number]
    reward_description = the_reward['description']
    rewards_descriptions.append(reward_description)

print(rewards_descriptions)

reward1_text, reward2_text, reward3_text = (rewards_descriptions + [None, None])[:3]

print(reward1_text)
print(reward2_text)
print(reward3_text)


