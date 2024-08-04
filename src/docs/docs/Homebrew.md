
# Homebrew

## Installation

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Basic Commands

```bash
brew update                      # Update Homebrew and all formulae
brew upgrade                     # Upgrade all installed formulae
brew cleanup                     # Remove old versions of installed formulae
brew doctor                      # Check your system for potential problems
brew list                        # List all installed formulae
brew info <formula>              # Show information about a formula
brew home <formula>              # Open the homepage of a formula
```

## Installing and Uninstalling Formulae

```bash
brew install <formula>           # Install a formula
brew install <formula>@<version> # Install a specific version of a formula
brew uninstall <formula>         # Uninstall a formula
brew reinstall <formula>         # Reinstall a formula
```

## Searching for Formulae

```bash
brew search <text>               # Search for formulae
brew search /<regex>/            # Search for formulae using a regular expression
brew search --desc <text>        # Search for formulae by description
```

## Using Casks

```bash
brew install --cask <cask>       # Install a cask
brew uninstall --cask <cask>     # Uninstall a cask
brew list --cask                 # List all installed casks
brew info --cask <cask>          # Show information about a cask
brew home --cask <cask>          # Open the homepage of a cask
```

## Services

```bash
brew services list               # List all services
brew services start <formula>    # Start a service
brew services stop <formula>     # Stop a service
brew services restart <formula>  # Restart a service
brew services run <formula>      # Run a service without starting at login
brew services cleanup            # Remove unused service configuration
```

## Taps

```bash
brew tap                         # List all tapped repositories
brew tap <user/repo>             # Tap a repository
brew untap <user/repo>           # Untap a repository
```

## Miscellaneous

```bash
brew config                      # Show Homebrew and system configuration
brew doctor                      # Check your system for potential problems
brew analytics                   # Show Homebrew analytics status
brew analytics off               # Turn off Homebrew analytics
brew analytics on                # Turn on Homebrew analytics
```

