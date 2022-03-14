import turtle
#Iseseisev töö

aken = turtle.Screen()
aken.setup(300,300)

tri = turtle.Turtle()

for i in range(5):
    tri.left(360/5)
    tri.forward(50)
    tri.left(120)
    tri.forward(100)
    tri.left(120)
        
    tri.forward(100)
    tri.left(120)
    tri.forward(50)
    
    

turtle.exitonclick()