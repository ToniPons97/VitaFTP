# VitaFTP

This script ONLY works on a jailbroken PS Vita with Adrenaline (PSP/PS1 emulator) and GBA (Game boy advanced emulator) installed.

It simplifies the process of uploading games to the system (Bye Bye FileZilla). 

<h4>It handles the following steps for you:</h4>
<ol>
    <li>
        Decompressing the file (if compressed).
    </li>
    <li>
        Checking the file's integrity by checking file extensions, basic PS1 directory structure and valid MIME types to determine if it's a PSP, PS1 or GBA game.
    </li>
    <li>
        Uploading the game to the appropiate directory on the Vita.
    </li>
</ol>

<h3>USAGE:</h3>
<ol>
    <li>
        Go to the directory where the file is (IMPORTANT!!).
    </li>
    <li>
        run the script and pass the name of the file as argument (Use quotation if the file's name contains spaces).
    </li>
    <li>
        Wait for the script to finish.
    </li>

</ol>

<h3>EXAMPLES:</h3>
<ol>
    <li>$ /opt/VitaFTP/src/vita_ftp_client.py file.zip</li>
    <li>$ /opt/VitaFTP/src/vita_ftp_client.py 'file with spaces.rar'</li>
    <li>$ /opt/VitaFTP/src/vita_ftp_client.py file.iso</li>
    <li>$ /opt/VitaFTP/src/vita_ftp_client.py file.gba</li>
    <li>$ /opt/VitaFTP/src/vita_ftp_client.py PS1_GAME_DIRECTORY</li>
</lo> 