import player as p
import random

def get_team_average(team):
    if not team:
        return 0
    return sum(player.elo for player in team) / len(team)

def find_closest_player(players, target_elo):
    left, right = 0, len(players) - 1
    closest_index = 0
    min_diff = float('inf')

    while left <= right:
        mid = (left + right) // 2
        
        diff = abs(players[mid].elo - target_elo)
        
        if diff < min_diff:
            min_diff = diff
            closest_index = mid

        if players[mid].elo < target_elo:
            left = mid + 1
        elif players[mid].elo > target_elo:
            right = mid - 1
        else:
            return mid

    return closest_index

class MatchMaker:
    def __init__(self):
        self.players = []
        self.matches = []
    
    def populate_players(self, num_players: int):

        for i in range(num_players):
            max_elo = 30000
            min_elo = 3000
            elo = int(max_elo - ((max_elo - min_elo) * random.random()**2))
            
            self.players.append(p.Player(i, elo))
        
        self.players = sorted(self.players, key=lambda x: x.id)
    
    def remove_player(self, player_id: int):
        left, right = 0, len(self.players) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.players[mid].id == player_id:
                self.players.pop(mid)
                return
            elif self.players[mid].id < player_id:
                left = mid + 1
            else:
                right = mid - 1
    
    def show_matches(self):
        if not self.matches:
            print("No matches found.")
            return
        
        for i, (team1, team2) in enumerate(self.matches):
            team1_str = ', '.join(str(player) for player in team1)
            team2_str = ', '.join(str(player) for player in team2)
            team1_avg_elo = get_team_average(team1)
            team2_avg_elo = get_team_average(team2)
            print(f"Match {i + 1}:")
            print(f"Team 1: {team1_str} (Avg Elo: {team1_avg_elo:.2f})")
            print(f"Team 2: {team2_str} (Avg Elo: {team2_avg_elo:.2f})")
            print("\n")
    
    def find_matches(self, team_size: int = 5):
        mobile_players = self.players.copy()
        mobile_players = sorted(mobile_players, key=lambda x: x.elo)
        
        if len(mobile_players) < team_size * 2:
            print("Not enough players to form a match.")
            return
        
        while len(mobile_players) >= team_size * 2:
            team1 = []
            team2 = []

            while len(team1) + len(team2) < team_size * 2:
                team1_elo = get_team_average(team1)
                team2_elo = get_team_average(team2)

                if len(team1) == 0:
                    player = random.choice(mobile_players)
                    team1.append(player)
                    mobile_players.remove(player)

                elif len(team1) == len(team2):
                    elo_goal = team2_elo * (len(team1) + 1) - sum(player.elo for player in team1)
                    index = find_closest_player(mobile_players, elo_goal)
                    player = mobile_players[index]
                    team1.append(player)
                    mobile_players.remove(player)

                else:
                    elo_goal = team1_elo * (len(team2) + 1) - sum(player.elo for player in team2)
                    index = find_closest_player(mobile_players, elo_goal)
                    player = mobile_players[index]
                    team2.append(player)
                    mobile_players.remove(player)
                

                if len(team1) + len(team2) == team_size * 2:
                    self.matches.append((team1, team2))

        print(f"Matches found: {len(self.matches)}")

