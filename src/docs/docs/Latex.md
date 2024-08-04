
# LaTex

## Document Structure

### Basic Structure

```latex
\documentclass{article}

\begin{document}

\title{Title of the Document}
\author{Author Name}
\date{\today}

\maketitle

\section{Introduction}
Your introduction text goes here.

\end{document}
```

### Preamble

```latex
\documentclass{article}

% Packages
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{hyperref}

% Custom Commands
\newcommand{\R}{\mathbb{R}}

\begin{document}
...
\end{document}
```

## Text Formatting

### Basic Text

```latex
\textbf{Bold text}

\textit{Italic text}

\underline{Underlined text}
```

### Lists

#### Unordered List

```latex
\begin{itemize}
    \item Item 1
    \item Item 2
    \item Item 3
\end{itemize}
```

#### Ordered List

```latex
\begin{enumerate}
    \item First item
    \item Second item
    \item Third item
\end{enumerate}
```

### Tables

```latex
\begin{tabular}{|c|c|c|}
    \hline
    Column 1 & Column 2 & Column 3 \\
    \hline
    Data 1 & Data 2 & Data 3 \\
    Data 4 & Data 5 & Data 6 \\
    \hline
\end{tabular}
```

## Mathematics

### Inline Math

```latex
This is inline math: $a^2 + b^2 = c^2$.
```

### Display Math

```latex
\begin{equation}
    E = mc^2
\end{equation}
```

### Common Symbols

```latex
\( \alpha, \beta, \gamma, \pi, \Sigma, \sum, \int, \infty \)
```

## Figures

### Including Graphics

```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=0.5\textwidth]{path/to/image.png}
    \caption{Caption for the figure.}
    \label{fig:label}
\end{figure}
```

## References

### Bibliography

```latex
\begin{thebibliography}{9}
    \bibitem{ref1}
    Author, \emph{Title}, Journal, Year.
\end{thebibliography}
```

### Hyperlinks

```latex
\href{https://www.example.com}{Example Link}
```

## Advanced Topics

### Custom Commands

```latex
\newcommand{\mycommand}[1]{This is my command: #1}
```

### Environments

```latex
\newenvironment{myenv}[1][default]{%
  \begin{center}
  \bfseries #1
}{%
  \end{center}
}
```

## Example Document

### Complete Example

```latex
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{hyperref}

\title{Example Document}
\author{Author Name}
\date{\today}

\begin{document}

\maketitle

\section{Introduction}
This is an example document.

\section{Mathematics}
Here is an inline equation: $E = mc^2$.

Here is a displayed equation:
\begin{equation}
    a^2 + b^2 = c^2
\end{equation}

\section{Figures}
\begin{figure}[h]
    \centering
    \includegraphics[width=0.5\textwidth]{example-image.png}
    \caption{Example image}
    \label{fig:example}
\end{figure}

\section{Tables}
\begin{tabular}{|c|c|c|}
    \hline
    Column 1 & Column 2 & Column 3 \\
    \hline
    Data 1 & Data 2 & Data 3 \\
    Data 4 & Data 5 & Data 6 \\
    \hline
\end{tabular}

\section{Lists}
\begin{itemize}
    \item Item 1
    \item Item 2
    \item Item 3
\end{itemize}

\section{Bibliography}
\begin{thebibliography}{9}
    \bibitem{ref1}
    Author, \emph{Title}, Journal, Year.
\end{thebibliography}

\end{document}
```
