row1 = ['-','-','-']
row2 = ['-','-','-']
row3 = ['-','-','-']
turnTrack = ['x','o']
turn = 0

def ask():
    print("where you do want to place an "+turnTrack[turn]+ "? Row, Column")
    ans = input()
    testa = ans.split(',')
    test = list(map(int, testa))
    print(test[0])
    if test[0] == 1:
        print("here you are")
        row1[test[1]] = turnTrack[turn]
    elif test[0] == 2:
        row2[test[1]] = turnTrack[turn]
    elif test[0] == 3:
        row3[test[1]] = turnTrack[turn]
    drawBoard()

def main():
    drawBoard()
    
def drawBoard():
    print("1: ", end="")
    for i in row1:
        print(i + "", end=" ") 
    print()
    print("2: ",end="")

    for i in row2:
        print(i + "", end=" ")
    print()
    print("3: ",end="")
    for i in row3:
        print(i + "", end=" ")
    print()
    print(" "+" " + " 1 2 3")
    ask()

main()