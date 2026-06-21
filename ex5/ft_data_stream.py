#!/usr/bin/env python3

import typing
import random

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "jump", "climb", "swim", "grab",
           "release", "move", "eat", "sleep", "use"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (player, action)


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        index = random.randint(0, len(events) - 1)
        event = events[index]
        del events[index]
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    play_act = gen_event()
    for event in range(1000):
        current = next(play_act)
        print(f"Event {event}: Player {current[0]} did action {current[1]}")
    event_list = []
    for i in range(10):
        current = next(play_act)
        event_list += [current]
    print(f"Built list of 10 events: {event_list}")
    for del_event in consume_event(event_list):
        print(f"Got event from list: {del_event}")
        print(f"Remains in list: {event_list}")
