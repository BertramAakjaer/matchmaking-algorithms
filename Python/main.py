import matchmaker as mm

def main():
    # Initialize the Matchmaker
    matchmaker = mm.MatchMaker()

    matchmaker.populate_players(20)
    print("\n")
    matchmaker.find_matches()
    

if __name__ == "__main__":
    main()