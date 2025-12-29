# Pygame Dropdown Menu

A simple dropdown menu module built from scratch for Pygame.

I created this because I couldn’t find a clean, reusable dropdown
menu solution for Pygame.

## Features
- Hover to open dropdown
- Select an option
- Custom colors and font size
- Lightweight and dependency-free

## Installation
Just copy `dropdown.py` into your project.

## Usage

```python
from dropdown import Dropdown

dropdown = Dropdown(
    x=100,
    y=100,
    btn_width=100,
    btn_height=50,
    names=["Start", "Options", "Quit"]
)

# inside game loop
dropdown.show(screen)

for btn in dropdown.content:
  if btn.clicked:
    # peform whatever action you want
    print("{btn.name} was clicked")  # placeholder code
