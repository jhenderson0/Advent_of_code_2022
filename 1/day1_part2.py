
data = []
elf = []
with open('1/data.csv') as f:
    for line in f:
        if line.strip() != '':
            elf.append(int(line.strip()))
        else:
            data.append(elf)
            elf = []
    data.append(elf)

print(data)

top_1 = 0
top_2 = 0
top_3 = 0 

index_1 = 0
index_2 = 0
index_3 = 0
for current_index, elf in enumerate(data):

    current_sum = 0
    for item in elf:
        current_sum += item
    
    if current_sum > top_1:
        top_3 = top_2
        index_3 = index_2
        top_2 = top_1
        index_2 = index_1
        top_1 = current_sum
        index_1 = current_index
    
    elif current_sum > top_2:
        top_3 = top_2
        index_3 = index_2
        top_2 = current_sum
        index_2 = current_index


    elif current_sum > top_3:
        top_3 = current_sum 
        index_3 = current_index    

print(f"""\n 
          Elf number: {index_1+1}, with calories: {top_1} \n 
          Elf number: {index_2+1}, with calories: {top_2} \n   
          Elf number: {index_3+1}, with calories: {top_3} \n 
          Total calories: {top_1 + top_2 + top_3}""")
    
