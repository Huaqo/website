
# Raygui

## Awesome links

- [C](../languages/c.md)
- [C++](../languages/cpp.md)
- [Documentation ->](https://github.com/raysan5/raygui)

## Getting Started

### Including raygui in Your Project

To use raygui, you need to include the `raygui.h` header file in your project.

```c
#include "raylib.h"
#define RAYGUI_IMPLEMENTATION
#include "raygui.h"
```

## Initializing and Closing

### Initializing raylib and raygui

```c
// Initialize the window
InitWindow(screenWidth, screenHeight, "Window Title");

// Set the target FPS
SetTargetFPS(60);
```

### Closing raylib and raygui

```c
// Close the window and clean up resources
CloseWindow();
```

## Creating a GUI

### Buttons

```c
if (GuiButton((Rectangle){ x, y, width, height }, "Button Text")) {
    // Button was clicked
}
```

### Labels

```c
GuiLabel((Rectangle){ x, y, width, height }, "Label Text");
```

### Checkboxes

```c
bool checked = false;
checked = GuiCheckBox((Rectangle){ x, y, width, height }, "Checkbox Text", checked);
```

### Textboxes

```c
char text[64] = "Default Text";
GuiTextBox((Rectangle){ x, y, width, height }, text, sizeof(text), true);
```

### Sliders

```c
float value = 50.0f;
value = GuiSlider((Rectangle){ x, y, width, height }, "Min", "Max", value, 0, 100);
```

### Dropdown Boxes

```c
int active = 0;
active = GuiDropdownBox((Rectangle){ x, y, width, height }, "Option1;Option2;Option3", &active, true);
```

### Spinners

```c
int value = 0;
value = GuiSpinner((Rectangle){ x, y, width, height }, &value, 0, 100, true);
```

### Scrollbars

```c
int value = 0;
value = GuiScrollBar((Rectangle){ x, y, width, height }, value, 0, 100);
```

## Styling the GUI

### Setting a Style

```c
GuiSetStyle(DEFAULT, TEXT_SIZE, 20);
GuiSetStyle(BUTTON, BORDER_WIDTH, 2);
```

### Loading a Custom Style

```c
GuiLoadStyle("path/to/style.rgs");
```

### Resetting to Default Style

```c
GuiLoadStyleDefault();
```

## Example

### Complete Example Program

```c
#include "raylib.h"
#define RAYGUI_IMPLEMENTATION
#include "raygui.h"

int main(void)
{
    // Initialization
    const int screenWidth = 800;
    const int screenHeight = 450;

    InitWindow(screenWidth, screenHeight, "raygui example - basic window");

    SetTargetFPS(60);

    bool checked = false;
    float sliderValue = 50.0f;
    char textBox[64] = "Edit me";

    // Main game loop
    while (!WindowShouldClose())
    {
        // Update

        // Draw
        BeginDrawing();

        ClearBackground(RAYWHITE);

        if (GuiButton((Rectangle){ 10, 10, 100, 30 }, "Button"))
        {
            // Button was clicked
        }

        GuiLabel((Rectangle){ 10, 50, 100, 30 }, "Label");

        checked = GuiCheckBox((Rectangle){ 10, 90, 20, 20 }, "Checkbox", checked);

        GuiTextBox((Rectangle){ 10, 130, 200, 30 }, textBox, sizeof(textBox), true);

        sliderValue = GuiSlider((Rectangle){ 10, 170, 200, 20 }, "Min", "Max", sliderValue, 0, 100);

        EndDrawing();
    }

    // De-Initialization
    CloseWindow();

    return 0;
}
```
