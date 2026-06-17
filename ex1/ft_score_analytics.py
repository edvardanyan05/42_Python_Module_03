#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) != 1:
        scores = []
        for arg in sys.argv[1:]:
            try:
                val = int(arg)
                scores += [val]
            except ValueError:
                print(f"Invalid parameter: '{arg}'")
        if len(scores) != 0:
            print(f"Scores processed: [{scores[0]}", end="")
            for val in scores[1:]:
                print(f", {val}", end="")
            print("]")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        else:
            print(f"No scores provided. Usage: "
                  f"python3 {sys.argv[0]} <score1> <score2> ...")
    else:
        print(f"No scores provided. Usage: "
              f"python3 {sys.argv[0]} <score1> <score2> ...")
