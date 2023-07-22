import shutil
import os
import sys

cwd = os.path.dirname(os.path.abspath(sys.argv[0]))

file_name = "Original_Text.txt"
original_path = cwd + "/" + file_name
target_path = cwd + "/backup/Original_Text_bkp.txt"

if(os.path.exists(target_path)) :
	print("The backup file already existed. Couldn't backup the file.")
else :
	shutil.copyfile(original_path, target_path)
	print("Done backed up " + file_name + " inside " + target_path)

with open(original_path , 'r') as file :
	data = file.read()
	if "30" in data :
		data = data.replace("30", "25")
		
		with open(original_path, 'w') as file :
			file.write(data)
			print("Successfully replaced the text!!")
	else :
		print("Data not found! Terminating the script...")
		exit()
