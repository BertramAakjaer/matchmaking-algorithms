import matchmaker as mm
import time

def main():
    # Initialize the Matchmaker
    matchmaker = mm.MatchMaker()

    matchmaker.populate_players(100000)
    print("Players populated successfully.")
    print("\n")

    start_time = time.time()
    matchmaker.find_matches()
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"The 'find_matches' function took {execution_time:.4f} seconds to execute.")
    
    print("\n")
    #matchmaker.show_matches()
    

if __name__ == "__main__":
    main()