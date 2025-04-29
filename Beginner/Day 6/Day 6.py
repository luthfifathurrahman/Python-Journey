# Functions
# defining functions
def my_function():
    print("hello")
    print("bye")

# calling functions
my_function()

# # Reeborg's World
# # https://reeborg.ca/reeborg.html
# # draw square
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()
#
# # hurdle 1
# # https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# def go_to_finish_flag():
#     for step in range(6):
#         jump()
#
# go_to_finish_flag()
#
# # While Loops
# # hurdle 2
# # https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# def go_to_finish_flag():
#     while not at_goal():
#         jump()
#
# go_to_finish_flag()
#
# # hurdle 3
# # https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# def go_to_finish_flag():
#     while not at_goal():
#         if front_is_clear():
#             move()
#         elif wall_in_front():
#             jump()
#
# go_to_finish_flag()
#
# # hurdle 4
# # https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
#
# def go_to_finish_flag():
#     while not at_goal():
#         if front_is_clear():
#             move()
#         elif wall_in_front():
#             jump()
#
# go_to_finish_flag()
#
# # Maze
# # https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def go_to_finish_flag():
#     while front_is_clear():
#         move()
#     turn_left()
#     while not at_goal():
#         if right_is_clear():
#             turn_right()
#             move()
#         elif front_is_clear():
#             move()
#         else:
#             turn_left()
#
# go_to_finish_flag()