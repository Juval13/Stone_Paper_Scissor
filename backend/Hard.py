from collections import Counter
import random
player_history = []  # keep track of player moves

def frequency_ai():
    if not player_history:
        return random.choice(["Rock", "Paper", "Scissors"])

    # Count most common move
    counts = Counter(player_history)
    most_common = counts.most_common(1)[0][0]

    # Play counter to that move
    counter = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
    return counter[most_common]
