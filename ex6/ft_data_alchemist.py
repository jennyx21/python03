import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    name_list = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam"
    ]
    print(f"Initial list of players {name_list}")
    new_name_list = [name.capitalize() for name in name_list]
    print(f"New list with all names capitalized: {new_name_list}")
    name_capitalized = [name
                        for name in name_list if name == name.capitalize()]
    print(f"New list of capitalized names only: {name_capitalized}")
    scores = {name: random.randint(50, 10000) for name in new_name_list}
    print(f"score dict: {scores}")
    average = sum(value for value in scores.values()) / len(scores)
    print(f"Score average is {round(average, 2)}")
    high = {value for value in scores.values() if value >= average}
    print(f"High scores: {high}")


if __name__ == "__main__":
    main()
