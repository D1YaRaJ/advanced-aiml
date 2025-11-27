sample_space_die = [1, 2, 3, 4, 5, 6]
event_even = [2, 4, 6]

def calculate_probability(event, sample_space):
    return len(event) / len(sample_space)

prob_even = calculate_probability(event_even, sample_space_die)
print(f"Probability of rolling an even number: {prob_even:.2f}")

event_greater_than_4 = [5, 6]
prob_gt_4 = calculate_probability(event_greater_than_4, sample_space_die)
print(f"Probability of rolling a number greater than 4: {prob_gt_4:.2f}")

event_3 = [3]
prob_3 = calculate_probability(event_3, sample_space_die)
print(f"Probability of rolling a '3': {prob_3:.2f}")
