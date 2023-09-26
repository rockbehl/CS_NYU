# part 1
# q1
import random


def odd_even(num):
    if num == 0:
        print('zero')
    elif num % 2 == 0:
        print('even')
    else:
        print('odd')
    if num % 3 == 0 and num != 0: print('divisible by three')


odd_even(0)


# q2
def num_conditionl(num):
    if num % 2 == 0 and num % 3 != 0:
        return True
    elif num % 2 != 0 and num % 3 == 0:
        return True
    else:
        return False


print(num_conditionl(4))


# q3
def generate_truth_table():
    print('p\t|\tq\t|\tp == q\t|\tp != q\t|\tp and q\t|\tp or q\t|\tnot p\t|')
    for i in range(1, 8): print('\t-', end='\t')
    print()
    for i in range(1, 4):
        if i % 2 == 0:
            q = True
        else:
            q = False
        if i == 1 or i == 2:
            p = False
        else:
            p = True
        generate_truth_table_rows(p, q)
    print()


def generate_truth_table_rows(p, q):
    print(p, end='\t|\t')
    print(q, end='\t|\t')
    print(p == q, end='\t|\t')
    print(p != q, end='\t|\t')
    print(p and q, end='\t|\t')
    print(p or q, end='\t|\t')
    print(not p, end='\t|\n')


generate_truth_table()

# part 2
# write an Interactive fiction game thats in the console that allows only the user to input yes or no, make a branching story with 5 endings and 15 unique decisions the user has to make
def game():
    print('Welcome to the game')
    gameplay = True
    #put all this code in a while loop and go until ganmeplay is false
    while gameplay:
        print('You are in a room with two doors, one to your left and one to your right')
        print('Which door do you choose?')
        choice = input('left or right?')
        if choice == 'left':
            print('You chose the left door')
            print('You are in a room with a table and a chair')
            print('Do you sit on the chair?')
            choice = input('yes or no?')
            if choice == 'yes':
                print('You sit on the chair and the chair breaks')
                print('You fall on the ground and a trap door opens')
                print('You fall into a pit of lava and die')
                print('GAME OVER')
            elif choice == 'no':
                print('You dont sit on the chair')
                print('You walk towards the table')
                print('Do you pick up the book on the table?')
                choice = input('yes or no?')
                if choice == 'yes':
                    print('You pick up the book and open it')
                    print('The book is a spell book')
                    print('You read the first spell and a fireball appears in your hand')
                    print('Do you cast the fireball?')
                    choice = input('yes or no?')
                    if choice == 'yes':
                        print('You cast the fireball and it hits the wall')
                        print('The wall collapses and you see a door')
                        print('Do you go through the door?')
                        choice = input('yes or no?')
                        if choice == 'yes':
                            print('You go through the door and you see a treasure chest')
                            print('Do you open the chest?')
                            choice = input('yes or no?')
                            if choice == 'yes':
                                print('You open the chest and find a key')
                                print('You take the key and go back to the room with the two doors')
                                print('Do you go through the left door or the right door?')
                                choice = input('left or right?')
                                if choice == 'left':
                                    print('You go through the left door and see a door with a lock')
                                    print('Do you use the key?')
                                    choice = input('yes or no?')
                                    if choice == 'yes':
                                        print('You use the key and the door opens')
                                        print('You win!')
                                    elif choice == 'no':
                                        print('You dont use the key and the door stays locked')
                                        print('You go back to the room with the two doors')
                                        print('Do you go through the left door or the right door?')
                                        choice = input('left or right?')
                                        if choice == 'left':
                                            print('You go through the left door and see a door with a lock')
                                            print('Do you use the key?')
                                            choice = input('yes or no?')
                                            if choice == 'yes':
                                                print('You use the key and the door opens')
                                                print('You win!')
                                            elif choice == 'no':
                                                print('You dont use the key and the door stays locked')
                                                print('You go back to the room with the two doors')
                                                print('Do you go through the left door or the right door?')
                                                choice = input('left or right?')
                                                if choice == 'left':
                                                    print('You go through the left door and see a door with a lock')
                                                    print('Do you use the key?')
                                                    choice = input('yes or no?')
                                                    if choice == 'yes':
                                                        print('You use the key and the door opens')
                                                        print('You win!')
                                                    elif choice == 'no':
                                                        print('You dont use the key and the door stays locked')
                                                        print('You go back to the room with the two doors')
                                                        print('Do you go through the left door or the right door?')
                                                        choice = input('left or right?')
                                                        if choice == 'left':
                                                            print('You go through the left door and see a door with a lock')
                                                            print('Do you use the key?')
                                                            choice = input('yes or no?')
                                                            if choice == 'yes':
                                                                print('You use the key and the door opens')
                                                                print('You win!')
                                                            elif choice == 'no':
                                                                print('You dont use the key and the door stays locked')
                                                                print('You go back to the room with the two doors')
                                                                print('Do you go through the left door or the right door?')
                                                                choice = input('left or right?')
                                                                if choice == 'left':
                                                                    print('You go through the left door and see a door with a lock')
                                                                    print('Do you use the key?')
                                                                    choice = input('yes or no?')
                                                                    if choice == 'yes':
                                                                        print('You use the key and the door opens')
                                                                        print('You win!')
                                                                        gameplay = False

game()
