import sys, magic, os
from pyunpack import Archive
from shutil import copyfile, rmtree

OUTPUT_DIR = f'{os.path.dirname(os.path.realpath(__file__))[:-3]}output'

def clear_output_directory():
    '''
        This function removes everything from the output directory.
    '''
    for i in os.listdir(OUTPUT_DIR):
        game_abspath = f'{OUTPUT_DIR}/{i}'
        if os.path.isfile(game_abspath):
            os.remove(game_abspath)
        elif os.path.isdir(game_abspath):
            rmtree(game_abspath)
    

def decompress_file(file):
    try:
        print(f'Extracting {file}')
        Archive(file).extractall(OUTPUT_DIR)
        os.remove(file)
        print('[+] File extracted.')
        
        for f in os.listdir(OUTPUT_DIR):
            if f[-3::] in ['gba', 'iso']:
                return f'{OUTPUT_DIR}/{f}'
            if os.path.isdir(f):
                return f'{OUTPUT_DIR}/{f}'
        return ''
    except Exception:
        print('[!] Couldn\'t extract file.')
        sys.exit(0)

def get_ps1_dir():
    for f in os.listdir(OUTPUT_DIR):
        if os.path.isdir(f):
            return f'{OUTPUT_DIR}/{f}'
    return ''


def get_mime(file):
    '''
        This function checks a file's magic number and returns its MIME type.
        If it is  a directory, then it verifies that it is a valid PS1 EBOOT directory, 
        and returns the string \'ps1\'.
    '''
    try:
        return magic.from_file(file, mime="True").split("/")[1]
    except IsADirectoryError:
        if is_ps1_eboot(file):
            return 'ps1'

def get_console(filename):
    '''
        This function determines and returns console type from file's name.
    '''
    valid_consoles = {
        'x-iso9660-image' : 'psp',
        'x-gba-rom' : 'gba',
        'ps1' : 'ps1'
    }

    try:
        return valid_consoles[get_mime(filename)]
    except KeyError:
        return ""


def copy_file_to_output(filename):
    '''
        This function copies a given file from the directory where the script is running, to this project's output directory.
    '''
    file_src = os.path.abspath(filename)
    file_dst = os.path.join(OUTPUT_DIR, filename)
    copyfile(file_src, file_dst)
    return file_dst


def is_ps1_eboot(directory_name):
    '''
        This function checks if the given file is a directory. If so, it changes to that directory and inspects all files by calling the __check_ps1_data__ function.
    '''
    if os.path.isdir(directory_name):
        #os.chdir(directory_name)
        #print("CWD: " + os.getcwd())
        #return __check_ps1_data__(os.listdir(directory_name), f'{OUTPUT_DIR}/{directory_name}')
        return __check_ps1_data__(directory_name)
    else:
        return False

def __check_ps1_data__(dir_name):
    '''
        This function checks if all files inside a given directory are consistent with a common PS1 EBOOT directory. This is done by checking magic numbers and file extensions. 
    '''
    valid_file_exts = ['DAT', 'BIN', 'PBP']
    valid_mime = 'octet-stream'


    os.chdir(dir_name)
    print("INSIDE: " + os.getcwd())
    
    valid_contents = []
    relative_path = dir_name.split('/')[-1]
    for i in os.listdir(dir_name):
        if (get_mime(i) == valid_mime) and (i.split('.')[1] in valid_file_exts):
            valid_contents.append(True)
        else:
            valid_contents.append(False)

    truth_count = 0
    for i in valid_contents:
        if i:
            truth_count += 1

    if truth_count == len(valid_contents):
        return True
    else:
        return False

def is_psp_or_gba(filename):
    if (get_console(filename) == 'x-iso9660-image') or (get_console(filename) == 'x-gba-rom'):
        return 'Cool'