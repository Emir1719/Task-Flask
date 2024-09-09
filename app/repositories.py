from .models import Task
from . import db

class TaskRepository:
    @staticmethod
    def get_all_tasks() -> list[Task]:
        return Task.query.all()

    @staticmethod
    def get_task_by_id(task_id) -> Task:
        return Task.query.get(task_id)

    @staticmethod
    def add_task(task_data):
        new_task = Task(title=task_data['title'].strip(), content=task_data['content'].strip(), complete=False)
        db.session.add(new_task)
        db.session.commit()

    @staticmethod
    def update_task(task):
        # task parameter is important to update!
        db.session.commit()

    @staticmethod
    def delete_task(task):
        db.session.delete(task)
        db.session.commit()

    @staticmethod
    def search_tasks_by_content(content_substring: str) -> list[Task]:
        """
        Search for tasks where content starts with the provided substring.
        """
        search_pattern = "%{}%".format(content_substring)
        return Task.query.filter(Task.content.like(search_pattern)).all()

    @staticmethod
    def get_tasks_by_complete(complete: bool) -> list[Task]:
        return Task.query.filter(Task.complete.is_(complete)).all()
