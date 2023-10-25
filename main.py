class Question:
    def __init__ (self, name ):
        self.name = name
        self.score = 0


player_one = Question('peter')

if player_one.name == 'Peter':
    player_one.score += 10
else:
    player_one.score -= 10

print(player_one.name, player_one.score)