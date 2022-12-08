import numpy as np

with open("8/data.csv") as f:
    map = []
    for line in f:
        map.append(list(line.strip()))

    
map = np.stack(map)

#Perimeter - 4 corners
perimeter = 2*len(map[:,0])+2*len(map[0]) - 4
score = perimeter
visible = np.zeros((len(map[:,0])-2,len(map[0])-2), dtype =str)
for i, row in enumerate(map[1:len(map[:,0])-1]):
    for j, tree in enumerate(row[1:len(map[0])-1]):

        #print(map[i+1, :j+1])
        #print(map[i+1, j+2:])
        #print(map[:i+1, j+1])
        #print(map[i+2:, j+1])

        #Visible from the left
        if np.all(tree > map[i+1, :j+1]):
            score += 1
            visible[i,j] = 'l'

        #Visible from the right
        elif np.all(tree > map[i+1, j+2:]):
            score += 1
            visible[i,j] = 'r'
            
        #Visible from the top
        elif np.all(tree > map[:i+1, j+1]):
            score += 1
            visible[i,j] = 't'

        #Visible from the bottom
        elif np.all(tree > map[i+2:, j+1]):
            score += 1
            visible[i,j] = 'b'


print(visible)         
print(score)
