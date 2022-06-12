import functools
import subprocess
from typing import Any, Dict, Optional


class Git:
    def run(self, cmd: str, *args: str, capture_stdout: bool = True) -> Optional[str]:
        kwargs: Dict[str, Any] = {"check": True}
        if capture_stdout:
            kwargs["stdout"] = subprocess.PIPE
            kwargs["text"] = True
        r = subprocess.run(["git", cmd, *args], **kwargs)
        return r.stdout.strip() if capture_stdout else None

    def __getattr__(self, name: str) -> functools.partial[Optional[str]]:
        name = name.replace("_", "-")
        return functools.partial(self.run, name)
