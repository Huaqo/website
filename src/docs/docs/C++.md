
# C++

## Basics

```cpp
#include <iostream>
using namespace std;

// Main Function
int main() {
    // Variable Declaration
    int a = 10;       // Integer
    double b = 20.5;  // Double
    char c = 'A';     // Character
    string str = "Hello World";  // String
    bool d = true;    // Boolean

    // Output
    cout << "Hello, World!" << endl;
    return 0;
}
```

## Operators

```cpp
// Arithmetic
int sum = 1 + 2;      // Addition
int diff = 5 - 3;     // Subtraction
int prod = 2 * 3;     // Multiplication
double quot = 10 / 2; // Division
int mod = 10 % 3;     // Modulus

// Assignment
int x = 10;
x += 5;  // x = x + 5
x -= 3;  // x = x - 3
x *= 2;  // x = x * 2
x /= 2;  // x = x / 2

// Comparison
bool isEqual = (1 == 1);      // true
bool isNotEqual = (1 != 2);   // true
bool isGreater = (5 > 3);     // true
bool isLesser = (3 < 5);      // true
```

## Control Structures

```cpp
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

```cpp
// Function Definition
int add(int x, int y) {
    return x + y;
}

// Function Call
int result = add(2, 3);
```

## Arrays

```cpp
int arr[3] = {1, 2, 3};

// Access Elements
int firstElement = arr[0];

// Loop through Array
for (int i = 0; i < 3; i++) {
    cout << arr[i] << endl;
}
```

## Vectors (STL)

```cpp
#include <vector>
#include <iostream>
using namespace std;

vector<int> vec = {1, 2, 3};

// Access Elements
int firstElement = vec[0];

// Add Elements
vec.push_back(4);

// Remove Elements
vec.pop_back();

// Loop through Vector
for (int i = 0; i < vec.size(); i++) {
    cout << vec[i] << endl;
}
```

## Strings

```cpp
#include <string>
#include <iostream>
using namespace std;

string str = "Hello, World!";

// String Methods
int length = str.length();       // Length
string upper = str;              // Uppercase
transform(upper.begin(), upper.end(), upper.begin(), ::toupper);
string lower = str;              // Lowercase
transform(lower.begin(), lower.end(), lower.begin(), ::tolower);
string substring = str.substr(0, 5);  // Substring

// String Concatenation
string greeting = "Hello, " + str + "!";
```

## File I/O

```cpp
#include <fstream>
#include <iostream>
using namespace std;

// Write to File
ofstream outFile("file.txt");
outFile << "Hello, World!" << endl;
outFile.close();

// Read from File
ifstream inFile("file.txt");
string content;
getline(inFile, content);
inFile.close();
```

## Classes

```cpp
// Class Definition
class Person {
public:
    string name;
    int age;

    Person(string n, int a) {
        name = n;
        age = a;
    }

    void greet() {
        cout << "Hello, " << name << "!" << endl;
    }
};

// Inheritance
class Student : public Person {
public:
    string grade;

    Student(string n, int a, string g) : Person(n, a) {
        grade = g;
    }

    void study() {
        cout << name << " is studying." << endl;
    }
};

// Create Object
Student student("John", 20, "A");
student.greet();
student.study();
```

## Exception Handling

```cpp
try {
    // code that might throw an exception
    if (b == 0) {
        throw runtime_error("Cannot divide by zero");
    }
    int result = a / b;
} catch (const runtime_error& e) {
    // code that runs if exception occurs
    cout << "Error: " << e.what() << endl;
} catch (...) {
    // code that runs for any other exception
    cout << "An unknown error occurred." << endl;
}
```

## Templates

```cpp
// Function Template
template <typename T>
T add(T x, T y) {
    return x + y;
}

int resultInt = add<int>(2, 3);  // 5
double resultDouble = add<double>(2.5, 3.5);  // 6.0

// Class Template
template <typename T>
class Box {
public:
    T value;
    Box(T v) : value(v) {}
    T getValue() {
        return value;
    }
};

Box<int> intBox(123);
Box<string> strBox("Hello");
```

## Standard Library Functions

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> vec = {1, 2, 3, 4, 5};

// Find Element
auto it = find(vec.begin(), vec.end(), 3);

// Sort Elements
sort(vec.begin(), vec.end());

// Lambda Function
auto add = [](int x, int y) { return x + y; };
int result = add(2, 3);  // 5
```
