## Repo cloning:

To clone the repo, just type this command:

    $ git clone https://github.com/Xabi08YT/CAPalgorythm.git

Enjoy !

## Python micro environment:

If you want to make a custom Install package, you will need to download and extract one of the archives below:

For Windows 10+: https://sourceforge.net/projects/portable-python/files/Portable%20Python%203.10/Portable%20Python-3.10.5.exe/download

For Windows 7+: https://sourceforge.net/projects/portable-python/files/Portable%20Python%203.7/Portable%20Python-3.7.7.exe/download

For MacOS or Linux: UNSUPPORTED YET

## For update deployment:

To deploy updates with the current updater, you need to make a zip archive with the following architecture:
Update/
    version.txt
    libs.txt
newupdater.py
ExecuterCAPS.bat
main.py

And that's all ! You can add what you want in the archive !
PS: newupdater.py can be a copy of the updater.py and don't forget to update the version.txt file.

Then, you need a web server: 
On your web server, you make an index html with two download links: one for a copy of version.txt used in the zip archive one for the zip archive created.

Don't forget to update the updater.py and the newupdater.py files with your new links !
The link for the version is line 17 and for the link for the archive is line 43.

## LICENSE

MIT License

Copyright (c) 2023 Xabi GOITY (Xabi08YT)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Code architecture

Update\
    libs.txt: contains all needed libs, automatically installed when updater.py is launched
    version.txt: contains current software version
fr-Xabi08-CAPAlgorythmCore\
    __init.py__: empty
    basicDBCtrl.py: Contains code for basic DB control like reset, create or config editor
    feedback.py: Contains code to manage feedback.csv
    relations.py: Contains code to manage relations.csv
    tuteurs.py: Contains code to manage tuteurs.csv
    utils.py: Contains useful functions for logging, initiating, dataFile gen... 
CoreProxy.py: load package fr-Xabi08-CAPAlgorythmCore
ExectuerCAPS.bat: script to execute the software with a portable python environment located in a folder named PythonEnv
logo.png: program icon
main.py: contains GUI and load CoreProxy.py
updater.py: contains updater

## Data files

All data files will be generated at startup.
config.csv: config for the soft. Mandatory and generated at startup.

feedback.csv: (WIP) database for feedback concerning relationships, used to avoid certains relationship if needed. Disabled by default, can be enabled through the GUI in 
Options > Configurer

relations.csv: (WIP) database for storing relationships. Needed to activate feedback.csv. Used to display warning to user if a Student already has a relationships. Disabled by default, can be enabled through the GUI in Options > Configurer

tuteurs.csv: mandatory, database used to store every volunteer to help other.

lastestlogs.txt: Enabled by default, can be partially disabled through Options > Configurer . File used to log everything during the run of the program. This file will be reset at every launch.

## Data files columns

config.csv: property, state

feedback.csv: feedbackid, tutore, tuteur, caractere, matiere, efficacite, idrelation, commentaires

relations.csv: id, tuteur, tutore, matiere, horaire

tuteurs.csv: nom, prenom, niveau, disponibilites, matiere, contact

## WARNING: THE SOFTWARE IS STILL WORK IN PROGRESS

WARNING: All the stuff written above may evolve as the software is still work in progress !