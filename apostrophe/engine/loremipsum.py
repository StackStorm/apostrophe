from taskflow.engines import base as engine
from apostrophe.persistence.storage import Storage


class Engine(engine.EngineBase):
    def __init__(self, flow, flow_detail, backend, conf):
        super(Engine, self).__init__(flow, flow_detail, backend, conf)
        self._compiled = False

    @property
    def _storage_cls(self):
        return Storage

    def compile(self):
        if self._compiled:
            return
        self._compiled = True

    def run(self):
        for task in self._flow:
            task.execute()

    def suspend(self):
        pass
