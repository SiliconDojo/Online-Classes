### File Path
Creates a file path based on operating system requirements
```
filename = file.txt
directory = some-directory
filename = os.path.join(directory, filename)
```


### Create Folder If It Does Not Exist
Creates folder, and ignores error if the folder alredy exists

```
directory = 'DIRECTORY-NAME'
os.makedirs(directory, exist_ok=True)
```
