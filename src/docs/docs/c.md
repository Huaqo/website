
# C

## Awesome links

- [GNU GCC Compiler ->](https://gcc.gnu.org/)
- [LLVM Compiler ->](https://llvm.org/)
- Libraries:
    - [raylib](../gamedev/raylib.md)
    - [raygui](../gamedev/raygui.md)

## Basics

```c
#include <stdio.h>

// Main Function
int main() {
    // Variable Declaration
    int a = 10;       // Integer
    float b = 20.5;   // Float
    char c = 'A';     // Character
    char str[] = "Hello World";  // String
    int d = 1;        // Boolean (no native bool type, using int)

    // Output
    printf("Hello, World!\n");
    return 0;
}
```

## Operators

```c
// Arithmetic
int sum = 1 + 2;      // Addition
int diff = 5 - 3;     // Subtraction
int prod = 2 * 3;     // Multiplication
float quot = 10 / 2;  // Division
int mod = 10 % 3;     // Modulus

// Assignment
int x = 10;
x += 5;  // x = x + 5
x -= 3;  // x = x - 3
x *= 2;  // x = x * 2
x /= 2;  // x = x / 2

// Comparison
int isEqual = (1 == 1);      // true
int isNotEqual = (1 != 2);   // true
int isGreater = (5 > 3);     // true
int isLesser = (3 < 5);      // true
```

## Control Structures

```c
// Conditional Statements
if (a > b) {
    // code if true
} else if (a == b) {
    // code if equal
} else {
    // code if false
}

// Switch Statement
switch (a) {
    case 1:
        // code for case 1
        break;
    case 2:
        // code for case 2
        break;
    default:
        // default code
}

// Loops
// For Loop
for (int i = 0; i < 5; i++) {
    // code
}

// While Loop
while (a < 10) {
    // code
    a++;
}

// Do-While Loop
do {
    // code
    a++;
} while (a < 10);
```

## Functions

```c
// Function Definition
int add(int x, int y) {
    return x + y;
}

// Function Call
int result = add(2, 3);
```

## Arrays

```c
int arr[3] = {1, 2, 3};

// Access Elements
int firstElement = arr[0];

// Loop through Array
for (int i = 0; i < 3; i++) {
    printf("%d\n", arr[i]);
}
```

## Strings

```c
#include <string.h>
#include <stdio.h>

char str[] = "Hello, World!";

// String Length
int length = strlen(str);  // Length

// String Copy
char str2[20];
strcpy(str2, str);

// String Concatenation
char greeting[50] = "Hello, ";
strcat(greeting, "World!");

// String Comparison
int result = strcmp(str, "Hello, World!");
```

## Pointers

```c
int a = 10;
int *p = &a;

// Accessing Value using Pointer
int value = *p;

// Modifying Value using Pointer
*p = 20;
```

## Structures

```c
#include <stdio.h>

// Structure Definition
struct Person {
    char name[50];
    int age;
};

// Structure Variable
struct Person person1 = {"John", 30};

// Accessing Structure Members
printf("Name: %s\n", person1.name);
printf("Age: %d\n", person1.age);
```

## File I/O

```c
#include <stdio.h>

// Write to File
FILE *outFile = fopen("file.txt", "w");
if (outFile != NULL) {
    fprintf(outFile, "Hello, World!\n");
    fclose(outFile);
}

// Read from File
FILE *inFile = fopen("file.txt", "r");
if (inFile != NULL) {
    char content[100];
    while (fgets(content, 100, inFile) != NULL) {
        printf("%s", content);
    }
    fclose(inFile);
}
```

## Dynamic Memory Allocation

```c
#include <stdlib.h>

// Allocating Memory
int *arr = (int *)malloc(5 * sizeof(int));

// Freeing Memory
free(arr);
```

## Preprocessor Directives

```c
// Macro Definition
#define PI 3.14159

// Include Header Files
#include <stdio.h>
#include <stdlib.h>
```

## Standard Library Functions

```c
#include <stdio.h>
#include <stdlib.h>

// String to Integer
int num = atoi("123");

// Integer to String
char str[10];
sprintf(str, "%d", 123);
```

## Error Handling

```c
#include <stdio.h>
#include <errno.h>
#include <string.h>

FILE *file = fopen("nonexistent.txt", "r");
if (file == NULL) {
    printf("Error opening file: %s\n", strerror(errno));
}
```
