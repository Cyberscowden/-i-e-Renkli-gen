import turtle

x = turtle.Turtle()
def kareCiz(): #kare çizme fonksiyonu

    turtle.color("black")

    x.pensize(5)
    x.begin_fill() #begin_fill karenin içini doldurur bu diğer nesneler içinde gecerli
    for i in range(4):
        x.forward(250)
        x.left(360 / 4)
        x.end_fill() #Bu yöntem, begin_fill () çağrısından sonra çizilen şekli doldurmak için kullanılır
def ücgenciz():
    x.color("black", "white")
    x.pensize(5)
    x.begin_fill()
    for i in range(3):
        x.forward(250)
        x.left(360 / 3)
        x.end_fill()


kareCiz()
ücgenciz()
turtle.done()