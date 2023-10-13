field = []
for i in range(3):
    row = input().strip()
    field.append(row)

winner = None

for i in range(3):
    if field[i][0] == field[i][1] == field[i][2] and field[i][0] != "_":
        winner = field[i][0]

for j in range(3):
    if field[0][j] == field[1][j] == field[2][j] and field[0][j] != "_":
        winner = field[0][j]
        
if field[0][0] == field[1][1] == field[2][2] and field[0][0] != "_":
    winner = field[0][0]
if field[0][2] == field[1][1] == field[2][0] and field[0][2] != "_":
    winner = field[0][2]

if winner:
    print(winner)
else:
    print("Ничья")
