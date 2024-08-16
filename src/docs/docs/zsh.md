
# Zsh

For more details, refer to the [Zsh documentation](http://zsh.sourceforge.net/Doc/Release/zsh_toc.html).

## Basic Commands

### Zsh Basics
- **Start Zsh**: Just type `zsh` in your terminal.
- **Exit Zsh**: Type `exit` or `Ctrl+D`.

### Navigation
- **Change directory**: `cd /path/to/directory`
- **List files**: `ls`
- **Current directory**: `pwd`

### File Management
- **Copy file**: `cp source_file destination_file`
- **Move file**: `mv source_file destination_file`
- **Remove file**: `rm filename`
- **Remove empty directory**: `rmdir directory`
- **Remove full directory**: `rm -r directory`
- **Create directory**: `mkdir directory_name`

### Command History
- **Show command history**: `history`
- **Repeat last command**: `!!`
- **Repeat specific command**: `!n` (where `n` is the command number in history)

## Aliases and Functions

### Creating Aliases
```zsh
alias ll='ls -la'
alias gs='git status'
```

### Unalias
```zsh
unalias ll
```

### Defining Functions
```zsh
myfunc() {
    echo "This is a custom function!"
}
```

## Zsh Options

### Listing Options
- **List all options**: `setopt`
- **Disable an option**: `unsetopt option_name`
- **Enable an option**: `setopt option_name`

### Common Options
- **Case-insensitive tab completion**: `setopt NO_CASE_GLOB`
- **Auto cd**: `setopt AUTO_CD`

## Globbing

### Basic Globbing
- **Match any file**: `*`
- **Match specific extension**: `*.txt`
- **Match any single character**: `?`
- **Match character range**: `[a-z]`

### Extended Globbing
- **Enable extended globbing**: `setopt EXTENDED_GLOB`
- **Match zero or more characters**: `*(pattern)`
- **Match zero or one occurrence**: `?(pattern)`
- **Match one or more occurrences**: `+(pattern)`
- **Exclude a pattern**: `~(pattern)`

## Prompt Customization

### Basic Prompt Customization
```zsh
export PS1="%n@%m:%~$ "
```
- `%n`: Username
- `%m`: Hostname
- `%~`: Current directory

### Using `PROMPT` and `RPROMPT`
```zsh
PROMPT='%n@%m:%~$ '
RPROMPT='%T'  # Time on the right side
```

## Zsh Plugins and Themes

### Oh-My-Zsh
- **Install Oh-My-Zsh**: 
```sh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### Managing Plugins
- **List plugins**: 
```zsh
plugins=(git zsh-syntax-highlighting zsh-autosuggestions)
```
- **Reload Zsh configuration**: `source ~/.zshrc`

### Changing Themes
- **Set theme in `.zshrc`**:
```zsh
ZSH_THEME="agnoster"
```

## Autocompletion

### Enable Autocompletion
```zsh
autoload -U compinit
compinit
```

### Custom Autocompletions
```zsh
# Example: Git autocompletion
autoload -Uz compinit && compinit
autoload -Uz bashcompinit && bashcompinit
source /usr/share/bash-completion/completions/git
```

## Useful Keybindings

### Editing Shortcuts
- **Move to the beginning of the line**: `Ctrl + A`
- **Move to the end of the line**: `Ctrl + E`
- **Delete word before cursor**: `Ctrl + W`
- **Clear the screen**: `Ctrl + L`

### Command Navigation
- **Previous command**: `Ctrl + P` or `Up Arrow`
- **Next command**: `Ctrl + N` or `Down Arrow`
- **Search command history**: `Ctrl + R`

## Scripting with Zsh

### Simple Script Example
```zsh
#!/bin/zsh

echo "Hello, Zsh!"
for i in {1..5}; do
    echo "Iteration $i"
done
```

### Running the Script
```sh
chmod +x script_name.zsh
./script_name.zsh
```
