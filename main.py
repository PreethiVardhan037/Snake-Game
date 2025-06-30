from os import remove
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("yellow")
screen.title("Serpent's chase")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect collision of snake head and food
    if snake.segments[0].distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snake.extend()
        scoreboard.update_score()
    #Detect collision with wall
    if snake.segments[0].xcor() > 297 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
    #detect collision with tail
    for segments in snake.segments[1:]:
        if snake.segments[0].distance(segments) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

