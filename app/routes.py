from flask import Blueprint, request, jsonify
from .services import TaskService

task_blueprint = Blueprint('tasks', __name__)

@task_blueprint.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = TaskService.get_all_tasks()
    tasks_list = [task.to_json() for task in tasks]
    return jsonify(tasks_list), 200


@task_blueprint.route("/tasks/<int:id>", methods=["GET"])
def get_task_by_id(id):
    try:
        task = TaskService.get_task(id)
        return jsonify(task.to_json()), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400


@task_blueprint.route("/tasks", methods=["POST"])
def add_task():
    try:
        task_data = request.json
        TaskService.create_task(task_data)
        return jsonify({"message": "Task added successfully"}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    

@task_blueprint.route("/tasks/<int:id>/complete", methods=["POST"])
def complete_task(id):
    try:
        TaskService.toggle_task_completion(id)
        return jsonify({"message": "Task status updated"}), 200
    except ValueError:
        return jsonify({"message": "Task not found"}), 404
    

@task_blueprint.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    try:
        TaskService.delete_task(id)
        return jsonify({"message": "Task deleted"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
