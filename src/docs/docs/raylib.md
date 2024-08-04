
# Raylib

## Getting Started

### Installing raylib

Download and install raylib from the [official website](https://www.raylib.com/).

### Including raylib in Your Project

```c
#include "raylib.h"
```

### Initializing and Closing

```c
// Initialize the window
InitWindow(screenWidth, screenHeight, "Window Title");

// Set the target FPS
SetTargetFPS(60);

// Close the window and clean up resources
CloseWindow();
```

## Basic Structure

### Main Game Loop

```c
while (!WindowShouldClose())    // Detect window close button or ESC key
{
    // Update game state

    // Draw everything
    BeginDrawing();

    ClearBackground(RAYWHITE);

    // Drawing code goes here

    EndDrawing();
}
```

## Drawing Shapes

### Drawing a Rectangle

```c
DrawRectangle(x, y, width, height, color);
```

### Drawing a Circle

```c
DrawCircle(x, y, radius, color);
```

### Drawing a Line

```c
DrawLine(startX, startY, endX, endY, color);
```

## Handling Input

### Keyboard Input

```c
if (IsKeyDown(KEY_RIGHT)) 
{
    // Right arrow key is being held down
}

if (IsKeyPressed(KEY_SPACE)) 
{
    // Space key was just pressed
}
```

### Mouse Input

```c
Vector2 mousePosition = GetMousePosition();

if (IsMouseButtonDown(MOUSE_LEFT_BUTTON)) 
{
    // Left mouse button is being held down
}
```

## Working with Textures

### Loading a Texture

```c
Texture2D texture = LoadTexture("path/to/texture.png");
```

### Unloading a Texture

```c
UnloadTexture(texture);
```

### Drawing a Texture

```c
DrawTexture(texture, x, y, WHITE);
```

## Fonts and Text

### Loading a Font

```c
Font font = LoadFont("path/to/font.ttf");
```

### Unloading a Font

```c
UnloadFont(font);
```

### Drawing Text

```c
DrawText("Hello, raylib!", x, y, fontSize, color);
```

## Audio

### Initializing and Closing Audio Device

```c
InitAudioDevice();
CloseAudioDevice();
```

### Loading a Sound

```c
Sound sound = LoadSound("path/to/sound.wav");
```

### Unloading a Sound

```c
UnloadSound(sound);
```

### Playing a Sound

```c
PlaySound(sound);
```

### Loading and Playing Music

```c
Music music = LoadMusicStream("path/to/music.mp3");
PlayMusicStream(music);
```

## Collision Detection

### Checking for Rectangle Collision

```c
bool collision = CheckCollisionRecs(rect1, rect2);
```

### Checking for Circle Collision

```c
bool collision = CheckCollisionCircles(center1, radius1, center2, radius2);
```

## Advanced Drawing

### Drawing Textured Shapes

```c
DrawTexturePro(texture, sourceRec, destRec, origin, rotation, WHITE);
```

### Drawing Text with a Font

```c
DrawTextEx(font, "Hello, raylib!", position, fontSize, spacing, color);
```

## Utility Functions

### Getting Frame Time

```c
float deltaTime = GetFrameTime();
```

### Getting Random Values

```c
int randomValue = GetRandomValue(min, max);
```

## Example

### Complete Example Program

```c
#include "raylib.h"

int main(void)
{
    // Initialization
    const int screenWidth = 800;
    const int screenHeight = 450;

    InitWindow(screenWidth, screenHeight, "raylib [core] example - basic window");

    SetTargetFPS(60);

    // Main game loop
    while (!WindowShouldClose())
    {
        // Update

        // Draw
        BeginDrawing();

        ClearBackground(RAYWHITE);

        DrawText("Congrats! You created your first window!", 190, 200, 20, LIGHTGRAY);

        EndDrawing();
    }

    // De-Initialization
    CloseWindow();

    return 0;
}
```
