import os
row1 = ['-','-','-']
row2 = ['-','-','-']
row3 = ['-','-','-']
turnTrack = ['x','o']


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    foo = 0
    while True:
        drawBoard()
        
        print("enter an: " + turnTrack[foo])
        ans = input()
        testa = ans.split(',')
        test = list(map(int, testa))
        try:
            if test[0] == 1:
                row1[test[1] -1 ] = turnTrack[foo]
            elif test[0] == 2:
                row2[test[1] -1 ] = turnTrack[foo]
            elif test[0] == 3:
                row3[test[1] -1 ] = turnTrack[foo]
        except:
            pass
        if foo == 0:
            foo+=1
        else:
            foo-=1
        os.system('cls' if os.name == 'nt' else 'clear')

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

main()