import random 
import subprocess
import ipdb


# 20 000 images

for i in range(0,100):
	to_call = [
		# "python",'single_video.py',
		"python3",'single_video_pybullet.py',
		'--path_single_obj', 'models/cup/meshes/model.stl',
		'--path_single_obj_texture', 'models/cup/texture_map.png',
		'--spp','100',
		'--nb_frames', '200',
		'--nb_objects', str(int(random.uniform(10,15))),
		'--nb_distractors', str(int(random.uniform(0,3))),
		# '--static_camera',
		# '--nb_frames', '1',
		# '--nb_objects',str(1),
		'--outf',f"dataset_cup_20k/{str(i).zfill(3)}",
	]
	subprocess.call(to_call)
	# subprocess.call(['mv',f'dataset/{str(i).zfill(3)}/video.mp4',f"dataset/{str(i).zfill(3)}.mp4"])
	# break
	# subprocess.Popen(["rsync",'-r',f'output/dataset/{str(i).zfill(3)}',
	# 	"/mnt/adlr/dataset_2/",";",
	# 	'rm','-rf',f'output/dataset/{str(i).zfill(3)}'])
	# subprocess.call([])
	# break