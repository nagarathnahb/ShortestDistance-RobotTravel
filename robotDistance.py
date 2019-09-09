import math
dest = [0,0]

def keepGivingDist():
    print('Do you want to keep the robot moving? (yes or no)')
    if input().startswith('y'):
        print('Enter the direction you want the robot to travel in from current position ({},{}): '
              '(UP/DOWN/LEFT/RIGHT)'.format(dest[0],dest[1]))
        return True
    return False

def getData():
    while True:
        dir = input()
        if dir.upper() in 'UP,DOWN,LEFT,RIGHT'.split(','):
            break
        else:
            print('The given direction is invalid, choose UP/DOWN/LEFT/RIGHT!')

    print('Enter the distance you want the robot to travel in the given direction:')
    while True:
        d = input()
        if d.isdigit() and d[0]!='-':
            break
        else:
            print('Invalid distance, give a valid positive integer')
    dis = int(d)
    print(dis)
    print(dir)
    updatePosition(dir, dis)
    return dir, dis

def updatePosition(dir, dis):
    print('direction = ' + dir.lower())
    if dir.lower() == 'up':
        dest[1] += dis
    elif dir.lower() =='down':
        dest[1] -= dis
    elif dir.lower()=='left':
        dest[0] -= dis
    else:
        dest[0] += dis
    print('destination = ' + str(dest))

def calculateDistance():
    finalD = math.sqrt(dest[0] ** 2 + dest[1] ** 2)
    print('The shortest distance of the robot from (0,0) to ({},{}) is {}'.format(dest[0],dest[1], finalD))


print('Enter the direction you want the robot to travel in: (UP/DOWN/LEFT/RIGHT)')
while True:
    dir, dis = getData()
    if not keepGivingDist():
        break

calculateDistance()