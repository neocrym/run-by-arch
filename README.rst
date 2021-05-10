##########################################################################
run-by-arch: Run different shell commands depending on your OS or CPU arch
##########################################################################

``run-by-arch`` helps you organize and run programs compiled for varying operating systems and CPU target architectures.

Installation
^^^^^^^^^^^^
``run-by-arch`` is a Python program that works with both Python 2 and 3. You can install it with ``pip install run-by-arch``.

``run-by-arch`` does not depend on any other Python packages, so it is safe to install it into your system Python.

Why do I need run-by-arch?
^^^^^^^^^^^^^^^^^^^^^^^^^^
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
