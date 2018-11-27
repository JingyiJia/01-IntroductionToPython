"""
An exercise that summarizes what you have learned in this Session.

Authors: Jingyi. Jia(Alan)
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
#
# Done: 2.
#   Write code that accomplishes the following (and ONLY the following),
#   in the order listed:
#
#    - Constructs a SimpleTurtle with a  'blue'  Pen.
#
#    - Makes the SimpleTurtle go straight UP 200 pixels.
#
#    - Makes the SimpleTurtle lift its pen UP
#         (so that the next movements do NOT leave a "trail")
#         HINT: Use the "dot trick" to figure out how to do this.
#
#    - Makes the SimpleTurtle go to the Point at (100, -40).
#
#    - Makes the SimpleTurtle put its pen DOWN
#         (so that the next movements will return to leaving a "trail").
#
#    - Makes the SimpleTurtle's pen have color 'green' and thickness 10.
#
#    - Makes the SimpleTurtle go 150 pixels straight DOWN.
#
#   Don't forget to:
#     - import rosegraphics and construct a TurtleWindow
#          at the BEGINNING of your code, and to
#     - ask your TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.
#   See the beginning and end of m4e_loopy_turtles for an example.
#
#   As always, test by running the module.
#   As always, COMMIT-and-PUSH when you are done with this module.
###########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
Alan = rg.SimpleTurtle('turtle')
Alan.pen = rg.Pen('blue',10)
Alan.left(90)
Alan.forward(200)
Alan.pen_up()
Alan.left(180)
Alan.forward(240)
Alan.right(90)
Alan.forward(100)
Alan.pen_down()
Alan.pen = rg.Pen('green', 10)
Alan.left(90)
Alan.forward(150)
window.close_on_mouse_click()
###########################################################################

