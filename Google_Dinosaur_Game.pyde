def setup():
    global player, obstacle1, obstacle2, gravity_var, ui
    player = {
    "skin": loadImage("Dinosaur.png"),
    "alive": True,
    "score": 0,
    "highest score": 0,
    "speed": 5,
    "x": 30,
    "y": height-50*1.5,
    "width": 45*1.5,
    "height": 45*1.5,      
    }
    
    ui = {
    "replayButton": loadImage("replay.png"),
    "replayButtonWidth": 50,
    "replayButtonHeight": 50,
    "restart": False 
    }
    
    obstacle1 = {
    "skin": loadImage("Cactus.png"),
    "x": width,
    "y": height-53*1.5,
    "width": 20*1.5,
    "height": 50*1.5
    }
    
    obstacle2 = {
    "skin": loadImage("Cactus2.png"),
    "x": width,
    "y": height-54*1.5,
    "width": 30*1.5,
    "height": 50*1.5
    }
    
    gravity_var = {
    "vy": 0,
    "ay": 0        
    }
    
    
    
    frameRate(60)
    size(960, 540)
        
def draw():
    Simulate()
    Render()
    UI()
    Obstacle(player["speed"])
    Player()
    if ui["restart"]:
        Obstacle(player["speed"])
        Player()
        
def Obstacle(Speed):
    if obstacle1["x"] > -22.5:
        obstacle1["x"] = obstacle1["x"] - Speed
        image(obstacle1["skin"],obstacle1["x"], obstacle1["y"], obstacle1["width"], obstacle1["height"])
    else:
        obstacle1["x"] = width
        
    if obstacle2["x"] > -22.5 and (obstacle1["x"] < width/2 or obstacle2["x"] < obstacle1["x"]):
        obstacle2["x"] = obstacle2["x"] - Speed
        image(obstacle2["skin"],obstacle2["x"], obstacle2["y"], obstacle2["width"], obstacle2["height"])
    else:
        obstacle2["x"] = width

def Render():
    background(255)
    line(0, height-10, width, height-10)

def keyPressed():
    if (key == " " and player["y"] == height-50*1.5 and player["alive"]):
        gravity_var["vy"] = -15
    if (key == " " and not player["alive"]):
        ui["restart"] = True

def UI():
    scoreX = width-125
    scoreY = 50
    
    highest_scoreX = width-150
    highest_scoreY = scoreY + 25
    
    fill(0)
    if player["score"] < 10:
        text("score: 0000" + str(int(player["score"])), scoreX, scoreY)
    elif player["score"] < 100:
        text("score: 000" + str(int(player["score"])), scoreX, scoreY)
    elif player["score"] < 1000:
        text("score: 00" + str(int(player["score"])), scoreX, scoreY)
    elif player["score"] < 10000:
        text("score: 0" + str(int(player["score"])), scoreX, scoreY)
    else:
        text("score: " + str(int(player["score"])), scoreX, scoreY)
        
    if player["highest score"] < 10:
        text("highest score: 0000" + str(int(player["highest score"])), highest_scoreX, highest_scoreY)
    elif player["highest score"] < 100:
        text("highest score: 000" + str(int(player["highest score"])), highest_scoreX, highest_scoreY)
    elif player["highest score"] < 1000:
        text("highest score: 00" + str(int(player["highest score"])), highest_scoreX, highest_scoreY)
    elif player["highest score"] < 10000:
        text("highest score: 0" + str(int(player["highest score"])), highest_scoreX, highest_scoreY)
    else:
        text("highest score: " + str(int(player["highest score"])), highest_scoreX, highest_scoreY)
    
    if not player["alive"]:
        text("You Lost!", width/2-25, height/2-25)
        player["speed"] = 0
        if player["score"] > player["highest score"]:
            player["highest score"] = player["score"]
        image(ui["replayButton"], width/2-25, height/2, ui["replayButtonWidth"], ui["replayButtonHeight"])
        if ui["restart"]:
            player["score"] = 0
            player["x"] = 30
            player["y"] = height-50*1.5
            player["speed"] = 5
            obstacle1["x"] = width
            obstacle2["x"] = width
            player["alive"] = True
            ui["restart"] = False
            
def Player():
    doesCollide()
    image(player["skin"], player["x"], player["y"], player["width"], player["height"])
    if player["alive"]:
        player["score"] = player["score"] + 0.10

def mouseClicked():
    if mouseX >= width/2-25 and mouseX <= (width/2-25+ui["replayButtonWidth"]) and mouseY >= height/2 and mouseY <= (height/2+ui["replayButtonHeight"]):
        ui["restart"] = True

def Simulate():
    gravity_var["ay"] = 0.80
    gravity_var["vy"] = gravity_var["vy"] + gravity_var["ay"]
    player["y"] = player["y"] + gravity_var["vy"]
    
    if (player["y"] > height-50*1.5):
        player["y"] = height-50*1.5
        gravity_var["vy"] = 0
        gravity_var["ay"] = 0
    
    if (player["y"] > height+60*1.5):
        player["y"] = -100
        gravity_var["vy"] = 10
    
def doesCollide():
    if((player["x"] >= obstacle1["x"] and player["x"] <= obstacle1["x"]+obstacle1["width"]) or (player["x"]+player["width"] >= obstacle1["x"] and player["x"]+player["width"] <= obstacle1["x"]+obstacle1["width"])):
        if ((player["y"] >= obstacle1["y"] and player["y"] <= obstacle1["y"]+obstacle1["height"]) or (player["y"]+player["height"] >= obstacle1["y"] and player["y"]+player["height"] <= obstacle1["y"]+obstacle1["height"])):
               player["alive"] = False
    if((player["x"] >= obstacle2["x"] and player["x"] <= obstacle2["x"]+obstacle2["width"]) or (player["x"]+player["width"] >= obstacle2["x"] and player["x"]+player["width"] <= obstacle2["x"]+obstacle2["width"])):
        if ((player["y"] >= obstacle2["y"] and player["y"] <= obstacle2["y"]+obstacle2["height"]) or (player["y"]+player["height"] >= obstacle2["y"] and player["y"]+player["height"] <= obstacle2["y"]+obstacle2["height"])):
               player["alive"] = False
