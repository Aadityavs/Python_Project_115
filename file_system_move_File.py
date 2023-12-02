import os

source = 'main.txt'

destiny='new_file.txt'
os.rename(source,destiny)

print('source path renamed to destination path successfully')