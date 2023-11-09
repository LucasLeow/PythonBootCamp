from turtle import Turtle, Screen
import random

class TurtleRace:
    # Constants
    WIDTH = 500
    HEIGHT = 400
    def __init__(self):
        self.colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        self.turtles = []
        self.screen = Screen()
        self.bet = ""
        self.race_on = True


    def create_turtles(self):
        for i in range(len(self.colours)):
            t = Turtle(shape='turtle')
            t.color(self.colours[i])
            self.turtles.append(t)

    def display_turtles(self):
        self.screen.setup(width=TurtleRace.WIDTH, height=TurtleRace.HEIGHT)

        x_start = -TurtleRace.WIDTH/2 + 10
        y_start = -TurtleRace.HEIGHT/2 + 50

        self.ask_bet()

        for i in range(len(self.turtles)):
            self.turtles[i].penup()
            self.turtles[i].goto(x_start, y_start)
            y_start += 50

    def ask_bet(self):
        self.bet = self.screen.textinput(title="Make your bet",
                                         prompt="Which turtle will win the race? red | orange | yellow | green | blue | indigo | violet")

    def turtle_race(self):
        while self.race_on:
            winner = self.check_winner()
            if winner:
                if self.bet.lower() == winner.fillcolor():
                    print('You won the bet!')
                else:
                    print("You lost the bet!")
                    print(f"Your bet was: {self.bet}.")
                    print(f" Winning Turtle: {winner.fillcolor()}.")
                break

            for turtle in self.turtles:
                if turtle.position():
                    turtle.forward(random.randint(1, 10))

    def check_winner(self):
        for turtle in self.turtles:
            if turtle.position()[0] >= TurtleRace.WIDTH / 2 - 20:
                self.race_on == False
                return turtle
        return None


if __name__ == '__main__':
    race = TurtleRace()
    race.create_turtles()
    race.display_turtles()
    race.turtle_race()