import os
row1 = ['-','-','-']
row2 = ['-','-','-']
row3 = ['-','-','-']
turnTrack = ['x','o']
topMessage = ['Enter a coordinate: ex: [1,2]',
    'Please Enter a vaild location on the board ex: [1,2]',
    'Please make sure all values are 3 or less'
    ]
msg = 0
def main():
    global msg
    os.system('cls' if os.name == 'nt' else 'clear')
    turnNum = 0
    
    while True:
        print(topMessage[msg])
        
        drawBoard()
      
        print("enter an: " + turnTrack[turnNum] + " or 'reset' to reset")
        ans = input()
        if ans == 'reset':
            reset()
        else:
            try:
                strList = ans.split(',')
                coordList = list(map(int, strList))
            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                msg = 1
                continue
    
        try:
            if coordList[0] == 1:
                row1[coordList[1] -1 ] = turnTrack[turnNum]
            elif coordList[0] == 2:
                row2[coordList[1] -1 ] = turnTrack[turnNum]
            elif coordList[0] == 3:
                row3[coordList[1] -1 ] = turnTrack[turnNum]
        except:
            pass
        if turnNum == 0:
            turnNum+=1
        else:
            turnNum-=1
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

def reset():
    print('reset called')
    global row1
    global row2
    global row3
    row1 = ['-','-','-']
    row2 = ['-','-','-']
    row3 = ['-','-','-']
    main()

main()