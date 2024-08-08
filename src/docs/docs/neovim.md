
# Neovim

## Awesome links

- [Documentation ->](https://neovim.io/doc/)

## Basic Commands

```plaintext
:q      Quit
:q!     Quit without saving
:w      Save
:wq     Save and quit
:x      Save and quit (same as :wq)
:w!     Force save
:wq!    Force save and quit
:e      Edit a file
:e!     Edit a file (discard unsaved changes)
```

## Navigation

```plaintext
h       Move left
j       Move down
k       Move up
l       Move right

0       Move to the beginning of the line
^       Move to the first non-blank character of the line
$       Move to the end of the line

gg      Go to the first line of the file
G       Go to the last line of the file
nG      Go to the nth line of the file

w       Move to the next word
b       Move to the previous word
e       Move to the end of the word
```

## Insertion Modes

```plaintext
i       Insert before the cursor
I       Insert at the beginning of the line
a       Insert after the cursor
A       Insert at the end of the line
o       Open a new line below the current line
O       Open a new line above the current line
```

## Editing

```plaintext
x       Delete the character under the cursor
X       Delete the character before the cursor

dw      Delete word
dd      Delete line
D       Delete from cursor to the end of the line

u       Undo
Ctrl+r  Redo

yy      Yank (copy) a line
yw      Yank (copy) a word
p       Paste after the cursor
P       Paste before the cursor

r       Replace the character under the cursor
R       Enter replace mode
cw      Change word
cc      Change line
C       Change from cursor to the end of the line
```

## Visual Mode

```plaintext
v       Start visual mode (character-wise)
V       Start visual mode (line-wise)
Ctrl+v  Start visual block mode

y       Yank (copy) selected text
d       Delete selected text
c       Change selected text
>       Indent selected text
<       Unindent selected text
```

## Searching

```plaintext
/pattern        Search for pattern
?pattern        Search for pattern backwards
n               Repeat search in the same direction
N               Repeat search in the opposite direction
*               Search for the word under the cursor
g*              Search for the partial word under the cursor

:%s/old/new/g   Replace all occurrences of old with new
:s/old/new/g    Replace all occurrences of old with new in the current line
```

## Buffers

```plaintext
:ls             List all buffers
:b <buffer>     Switch to buffer
:bd             Delete a buffer
:bn             Go to the next buffer
:bp             Go to the previous buffer
```

## Splits

```plaintext
:sp <file>      Horizontal split
:vsp <file>     Vertical split
Ctrl+w h        Move to the left split
Ctrl+w j        Move to the split below
Ctrl+w k        Move to the split above
Ctrl+w l        Move to the right split
Ctrl+w q        Quit a split
Ctrl+w o        Close all other splits
```

## Tabs

```plaintext
:tabnew <file>  Open a new tab
:tabnext        Go to the next tab
:tabprev        Go to the previous tab
:tabclose       Close the current tab
:tabs           List all tabs
```

## Miscellaneous

```plaintext
.               Repeat the last command
:!command       Execute external command
:help <command> Get help for command
:set number     Show line numbers
:set nonumber   Hide line numbers
:set relativenumber Show relative line numbers
:set norelativenumber Hide relative line numbers
```

## Plugin Management with Vim-Plug

```plaintext
call plug#begin('~/.config/nvim/plugged')
Plug 'plugin/name'
call plug#end()

:PlugInstall    Install plugins
:PlugUpdate     Update plugins
:PlugClean      Remove unused plugins
```
