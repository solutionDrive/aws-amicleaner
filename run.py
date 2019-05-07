from __future__ import print_function
from __future__ import absolute_import
import sys

from amicleaner.utils import parse_args
from amicleaner.cli import App


def main():

    args = parse_args(sys.argv[1:])
    if not args:
        sys.exit(1)

    app = App(args)

    if app.version is True:
        app.print_version()
    else:
        app.run_cli()


if __name__ == "__main__":
    main()
