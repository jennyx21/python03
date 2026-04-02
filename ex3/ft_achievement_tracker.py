import random


def gen_player_achievements(num: int) -> set:
    achievement = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
        "Hidden Path Finder",
        "Unstoppable"
                ]
    achiv_set = set()
    for i in range(num):
        achiv_set.add(random.choice(achievement))
    achiv_set.add("Untouchable")
    return achiv_set


def ft_achievement_tracker():
    print("=== Achievement Tracker System ===\n")
    alice = gen_player_achievements(random.randint(4, 9))
    bob = gen_player_achievements(random.randint(4, 9))
    charlie = gen_player_achievements(random.randint(4, 9))
    dylan = gen_player_achievements(random.randint(4, 9))
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    all_achiv = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_achiv}")
    print()

    common = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common}")
    print()
    print(f"Only alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only charlie has: {charlie.difference(bob, alice, dylan)}")
    print(f"Only dylan has: {dylan.difference(bob, charlie, alice)}")

    print()
    print(f"Alice is missing: {all_achiv.difference(alice)}")
    print(f"Bob is missing: {all_achiv.difference(bob)}")
    print(f"Charlie is missing: {all_achiv.difference(charlie)}")
    print(f"Dylan is missing: {all_achiv.difference(dylan)}")


if __name__ == "__main__":
    ft_achievement_tracker()
