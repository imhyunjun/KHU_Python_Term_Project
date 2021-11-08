import turtle

n = 5
count = 0
turtle.shape("turtle")

while count < n:
    turtle.forward(100)
    turtle.right((360 / n) * 2)
    turtle.forward(100)
    turtle.left(360 / n)
    count += 1
