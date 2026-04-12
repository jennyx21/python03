from typing import Generator
import random


def consume_event(events: list):
    for event in events:
        x = random.choice(events)
        rest = events.copy()
        rest.remove(x)
        yield x, rest


def gen_event(name: list,
              action: list) -> Generator[tuple[str, str], None, None]:
    for i in range(1000):
        player_event = (random.choice(name), random.choice(action))
        yield player_event


def main():
    print("=== Game Data Stream Processor ===")
    i = 0
    name_list = [
        "Dylan",
        "Alice",
        "Bob",
        "Charlie",
        "James",
        "Tjark",
        "Max",
        "Enrico",
        "Gerald",
        "Helen"
    ]
    action_list = [
        "Jump",
        "Run",
        "Climb",
        "Move",
        "kill",
        "Sleep",
        "Swim",
        "Grab",
        "Eat",
        "hit",
        "Take",
        "Drink",
        "Heal",
        "Hurt",
        "Wake",
        "Stand",
        "Sit"
    ]

    gen = gen_event(name_list, action_list)
    for i in range(1000):
        x = next(gen)
        player, action = x
        print(f"Event {i}: Player {player} did Action {action}")
    gen = gen_event(name_list, action_list)
    events = []
    for i in range(10):
        events.append(next(gen))
    print(f"Build list of 10 Events: {events}")
    x = ()
    for event in events:
        gen = consume_event(events)
        x, events = next(gen)
        print(f"got event from list: {x}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
