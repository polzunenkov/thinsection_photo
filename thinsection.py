import subprocess
import os	
import click

def _create_new_path(old_path, thinsection_name, lense_name):
	''' Возвращает новое имя для фотографий шлифов с учетом имени thinsection_name
	'''
	path_new = os.path.join(old_path, thinsection_name, lense_name,"")
	subprocess.run(["mkdir", "-p", path_new])
	
	return path_new

def copy(path):
	''' копирует фотографии с телефона из дирректории Camera 
            -стандартной камеры Honor
        и удаляет папку cache из новой дирректории на компьютере
	''' 
	cache_path=os.path.join(path, "cache")
	
	subprocess.run(["adb", "pull", "/sdcard/DCIM/Camera/.", path])		
	subprocess.run(["rm", "-R", cache_path])

def del_photo_folder(pattern):
	''' удаляет фотографии с телефона из дирректории Camera 
        -стандартной камеры Honor
	pattern - <common prefix>*.расширение файла- например jpg
	'''
 
	subprocess.run(["adb", "shell", "rm", "-f", 
                        f"/sdcard/DCIM/Camera/{pattern}"])		




@click.command()
@click.option('--path', help='Path to destination folder', required=True)
@click.option('--pattern', 
              help='pattern to delete files from Camera folder', 
              default="IMG_*.jpg")
@click.option('--thinsection_name', help='name for the thin section', 
              default="thin01")
@click.option('--lense_name', help='name of the lesne used', 
              default="x5")
@click.option('--do_not_remove_from_phone', '-D', 
              help='remove phtos from phone folder ', 
              is_flag=True, default=False)
def main(path, pattern, thinsection_name, lense_name, do_not_remove_from_phone):
	'''
	Копирует файлы с камеры телефона на компьютер
	'''
	old_path = os.path.normpath(path)
	new_path = _create_new_path(old_path, thinsection_name, lense_name)
	
	#click.echo(old_path)
	#click.echo(new_path)
	#click.echo(cache_path)
	
	copy(new_path)	
	
	
	if not do_not_remove_from_phone:
		del_photo_folder(pattern)

if __name__=="__main__":
	main()






