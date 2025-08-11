"""
File: 
Name:
----------------------
"""
"""
Title: Hogwarts at Night    

Harry Potter is my favoirite book series, and I love the Hogwarts castle at night.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon
from campy.graphics.gwindow import GWindow

def main():
    window = GWindow(800, 600, title="Hogwarts at Night")

    ### --- 建立所有圖形物件（先不要加到 window） ---

    # --- 背景 ---
    sky = GRect(800, 600)
    sky.filled = True
    sky.fill_color = 'midnightblue'

    moon = GOval(100, 100)
    moon.filled = True
    moon.fill_color = 'lightyellow'
    moon.x = 620
    moon.y = 70

    stars = []
    star_positions = [(100, 100), (200, 50), (300, 150), (500, 40), (700, 200), (650, 150), (150, 200)]
    for x, y in star_positions:
        s = GOval(4, 4)
        s.filled = True
        s.fill_color = 'white'
        s.x = x
        s.y = y
        stars.append(s)

    # --- 湖泊與草地 ---
    lake = GRect(800, 150)
    lake.filled = True
    lake.fill_color = 'steelblue'
    lake.x = 0
    lake.y = 450

    grass = GRect(800, 100)
    grass.filled = True
    grass.fill_color = 'darkgreen'
    grass.x = 0
    grass.y = 400

    # --- 左塔 ---
    left_tower = GPolygon()
    left_tower.add_vertex((250, 400))
    left_tower.add_vertex((280, 300))
    left_tower.add_vertex((310, 400))
    left_tower.filled = True
    left_tower.fill_color = 'peru'

    left_windows = []
    for y in [320, 350, 380]:
        w = GRect(10, 15)
        w.filled = True
        w.fill_color = 'gold'
        w.x = 275
        w.y = y
        left_windows.append(w)

    # --- 右塔 ---
    right_tower = GPolygon()
    right_tower.add_vertex((470, 400))
    right_tower.add_vertex((500, 300))
    right_tower.add_vertex((530, 400))
    right_tower.filled = True
    right_tower.fill_color = 'peru'

    right_windows = []
    for y in [320, 350, 380]:
        w = GRect(10, 15)
        w.filled = True
        w.fill_color = 'gold'
        w.x = 495
        w.y = y
        right_windows.append(w)

    # --- 城牆 ---
    wall = GRect(280, 50)
    wall.filled = True
    wall.fill_color = 'sienna'
    wall.x = 250
    wall.y = 400

    wall_windows = []
    for x in range(260, 500, 30):
        w = GRect(10, 20)
        w.filled = True
        w.fill_color = 'gold'
        w.x = x
        w.y = 415
        wall_windows.append(w)

    # --- 主塔（最後才加） ---
    main_tower = GPolygon()
    main_tower.add_vertex((350, 400))
    main_tower.add_vertex((390, 250))
    main_tower.add_vertex((430, 400))
    main_tower.filled = True
    main_tower.fill_color = 'saddlebrown'

    main_windows = []
    for y in [280, 310, 340, 370]:
        w = GRect(12, 18)
        w.filled = True
        w.fill_color = 'gold'
        w.x = 388
        w.y = y
        main_windows.append(w)

    # --- 旗幟 ---
    flag = GPolygon()
    flag.add_vertex((500, 300))
    flag.add_vertex((530, 310))
    flag.add_vertex((500, 320))
    flag.filled = True
    flag.fill_color = 'crimson'


    ### --- 統一加入 window（順序 = 從後到前） ---

    window.add(sky)
    window.add(moon)
    for star in stars:
        window.add(star)
    window.add(lake)
    window.add(grass)

    window.add(left_tower)
    for w in left_windows:
        window.add(w)

    window.add(right_tower)
    for w in right_windows:
        window.add(w)

    window.add(wall)
    for w in wall_windows:
        window.add(w)

    window.add(main_tower)
    for w in main_windows:
        window.add(w)

    window.add(flag)

if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()