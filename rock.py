import time
import os
import random
os.system ('cls')
print ('')
print ('')
print ('')
print ('')
print ('')
print ("""........##......##.########.##........######...#######..##.....##.########....########..#######.....########.##.....##.########
........##..##..##.##.......##.......##....##.##.....##.###...###.##.............##....##.....##.......##....##.....##.##......
........##..##..##.##.......##.......##.......##.....##.####.####.##.............##....##.....##.......##....##.....##.##......
........##..##..##.######...##.......##.......##.....##.##.###.##.######.........##....##.....##.......##....#########.######..
........##..##..##.##.......##.......##.......##.....##.##.....##.##.............##....##.....##.......##....##.....##.##......
........##..##..##.##.......##.......##....##.##.....##.##.....##.##.............##....##.....##.......##....##.....##.##......
.........###..###..########.########..######...#######..##.....##.########.......##.....#######........##....##.....##.########
........########.##.....##.##.....##.##....##.########..########.########..########...#######..##.....##.########
...........##....##.....##.##.....##.###...##.##.....##.##.......##.....##.##.....##.##.....##.###...###.##......
...........##....##.....##.##.....##.####..##.##.....##.##.......##.....##.##.....##.##.....##.####.####.##......
...........##....#########.##.....##.##.##.##.##.....##.######...########..##.....##.##.....##.##.###.##.######..
...........##....##.....##.##.....##.##..####.##.....##.##.......##...##...##.....##.##.....##.##.....##.##......
...........##....##.....##.##.....##.##...###.##.....##.##.......##....##..##.....##.##.....##.##.....##.##......
...........##....##.....##..#######..##....##.########..########.##.....##.########...#######..##.....##.########""")
print ('')
print ('')
print ('')
print ('')
print ('')
print ('')
print ('')
name1=input('        Name of Player one    :  ')
last=input('        Last Name    :  ')
def name(name1,last):
    p1 = name1 + " " + last
    print('        Master ',p1)
    return
print ('')
print ('')
print ('')
print ('')
name2=input('        Name of Player two    :  ')
last2=input('        Last Name    :  ')
def player2(name2,last2):
    d1 = name2 + " "  +last2
    print('        Master ',d1)
    return
print('')
print('')
print('')
print('')
print('')
name(name1,last)    
player2(name2,last2)
print('')
print('')
print('')
print('')
time.sleep(4)
os.system ('cls')
print ('')
print ('')
print ('')
print ('')
print ('')
print ('')
print ('')
print ('')
print ('             WELCOME TO THE THUNDERDOME')
time.sleep(2)
print('')
print('')
print('')
print('')
print ('          You are entering in a very dangerous game')
time.sleep(2)
print ('          here we have very simple rules in this place')
time.sleep(2)
print ('          we will playing with two dices,the player will guess a numbe ')
time.sleep(2)
print ('          the only objective in this game its to get close to 28')
time.sleep(2)
print ('          Good Luck Players     ')
print('')
time.sleep(3)
os.system ('cls')
print ('')
print ('')
print ('')
print ('')
print ('')
list1 = [1, 2, 3, 4, 5, 6];
list2 = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
r = input('        How Many Rounds Would You Like To Play:    ')
r = int(r)
playerscore1 = 0
playerscore2 = 0
def game(list1,list2,playerscore1,playerscore2):
    rn = random.choice(list1)
    rn2 = random.choice(list2)
    print ('')
    print ('')
    print ('    The first dice is:  ', rn)
    print('')
    name(name1,last)
    ch = input('    Choose a Number:  ')
    ch = int(ch)
    print ('')
    print ('')
    
    player2(name2,last2)
    ch1 = input('   Choose a Number:  ')
    ch1 = int(ch1)
    time.sleep(2)
    
    print ('    Second Dice for players :  ', rn2)
    
    total1 = rn + rn2 + ch
    total2 = rn + rn2 + ch1
    print ('')
    time.sleep(2)
    print ('        Your total  :  ', total1)
    print('')
    time.sleep(2)
    print ('        Your total :  ', total2)
    print ('')
    
    if total1 == 31:
        print ('    you are the winner')
        name(name1,last)
        print ('')
        playerscore1 = playerscore1 + 1
    if total2 == 31:
        print ('        you are the winner')
        player2(name2,last2)
        print ('')
        playerscore2 = playerscore2 + 1
    if total1 > 31:
        print ('        its over 31... you loose')
        name(name1,last)
        print ('')
    if total2 > 31:
        print ('        its over 31... you loose')
        player2(name2,last2)
        print ('')
    if total2 > total1 < 31:
        print ('        You win this round')
        player2(name2,last2)
        print('')
        playerscore2 = playerscore2 + 1
    if  total1 > total2 < 31:
        print ('        you win this round')
        name(name1,last)  
        playerscore1 = playerscore1 + 1        
    print('')
    print('')
    time.sleep(1)
    print ('      your score is:',playerscore1) 
    name(name1,last)
    print ('      your score is:', playerscore2)
    player2(name2,last2)
    return
def repeat(game):
    n = 0
    while  n < r:
        n = n + 1    
        game(list1,list2,playerscore1,playerscore2)
repeat(game)        

while True:
    x = input ("       ARE YOU DONE?:")
    if x.strip() == 'done':
        break
    else:
        repeat(game)    
   
print ('           Thanks for Playing')
print('')
print('                GAME OVER')