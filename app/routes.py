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


@task_blueprint.route("/tasks/search", methods=["GET"])
def search_content():
    try:
        # GET isteği olduğu için request.args.get kullanmalısınız.
        content = request.args.get("content")  # request.form yerine request.args kullanılıyor

        if not content:
            return jsonify({"message": "Content parameter is missing"}), 400
        
        results = TaskService.search_tasks_by_content(content)
        tasks_list = [task.to_json() for task in results]

        # Eğer filtre sonucunda hiçbir sonuç bulunmazsa:
        if not tasks_list:
            return jsonify({"message": "No tasks found matching the content"}), 404

        return jsonify(tasks_list), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@task_blueprint.route("/tasks/state", methods=["GET"])
def is_complete_task():
    try:
        complete = request.args.get("complete")

        if not complete:
            return jsonify({"message": "Complete parameter is missing"}), 400
        
        results = TaskService.get_tasks_by_complete(complete)
        tasks_list = [task.to_json() for task in results]

        # Eğer filtre sonucunda hiçbir sonuç bulunmazsa:
        if not tasks_list:
            return jsonify({"message": "No tasks found matching the complete"}), 404

        return jsonify(tasks_list), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500