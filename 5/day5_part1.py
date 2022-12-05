
#test_stacks =     [['Z','N'],['M','C','D'],['P']]

stacks = [['N','D','M','Q','B','P','Z'],
          ['C','L','Z','Q','M','D','H','V'],
          ['Q','H','R','D','V','F','Z','G'],
          ['H','G','D','F','N'],
          ['N','F','Q'],
          ['D','Q','V','Z','F','B','T'],
          ['Q','M','T','Z','D','V','S','H'],
          ['M','G','F','P','N','Q'],
          ['B','W','R','M']
        ]

with open('5/data.csv') as f:
    instructions = []
    for line in f:
        txt = line.strip()
        instruction = [int(s) for s in txt.split() if s.isdigit()]
        instructions.append(instruction)

for instruction in instructions:
    for i in range(instruction[0]):
        stacks[instruction[2]-1].append(stacks[instruction[1]-1].pop())

final_letters = ""
for stack in stacks:
    final_letters += stack[-1]

print(final_letters)