#1
import time

def triangle_number(num):
    if num <= 0: return 0
    for i in range(1,num):
        if i != num: num += i
    return num
print(triangle_number(5))

print('------------')

#2
def rect_maker(h, w, char):
    for i in range(h):
        for j in range(w):
            print(char, end=' ')
        print()
rect_maker(5,10,'*')

print('---------')

#3
def Make_character_parallelogram(height, width, char):
    rollingheight = height-1
    for i in range(height):
        for k in range(rollingheight):
            print(end=' ')
        rollingheight -= 1 
        for j in range(width):
            print(char, end=' ')   
        print()    
Make_character_parallelogram(5,10,'*')

print('---------')

#4
def one_tenth_clock():
    HOURS = 0
    MINS = 0
    SECS = 0
    FRACTION = 0
    clockBool = True

    while clockBool:
        FRACTION += 1
        time.sleep(.1)
        printTime(HOURS, MINS, SECS, FRACTION)
        if FRACTION == 10:
            FRACTION = 0
            SECS += 1
            if SECS == 60:
                MINS += 1
                SECS = 0
                if MINS == 60:
                    HOURS += 1
                    MINS = 0
                    if HOURS == 24:
                        HOURS = 0


def printTime(hrs, mins, secs, frac):
        print(f'{str(hrs):>02}:{str(mins):>02}:{str(secs):>02}.'+str(frac))

one_tenth_clock()