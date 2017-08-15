import csv
import os, shutil

src_folder = ''
dest_folder = ''
output = ''
last_file = ''
                    
def copy(src):
    if not src.startswith('='):
        try:
            shutil.copy(os.path.join(src_folder, src), dest_folder)
        except:
            print('error: ' + os.path.join(src_folder, src))
    else:
        src_filename = src.lstrip('=').lstrip('\"').rstrip('\"')
        try:
            shutil.copy(os.path.join(src_folder, src_filename), dest_folder)
        except:
            print('error: ' + os.path.join(src_folder, src_filename))
            

with open('export.csv', newline='', encoding='utf-16') as csvfile:
    reader = csv.reader(csvfile,  delimiter='\t', quoting=csv.QUOTE_NONE)
    
    for line in reader:
        if len(line[3]) == 0 and len(line[0]) > 0:
            src_folder = line[0]
            dest_folder = os.path.join(output, src_folder.split(':')[1].lstrip('\\'))
            os.makedirs(dest_folder)
        elif line[5] == 'add' and int(line[3]) > 0 and len(dest_folder) > 0:
            copy(line[0])
        elif line[5] == 'old':
            last_file = line[0]
        elif line[5] == 'new' and int(line[3]) > 0 and len(line[0]) == 0 and len(last_file) > 0 and len(dest_folder) > 0:
            copy(last_file)
            print('mod file: ' + last_file)
            last_file = ''
