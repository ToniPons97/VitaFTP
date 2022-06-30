#!/usr/local/bin/python3
from ftplib import FTP
from tqdm import tqdm
import sys, os
from file_handling import *

def upload(filename, filesize, file):
	with tqdm(unit = 'blocks', unit_scale = True, leave = False, miniters = 1, desc = 'Uploading', total = filesize) as tqdm_instance:
		ftp.storbinary(f'STOR {filename}', file, 1024, callback = lambda sent: tqdm_instance.update(len(sent)))	


if len(sys.argv) == 2:
	server_ip = '192.168.1.138'
	port = 1337

	dst_dirs = {
		'psp' : 'ux0:/pspemu/ISO/',
		'ps1' : 'ux0:/pspemu/PSP/GAME/',
		'gba' : 'ux0:/roms/'
	}

	file = copy_file_to_output(sys.argv[1])
	print("copied: " + file)
	
	os.chdir(OUTPUT_DIR)

	console = get_console(file)

	if not console:
		file = decompress_file(file)
		print(f'File: {file.split("/")[-1]}')
		print(f'[+] Extracted: {file.split("/")[-1]}')

		console = get_console(file)
		if not console:
			print("[!] Invalid file.")
			clear_output_directory()
			sys.exit(0)
		
	
	upload_dir = dst_dirs[console]
			
	print(f'To upload: {file}')
	print(f'Console: {console.upper()}')
	print(f'Destination directory: {upload_dir}')
		
	print('PS Vita FTP Client!')
	print(f'Connecting to ftp://{server_ip}:{port}')
	
	ftp = FTP()
	ftp.connect(server_ip, port)
	ftp.login('anonymous', '')

	print(ftp.getwelcome())
	print(f'\nCurrent directory: {ftp.pwd()}')
	print(f'Changing directory...')

	ftp.cwd(upload_dir)
	print(f'Current directory: {ftp.pwd()}')

	# List pertinent directory
	print('\nListing files:')
	files = []
	ftp.dir(files.append)
	for f in files:
		print(f)

	
	if console == 'psp' or console == 'gba':
		gamefile = open(file, 'rb')
		filesize = os.path.getsize(file)
		
		upload(file.split('/')[-1], filesize, gamefile)
		gamefile.close()		

	elif console == 'ps1':
		dir_name = file		
		ps1_files = os.listdir(dir_name)

		print('\nFiles to upload:', ps1_files)
		os.chdir(dir_name)

		print('Creating and changing directory to', dir_name)
		ftp.mkd(dir_name.split("/")[-1])
		ftp.cwd(dir_name.split("/")[-1])

		for f in ps1_files:
			filesize = os.path.getsize(f)
			gamefile = open(f, 'rb')
			upload(f, filesize, gamefile)
			gamefile.close()
	else:
		print("[-] This script is expecting an .iso, .gba or a PS1 Eboot directory as an argument.")
		sys.exit(0)

	ftp.close()
	clear_output_directory()
	print('Done!')
else:
	print(f'Usage: {sys.argv[0]} <file>')
	print('[!] To upload a file, you need to pass the file name to this progam as a command line argument.')