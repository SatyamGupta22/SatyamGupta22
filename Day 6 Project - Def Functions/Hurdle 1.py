def turn_around():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    move()
    turn_left()
    move()
    turn_around()
    move()
    turn_around()
    move()
    turn_left()
    
 
for step in range(6):
    hurdle()
    


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
