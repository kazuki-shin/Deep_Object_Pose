import subprocess

to_call = [
	"python3", '-m', 'torch.distributed.launch',
	'--nproc_per_node', '1', 'train.py',
	'--network', 'dope',
	'--epochs', '1',
	'--batchsize', '128',
	'--subbatchsize', '10',
	'--gpuids', '0',
	'--objects', 'spoon',
	'--outf', 'spoon',
	'--data', '../nvisii_data_gen/output/spoon_indoor_dist_1k_021022',
]
subprocess.call(to_call)