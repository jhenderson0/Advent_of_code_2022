with open('6/data.csv') as f:
    signals = []
    for line in f:
        signals.append(line.strip())

score = []
for signal in signals:
    buffer = []
    seen_chars = 0
    for char in signal:
        seen_chars += 1
        buffer.append(char)
        
        if len(buffer) == 4:

            if len(buffer) == len(set(buffer)):
                score.append(seen_chars)
                break
            
            buffer.pop(0)

print(score)