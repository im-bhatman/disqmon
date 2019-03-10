from pydisque.client import Client
from config import DISQUE_CLIENT

disque = Client()


def get_queue_size(queue_names=None):
	res = {}
	for q_name in queue_names:
		length = disque.qlen(q_name)
		res[q_name] = length
	return res

def get_queue_stats(queue_names=None):
	res={}
	for q_name in queue_names:
		data = disque.qstat(q_name, True)
		res[q_name]=(data)
	return res

def show_job(job_ids=None):
	res = {}
	for job_id in job_ids:
		res[job_id]=disque.show(job_id, True)
	return res

def queue_peek(queue_name=None, count=25):
	res = {}
	for q_name in queue_name:
		for job_arr in disque.qpeek(q_name, count):
			print("JOB-ARR ===>> ", job_arr)
			key = job_arr[1]
			res[key] = job_arr[2]
	print("RESPONSE -->>> ", res)
	return res

def info():
	return disque.info()