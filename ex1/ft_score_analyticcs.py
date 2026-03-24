import sys

def ft_score_analytics():
    print("=== Player Score Analytics ===")
    arglist = []
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
        print("bad input")
  
    


if __name__ == "__main__":
    ft_score_analytics()