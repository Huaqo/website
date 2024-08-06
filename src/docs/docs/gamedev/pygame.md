
# Pygame

## Awesome links

- [Python](../languages/python.md)
- [Documentation ->](https://www.pygame.org/docs/)

## Getting Started

### Installing Pygame

```bash
pip install pygame
```

### Importing Pygame

```python
import pygame
from pygame.locals import *
```

### Initializing and Quitting

```python
# Initialize Pygame
pygame.init()

# Quit Pygame
pygame.quit()
```

## Creating a Game Window

### Setting Up the Display

```python
# Set up the game window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Title")
```

### Main Game Loop

```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Update game state

    # Draw everything
    pygame.display.update()

pygame.quit()
```

## Drawing Shapes

### Drawing a Rectangle

```python
rect = pygame.Rect(x, y, width, height)
pygame.draw.rect(screen, (255, 0, 0), rect)
```

### Drawing a Circle

```python
pygame.draw.circle(screen, (0, 255, 0), (x, y), radius)
```

### Drawing a Line

```python
pygame.draw.line(screen, (0, 0, 255), (start_x, start_y), (end_x, end_y), width)
```

## Handling Events

### Event Types

```python
for event in pygame.event.get():
    if event.type == QUIT:
        running = False
    elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            running = False
    elif event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
            print("Left mouse button clicked at", event.pos)
```

## Working with Surfaces

### Creating a Surface

```python
surface = pygame.Surface((width, height))
```

### Blitting a Surface

```python
screen.blit(surface, (x, y))
```

## Loading and Displaying Images

### Loading an Image

```python
image = pygame.image.load("path/to/image.png")
```

### Displaying an Image

```python
screen.blit(image, (x, y))
```

## Playing Sounds

### Loading a Sound

```python
sound = pygame.mixer.Sound("path/to/sound.wav")
```

### Playing a Sound

```python
sound.play()
```

### Loading and Playing Background Music

```python
pygame.mixer.music.load("path/to/music.mp3")
pygame.mixer.music.play(-1)  # -1 means loop indefinitely
```

## Handling Keyboard Input

### Checking Key States

```python
keys = pygame.key.get_pressed()
if keys[K_LEFT]:
    print("Left arrow key is pressed")
if keys[K_RIGHT]:
    print("Right arrow key is pressed")
```

## Handling Mouse Input

### Getting Mouse Position

```python
mouse_pos = pygame.mouse.get_pos()
print(mouse_pos)
```

### Checking Mouse Buttons

```python
mouse_buttons = pygame.mouse.get_pressed()
if mouse_buttons[0]:  # Left mouse button
    print("Left mouse button is pressed")
```

## Fonts and Text

### Creating a Font

```python
font = pygame.font.Font(None, 36)  # None for default font, 36 for font size
```

### Rendering Text

```python
text = font.render("Hello, Pygame!", True, (255, 255, 255))  # True for antialiasing
screen.blit(text, (x, y))
```

## Setting Up the Clock

### Creating a Clock

```python
clock = pygame.time.Clock()
```

### Limiting the Frame Rate

```python
clock.tick(60)  # Limit to 60 frames per second
```
