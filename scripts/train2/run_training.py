import subprocess

to_call = [
	"python3", '-m', 'torch.distributed.launch',
	'--nproc_per_node', '1', 'train.py',
	'--network', 'dope',
	'--epochs', '100',
	'--batchsize', '128',
	'--subbatchsize', '100',
	'--gpuids', '0', '1',
	'--objects', 'obj',
	'--outf', 'bowl',
	'--data', '../nvisii_data_gen/output/dataset_bowl_20k',
	'--net', '/home/kimlab/catkin_ws/src/Deep_Object_Pose/weights/bowl_9e.pth',
]
subprocess.call(to_call)