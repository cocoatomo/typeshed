from typing import Any, Sequence, Optional, Iterable
from wsgiref.types import WSGIApplication, WSGIEnvironment, StartResponse

class CGIRootFix:
    app = ...  # type: Any
    app_root = ...  # type: Any
    def __init__(self, app, app_root=''): ...
    def __call__(self, environ, start_response): ...

LighttpdCGIRootFix = ...  # type: Any

class PathInfoFromRequestUriFix:
    app = ...  # type: Any
    def __init__(self, app): ...
    def __call__(self, environ, start_response): ...

class ProxyFix(object):
    app: WSGIApplication
    num_proxies: int
    def __init__(self, app: WSGIApplication, num_proxies: int = ...) -> None: ...
    def get_remote_addr(self, forwarded_for: Sequence[str]) -> Optional[str]: ...
    def __call__(self, environ: WSGIEnvironment, start_response: StartResponse) -> Iterable[bytes]: ...

class HeaderRewriterFix:
    app = ...  # type: Any
    remove_headers = ...  # type: Any
    add_headers = ...  # type: Any
    def __init__(self, app, remove_headers=None, add_headers=None): ...
    def __call__(self, environ, start_response): ...

class InternetExplorerFix:
    app = ...  # type: Any
    fix_vary = ...  # type: Any
    fix_attach = ...  # type: Any
    def __init__(self, app, fix_vary=True, fix_attach=True): ...
    def fix_headers(self, environ, headers, status=None): ...
    def run_fixed(self, environ, start_response): ...
    def __call__(self, environ, start_response): ...
