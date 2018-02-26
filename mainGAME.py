from tkinter import *
import table, ball, ship, random

window = Tk()
window.title("NAME")
my_table = table.Table(window)

#initialise global variablesx
x_velocity = 35
y_velocity = 0
first_serve = True

#order a ball from the ball class
my_ball = ball.Ball(table=my_table, x_speed=x_velocity, y_speed=y_velocity, width=24, colour="red", x_start=288, y_start=188)

#order a ship from the ship class
ship_B = ship.Ship(table = my_table, width=100 height=10, x_posn=250, y_posn=370, colour="blue")

#order further ships from the ship class but call them cards
cards = []
b=1
while b < 7:
    cards.append(ship.Ship(table = my_table, width=50, height=20, x_posn=(b*i), y_posn=75, colour="green"))
    b = b+1

####function:
def game_flow():
    global first_serve
    #wait for first serve:
    if(first_serve == True):
        my_ball.stop_ball()
        first_serve = False

    #detect if ball hit the ships
    ship_B.detect_collision(my_ball, sides_sweet_spot=False, topnbottom_sweet_spot=True)

    #detect if ball has hit the cards:
    for b in cards:
        if(b.detect_collision(my_ball, sides_sweet_spot=False) != None):
            my_table.remove_item(b.rectangle)
            cards.remove(b)
        if(len(bricks) == 0):
            my_ball.stop_ball()
            my_ball.start_position()
            my_table.draw_score("", " YOU WIN!")

    #detect if ball hit the bottom wall
    if(my_ball.y_posn >= my_table.height - my_ball.height):
        my_ball.stop_ball()
        my_ball.start_position()
        first_serve = True
        my_table.draw_score("", " WHOOPS!")

    my_ball.move_next()
    window.after(50, game_flow)

def restart_game(master):
    my_ball.start_ball(x_speed=x_velocity, y_speed=y_velocity)
    my_table.draw_score("", "")

#bind the controls of the ship to the keys on the keyboard
window.bind("<left>", ship_B.move_left)
window.bind("<Right>", ship_B.move_right)
window.bind("<Up>", ship_B.move_up)
window.bind("<Down>", ship_B.move_down)

#bind the restart to spacebar
window.bind("<space>", restart_game)

game_flow()
window.mainloop()
