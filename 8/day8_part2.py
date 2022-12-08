import numpy as np

with open("8/data.csv") as f:
    map = []
    for line in f:
        map.append(list(line.strip()))

    
map = np.stack(map)


scores = np.zeros((len(map[:,0]),len(map[0])))

for i, row in enumerate(map[0:len(map[:,0])]):
    for j, tree in enumerate(row[0:len(map[0])]):

        #Look left
        left = map[i, :j]
        d_left = 0
        for t in np.flip(left):
            if t < tree:
                d_left += 1
            else:
                d_left += 1
                break

        #Look right
        right = map[i, j+1:]
        d_right = 0
        for t in right:
            if t < tree:
                d_right += 1
            else:
                d_right += 1
                break


        #Look up
        up = map[:i, j]
        d_up = 0
        for t in np.flip(up):
            if t < tree:
                d_up += 1
            else:
                d_up += 1
                break

        #Look down
        down = map[i+1:, j]
        d_down = 0
        for t in down:
            if t < tree:
                d_down += 1
            else:
                d_down += 1
                break

        scenic_score = d_left*d_right*d_up*d_down

        scores[i,j] = scenic_score
        


 
print(scores)
print(np.amax(scores))