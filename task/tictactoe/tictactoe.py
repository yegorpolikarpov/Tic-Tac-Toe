def print_stage(a):
    print("---------")
    print(f"| {a[0][0]} {a[0][1]} {a[0][2]} |")
    print(f"| {a[1][0]} {a[1][1]} {a[1][2]} |")
    print(f"| {a[2][0]} {a[2][1]} {a[2][2]} |")
    print("---------")
    return None


def prompt():
    coords_str = input("Enter the coordinates: ").split()
    try:
        coords = [int(coords_str[i]) for i in range(2)]
    except:
        print("You should enter numbers!")
        return prompt()
    for i in coords:
        if i > 3 or i < 1:
            print("Coordinates should be from 1 to 3!")
            return prompt()
    if stage_mat[coords[0]-1][coords[1]-1] != ' ':
        print("This cell is occupied! Choose another one!")
        return prompt()
    return coords


def stage_check():
    x_count = sum(row.count("X") for row in stage_mat)
    o_count = sum(row.count("O") for row in stage_mat)
    count_diff = x_count - o_count
    if count_diff > 1 or count_diff < -1:
        print("Impossible")
        exit()

    triplet = []
    Xwin = False
    Owin = False
    for i in range(3):
        triplet.append("".join(stage_mat[i][j] for j in range(3)))
        triplet.append("".join(stage_mat[j][i] for j in range(3)))
    triplet.append(stage_mat[0][0] + stage_mat[1][1] + stage_mat[2][2])
    triplet.append(stage_mat[0][-1] + stage_mat[1][-2] + stage_mat[2][-3])
    for i in triplet:
        if i == "XXX":
            if Owin:
                return "Impossible"
            Xwin = True
        elif i == "OOO":
            if Xwin:
                return "Impossible"
            Owin = True
    if Xwin:
        return "X wins"
    elif Owin:
        return "O wins"
    elif sum(row.count(" ") for row in stage_mat) != 0:
        return "Game not finished"
    else:
        return "Draw"


stage_mat = [[" " for _ in range(3)] for __ in range(3)]
print_stage(stage_mat)
turn = 0
while True:
    turn += 1
    coords = prompt()
    stage_mat[coords[0]-1][coords[1]-1] = 'X' if turn % 2 else 'O'
    print_stage(stage_mat)
    game_state = stage_check()
    if game_state == "X wins" or game_state == "O wins" or game_state == "Draw":
        print(game_state)
        break
