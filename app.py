from flask import Flask, request, jsonify
import utils
app = Flask(__name__)

def extract_req_data(data):
	if isinstance(data, str):
		return data.split("|")
	elif isinstance(data, list):
		return data
	else:
		raise Exception("Invalid Request format !!")

@app.route("/info")
def get_disque_info():
	return jsonify(utils.info())

@app.route("/qsize")
def get_queue_size():
	payload = request.json
	queue = payload["queue_name"]
	queue_names=[]
	if isinstance(queue, str):
		queue_names.append(queue.split("|"))
	elif isinstance(queue, list):
		queue_names = queue
	return jsonify(utils.get_queue_size(queue_names))

@app.route("/show_job")
def show_job():
	payload = request.json
	job_id = payload["job_id"]
	job_ids = []
	if isinstance(job_id, str):
		job_ids = job_id.split("|")
	elif isinstance(job_id, list):
		job_ids = job_id
	return jsonify(utils.show_job(job_ids))

@app.route("/qstats")
def queue_stats():
	payload = request.json
	queue_name = payload["queue_name"]
	queue_name = extract_req_data(queue_name)
	resp = utils.get_queue_stats(queue_name)
	return jsonify(resp)

@app.route("/qpeek")
def queue_peek():
	payload = request.json
	queue_name = payload["queue_name"]
	count = payload.get("count")
	queue_name = extract_req_data(queue_name)
	resp = utils.queue_peek(queue_name)
	return jsonify(resp)
