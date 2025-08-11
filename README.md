# SC101

# SC101 — StanCode: Build Four Python Projects
## Summary
I completed four core projects in **StanCode SC101**, focusing on Python fundamentals and event-driven graphics with `campy`.  
These projects helped me practice clean structure, collision logic, file parsing/visualization, and user interaction.  
The repo includes only **my own code**; course materials are not uploaded.

### my_project
- Includes: my Python source code for the four projects
- Excludes: original problem statements, datasets that are not public, and any staff-provided solutions
- Environment: Python 3.x, `campy` (graphics), standard library

---
## Projects
### 1) My Drawing
- A small creative scene using `campy` shapes and layering.
- Highlights: constants for sizes/colors, helper functions for components.
- Demo: *(add screenshot)*

### 2) Bouncing Ball 
- A object oriented Project with buncing ball Scene
  
### 3) Breakout
- A classic brick breaker game (paddle, ball, bricks, lives).
- Highlights: animation loop, four-corner collision checks, state reset on life loss.
- Demo: *(add GIF/screenshot)*

### 4) Hangman
- Console word-guessing game with duplicate-guess protection.
- Highlights: set/dict usage, input validation, clean game loop.
- Demo: *(add screenshot)*

### 5) Baby Names (`babygraphics.py`)
- Visualizes name popularity by decade.
- Highlights: file parsing → dict of dicts, rank→Y mapping (cap at 1000), multiple names overlay.
- Demo: *(add screenshot)*



---

## How to Run
```bash
# Clone
git clone https://github.com/your-username/sc101-projects.git
cd sc101-projects

# (Optional) create venv
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install campy

# Run a project
python breakout.py      # or hangman.py / babygraphics.py / my_drawing.py
