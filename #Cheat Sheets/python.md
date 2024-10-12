## Basics

## Concatenation

### F Strings

```
name = 'bob'

greeting = 'hello'

print(f'{greeting} {name}')
```


### If/ Elif/ Else Statements

```
if x >= 0:
  print('positive')
else:
  print('negative')
```

```
if x >= 10:
  print('big')
elif x >=5 and x < 10:
  print('medium')
else:
  print('small')
```

### Try / Except Statements

```
try:
  #do something such as an OS command
except:
  #if command fails do this
else:
  #if command works also do this
finally:
  #whether it works or not do this at the end
```

### For Loops

```
my_list = ['bob','sue','tim']

for x in my_list:
  print(x)
```

### While Loops

```
x = 0
while x <= 10:
  print(x)
  x += 1
```

## Sets

### Lists
#### Add to List
```
my_list = ['tim','sue','phil']
name = bob

my_list.append(name)

```

#### Delete from List


Remove Based on Index:
```
my_list = ['tim','sue','phil','bob']

my_list.pop(3)

```

Remove Based on Value:
```
my_list = ['tim','sue','phil','bob']
name = bob

my_list.remove(name)
```

## File Paths

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