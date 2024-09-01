# FireTune
this is a music stealing malware concept made with python and php

![XW](https://res.cloudinary.com/dxubkzzbx/image/upload/v1725233546/ft1_quctnm.png)

Overview of Firetune

ftune.py:

    Purpose: Finds and sends certain audio files (e.g., MP3s and WAVs) from a user's computer to a server.
    Process: The script searches for these files, encodes them for safe transmission, and then sends them to the server via a network connection.

upload.php:

    Purpose: Receives the encoded files from the Python script and saves them on the server.
    Process: It decodes the received data and stores the files in a designated folder on the server, organizing them by the client's hostname.

Summary: The Python script from.py handles file discovery and transmission, while the PHP script upload.php handles reception and storage of the files on the server.
