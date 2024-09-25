### File Path
Creates a file path based on operating system requirements
```
filename = file.txt
directory = some-directory
filename = os.path.join(directory, filename)
```

### Open File in Same Directory as Script
This allows you to interact with a file in the same directory the script is running in.
```
import os

file_name = 'file.txt'
dir_current = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_current, file_name)
```

### Create Folder If It Does Not Exist
Creates folder, and ignores error if the folder alredy exists

```
directory = 'DIRECTORY-NAME'
os.makedirs(directory, exist_ok=True)
```
