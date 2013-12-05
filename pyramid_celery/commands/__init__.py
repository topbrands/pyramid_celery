import sys
from pyramid.paster import bootstrap
from celery.app import default_app


class CommandMixin(object):
    preload_options = []
    conf  = None


    def setup_app_from_commandline(self, argv):
        if argv is None:
            argv = sys.argv
        print argv
        if len(argv) < 2:
            print >> sys.stderr, 'No configuration file specified.'
            return argv
        if not self.conf:
            self.conf = argv.pop(1)
            argv.insert(1, 'worker')
        bootstrap(self.conf)

        self.app = default_app
        return argv
