
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

## Undoing Changes

```bash
git checkout -- <file>       # Discard changes in working directory
git reset <file>             # Unstage a file
git reset --hard             # Reset the working directory and staging area to the last commit
git reset --hard <commit>    # Reset the working directory and staging area to a specific commit
git revert <commit>          # Create a new commit that undoes a specific commit
```
