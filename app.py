# File manager Script app in Python
# library Used: Os and Shutill
# Git Hub : https://github.com/AyanUpadhaya
# twitter : Code Tech -> @ayanupadhaya96
#-------------------------------------------
import os
import shutil

main_file="app.py"
#directory paths
source="/home/ayan/Desktop/filemanager"

audio_folder="/home/ayan/Desktop/filemanager/audio"

images_folder="/home/ayan/Desktop/filemanager/images"

programming_folder="/home/ayan/Desktop/filemanager/programming"

text_folder="/home/ayan/Desktop/filemanager/text"

video_folder="/home/ayan/Desktop/filemanager/video"

files = os.listdir(source)

#file formats list
audio_file_formats=['mp3','wav']
doc_file_formats=['doc','docx','xlsx']
text_file_formats=['txt']
video_file_formates=['mp4','mkv']
programming_file_formats=['py','js','cpp']
images_file_formats= ['PNG','jpg','png','jpeg']

#delete app.py file from list
if main_file in files:
    get_file_index=files.index(main_file)
    del files[get_file_index]

for file in files:
	
    file_ext= file.split('.')[-1]

    if file_ext in audio_file_formats:
        shutil.move(file,audio_folder)

    if file_ext in doc_file_formats:
        shutil.move(file,text_folder)

    if file_ext in text_file_formats:
        shutil.move(file,text_folder)

    if file_ext in video_file_formates:
        shutil.move(file,video_folder)

    if file_ext in programming_file_formats:
	
        shutil.move(file,programming_folder)

    if file_ext in images_file_formats:
	
        shutil.move(file,images_folder)
