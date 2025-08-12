"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

All function 
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        # window
        self.window = GWindow(width=self.window_width, height= self.window_height, title=title)
        self.background = GRect(self.window.width, self.window_height)
        self.background.filled = True
        self.background.fill_color = 'white'
        self.window.add(self.background, 0, 0)
        # ball 
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window_width - ball_radius * 2) / 2, (self.window_height - ball_radius * 2) / 2)
        # paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window_width - paddle_width) / 2, self.window_height - paddle_offset - paddle_height)
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset
        self.label = GLabel('Number of Live')
        self.label.color = 'black'    
        x_pos = 10
        y_pos = self.window.height - 10
        self.window.add(self.label, x_pos, y_pos) 
        self.__dx = 0 
        self.__dy = 0
        self._moving = False
        self.total_bricks = brick_rows * brick_cols

        palette = ['red', 'orange', 'yellow', 'green', "gray"]
        rows_per_color = max(1, brick_rows // len(palette))  # change color of brick 

        for row in range(brick_rows):
            for col in range(brick_cols):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                color_index = row // rows_per_color
                brick.fill_color = palette[color_index % len(palette)]
                x = col * (brick_width + brick_spacing)
                y = brick_offset + row * (brick_height + brick_spacing)
                self.window.add(brick, x, y)

        onmouseclicked(self._click_mouse)
        onmousemoved(self._handle_mouse_move)

    def _click_mouse(self, event):
        
        if self._moving:
            return

        self.__dy = INITIAL_Y_SPEED

        # dx 取 1..MAX_X_SPEED 避免 0，再隨機決定左右方向
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        
        self._moving = True
    
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy
        
    def _handle_mouse_move(self, event):         
        new_x = event.x - self.paddle_width / 2

        # check border
        if new_x < 0:
            new_x = 0
        elif new_x > self.window_width - self.paddle_width:
            new_x = self.window_width - self.paddle_width

        self.paddle.x = new_x

    def check_for_collison(self):

        bx, by = self.ball.x, self.ball.y
        bw, bh = self.ball.width, self.ball.height

        # putting every 
        corners = [
        (bx,       by),        
        (bx + bw,  by),        
        (bx,       by + bh),   
        (bx + bw,  by + bh)    
         ]   

        for px, py in corners:
            obj = self.window.get_object_at(px, py)
            if obj is None:
                continue
        
            if obj is self.ball:
                continue
        
            if obj is self.background:
                continue
        
            if obj is self.paddle:
                return 'paddle'
            
            if obj is self.label:
                return 'label'
            
            self.window.remove(obj)
            self.total_bricks -= 1 
            return 'brick'
        
        return None

        # Create a paddle
        # Center a filled ball in the graphical window
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        # Draw bricks
