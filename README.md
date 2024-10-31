# Backup Program

This program automates the creation of backups for specified directories, compressing them into a `.zip` file and logging the process.

## Features

- **Scheduled Backups**: Runs every Sunday at 02:00 PM. (optional, you can change it for other day and time)
- **Directory Compression**: Creates a timestamped `.zip` file of the specified source directories.
- **Logging**: Records the backup process and any errors in a log file.

## Requirements

- Python 3.x
- Required libraries: `os`, `zipfile`, `datetime`, `schedule`, `logging`

## Configuration

### Source Directories

Edit the `SOURCE_DIRS` list to include the paths of directories you want to back up.

```python
SOURCE_DIRS = [
    r"C:\Path\To\Copy\Files\Folder1",
    r"C:\Path\To\Copy\Files\Folder2",
    r"C:\Path\To\Copy\Files\Folder3"
]
```

## Backup Directory
Set the `BACKUP_DIR` to the desired location for storing backups.

```python
BACKUP_DIR = r"C:\Path\To\Paste\Files\Folder"
```

## Usage
1. **Clone the Repository**:
    ``` 
    git clone https://github.com/luanfelixcoding/backup-system.git
    cd backup-system
    ```

2. **Create a Virtual Environment** (optional, but recommended):
    ```
    python -m venv .venv
    ```

3. **Activate the Virtual Environment:**
    - On Windows:
        ``.venv\Scripts\activate ``
    - On Linux or Mac: 
         ``source .venv/bin/activate``

4. **Install Dependencies** (if any):
    ```
    pip install -r requirements.txt
    ```

5. **Run the Program**:
    ```
    python backup_program.py
    ```
