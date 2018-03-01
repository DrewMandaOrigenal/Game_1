from tkinter import *
import table, Invaders_missle, bat

# order a window from the tkinter window factory
window = Tk()
window.title("MyPong")
my_table = table.Table(window)

# initialise global variables
x_velocity = 10
y_velocity = 0
score_left = 0
score_right = 0
first_serve = True

# order a ball from the ball factory
my_invaders_missle = Invaders_missle.Invaders_missle(table=my_table, x_speed=x_velocity, y_speed=y_velocity,
                    width=24, height=24, colour="red", x_start=288, y_start=188)
#my_invaders_missle = Invaders_missle.Invaders_missle()

# order a left and right bat from the bat class
bat_L = bat.Bat(table=my_table, width=15, height=100, x_posn=20, y_posn=150, colour="blue")
bat_R = bat.Bat(table=my_table, width=15, height=100, x_posn=575, y_posn=150, colour="yellow")
#bat_L = bat.Bat()
#bat_R = bat.Bat()

#### functions:
def game_flow():
    global first_serve
    global score_left
    global score_right
    
    # wait for first serve:
    if(first_serve == True):
        my_invaders_missle.stop_ball()
        first_serve = False
    
    # detect if ball has hit the bats:
    bat_L.detect_collision(my_invaders_missle)
    bat_R.detect_collision(my_invaders_missle)

    # detect if the ball has hit the left wall:
##    if(my_invaders_missle.x_posn <= 3):
##        my_invaders_missle.stop_invaders_missle()
##        my_invaders_missle.start_position()
##        bat_L.start_position()
##        bat_R.start_position()
##        my_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
##        my_table.move_item(bat_R.rectangle, 575, 150, 590, 250)
##        score_left = score_left + 1
##        if(score_left >= 10):
##            score_left = "W"
##            score_right = "L"
##        first_serve = True
##        my_table.draw_score(score_left, score_right)

    # detect if the ball has hit the right wall:
##    if(my_invaders_missle.x_posn + my_ball.width >= my_table.width - 3):
##        my_invaders_missle.stop_invaders_missle()
##        my_invaders_missle.start_position()
##        bat_L.start_position()
##        bat_R.start_position()
##        my_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
##        my_table.move_item(bat_R.rectangle, 575, 150, 590, 250)
##        score_right = score_right + 1
##        if(score_right >= 10):
##            score_right = "W"
##            score_left = "L"
##        first_serve=True
##        my_table.draw_score(score_left, score_right)
     
    my_invaders_missle.move_next()
    window.after(50, game_flow)

# add restart_game function here:
def restart_game(master):
    global score_left
    global score_right
    my_ball.start_invaders_missle(x_speed=x_velocity, y_speed=0)
    if(score_left == "W" or score_left == "L"):
        score_left = 0
        score_right = 0
    my_table.draw_score(score_left, score_right)

# bind the controls of the bats to keys on the keyboard
window.bind("a", bat_L.move_up)
window.bind("z", bat_L.move_down)
window.bind("<Up>", bat_R.move_up)
window.bind("<Down>", bat_R.move_down)

# bind restart to the spacebar
window.bind("<space>", restart_game)

# call the game_flow loop
game_flow()

# start the tkinter loop process
window.mainloop()
