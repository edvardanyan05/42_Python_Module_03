#!/usr/bin/env python3

import random


PLAYERS = ["Alice", "bob", "Charlie", "dylan",
           "Emma", "Gregory", "john", "kevin", "Liam"]

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {PLAYERS}")
    MAKE_CAP_PLAYERS = [player.capitalize() for player in PLAYERS]
    print(f"New list with all names capitalized: {MAKE_CAP_PLAYERS}")
    ONLY_CAP_PLAYERS = [player for player in PLAYERS if player[0].isupper()]
    print(f"New list of capitalized names only: {ONLY_CAP_PLAYERS}")
    SCORE_DICT = {player: random.randint(0, 1000)
                  for player in MAKE_CAP_PLAYERS}
    print(f"Score dict: {SCORE_DICT}")
    avg = round(sum(SCORE_DICT.values()) / len(SCORE_DICT), 2)
    print(f"Score average is {avg}")
    HIGH_SCORES = {player: SCORE_DICT[player]
                   for player in SCORE_DICT if SCORE_DICT[player] > avg}
    print(f"High scores: {HIGH_SCORES}")
