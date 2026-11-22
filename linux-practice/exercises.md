# Linux Command-Line Exercises

Use a dedicated practice folder for these exercises. Do not use administrator privileges, and avoid changing or deleting files outside your practice folder.

## 1. Explore Your Location

- Find out which directory you are currently in.

```bash
pwd
```

- List the files and folders there, including hidden items.

```bash
ls -la
```

- Find out how to get help for a command-line utility.

```bash
man ls
```

## 2. Create and Organize Files

- Create folders named `notes` and `backup`.

```bash
mkdir notes backup
```

- Create an empty file named `todo.txt`.

```bash
touch todo.txt
```

- Open the file in a terminal text editor and write three tasks in it.

```bash
nano todo.txt
```

## 3. Read and Update a File

- Display the contents of `todo.txt`.

```bash
cat todo.txt
```

- Add another line to the file without opening a text editor.

```bash
echo "Olá mundo" >> todo.txt
```

- Count the lines, words, and bytes in the file.

```bash
wc todo.txt
```

**Output:**

```text
4  5 19 todo.txt
```

4 lines, 5 words, 19 bytes.

## 4. Copy and Rename

- Copy `todo.txt` into the `backup` folder.

```bash
cp todo.txt backup/
```

- Rename the copied file to `todo-old.txt`.

```bash
mv backup/todo.txt backup/todo-old.txt
```

- Check that the original and the renamed copy both exist.

```bash
ls -la todo.txt backup/todo-old.txt
```

## 5. Find Files and Text

- Create two more text files in your practice folder.

```bash
touch boas.txt nice.txt
```

- Search for a word that appears in one of those files.

```bash
grep "ola" boas.txt
```

- Find all text files in your practice folder.

```bash
find -name "*.txt"
ls -la *.txt
```

## 6. Practice File Permissions

- Inspect the permissions of your files.

```bash
ls -l
```

- Remove write permission from yourself for one practice file.

```bash
chmod u-w boas.txt
```

- Check the permission change, then restore write permission.

```bash
ls -l boas.txt
chmod u+w boas.txt
```

## 7. Combine Command Output

- List the files in your practice folder and filter the results to show only names containing a chosen word.

```bash
ls -la | grep "boas"
```

- Count how many files are in the folder.

```bash
ls -1 | wc -l
```

## 8. Inspect Running Processes

- Display a list of running processes.

```bash
ps aux
```

- Find a process by its name.

```bash
pgrep -a spotify
```
