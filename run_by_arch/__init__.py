#!/usr/bin/env python3
"""
run-by-arch: Run different commands depending on your OS or CPU arch
"""

from __future__ import nested_scopes
from __future__ import generators
from __future__ import division
from __future__ import absolute_import
from __future__ import with_statement
from __future__ import print_function
from __future__ import unicode_literals

import errno
import os
import platform
import sys


HELP_TEXT = """run-by-arch: Run different shell commands depending on your OS or CPU arch
**************************************************************************

``run-by-arch`` helps you organize and run programs compiled for varying operating systems and CPU target architectures.

For example, if you are working on a program called ``my-program`` with binaries stored on a Network File System instance shared between 64-bit Linux and MacOS users, then users of both
operating systems can run ``run-by-arch my-program`` followed by the arguments for that program.

For a Linux user, ``run-by-arch`` will run the binary found at the directory ``./run-by-arch/linux-x86_64/my-program``.

For a MacOS user, ``run-by-arch`` will run the binary found at ``./run-by-arch/darwin-x86_64/my-program``.

If you set the environment variable ``RUN_BY_ARCH_PREFIX``, you can tell ``run-by-arch`` to look anywhere else on your filesystem.

``run-by-arch`` expects the path at ``RUN_BY_ARCH_PREFIX`` to have subdirectories named after the operating system hyphenated with the CPU architecture. If you set ``RUN_BY_ARCH_PREFIX=/prefix``, then your binaries should be located at:

- ``/prefix/darwin-x86_64/`` for 64-bit MacOS computers with Intel CPUs (not the Apple M1)
- ``/prefix/linux-x86_64/`` for 64-bit Linux computers
- ``/prefix/windows-x86_64/`` for 64-bit Windows computers
- ``/prefix/linux-i386/`` for 32-bit Linux computers
- ...and so on...

"""


DEFAULT_PREFIX = os.path.join(os.getcwd(), "run-by-arch")


RUN_BY_ARCH_PREFIX = os.environ.get("RUN_BY_ARCH_PREFIX", DEFAULT_PREFIX)


def platform_name():
    uname = platform.uname()
    operating_system = uname[0].lower()
    raw_architecture = uname[4].lower()
    if raw_architecture == "amd64":
        architecture = "x86_64"
    else:
        architecture = raw_architecture
    return "-".join((operating_system, architecture))


PLATFORM_PATH = os.path.join(RUN_BY_ARCH_PREFIX, platform_name())


def main():
    CMD_AND_ARGS = sys.argv[1:]
    if CMD_AND_ARGS:
        CMD_NAME = os.path.join(PLATFORM_PATH, CMD_AND_ARGS[0])
        try:
            os.execv(CMD_NAME, CMD_AND_ARGS)
        except OSError as exc:
            print(CMD_NAME, ": ", exc.__class__.__name__, ": ", str(exc), sep="")
            sys.exit(1)
    else:
        print(HELP_TEXT)


if __name__ == "__main__":
    main()
