from taskflow import flow


class Flow(flow.Flow):
    def __init__(self, name):
        super(Flow, self).__init__(name)
        self._children = []

    def add(self, *items):
        self._children.extend(items)
        return self

    def __len__(self):
        return len(self._children)

    # Why aren't __len__ and __iter__ abstract in task.Flow?
    def __iter__(self):
        for child in self._children:
            yield child

    def __getitem__(self, index):
        return self._children[index]

    @property
    def provides(self):
        return None

    @property
    def requires(self):
        return None