# CaviClean

Python package CaviClean for cleaning and agregating cavit files from separate folders


## How to install ?

Download the last version from github

>
> git clone https://github.com/xbouteiller/cavitron.git
>
> python setup.py develop
>

## How to use ?

In the exec folder:

- double clic on : launch.bat
- should be located in the same folder than caviclean-python-exec.py


## What are the possibilities ?

3 choices are offered at the beginning of the program

1. Parse a folder and subfolders
	- automatically detect raw files from cavitron within each subfolder
	- check the coherence of files within each subfolder
	- finally concatenate all files
	
2. Check and correct an individual file already made by the program
	- useful if we want to inactive individuals, change some columns values (e.g. treatement) 
	
3. Concatenate 2 files
	- typically if we want to add a new population to the database
	

## What do the program ?

1. Detection of error within several columns (e.g. typos)
	- if potential errors are detected, several options are proposed to the user to correct them
	
2. Detection of empty field

3. Concatenation of files

4. Assert if each cavit number (sample ref 1) corresponds to an unique combination of columns (campaign name, species, treatment, repetition, tree number - sample ref 2 -)
	- if a problem is detected several options are available (do nothing, automatically compute repetition number, change a column value, inactive individual)
	

** sample ref 1 - cavitron number - can never be changed by the program **