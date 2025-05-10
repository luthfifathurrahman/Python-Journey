from turtle import Turtle, Screen

class Background():
    def __init__(self):
        self.screen = Screen()
        self.turtle = Turtle()
        self.screen.setup(width=725, height=491)
        self.screen.title("U.S. States Game")
        self.image = "blank_states_img.gif"
        self.screen.addshape(self.image)
        self.turtle.shape(self.image)

    def mainloop_screen(self):
        self.screen.mainloop()

    def close_screen(self):
        self.screen.bye()

