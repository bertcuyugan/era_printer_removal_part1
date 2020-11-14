#!/usr/bin/python3


## Part1 main code
## logic

import shutil


#logic1 - user input and verify user input



#logic2 - backup the /etc/hosts file

	# task1 - make a backup of the /etc/hosts file
	# https://stackabuse.com/how-to-copy-a-file-in-python/

		##code - shutil.copy("source","destination")

	# task2 - tar the /etc/hosts backup file from task1
	# https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory-in-python

		##code - shutil.make_archive('/home/user/Desktop/Filename','zip','/home/username/Desktop/Directory')


			#1st arg: Filename of resultant zip/tar file,
			#2nd arg: zip/tar,
			#3rd arg: dir_name


#logic3 - checking the printer queue

#logic4 - removing the printer jobs

#logic5 - removing the printer queue

#logic6 - commenting the printer queue
