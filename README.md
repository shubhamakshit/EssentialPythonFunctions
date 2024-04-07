# EssentialPythonFunctions
one stop place for your python project


## Points
- [WinUtiks](#winpy)
- [Process.py](#processpy)
- [PathOps.py](#pathopspy)


# Win.py

This Python module contains a class `WinUtiks` that provides various utility methods for Windows operations.

## Class: WinUtiks

This class represents a collection of Windows utility methods. All methods are static and can be called directly from the class.

### Static Method: change_wallpaper

This method changes the desktop wallpaper to the image file at the specified path.

#### Parameters:

- `path` (str): The path to the image file.

#### Usage:

```python
from win import WinUtiks

# Change the wallpaper
WinUtiks.change_wallpaper('path/to/image.jpg')
```

### Static Method: mute_audio

This method mutes the system audio.

#### Usage:

```python
from win import WinUtiks

# Mute the audio
WinUtiks.mute_audio()
```

### Static Method: lock_screen

This method locks the screen.

#### Usage:

```python
from win import WinUtiks

# Lock the screen
WinUtiks.lock_screen()
```

### Static Method: shutdown

This method shuts down the system.

#### Usage:

```python
from win import WinUtiks

# Shutdown the system
WinUtiks.shutdown()
```

### Static Method: restart

This method restarts the system.

#### Usage:

```python
from win import WinUtiks

# Restart the system
WinUtiks.restart()
```

### Static Method: log_off

This method logs off the current user.

#### Usage:

```python
from win import WinUtiks

# Log off the current user
WinUtiks.log_off()
```

### Static Method: get_ip_address

This method returns the IP address of the system.

#### Returns:

- `str`: The IP address of the system.

#### Usage:

```python
from win import WinUtiks

# Get the IP address
ip_address = WinUtiks.get_ip_address()
```
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

This Python module contains a class `PathOps` that provides methods for various path operations.

## Class: PathOps

This class represents a path operation. It currently has no instance variables and only static methods.

### Static Method: join

This method joins two or more pathname components, inserting '/' as needed.

#### Parameters:

- `*paths` (str): Arbitrary number of path strings to be joined.

#### Returns:

- `str`: The joined path.

#### Usage:

```python
from pathops import PathOps

# Join multiple paths
joined_path = PathOps.join('path1', 'path2', 'path3')
```

### Static Method: normalize

This method normalizes a pathname by collapsing redundant separators and up-level references.

#### Parameters:

- `