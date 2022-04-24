import random 
import subprocess
import ipdb


# 20 000 images

for i in range(0,100):
	to_call = [
		"python3",'single_video_pybullet.py',
		'--path_single_obj', 'models/cup/meshes/model.stl',
		'--path_single_obj_texture', 'models/cup/texture_map.png',
		'--spp','400',
		'--nb_frames', '200',
		'--nb_objects', str(int(random.uniform(2,10))),
		'--nb_distractors', str(int(random.uniform(0,3))),
		'--height', '480',
		'--width', '640',
		'--outf',f"dataset_cup_kimlab_20k/{str(i).zfill(3)}",
		'--skyboxes_folder','dome_hdri_haven/selected_hdri/',
		# '--interactive'
	]
	subprocess.call(to_call)
