import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    arglist = []
    if len(sys.argv) > 1:
        i = 1
        try:
            for arg in sys.argv[1:]:
                arglist.append(int(arg))
                i += 1
            print(f"Scores Processed: {arglist}")
            print(f"Total Player: {len(arglist)}")
            print(f"Total Score: {sum(arglist)}")
            print(f"Average score: {sum(arglist) / len(arglist)}")
            print(f"High Score: {max(arglist)}")
            print(f"Low Score: {min(arglist)}")
            print(f"Score rannge: {max(arglist) - min(arglist)}")
        except ValueError:
            print(f"Invalid Parameter: '{sys.argv[i]}'")
            print("No scores provided. Usage: python3 ft_score_analytics.py "
                  "<score1 : int> <score2 :int> ...")
    else:
        print("No scores provided. Usage: python3 "
              "ft_score_analythics.py <score1> <score2> ...")


if __name__ == "__main__":
    ft_score_analytics()
