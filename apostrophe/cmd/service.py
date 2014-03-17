from apostrophe.model.action import EchoAction
from apostrophe.model.task import Task
from apostrophe.model.flow import Flow
import taskflow.engines


def main():
    flow = Flow('some').add(
        Task('one', EchoAction, {"text": "Hi!"}),
        Task('two', EchoAction, {"text": "How are you?"}),
        Task('three', EchoAction, {"text": "See you later."}),
    )

    engine = taskflow.engines.load(flow, namespace='apostrophe.engines')

    engine.run()

if __name__ == '__main__':
    main()
