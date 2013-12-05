import sys
from pyramid_celery.commands import CommandMixin
from celery.bin.celery import CeleryCommand

try:
    from celery.concurrency.processes.forking import freeze_support
except ImportError:  # pragma: no cover
    freeze_support = lambda: True  # noqa



class WorkerCommand(CommandMixin, CeleryCommand):
    preload_options = ()

    def execute_from_commandline(self, argv=None):
        if argv is None:
            argv = self.setup_app_from_commandline(argv)
        print "ARGV", argv
        return CeleryCommand.execute_from_commandline(self, argv)


def main():
    # Fix for setuptools generated scripts, so that it will
    # work with multiprocessing fork emulation.
    # (see multiprocessing.forking.get_preparation_data())
    if __name__ != "__main__":
        sys.modules["__main__"] = sys.modules[__name__]
    freeze_support()
    worker = WorkerCommand()
    worker.execute_from_commandline()
