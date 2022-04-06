import turtle
import random

# <START SCREEN>

def main(): 
  '''' this is the function for the start screen'''

  s = turtle.Screen()
  s.setup(320,320)
  s.screensize(300,300)
  s.bgpic("start_screen.gif") # sets the background picture the the start_screen gif
  s.title('Spacer') 
  s.tracer(0)
  w, h = s.screensize()

  t1 = turtle.Turtle()
  t1.color('white')
  t1.goto(-120, -140)
  t1.write('Press SPACE to start\nUse the arrow buttons to play\n\nDodge the asteroids and touch\nthe black hole to win', font = 50)

  def space():
    '''function for when space button is pressed'''
    s.clear()
    game_screen()
  
  s.onkey(space, ' ')  # will call the game_screen function when space is pressed
  s.listen()

# <GAME SCREEN>

def game_screen(): 
  '''this is the main game function'''

  s = turtle.Screen()
  s.setup(320,320)
  s.screensize(300,300)
  s.bgpic("bg_pic.gif")
  s.title('Spacer')
  s.tracer(0)

  w, h = s.screensize()

  # a list of dictionaries to store all the variables
  game_objects = [{"t": turtle.Turtle(),"x": 0, "y": -135, "radius": 10, "image":"space_ship.gif", "type":"player", "speed": 40},
  
  {"t": turtle.Turtle(),"x": random.randint(-w/2, w/2), "y": 140, "radius": 10, "image":"black_hole.gif", "type":"destination"}, 
  
  {"t": turtle.Turtle(),"x": random.randint(-w/2, w/2), "y": 0, "radius": 10, "image":"rock.gif", "type":"harm3"},
  
  {"t": turtle.Turtle(),"x": random.randint(-w/2, w/2), "y": 50, "radius": 10, "image":"rock.gif", "type":"harm2"},
  
  {"t": turtle.Turtle(),"x": random.randint(-w/2, w/2), "y": -50, "radius": 10, "image":"rock.gif", "type":"harm4"},
  
  {"t": turtle.Turtle(),"x": random.randint(-w/2, w/2), "y": 100, "radius": 10, "image":"rock.gif", "type":"harm1"},

  {"t": turtle.Turtle(),"x": random.randint(-w/2, w/2), "y": -100, "radius": 10, "image":"rock.gif", "type":"harm5"}
   ]

  player = game_objects[0]
  
  for obj in game_objects: #adds the image to the turtle
    s.addshape(obj["image"])
    obj["t"].shape(obj["image"])

  game_state = "play"

#all the variables for the lives and score
  t_lives = turtle.Turtle()
  t_lives.ht()
  t_score = turtle.Turtle()
  t_score.ht()
  t_level = turtle.Turtle()
  t_level.ht()
  
  lives = 3
  score = 0
  level = 1

  t_lives.penup()
  t_lives.goto(-150, -150)
  t_lives.pendown()
  t_lives.color('white')
  t_lives.write('Lives: ' + str(lives), font = 50)

  t_score.color('white')
  t_score.penup()
  t_score.goto(75, -150)
  t_score.pendown()
  t_score.write('Score: ' + str(score), font = 50)

  t_level.penup()
  t_level.goto(75, -135)
  t_level.pendown()
  t_level.color('white')
  t_level.write('Level: ' + str(level), font = 50)

# a while loop to keep the game playing as long as the game state is not over
  while (game_state != "over"):
    for obj in game_objects:
      obj["t"].clear()

# all the rocks that are moving accross the screen
    for obj in game_objects:
      if (obj["type"] == "harm1"):
        obj["x"] -= .1 * level
        if obj["x"] <  -w/2:
          obj["x"] = w/2

    for obj in game_objects:
      if (obj["type"] == "harm2"):
        obj["x"] += .1 * level
        if obj["x"] >  w/2:
          obj["x"] = -w/2

    for obj in game_objects:
      if (obj["type"] == "harm3"):
        obj["x"] -= .1 * level
        if obj["x"] <  -w/2:
          obj["x"] = w/2

    for obj in game_objects:
      if (obj["type"] == "harm4"):
        obj["x"] += .1 * level
        if obj["x"] >  w/2:
          obj["x"] = -w/2

    for obj in game_objects:
      if (obj["type"] == "harm5"):
        obj["x"] -= .1 * level
        if obj["x"] <  -w/2:
          obj["x"] = w/2

    for obj in game_objects:
      obj["t"].goto(obj["x"], obj["y"])

# functions for the arrow buttons to work
    def left():
      player["x"] -= player["speed"]
      if player["x"] < -w/2:
        player["x"] = -w/2 + 10

    def right():
      player["x"] += player["speed"]
      if player["x"] > w/2:
        player["x"] = w/2 - 10

    def up():
      player["y"] += player["speed"]
      if player["y"] > h/2:
        player["y"] = h/2 - 10

    def down():
      player["y"] -= player["speed"]
      if player["y"] < -h/2:
        player["y"] = -h/2 + 15

# this is calling the functions for the arrow buttons
    s.onkey(left, "Left")
    s.onkey(right, "Right")
    s.onkey(up, "Up")
    s.onkey(down, "Down")
    s.listen()

# loops for the collision
    for obj in game_objects:
      if obj["type"] != "player":
        if obj["type"] == "harm1" or obj["type"] == "harm2" or obj["type"] == "harm3" or obj["type"] == "harm4" or obj["type"] == "harm5":
          if game_objects[0]["t"].distance(obj["t"]) < 35:
            t_lives.clear()
            lives -= 1
            t_lives.write('Lives: ' + str(lives), font = 50)
            game_objects[0]["x"] = 0
            game_objects[0]["y"] = -135
            game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])

        elif obj["type"] == "destination":
          if game_objects[0]["t"].distance(obj["t"]) < 35:
            t_score.clear()
            t_level.clear()
            score += 10
            level += 1
            t_score.write('Score: ' + str(score), font = 50)
            t_level.write('Level: ' + str(level), font = 50)
            obj["x"] = random.randint(-w/ + 25, w/2 -25)
            game_objects[0]["x"] = 0
            game_objects[0]["y"] = -135
            game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])
          s.update()

    if lives == 0:
      s.clear()
      game_over(s, score)
      break

# <GAMEOVER SCREEN>
def game_over(s, score):
  '''fucntion for when the game is over'''
  s.setup(320,320)
  s.screensize(300,300)
  s.bgpic("game_over.gif")
  s.title('Spacer')
  s.tracer(0)
  t_over = turtle.Turtle()
  t_over.ht()
  t_over.penup()
  t_over.goto(-140, -130)
  t_over.pendown()
  t_over.write('Total Score:' + str(score), font = ("Arial", 20)) # prints out the total score the player have
  s.update()

main()