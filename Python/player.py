class Player:
    def __init__(self, id: int, elo: int):
        self.id = id
        self.elo = elo
        
        self.picked = False
        
        self.continent = "EU"
        
        

    def __str__(self):
        return f"{self.id} (Elo: {self.elo})"