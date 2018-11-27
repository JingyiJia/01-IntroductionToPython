"""
Your chance to explore Loops and Turtles!

Authors: Jingyi. Jia
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
import math
window = rg.TurtleWindow()
Jingyi = rg.SimpleTurtle('turtle')
Jingyi.pen_up()
Jingyi.left(90)
Jingyi.forward(250)
Jingyi.pen_down()
Jingyi.pen = rg.Pen('black',6)
Jingyi.speed = 1
Jingyi.left(90)
Jingyi.forward(70)
Jingyi.left(45)
Jingyi.forward(70)
Jingyi.left(135)
Jingyi.forward(2*70/math.sqrt(2)+70)
Jingyi.left(135)
Jingyi.forward(70)
Jingyi.speed = 100
Jingyi.pen_up()
Jingyi.left(135)
Jingyi.forward(70/math.sqrt(2))
Jingyi.right(90)
Jingyi.forward(35)
Jingyi.pen_down()
Jingyi.speed = 3
Jingyi.draw_circle(120)
Jingyi.pen_up()
Jingyi.left(90)
Jingyi.forward(100)
Jingyi.right(90)
Jingyi.pen_down()
for k in range(2):
    Jingyi.draw_circle(150 + 15 * k)
Jingyi.pen_up()
Jingyi.forward(50)
Jingyi.right(50)
Jingyi.forward(25)
Jingyi.pen_down()
Jingyi.draw_circle(10)
Jingyi.pen_up()
Jingyi.right(135)
Jingyi.forward(135)
Jingyi.pen_down()
Jingyi.draw_circle(10)
Jingyi.right(90)
Jingyi.pen_up()
Jingyi.forward(23)
Jingyi.pen_down()
Jingyi.forward(100)
Jingyi.right(145)
Jingyi.forward(125)
Jingyi.left(125)
Jingyi.forward(125)
Jingyi.right(145)
Jingyi.forward(100)
Jingyi.left(145)
for k in range(2):
    Jingyi.right(88)
    Jingyi.forward(90)
    Jingyi.right(180)
    Jingyi.forward(90)
Jingyi.pen_up()
Jingyi.right(70)
Jingyi.forward(170)
Jingyi.pen_down()
for k in range(2):
    Jingyi.left(55)
    Jingyi.forward(90)
    Jingyi.left(180)
    Jingyi.forward(90)
window.close_on_mouse_click()
# A snowman completes!