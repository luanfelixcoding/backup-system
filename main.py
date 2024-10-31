"""
TODO: use cryptography library in python
in order to crytograph the .zip backups
and descryptograph them

TODO: analyze the use of 'shutil' library in python
in order to optimize the process getting it faster
and replace 'os' library for a better one
"""
from crypto_module import cryptograph_backup
import os
import zipfile
from datetime import datetime
import schedule
import time
import logging

"""
PATH FORMATS

LINUX: "/name/of/the/folder"
WINDOWS: r"\name\of\the\folder"

PATH TO DIRS YOU WANT TO COPY
"""
SOURCE_DIRS = [
    "/home/tatico-mendo/Desktop",
    # r"C:\Caminho\Para\Pasta2",
    # r"C:\Caminho\Para\Pasta3"
]

# PATH TO DIR YOU WANT TO PASTE
BACKUP_DIR = "/home/tatico-mendo"


def create_backup():
    """
    Create a backup of specified source directories in a .zip format.

    This function traverses the directories listed in `SOURCE_DIRS`, 
    gathers all files, and writes them into a timestamped backup .zip file 
    located in the `BACKUP_DIR`. A log file is created or updated 
    in the `BACKUP_DIR` to record the backup process.

    The backup file is named using the current date and time to ensure 
    uniqueness. In case of any errors during the backup creation, an 
    error message is logged.

    Returns:
        None

    Raises:
        Exception: Logs any exceptions that occur during the backup process.
    """
    try:
        date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_filename = os.path.join(BACKUP_DIR, f'backup_{date_str}.zip')

        with zipfile.ZipFile(backup_filename, 'w') as backup_zip:
            for source_dir in SOURCE_DIRS:
                for foldername, subfolders, filenames in os.walk(source_dir):
                    for filename in filenames:
                        file_path = os.path.join(foldername, filename)
                        backup_zip.write(
                            file_path, os.path.relpath(file_path, source_dir))
        # cryptograph_backup(backup_zip)
        logging.info(f"Backup created in success: {backup_filename}")
    except Exception as e:
        logging.error(f"ERROR in creating backup: {e}")

    # Creating log-file basic configuration
    logging.basicConfig(
        filename=os.path.join(BACKUP_DIR, 'backup_log.log'),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def job():
    logging.info("Initializing weekly backup...")
    create_backup()
    # create_backup()
    # print(create_backup.__doc__)


schedule.every().sunday.at("02:00").do(job)


if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(60)
