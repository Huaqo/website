
# CSS

## Awesome links

- [Specification ->](https://www.w3.org/Style/CSS/specs.en.html)
- [CodePen ->](https://codepen.io/): social development environment for front-end designers and developers.
- Framworks:
    - [Bootstrap ->](https://getbootstrap.com/)
    - [Bulma ->](https://bulma.io/)
    - [TailwindCSS ->](https://tailwindcss.com/)

## Basic Syntax

```css
selector {
    property: value;
}
```

## Selectors

### Type Selector

```css
p {
    color: blue;
}
```

### Class Selector

```css
.classname {
    color: red;
}
```

### ID Selector

```css
#idname {
    color: green;
}
```

### Attribute Selector

```css
input[type="text"] {
    background-color: yellow;
}
```

### Descendant Selector

```css
div p {
    color: purple;
}
```

### Child Selector

```css
div > p {
    color: orange;
}
```

### Adjacent Sibling Selector

```css
h1 + p {
    color: pink;
}
```

### General Sibling Selector

```css
h1 ~ p {
    color: brown;
}
```

### Pseudo-class Selector

```css
a:hover {
    color: red;
}
```

### Pseudo-element Selector

```css
p::first-line {
    font-weight: bold;
}
```

## Colors

### Named Colors

```css
p {
    color: red;
}
```

### Hex Colors

```css
p {
    color: #ff0000;
}
```

### RGB Colors

```css
p {
    color: rgb(255, 0, 0);
}
```

### RGBA Colors

```css
p {
    color: rgba(255, 0, 0, 0.5);
}
```

### HSL Colors

```css
p {
    color: hsl(0, 100%, 50%);
}
```

### HSLA Colors

```css
p {
    color: hsla(0, 100%, 50%, 0.5);
}
```

## Text

### Text Color

```css
p {
    color: blue;
}
```

### Text Alignment

```css
p {
    text-align: center;
}
```

### Text Decoration

```css
p {
    text-decoration: underline;
}
```

### Text Transform

```css
p {
    text-transform: uppercase;
}
```

### Text Indentation

```css
p {
    text-indent: 20px;
}
```

### Line Height

```css
p {
    line-height: 1.5;
}
```

### Letter Spacing

```css
p {
    letter-spacing: 2px;
}
```

## Fonts

### Font Family

```css
p {
    font-family: 'Arial', sans-serif;
}
```

### Font Size

```css
p {
    font-size: 16px;
}
```

### Font Style

```css
p {
    font-style: italic;
}
```

### Font Weight

```css
p {
    font-weight: bold;
}
```

## Box Model

### Width and Height

```css
div {
    width: 100px;
    height: 100px;
}
```

### Padding

```css
div {
    padding: 10px;
}
```

### Border

```css
div {
    border: 1px solid black;
}
```

### Margin

```css
div {
    margin: 10px;
}
```

### Box Sizing

```css
div {
    box-sizing: border-box;
}
```

## Backgrounds

### Background Color

```css
div {
    background-color: lightblue;
}
```

### Background Image

```css
div {
    background-image: url('image.jpg');
}
```

### Background Repeat

```css
div {
    background-repeat: no-repeat;
}
```

### Background Size

```css
div {
    background-size: cover;
}
```

### Background Position

```css
div {
    background-position: center;
}
```

## Layout

### Display

```css
div {
    display: block;
}

span {
    display: inline;
}
```

### Position

```css
div {
    position: relative;
    top: 10px;
    left: 10px;
}
```

### Z-index

```css
div {
    position: absolute;
    z-index: 10;
}
```

### Float

```css
div {
    float: left;
}
```

### Clear

```css
div {
    clear: both;
}
```

## Flexbox

### Container

```css
.container {
    display: flex;
    justify-content: center;
    align-items: center;
}
```

### Item

```css
.item {
    flex: 1;
}
```

## Grid

### Container

```css
.container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 10px;
}
```

### Item

```css
.item {
    grid-column: span 2;
}
```

## Transitions

```css
div {
    transition: background-color 0.5s ease;
}

div:hover {
    background-color: lightgreen;
}
```

## Transforms

### Translate

```css
div {
    transform: translate(50px, 100px);
}
```

### Rotate

```css
div {
    transform: rotate(45deg);
}
```

### Scale

```css
div {
    transform: scale(1.5);
}
```

### Skew

```css
div {
    transform: skew(10deg, 20deg);
}
```

## Animations

### Keyframes

```css
@keyframes example {
    from {background-color: red;}
    to {background-color: yellow;}
}
```

### Animation

```css
div {
    animation-name: example;
    animation-duration: 4s;
}
```
