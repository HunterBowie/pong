import pygame, random
import constants, windowgui

class Game:
    def __init__(self, window):
        self.window = window
        self.paddles = []
        self.balls = []
        self.items = []
        self.collisions = []

        self.create_paddle("left")
        self.create_paddle("right")
        self.create_ball()

        self.left_score = 0
        self.right_score = 0
    
        self.paddle_slow_timer = windowgui.Timer()
        self.paddle_slow_timer.start()

    def create_ball(self):
        ball = {
            "type": "ball",
            "rect": pygame.Rect(
                constants.SCREEN_WIDTH//2-constants.BALL_RADIUS,
                constants.SCREEN_HEIGHT//2-constants.BALL_RADIUS,
                constants.BALL_RADIUS*2, constants.BALL_RADIUS*2
            ),  
            "vel": random.choice([[constants.BALL_X_VEL, 0], [-constants.BALL_X_VEL, 0]]),
        }
        self.items.append(ball)
        self.balls.append(ball)
    
    def create_paddle(self, side):
        x = constants.SCREEN_WIDTH-constants.PADDLE_WIDTH*2
        if side == "left":
            x = constants.PADDLE_WIDTH 

        paddle = {
            "type": "paddle",
            "rect": pygame.Rect(x, constants.SCREEN_HEIGHT//2-constants.PADDLE_HEIGHT//2,
            constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT),
            "vel": [0, 0]
        }
        self.items.append(paddle)
        self.paddles.append(paddle)
    
    def destroy_ball(self, ball):
        self.items.remove(ball)
        self.balls.remove(ball)

    def eventloop(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.create_ball()

    def update(self):
        if self.left_score > 10:
            print(f"Left Paddle Wins!")
            self.window.end()
        if self.right_score > 10:
            print(f"Right Paddle Wins!")
            self.window.end()
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.paddles[1]["vel"][1] = -constants.PADDLE_SPEED
        elif keys[pygame.K_DOWN]:
            self.paddles[1]["vel"][1] = constants.PADDLE_SPEED
        if keys[pygame.K_w]:
            self.paddles[0]["vel"][1] = -constants.PADDLE_SPEED
        elif keys[pygame.K_s]:
            self.paddles[0]["vel"][1] = constants.PADDLE_SPEED
        
        if self.paddle_slow_timer.passed(.1):
            self.paddle_slow_timer.start()
            for paddle in self.paddles:
                if paddle["vel"][1] < 0:
                    paddle["vel"][1] += constants.PADDLE_SLOW
                elif paddle["vel"][1] > 0:
                    paddle["vel"][1] -= constants.PADDLE_SLOW  
        
        for item in self.items:
            item["rect"].x += item["vel"][0]
            for item2 in self.items:
                if item2 != item:
                    if item["rect"].colliderect(item2["rect"]):
                        self.collisions.append({"item1": item, "item2": item2, "axis": 0})
                        if item["vel"][0] > 0:
                            item["rect"].right = item2["rect"].left
                        elif item["vel"][0] < 0:
                            item["rect"].left = item2["rect"].right
                    
    
            item["rect"].y += item["vel"][1]
            for item2 in self.items:
                if item2 != item:
                    if item["rect"].colliderect(item2["rect"]):
                        self.collisions.append({"item1": item, "item2": item2, "axis": 1})
                        if item["vel"][1] > 0:
                            item["rect"].bottom = item2["rect"].top
                        elif item["vel"][1] < 0:
                            item["rect"].top = item2["rect"].bottom
        
        for paddle in self.paddles:
            if paddle["rect"].top < 0:
                paddle["rect"].top = 0
            if paddle["rect"].bottom > constants.SCREEN_HEIGHT:
                paddle["rect"].bottom = constants.SCREEN_HEIGHT
        
        reset_balls = []
        
        for ball in self.balls:
            for collision in self.collisions:                    
               if collision["item1"] == ball or collision["item2"] == ball: 
                    item = collision["item1"]
                    if collision["item1"] == ball:
                        item = collision["item2"]
                    if item["type"] == "paddle":
                        paddle = item                        
                        # paddle isn't moving
                        if paddle["vel"][1] == 0:
                            ball["vel"][1] = ball["vel"][1]//2
                            ball["vel"][0] *= -1
                        # paddle is moving
                        else:
                            force = constants.PADDLE_FORCE
                            if paddle["vel"][1] < 1:
                                force *= -1
                            ball["vel"][1] = paddle["vel"][1] + force

                            # paddle not above or below ball
                            if paddle["rect"].bottom != ball["rect"].top and paddle["rect"].top != ball["rect"].bottom: 
                                ball["vel"][0] *= -1
                           
                    else:
                        ball["vel"][0] *= -1
                        ball["vel"][1] *= -1
                        
            if ball["rect"].top < 0:
                ball["rect"].top = 0
                ball["vel"][1] *= -1

            if ball["rect"].bottom > constants.SCREEN_HEIGHT:
                ball["rect"].bottom = constants.SCREEN_HEIGHT
                ball["vel"][1] *= -1
            
            if ball["rect"].left < 0:
                self.right_score += 1
                reset_balls.append(ball)
            
            if ball["rect"].right > constants.SCREEN_WIDTH:
                self.left_score += 1
                reset_balls.append(ball)
            
        self.collisions.clear()
            
        for ball in reset_balls:
            self.destroy_ball(ball)
            self.create_ball()          
        
        for item in self.items:
            if item["type"] == "ball":
                pygame.draw.circle(self.window.screen, windowgui.Colors.ORANGE, 
                item["rect"].center, constants.BALL_RADIUS)
            else:
                pygame.draw.rect(self.window.screen, windowgui.Colors.BLACK, item["rect"], border_radius=5)

        windowgui.Text(200, 20, str(self.left_score), style={"size": 35}).render(self.window.screen)
        windowgui.Text(constants.SCREEN_WIDTH-200, 20, str(self.right_score), style={"size": 35}).render(self.window.screen)
        
        
        
        

        


        

        
