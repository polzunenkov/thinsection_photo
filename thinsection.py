import subprocess
import os	
import click

def _create_new_path(old_path, thinsection_name):
	''' Возвращает новое имя для фотографий шлифов с учетом имени thinsection_name
	'''
	path_new = os.path.join(old_path, thinsection_name)
	return path_new

def copy(path):
	''' копирует фотографии с телефона из дирректории Camera 
            -стандартной камеры Honor
	''' 
	# create main folder
	subprocess.run(["mkdir", "-p", path])
	
	subprocess.run(["adb", "pull", "/sdcard/DCIM/Camera", path])		

def rename(path, thinsection_name):
	''' переименовывает в name_folder скопированную папку 
            с телефона из дирректории Camera -стандартной камеры Honor
	''' 
	path_old = os.path.join(path, "Camera")
	path_new = _create_new_path(path, thinsection_name)
	subprocess.run(["mv", path_old, path_new])		
	

def del_photo_folder(pattern):
	''' удаляет фотографии с телефона из дирректории Camera 
        -стандартной камеры Honor
	pattern - <common prefix>*.расширение файла- например jpg
	'''
 
	subprocess.run(["adb", "shell", "rm", "-f", 
                        f"/sdcard/DCIM/Camera/{pattern}"])		


def add_info_obiective(path, thinsection_name): 
	path_new = _create_new_path(path, thinsection_name)
	for count, filename in enumerate(os.listdir(path_new)): 
		dst ="Hostel" + str(count) + ".jpg"
		src = os.path.join(path_new, filename )
		dst =os.path.join(path_new, dst )
		  
		# rename() function will 
		# rename all the files 
		os.rename(src, dst) 




@click.command()
@click.option('--path', help='Path to destination folder', required=True)
@click.option('--pattern', 
              help='pattern to delete files from Camera folder', 
              default="IMG_*.jpg")
@click.option('--thinsection_name', help='name for the thin section', 
              default="thin01")
@click.option('--do_not_remove_from_phone', '-D', 
              help='remove phtos from phone folder ', 
              is_flag=True, default=False)
def main(path ,pattern, thinsection_name, do_not_remove_from_phone):
	'''
	Копирует файлы с камеры телефона на компьютер
	'''
	path = os.path.normpath(path)
	
	click.echo(do_not_remove_from_phone)
	
	copy(path)	
	rename(path, thinsection_name)
	add_info_obiective(path, thinsection_name)
	if not do_not_remove_from_phone:
		del_photo_folder(pattern)

if __name__=="__main__":
	main()






