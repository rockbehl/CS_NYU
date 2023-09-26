# 1
import random

big_total = 0
maximum_share = 0


def mutate_big_total(num):
    global big_total
    big_total += num


def mutate_maximum_share(num):
    global maximum_share
    maximum_share += num


def div_w_remainder(dividend, divisor):
    whole = dividend // divisor
    remainder = dividend % divisor
    return whole, remainder


def share_items(number_of_things, number_of_people):
    mutate_big_total(number_of_things)
    mutate_maximum_share(div_w_remainder(number_of_things, number_of_people)[0])
    if div_w_remainder(number_of_things, number_of_people)[1] > 0:
        mutate_maximum_share(1)


def question1():
    share_items(10, 4)
    share_items(20, 3)
    share_items(14, 7)


question1()
print(big_total, maximum_share)

# 2
import turtle

window = turtle.Screen()
window.title("Stickfigure")
window.setup(720, 720)
window.screensize(window.window_width(),window.window_height(), "white")

runLoop = True

def draw_stick_figure(armLen, legLen, headRadius, x, y):
    jim = turtle.Turtle()
    jim.speed(-1)
    jim.pensize(3)
    arm_length = armLen  # Change these if you want
    leg_length = legLen

    if x > 0 and y > 0:
        jim.pencolor("blue")
        jim.pensize(random.randint(1, 5))
    elif x < 0 < y:
        jim.pencolor("green")
        jim.pensize(random.randint(3, 6))
    elif x < 0 and y < 0:
        jim.pencolor("yellow")
        jim.pensize(random.randint(1, 10))
    elif x > 0 > y:
        jim.pencolor("red")
        jim.pensize(random.randint(4, 7))
    else: jim.pencolor("black")

    # if the x and values indicate that the stickman is near the middle use the change_color function
    if -100 < x < 100 and -100 < y < 100:
        jim.pencolor("purple")




    def reset():
        jim.pu()
        jim.setpos(x, y)
        jim.pd()

        # draw a stickman

    reset()

        # head
    jim.seth(90)
    jim.fd(30)
    jim.rt(90)
    headRand = random.randint(1, 10)
    if headRand > 5:
        jim.circle(headRadius)
        jim.fillcolor()
    else:
        jim.circle(headRadius)


    reset()

        # arm 1
    jim.seth(160)
    jim.fd(arm_length / 2)
    jim.rt(20)
    jim.fd(arm_length / 2)

    reset()

        # arm 2
    jim.seth(20)
    jim.fd(arm_length / 2)
    jim.lt(20)
    jim.fd(arm_length / 2)

    reset()

        # leg 1
    jim.seth(270)
    jim.fd(50)
    jim.seth(230)
    jim.fd(leg_length / 2)
    jim.lt(40)
    jim.fd(leg_length / 2)

    reset()

        # leg 2
    jim.seth(270)
    jim.fd(50)
    jim.seth(310)
    jim.fd(leg_length / 2)
    jim.rt(40)
    jim.fd(leg_length / 2)

def drawCheckingSq(color, rtVal):
    checkingSq = turtle.Turtle()
    checkingSq.speed(2)
    checkingSq.color(color)
    checkingSq.pensize(5)
    checkingSq.pu()
    checkingSq.setpos(0, 0)
    checkingSq.pd()
    checkingSq.seth(rtVal)
    checkingSq.fd((window.window_width() / 2)+10)
def mainPictureLoop():
    window.clear()
    window.listen()
    window.onkey(mainPictureLoop, "space")
    window.onkey(window.bye, "Escape")
    window.tracer(0)

    for i in range(500):
        draw_stick_figure(random.randint(10, 100), random.randint(10, 100), random.randint(10, 100),
                          random.randint(-(window.canvwidth) * 2, window.canvwidth * 2),
                          random.randint(-(window.canvheight), window.canvheight))

    window.update()

    window.tracer(1)

mainPictureLoop()

window.mainloop()





