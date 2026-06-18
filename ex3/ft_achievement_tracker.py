#!/usr/bin/env python3

import random

ACHIEVEMENTS = [
    "First Steps", "Boss Slayer", "Speed Runner",
    "Master Explorer", "Untouchable", "Collector Supreme",
    "World Savior", "Crafting Genius", "Strategist",
    "Survivor", "Treasure Hunter", "Unstoppable",
    "Sharp Mind", "Hidden Path Finder", "Dragon Slayer",
    "Ghost Hunter", "Legendary", "Iron Will"
]


def gen_player_achievements() -> set[str]:
    ach_count = random.randint(1, len(ACHIEVEMENTS))
    res = set(random.sample(ACHIEVEMENTS, ach_count))
    return res


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    alice_set = gen_player_achievements()
    print(f"Player Alice: {alice_set}")
    bob_set = gen_player_achievements()
    print(f"Player Bob: {bob_set}")
    charlie_set = gen_player_achievements()
    print(f"Player Charlie: {charlie_set}")
    dylan_set = gen_player_achievements()
    print(f"Player Dylan: {dylan_set}")
    ada = alice_set.union(bob_set, charlie_set, dylan_set)
    print(f"All distinct achievements: {ada}")
    common = alice_set.intersection(bob_set, charlie_set, dylan_set)
    print(f"Common achievements: {common}")
    only_alice = alice_set.difference(bob_set, charlie_set, dylan_set)
    print(f"Only Alice has: {only_alice}")
    only_bob = bob_set.difference(alice_set, charlie_set, dylan_set)
    print(f"Only Bob has: {only_bob}")
    only_charlie = charlie_set.difference(bob_set, alice_set, dylan_set)
    print(f"Only Charlie has: {only_charlie}")
    only_dylan = dylan_set.difference(bob_set, charlie_set, alice_set)
    print(f"Only Dylan has: {only_dylan}")
    alice_miss = set(ACHIEVEMENTS).difference(alice_set)
    print(f"Alice is missing: {alice_miss}")
    bob_miss = set(ACHIEVEMENTS).difference(bob_set)
    print(f"Bob is missing: {bob_miss}")
    charlie_miss = set(ACHIEVEMENTS).difference(charlie_set)
    print(f"Charlie is missing: {charlie_miss}")
    dylan_miss = set(ACHIEVEMENTS).difference(dylan_set)
    print(f"Dylan is missing: {dylan_miss}")
