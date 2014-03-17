from taskflow import task


class Task(task.BaseTask):
    def __init__(self, name, action, params):
        super(Task, self).__init__(name, None)
        self._action = action()
        self._params = params

    def execute(self, *args, **kwargs):
        self._action.execute(self._params)
