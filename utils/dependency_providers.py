from nameko.extensions import DependencyProvider


class RpcMethodList(DependencyProvider):
    def get_dependency(self, worker_ctx):
        return [ep.method_name for ep in list(self.container.entrypoints) if type(ep).__name__ == "Rpc"]
