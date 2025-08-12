"""
File: bouncing_ball.py
Name: Jeffrey Tseng
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# 常數設定
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# 全域變數
window = GWindow(800, 500, title='bouncing_ball.py')
window.background_color = 'white'
background = GRect(800, 500)
background.filled = True
background.fill_color = 'white'  # 改成你想要的顏色
background.color = 'white'       # 邊框顏色也改掉
window.add(background, 0, 0)
ball = GOval(SIZE, SIZE)
ball_count = 0          
is_moving = False  # 防止多次點擊
game_over = False

def main():
    global ball
    onmouseclicked(handle_click)
    ball.filled = True
    ball.color = 'black'
    ball.fill_color = 'black'
    window.add(ball, START_X, START_Y)

def handle_click(event):
    global is_moving, game_over, ball_count

    # 防止多個 while 同時運行
    if is_moving or game_over:  # 如果正在動或遊戲結束，忽略點擊
        return
    is_moving = True

    vx = VX
    vy = 0
    x = START_X
    y = START_Y

    while True:
        # 更新位置
        x += vx
        y += vy

        # 碰到左右牆反彈
        if x + SIZE > window.width:
            window.add(ball, START_X, START_Y)
            break

        # 碰到地板反彈
        if y + SIZE >= window.height:
            vy = -vy * REDUCE
            y = window.height - SIZE

        # 重力影響
        vy += GRAVITY

        # 更新畫面位置
        ball.move(vx, vy)

        pause(DELAY)


    is_moving = False  # 重置狀態，允許再次點擊

if __name__ == "__main__":
    main()

