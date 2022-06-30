# VitaFTP

This script ONLY works on a jailbroken PS Vita with Adrenaline (PSP/PS1 emulator) and GBA (Game boy advanced emulator) installed.

It simplifies the process of uploading games to the system (Bye Bye FileZilla). 

It handles the following steps for you:
    1) decompressing the file (if compressed).
    
    2) checking the file's integrity by checking file extensions, basic PS1 directory structure and valid MIME types to determine if it's a PSP, PS1 or GBA game.

    3) Then it uploads the game to the appropiate directory on the Vita.

USAGE:
    1) Go to the directory where the file is (IMPORTANT!!).
    2) run the script and pass the name of the file as argument (Use quotation if the file's name contains spaces).
    3) Wait for the script to finish.

EXAMPLES:
    1)
        $ /opt/VitaFTP/src/vita_ftp_client.py file.zip
    2) 
        $ /opt/VitaFTP/src/vita_ftp_client.py 'file with spaces.rar'
    3) 
        $ /opt/VitaFTP/src/vita_ftp_client.py file.iso
    4)
        $ /opt/VitaFTP/src/vita_ftp_client.py file.gba
    5)
        $ /opt/VitaFTP/src/vita_ftp_client.py PS1_GAME_DIRECTORY