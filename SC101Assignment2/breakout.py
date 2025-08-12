"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Game Over 
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    global NUM_LIVES
    graphics = BreakoutGraphics()
   
    dx = 0
    dy = 0
    graphics.label.text = f"Lives: {NUM_LIVES}"  
    # Add the animation loop here!
    while True:
        
        if not graphics._moving:
            dx = 0
            dy = 0
            pause(10)     
            continue

        # move 
        if dx == 0 and dy == 0:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            if dx == 0 and dy == 0:
                pause(10)
                continue

        graphics.ball.move(dx, dy)

        # setting default position of ball
        x, y = graphics.ball.x, graphics.ball.y
        w, h = graphics.ball.width, graphics.ball.height
        W, H = graphics.window.width, graphics.window.height

        # setting left and right bounderies
        if x <= 0:
            dx = -dx
            graphics.ball.x = 0                     
        elif x + w >= W:
            dx = -dx
            graphics.ball.x = W - w

        # setting up and down bounderies
        if y <= 0:
            dy = -dy
            graphics.ball.y = 0
        elif y + h >= H:
            graphics.ball.x = (W - w) / 2
            graphics.ball.y = (H - h) / 2
            dx = 0
            dy = 0
            graphics._moving = False  
            NUM_LIVES = NUM_LIVES - 1
            graphics.label.text = f"Lives: {NUM_LIVES}"    
        collied = graphics.check_for_collison()
        if collied == 'paddle':
            if dy > 0:
                dy = -dy
        elif collied == 'brick':
            dy = -dy
        if NUM_LIVES == 0: 
            graphics.label.text = f"Game Over"  
            break 
        elif graphics.total_bricks == 0:
            print('You Win!')
            break

        pause(FRAME_RATE)

    

if __name__ == '__main__':
    main()
