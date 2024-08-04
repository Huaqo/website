
# HTML

## Basic Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

## Text Formatting

```html
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>

<p>This is a paragraph.</p>
<strong>Bold text</strong>
<em>Italic text</em>
<mark>Highlighted text</mark>
<del>Deleted text</del>
<ins>Inserted text</ins>
<sub>Subscript text</sub>
<sup>Superscript text</sup>
```

## Links

```html
<a href="https://www.example.com">This is a link</a>
<a href="https://www.example.com" target="_blank">Open link in new tab</a>
<a href="#section1">Jump to section 1</a>
```

## Images

```html
<img src="image.jpg" alt="Description of image" width="500" height="600">
<img src="image.jpg" alt="Description of image" style="width:100%;">
```

## Lists

### Unordered List

```html
<ul>
    <li>List item 1</li>
    <li>List item 2</li>
    <li>List item 3</li>
</ul>
```

### Ordered List

```html
<ol>
    <li>List item 1</li>
    <li>List item 2</li>
    <li>List item 3</li>
</ol>
```

### Description List

```html
<dl>
    <dt>Term 1</dt>
    <dd>Description 1</dd>
    <dt>Term 2</dt>
    <dd>Description 2</dd>
</dl>
```

## Tables

```html
<table>
    <tr>
        <th>Header 1</th>
        <th>Header 2</th>
    </tr>
    <tr>
        <td>Data 1</td>
        <td>Data 2</td>
    </tr>
    <tr>
        <td>Data 3</td>
        <td>Data 4</td>
    </tr>
</table>
```

## Forms

```html
<form action="/submit" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email">
    
    <input type="submit" value="Submit">
</form>
```

## Input Types

```html
<input type="text" placeholder="Text input">
<input type="password" placeholder="Password input">
<input type="email" placeholder="Email input">
<input type="number" placeholder="Number input">
<input type="date">
<input type="color">
<input type="checkbox"> Checkbox
<input type="radio"> Radio
<input type="range" min="0" max="100">
<input type="file">
```

## Multimedia

### Audio

```html
<audio controls>
    <source src="audio.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
</audio>
```

### Video

```html
<video width="320" height="240" controls>
    <source src="video.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>
```

## Semantic Elements

```html
<header>
    <h1>Page Title</h1>
</header>
<nav>
    <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#contact">Contact</a></li>
    </ul>
</nav>
<main>
    <article>
        <h2>Article Title</h2>
        <p>Article content...</p>
    </article>
</main>
<footer>
    <p>Footer content...</p>
</footer>
```

## Meta Tags

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Description of the webpage">
<meta name="keywords" content="HTML, CSS, JavaScript">
<meta name="author" content="Author Name">
```

## Character Entities

```html
&lt;   <!-- less than -->
&gt;   <!-- greater than -->
&amp;  <!-- ampersand -->
&quot; <!-- double quote -->
&apos; <!-- single quote -->
```
