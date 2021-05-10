from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

with open(".version.txt", "r") as fh:
    version = fh.read().strip()

setup(
    name="run-by-arch",
    version=version,
    license="MIT",
    url="https://github.com/neocrym/run-by-arch",
    description="Run different shell commands depending on your OS or CPU arch.",
    long_description=long_description,
    author="Neocrym Records Inc.",
    author_email="engineering@neocrym.com",
    packages=["run_by_arch"],
    entry_points=dict(
        console_scripts=["run-by-arch=run_by_arch:main"],
    ),
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
)
