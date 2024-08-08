
# Tmux

## Awesome links

- [Wiki ->](https://github.com/tmux/tmux/wiki)

## Starting Tmux

```plaintext
tmux              Start a new tmux session
tmux new -s name  Start a new session with a name
tmux attach       Attach to the last session
tmux attach -t name  Attach to a session by name
tmux ls           List all sessions
tmux kill-session -t name  Kill a session by name
```

## Session Management

```plaintext
Ctrl+b s         List sessions
Ctrl+b $         Rename the current session
Ctrl+b d         Detach from the current session
```

## Window Management

```plaintext
Ctrl+b c         Create a new window
Ctrl+b ,         Rename the current window
Ctrl+b w         List windows
Ctrl+b n         Go to the next window
Ctrl+b p         Go to the previous window
Ctrl+b 0-9       Go to window number 0-9
Ctrl+b &         Kill the current window
```

## Pane Management

```plaintext
Ctrl+b %         Split the current pane vertically
Ctrl+b "         Split the current pane horizontally
Ctrl+b x         Kill the current pane
Ctrl+b o         Toggle between panes
Ctrl+b ;         Go to the last active pane
Ctrl+b q         Show pane numbers
Ctrl+b {         Move the current pane left
Ctrl+b }         Move the current pane right
Ctrl+b z         Toggle zoom for the current pane
```

## Resizing Panes

```plaintext
Ctrl+b Ctrl+arrow keys  Resize pane in the direction of the arrow key
```

## Copy Mode

```plaintext
Ctrl+b [         Enter copy mode
Space            Start selection
Enter            End selection and copy to buffer
Ctrl+b ]         Paste buffer
```

## Miscellaneous

```plaintext
Ctrl+b ?         List all keybindings
Ctrl+b d         Detach from the current session
Ctrl+b t         Show the time
```

## Configuring Tmux

Edit the tmux configuration file `~/.tmux.conf` to customize your tmux experience.

Example configuration:

```plaintext
# Set prefix to Ctrl+a
unbind C-b
set -g prefix C-a
bind C-a send-prefix

# Enable mouse support
set -g mouse on

# Start windows and panes at 1, not 0
set -g base-index 1
setw -g pane-base-index 1

# Reload configuration
bind r source-file ~/.tmux.conf \; display "Reloaded!"
```
