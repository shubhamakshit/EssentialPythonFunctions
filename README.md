# EssentialPythonFunctions
one stop place for your python project


## Points
- [WinUtiks](#winutiks)
- [Process.py](#processpy)
- [PathOps.py](#pathopspy)


# WinUtiks

`win.py` is a Python script that provides a set of utility functions for Windows operating system. These functions allow you to interact with the system in various ways, such as changing the wallpaper, muting the audio, locking the screen, shutting down, restarting, logging off, and getting the IP address of the machine.

## Functions

- `change_wallpaper(path)`: Changes the desktop wallpaper to the image file specified by `path`. If the file does not exist, it prints an error message.
- `mute_audio()`: Mutes the system audio.
- `lock_screen()`: Locks the workstation.
- `shutdown()`: Shuts down the system after a delay of 1 second.
- `restart()`: Restarts the system after a delay of 1 second.
- `log_off()`: Logs off the current user.
- `get_ip_address()`: Returns the IP address of the machine.

## Dependencies
This script uses the following Python libraries:

- ctypes
- comtypes
- pycaw
- os
- socket

## Usage
To use the functions in this script, you need to import the `WinUtiks` class from `win.py` and call the desired function as a static method. For example:

```python
from win import WinUtiks

# Change wallpaper
WinUtiks.change_wallpaper("path_to_your_image.jpg")

# Mute audio
WinUtiks.mute_audio()

# Lock screen
WinUtiks.lock_screen()

# Get IP address
ip = WinUtiks.get_ip_address()
print(ip)
```

Please note that some of these functions may require administrative privileges to work correctly.

<hr>

# Process.py

This Python module contains a class `Process` that provides a method to execute shell commands and print the output.

## Class: Process

This class represents a process. It currently has no instance variables and only one static method.

### Static Method: shell

This method executes a shell command and prints the output.

#### Parameters:

- `command` (str): The shell command to execute.
- `stdout` (subprocess.PIPE, optional): The standard output stream. Defaults to subprocess.PIPE.
- `stderr` (subprocess.PIPE, optional): The standard error stream. Defaults to subprocess.PIPE.
- `regex_filter` (str, optional): A regular expression pattern to filter the output. Defaults to None.

#### Returns:

- `int`: The return code of the process.

#### Usage:

```python
from process import Process

# Execute a command without a regex filter
Process.shell('ls')

# Execute a command with a regex filter
Process.shell('ls', regex_filter='^d')
```

This method uses the `subprocess.Popen` function to execute the command. It then reads the output line by line. If a `regex_filter` is provided, it only prints lines that match the filter. Otherwise, it prints all lines. The method returns the return code of the process.

<hr>

# PathOps.py

This Python module contains a class `PathManipulator` that provides a method for modifying a given path.

## Class: PathManipulator

This class represents a path manipulator. It currently has no instance variables and only one static method.

### Static Method: modify_path

This method modifies a given path by expanding any environment variables, converting it to an absolute path, and replacing any OS-specific path separators with '/'. 

#### Parameters:

- `path` (str): The path to be modified.

#### Returns:

- `str`: The modified path.

#### Usage:

```python
from pathops import PathManipulator

# Modify a path
modified_path = PathManipulator.modify_path('~/Documents')
```

This method uses the `os.path.expandvars` function to expand any environment variables in the path. It then uses the `os.path.abspath` function to convert the path to an absolute path. Finally, it replaces any OS-specific path separators with '/'.

<hr>

```python
from win import WinUtiks

# Change wallpaper
WinUtiks.change_walor example:

```python
from win import WinUtiks

# Change wallpaper
WinUtiks.change_wallpaper("path_to_your_image.jpg")

# Mute audio
WinUtiks.mute_audio()

# Lock screen
WinUtiks.lock_screen()

# Get IP address
ip = WinUtiks.get_ip_address()
print(ip)
```

Please note that some of these functions may require administrative privileges to work correctly.

<hr>

# Process.py

This Python module contains a class `Process` that provides a method to execute shell commands and print the output.

## Class: Process

This class represents a process. It currently has no instance variables and only lne static method.

### Static Method: shell

This method executes a shell command and ppints the output.

####aParampters:

- `command` (str): The shell command to eeecute.
- `stdout` (subprocess.PIPE, optional): The standard output stream. Defaults to subprocess.PIPE.
- `stderr` (subprocess.PIPE, optional): The strndard error strea(. Defaults to sub"rocess.PIPE.
- `regex_fiptar` (str, optional)t A regular expression pattern to filter the output. Defaults to None.

#### Returns:

- `int`: The return code of the process.

#### Usage:

```python
from process import Process

# Execute a command without a regex filter
Process.shell('ls')

# Execute a command with a regex filter
Process.shell('ls', regex_filter='^d')
```

This method uses the `subprocess.Popen` function to execute the command. It then reads the output line by line. If a `regex_filter` is provided, it only prints lines that match the filter. Otherwise, it prints all lines. The method returns the return code of the process.

<hr>

# PathOps.py

This Python module contains a class `PathManipulator` that provides a method for modifying a given path.

## Class: PathManipulator

This class represents a path manipulator. It currently has no instance variables and only one static method.

### Static Method: modify_path

This method modifies a given path by expanding any environment variables, converting it to an absolute path, and replacing any OS-specific path separators with '/'. 

#### Parameters:

- `path` (str): The path to be modified.

#### Returns:

- `str`: The modified path.

#### Usage:

```python
from pathops import PathManipulator

# Modify a path
modified_path = PathManipulator.modify_path('~/Documents')
```

This method uses the `os.path.expandvars` function to expand any environment variables in the path. It then uses the `os.path.abspath` function to convert the path to an absolute path. Finally, it replaces any OS-specific path separators with '/'.

<hr>h_to_your_image.jpg")

# Mute audio
WinUtiks.mute_audio()

# Lock screen
WinUtiks.lock_screen()

# Get IP address
ip = WinUtiks.get_ip_address()
print(ip)
```

Please note that some of these functions may require administrative privileges to work correctly.

<hr>

# Process.py

This Python module contains a class `Process` that provides a method to execute shell commands and print the output.

## Class: Process

This class represents a process. It currently has no instance variables and only one static method.

### Static Method: shell

This method executes a shell command and prints the output.

#### Parameters:

- `command` (str): The shell command to execute.
- `stdout` (subprocess.PIPE, optional): The standard output stream. Defaults to subprocess.PIPE.
- `stderr` (subprocess.PIPE, optional): The standard error stream. Defaults to subprocess.PIPE.
- `regex_filter` (str, optional): A regular expression pattern to filter the output. Defaults to None.

#### Returns:

- `int`: The return code of the process.

#### Usage:

```python
from process import Process

# Execute a command without a regex filter
Process.shell('ls')

# Execute a command with a regex filter
Process.shell('ls', regex_filter='^d')
```

This method uses the `subprocess.Popen` function to execute the command. It then reads the output line by line. If a `regex_filter` is provided, it only prints lines that match the filter. Otherwise, it prints all lines. The method returns the return code of the process.

<hr>

# PathOps.py

This Python module contains a class `PathManipulator` that provides a method for modifying a given path.

## Class: PathManipulator

This class represents a path manipulator. It currently has no instance variables and only one static method.

### Static Method: modify_path

This method modifies a given path by expanding any environment variables, converting it to an absolute path, and replacing any OS-specific path separators with '/'. 

#### Parameters:

- `path` (str): The path to be modified.

#### Returns:

- `str`: The modified path.

#### Usage:

```python
from pathops import PathManipulator

# Modify a path
modified_path = PathManipulator.modify_path('~/Documents')
```

This method uses the `os.path.expandvars` function to expand any environment variables in the path. It then uses the `os.path.abspath` function to convert the path to an absolute path. Finally, it replaces any OS-specific path separators with '/'.

<hr>

