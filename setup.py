from setuptools import setup, find_packages
from singletonmeta import __version__

setup(
    name="simplestatemachine",
    version=__version__,
    packages=find_packages("singletonmeta"),
    author="Nicolas Limage",
    author_email="github@xephon.org",
    description="singleton metaclass",
    license="GPL",
    keywords="singleton metaclass",
    url="https://github.com/nlm/python-singletonmeta",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
)
