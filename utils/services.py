from nameko.rpc import rpc
from nameko_sentry import SentryReporter
from .dependency_providers import RpcMethodList


class MethodDiscovery:
    """
    Gives your service method discovery.
    """

    method_names: list = RpcMethodList()

    @rpc
    def methods(self):
        return self.method_names


class ErrorTracking:
    """
    Gives your service Sentry.io error tracking.

    Requires the following values in config.yaml
    SENTRY:
         DSN: ${SENTRY_DSN}
    """

    sentry = SentryReporter()


class BaseService(MethodDiscovery, ErrorTracking):
    pass
