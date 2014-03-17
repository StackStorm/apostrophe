import abc


class BaseAction(object):
    def __init__(self):
        pass

    @abc.abstractmethod
    def execute(self, *args, **kwargs):
        """
        Some description
        """


class EchoAction(BaseAction):
    def __init__(self):
        super(EchoAction, self).__init__()

    def execute(self, params):
        print(params['text'])
