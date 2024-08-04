
# JavaScript

## Basics

```javascript
// Variable Declaration
let a = 10;      // Block-scoped
const b = 20;    // Block-scoped and constant
var c = 30;      // Function-scoped

// Data Types
let num = 100;               // Number
let str = "Hello World";     // String
let bool = true;             // Boolean
let arr = [1, 2, 3];         // Array
let obj = { key: "value" };  // Object
let func = function() {};    // Function
let undef;                   // Undefined
let nul = null;              // Null
```

## Operators

```javascript
// Arithmetic
let sum = 1 + 2;     // Addition
let diff = 5 - 3;    // Subtraction
let prod = 2 * 3;    // Multiplication
let quot = 10 / 2;   // Division
let mod = 10 % 3;    // Modulus

// Assignment
let x = 10;
x += 5;  // x = x + 5
x -= 3;  // x = x - 3
x *= 2;  // x = x * 2
x /= 2;  // x = x / 2

// Comparison
let isEqual = (1 == '1');     // true (loose equality)
let isStrictEqual = (1 === 1); // true (strict equality)
let isNotEqual = (1 != '1');   // false
let isGreater = (5 > 3);       // true
let isLesser = (3 < 5);        // true
```

## Control Structures

```javascript
// Conditional Statements
if (a > b) {
  // code if true
} else if (a === b) {
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
for (let i = 0; i < 5; i++) {
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

```javascript
// Function Declaration
function greet(name) {
  return "Hello, " + name;
}

// Function Expression
const greet = function(name) {
  return "Hello, " + name;
};

// Arrow Function
const greet = (name) => "Hello, " + name;

// Immediately Invoked Function Expression (IIFE)
(function() {
  // code
})();
```

## Arrays

```javascript
let fruits = ["Apple", "Banana", "Cherry"];

// Access Elements
let firstFruit = fruits[0];

// Array Methods
fruits.push("Orange");    // Add to end
fruits.pop();             // Remove from end
fruits.shift();           // Remove from start
fruits.unshift("Lemon");  // Add to start
let sliced = fruits.slice(1, 3);  // Slice array

// Loop through Array
fruits.forEach((fruit) => console.log(fruit));
```

## Objects

```javascript
let person = {
  name: "John",
  age: 30,
  greet: function() {
    return "Hello";
  }
};

// Access Properties
let name = person.name;  // Dot notation
let age = person['age']; // Bracket notation

// Add/Modify Properties
person.email = "john@example.com";

// Loop through Object
for (let key in person) {
  console.log(key + ": " + person[key]);
}
```

## DOM Manipulation

```javascript
// Select Elements
let element = document.getElementById("myId");
let elements = document.getElementsByClassName("myClass");
let elements = document.getElementsByTagName("div");
let element = document.querySelector(".myClass");
let elements = document.querySelectorAll(".myClass");

// Modify Content
element.innerHTML = "New Content";
element.textContent = "New Text";

// Modify Attributes
element.setAttribute("src", "image.jpg");
element.getAttribute("src");
element.removeAttribute("src");

// Modify Styles
element.style.color = "red";
element.style.fontSize = "20px";

// Event Listeners
element.addEventListener("click", function() {
  alert("Clicked!");
});
```

## Promises and Async/Await

```javascript
// Promises
let myPromise = new Promise((resolve, reject) => {
  let success = true;
  if (success) {
    resolve("Promise fulfilled");
  } else {
    reject("Promise rejected");
  }
});

myPromise.then((message) => {
  console.log(message);
}).catch((message) => {
  console.log(message);
});

// Async/Await
async function fetchData() {
  try {
    let response = await fetch("https://api.example.com/data");
    let data = await response.json();
    console.log(data);
  } catch (error) {
    console.log(error);
  }
}

fetchData();
```

## Classes

```javascript
// Class Declaration
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    return "Hello, " + this.name;
  }
}

// Inheritance
class Student extends Person {
  constructor(name, age, grade) {
    super(name, age);
    this.grade = grade;
  }

  study() {
    return this.name + " is studying.";
  }
}

let student = new Student("John", 20, "A");
console.log(student.greet());
console.log(student.study());
```

## Modules (ES6)

```javascript
// Export
export const name = "John";
export function greet() {
  return "Hello, " + name;
}

// Import
import { name, greet } from './module.js';
console.log(greet());
```
