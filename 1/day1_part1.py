
data = []
elf = []
with open('1/test_data.csv') as f:
    for line in f:
        if line.strip() != '':
            elf.append(int(line.strip()))
        else:
            data.append(elf)
            elf = []
    data.append(elf)

print(data)

top_1 = 0
index_1 = 0

for current_index, elf in enumerate(data):

    current_sum = 0
    for item in elf:
        current_sum += item
    
    if current_sum > top_1:
        top_1 = current_sum
        index_1 = current_index
   

print(f"""\n 
          Elf number: {index_1+1}, with calories: {top_1} """)
    


        