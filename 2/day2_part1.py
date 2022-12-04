with open('2/data.csv') as f:
    games = []
    for line in f:
        games.append(line.strip())


hands = {'A X' : 4, 'A Y' : 8, 'A Z' : 3,
         'B X' : 1, 'B Y' : 5, 'B Z' : 9,
         'C X' : 7, 'C Y' : 2, 'C Z' : 6}

score = 0
for game in games:
    score += hands[game]

print(score)