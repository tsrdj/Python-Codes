import turtle as t
#d_codez2021
import colorsys
t.bgcolor('black')
t.setpos(-90,80)
#d_codez2021
t.tracer(200)
t.pensize(2)
#d_codez2021
hue=0.0
t.hideturtle()
for i in range(800):
  color=colorsys.hsv_to_rgb(hue,1,1)
  t.fd(200)
  #d_codez2021
  t.pencolor(color)
  t.rt(91)
  t.circle(90)
  hue+=0.009
  #d_codez2021
t.exitonclick
