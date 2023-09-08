import turtle
import time
import random
import threading


screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(800,800)
screen.title("Catch the Freaking Turtle")
ekran_genislik = screen.window_width()
ekran_yukseklik = screen.window_height()

freaking_turtle = turtle.Turtle()
freaking_turtle.shape("turtle")
freaking_turtle.speed(0)
freaking_turtle.penup()


# Rastgele başlangıç konumu için sınırları ayarla
x_min, x_max = -180, 180
y_min, y_max = -200, 180

def belir_ve_kaybol():
    while True:
        for i in range(20):
            x = random.randint(x_min, x_max)
            y = random.randint(y_min, y_max)
            freaking_turtle.goto(x, y)
            freaking_turtle.showturtle()
            time.sleep(0.5)
            freaking_turtle.hideturtle()
        freaking_turtle.clear()
        turtle.done()

# işaret
timeR = turtle.Turtle()
timeR.shape("turtle")
timeR.speed(0)
timeR.penup()

timeR.goto(0, ekran_yukseklik // 2.8 - 20)
timeR.hideturtle()
timeR.clear()
def geri_sayim():
    for i in range(10, 0, -1):
        timeR.clear()
        timeR.write("Time: {}".format(i), align="center", font=("Arial", 24, "normal"))
        time.sleep(1)

    timeR.clear()
    timeR.write("Game Over", align="center", font=("Arial", 24, "normal"))
    turtle.done()

if __name__ == '__main__':
    threading.Thread(target=geri_sayim).start()
    threading.Thread(target=belir_ve_kaybol).start()





screen.exitonclick()



