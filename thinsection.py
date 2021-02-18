import subprocess
import click

def copy(path):
	''' копирует фотографии с телефона из дирректории Camera -стандартной камеры Honor
	''' 
	subprocess.run(["adb", "pull", "/sdcard/DCIM/Camera", path])		

def rename(path, name_folder):
	''' переименовывает в name_folder скопированную папку с телефона из дирректории Camera -стандартной камеры Honor
	''' 
	subprocess.run(["mv", path, "/sdcard/DCIM/Camera"])		
	mv /tmp/test2/Camera /tmp/test2/S7-006A

def del_photo_folder(pattern):
	''' удаляет фотографии с телефона из дирректории Camera -стандартной камеры Honor
	pattern - <common prefix>*.расширение файла- например jpg
	'''
 
	subprocess.run(["adb", "shell", "rm", "-f", f"/sdcard/DCIM/Camera/{pattern}"])		

@click.command()
@click.option('--path', help='Path to destination folder', required=True)
@click.option('--pattern', help='pattern to delete files from Camera folder', default="IMG_*.jpg")
def main(path, pattern):
	copy(path)
	del_photo_folder(patter)

if __name__=="__main__":
	main()














