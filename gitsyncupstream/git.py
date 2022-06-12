import functools
import subprocess


class Git:
    def run(self, cmd, *args, capture_stdout=True):
        kwargs = {"check": True}
        if capture_stdout:
            kwargs["stdout"] = subprocess.PIPE
            kwargs["text"] = True
        r = subprocess.run(["git", cmd, *args], **kwargs)
        return r.stdout.strip() if capture_stdout else None

    def __getattr__(self, name):
        name = name.replace("_", "-")
        return functools.partial(self.run, name)
