import os
import json
from task_manager import Task

class Storage:

	def __init__(self):
		self.tasks_file_name = 'tasks.json'
		self.tasks = self.load_tasks()

	def load_tasks(self):
		if os.path.exists(self.tasks_file_name):
			with open(self.tasks_file_name, 'r') as file:
				try:
					tasks_data = json.load(file)
					loaded_tasks = [Task.from_dict(task_dict) for task_dict in tasks_data]
					return loaded_tasks
				except json.JSONDecodeError:
					return []
		return []

	def save_task(self, task):
		self.tasks.append(task)

	def update_task(self, updated_task):
		for i, task in enumerate(self.tasks):
			if task.title == updated_task.title:
				self.tasks[i] = updated_task
				break

	def get_task(self, title):
		for task in self.tasks:
			if task.title == title:
				return task
		return None

	def get_all_tasks(self):
		return list(self.tasks)

	def clear_all_tasks(self):
		self.tasks = []

	def __del__(self):
		with open(self.tasks_file_name, 'w') as file:
			json.dump([task.to_dict() for task in self.tasks], file, indent=4)
