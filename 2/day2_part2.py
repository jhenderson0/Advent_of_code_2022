with open('data.csv') as f:
    games = []
    for line in f:
        games.append(line.strip())


hands = {'A X' : 3, 'A Y' : 4, 'A Z' : 8,
         'B X' : 1, 'B Y' : 5, 'B Z' : 9,
         'C X' : 2, 'C Y' : 6, 'C Z' : 7}

score = 0
for game in games:
    score += hands[game]

print(score)