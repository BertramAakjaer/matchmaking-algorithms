import random

def get_weighted_random_number():
    min_val = 3000
    max_val = 30000
    
    numbers = list(range(min_val, max_val + 1))
    weights = [1 / num for num in numbers]
    
    return random.choices(numbers, weights=weights, k=1)[0]

class MatchMaker:
    def __init__(self):
        self.players = []
    
    def populate_players(self, num_players: int):
        for i in range(num_players):
            elo = get_weighted_random_number()
            self.players.append({"id": i, "elo": elo})
        
                
    def remove_player(self, player_id: int):
        player_to_remove = next((player for player in self.players if player["id"] == player_id), None)
        
        if player_to_remove:
            self.players.remove(player_to_remove)

    
    def find_matches(self, team_size: int = 5):
        mobile_players = self.players.copy()
        mobile_players = sorted(mobile_players, key=lambda x: x["elo"])
        
        if len(mobile_players) < team_size * 2:
            print("Not enough players to form a match.")
            return
        
        while len(mobile_players) >= team_size * 2:
            team1 = mobile_players[:team_size]
            team2 = mobile_players[team_size:team_size * 2]
            
            print(f"Match found: Team 1: {[player['id'] for player in team1]} vs Team 2: {[player['id'] for player in team2]}")
            
            for player in team1 + team2:
                self.remove_player(player["id"])
        
    