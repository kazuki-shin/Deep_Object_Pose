import subprocess

to_call = [
	"python3", '-m', 'torch.distributed.launch',
	'--nproc_per_node', '1', 'train.py',
	'--network', 'dope',
	'--epochs', '200',
	'--batchsize', '128',
	'--subbatchsize', '10',
	'--gpuids', '0',
	'--objects', 'obj',
	'--outf', 'cup',
	'--data', '../nvisii_data_gen/output/dataset_cup_20k',
]
subprocess.call(to_call)