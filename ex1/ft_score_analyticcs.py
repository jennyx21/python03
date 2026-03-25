import sys

def ft_score_analytics():
    print("=== Player Score Analytics ===")
    arglist = []
    if len(sys.argv) > 1:
        try: 
            for i  in range (1,len(sys.argv)):
                args = int(sys.argv[i])
                arglist.append(args)
            print(f"Scores Processed: {arglist}")
            print (f"Total Player: {len(arglist)}")
            print(f"Total Score: {sum(arglist)}")
            print(f"Average score: {sum(arglist) / len(arglist)}")
            print(f"High Score: {max(arglist)}")
            print(f"Low Score: {min(arglist)}")
            print(f"Score rannge: {max(arglist) - min(arglist)}")
        except ValueError:
            print(f"bad input '{sys.argv[i]}' is not a Number")
    else:
        print("No scores provided. Usage: python3 ft_score_analythics.py <score1> <score2> ...")
  
    


if __name__ == "__main__":
    ft_score_analytics()