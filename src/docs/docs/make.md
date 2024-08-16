
# Makefile Cheat Sheet

For more details, refer to the [GNU Make documentation](https://www.gnu.org/software/make/manual/make.html).

## Basic Syntax

### Makefile Structure
A Makefile typically contains:

1. **Targets**: The goal you want to build (e.g., an executable or object file).
2. **Dependencies**: The files that the target depends on.
3. **Commands**: The shell commands to execute to build the target.

```make
target: dependencies
    command
```

### Example
```make
# Compile an object file
main.o: main.c
    gcc -c main.c

# Link object files to create an executable
main: main.o utils.o
    gcc -o main main.o utils.o

# Clean up
clean:
    rm -f main *.o
```

## Variables

### Defining Variables
Variables allow you to reuse values throughout your Makefile.

```make
CC = gcc
CFLAGS = -Wall -g

main: main.o utils.o
    $(CC) $(CFLAGS) -o main main.o utils.o
```

### Using Variables
Use `$(VAR_NAME)` to reference a variable.

```make
OBJS = main.o utils.o
CC = gcc
CFLAGS = -Wall -g

main: $(OBJS)
    $(CC) $(CFLAGS) -o main $(OBJS)
```

## Special Variables

### Commonly Used Special Variables
- `$@`: The file name of the target.
- `$<`: The first prerequisite (dependency).
- `$^`: The list of all prerequisites.

### Example
```make
main: main.o utils.o
    $(CC) -o $@ $^
```

## Pattern Rules

### Compiling Multiple Files
Use pattern rules to define how to build files of a particular type.

```make
# Pattern rule for object files
%.o: %.c
    $(CC) $(CFLAGS) -c $< -o $@
```

### Example with Multiple Files
```make
OBJS = main.o utils.o

main: $(OBJS)
    $(CC) $(CFLAGS) -o $@ $^

%.o: %.c
    $(CC) $(CFLAGS) -c $< -o $@
```

## Phony Targets

### Defining Phony Targets
Phony targets are not actual files; they are simply names for commands you want to run.

```make
.PHONY: clean

clean:
    rm -f main *.o
```

### Example with Phony Targets
```make
.PHONY: clean all

all: main

clean:
    rm -f main *.o
```

## Automatic Variables

### List of Automatic Variables
- `$@`: The target name.
- `$<`: The first prerequisite.
- `$^`: All prerequisites.

### Example Usage
```make
main: main.o utils.o
    $(CC) -o $@ $^

%.o: %.c
    $(CC) -c $< -o $@
```

## Conditionals

### Using Conditionals
Conditionals allow you to define variables or rules based on conditions.

```make
ifeq ($(CC),gcc)
    CFLAGS = -g
else
    CFLAGS = -O2
endif
```

### Example with Conditionals
```make
CC = gcc

ifeq ($(CC),gcc)
    CFLAGS = -Wall -g
else
    CFLAGS = -O2
endif

main: main.o utils.o
    $(CC) $(CFLAGS) -o main main.o utils.o
```

## Example Workflow

### Complete Example Makefile
```make
CC = gcc
CFLAGS = -Wall -g
OBJS = main.o utils.o

.PHONY: clean all

all: main

main: $(OBJS)
    $(CC) $(CFLAGS) -o $@ $^

%.o: %.c
    $(CC) $(CFLAGS) -c $< -o $@

clean:
    rm -f main *.o
```
