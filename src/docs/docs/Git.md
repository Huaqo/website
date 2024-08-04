
# Git

## Configuration

```bash
git config --global user.name "Your Name"         # Set the global username for commits
git config --global user.email "you@example.com"  # Set the global email for commits
git config --global core.editor "vim"             # Set the default editor for Git
git config --global merge.tool "vimdiff"          # Set the default merge tool for Git
```

## Getting Started

```bash
git init                     # Initialize a new Git repository
git clone <repo>             # Clone an existing repository
```

## Basic Commands

```bash
git status                   # Show the status of the working directory
git add <file>               # Add a file to the staging area
git add .                    # Add all changes to the staging area
git commit -m "message"      # Commit changes with a message
git commit -am "message"     # Add and commit tracked files with a message
git diff                     # Show changes between working directory and staging area
git diff --staged            # Show changes between staging area and last commit
git log                      # Show commit history
git log --oneline            # Show commit history in one line per commit
git blame <file>             # Show who last modified each line of a file
git show <commit>            # Show details of a specific commit
```

## Branching and Merging

```bash
git branch                   # List branches
git branch <branch>          # Create a new branch
git checkout <branch>        # Switch to a branch
git checkout -b <branch>     # Create and switch to a new branch
git merge <branch>           # Merge a branch into the current branch
git branch -d <branch>       # Delete a branch
git branch -D <branch>       # Force delete a branch
git log --graph --oneline --all  # Show branch and merge history
```

## Remote Repositories

```bash
git remote -v                # List remote repositories
git remote add <name> <url>  # Add a new remote repository
git fetch <remote>           # Fetch changes from a remote repository
git pull <remote> <branch>   # Pull changes from a remote branch
git push <remote> <branch>   # Push changes to a remote branch
git remote rm <name>         # Remove a remote repository
```

## Stashing

```bash
git stash                    # Stash changes in a dirty working directory
git stash list               # List stashed changes
git stash apply              # Apply the latest stash
git stash apply stash@{n}    # Apply a specific stash
git stash drop               # Drop the latest stash
git stash drop stash@{n}     # Drop a specific stash
git stash pop                # Apply and drop the latest stash
git stash pop stash@{n}      # Apply and drop a specific stash
```

## Undoing Changes

```bash
git checkout -- <file>       # Discard changes in working directory
git reset <file>             # Unstage a file
git reset --hard             # Reset the working directory and staging area to the last commit
git reset --hard <commit>    # Reset the working directory and staging area to a specific commit
git revert <commit>          # Create a new commit that undoes a specific commit
```

## Tagging

```bash
git tag                      # List tags
git tag <tag>                # Create a new tag
git tag -a <tag> -m "message"  # Create an annotated tag
git show <tag>               # Show details of a tag
git push <remote> <tag>      # Push a tag to a remote repository
git push <remote> --tags     # Push all tags to a remote repository
git tag -d <tag>             # Delete a tag
git push <remote> :refs/tags/<tag>  # Delete a remote tag
```

## Aliases

```bash
git config --global alias.co checkout     # Create an alias for checkout
git config --global alias.br branch       # Create an alias for branch
git config --global alias.ci commit       # Create an alias for commit
git config --global alias.st status       # Create an alias for status
```
