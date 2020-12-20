class Task(object):
    def __init__(self, name, description="", task_id=None):
        self.id = task_id
        self.name = name
        self.description = description

    def serialize(self):
        return {
            "id":          self.id,
            "name":        self.name,
            "description": self.description
        }

    @staticmethod
    def serialize_multiple(tasks):
        return [task.serialize() for task in tasks]
