from .repositories import TaskRepository

class TaskService:
    @staticmethod
    def get_all_tasks():
        return TaskRepository.get_all_tasks()

    @staticmethod
    def get_task(task_id):
        return TaskRepository.get_task_by_id(task_id)

    @staticmethod
    def create_task(task_data):
        if not task_data.get('title') or not task_data.get('content'):
            raise ValueError("Title and content are required")
        TaskRepository.add_task(task_data)

    @staticmethod
    def toggle_task_completion(task_id):
        task = TaskRepository.get_task_by_id(task_id)
        if task:
            task.complete = not task.complete
            TaskRepository.update_task(task)

    @staticmethod
    def delete_task(task_id):
        task = TaskRepository.get_task_by_id(task_id)
        if task:
            TaskRepository.delete_task(task)
        else:
            raise ValueError("The task was not found")
