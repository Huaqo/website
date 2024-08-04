
# Tree

## Installation

```bash
# Install tree on macOS using Homebrew
brew install tree
```

## Basic Usage

```bash
# Display the tree structure of the current directory
tree

# Display the tree structure of a specific directory
tree /path/to/directory
```

## Display Options

```bash
# Display all files and directories, including hidden ones
tree -a

# Display only directories
tree -d

# Display the full path prefix for each file
tree -f

# Follow symbolic links
tree -l
```

## Sorting Options

```bash
# Sort files alphabetically (default)
tree -v

# Sort files by last modification time
tree -t

# Sort files by size
tree -s

# Reverse the order of the sort
tree -r
```

## Depth Options

```bash
# Limit the depth of the tree
tree -L 2

# Print the tree depth of each file and directory
tree -D
```

## File Options

```bash
# Print the size of each file in bytes
tree -s

# Print the size of each file in human-readable format
tree -h

# Print the date of the last modification time for each file
tree -p
```

## Output Options

```bash
# Print the tree structure without indentation lines
tree -i

# Print the tree structure with ANSI colorization
tree -C

# Print the tree structure with file permissions
tree -p

# Print the tree structure and include the report at the end
tree -v
```

## Example Commands

```bash
# Display the tree structure of the current directory, including hidden files, with human-readable sizes
tree -a -h

# Display only directories, with a depth of 2
tree -d -L 2

# Display the tree structure of a specific directory, sorted by modification time, with full paths
tree -t -f /path/to/directory

# Display the tree structure of the current directory, with ANSI colorization, and save to a file
tree -C > tree_structure.txt
```

## Help

```bash
# Show help for the tree command
tree --help
```