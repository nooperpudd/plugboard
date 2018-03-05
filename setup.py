# encoding:utf-8
import codecs
import os
import re
from distutils.core import setup


def find_version(*file_paths):
    """
    Don't pull version by importing package as it will be broken due to as-yet uninstalled
    dependencies, following recommendations at  https://packaging.python.org/single_source_version,
    extract directly from the init file
    """
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *file_paths), 'r', encoding="utf-8") as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="devops_plugins",
    version=find_version("devops_plugins", "__init__.py"),
    packages=["devops_plugins"],
    platforms=["win32", "linux"],
    description="Python wrapper for hiredis",
    url="https://github.com/redis/hiredis-py",
    author="Jan-Erik Rediger, Pieter Noordhuis",
    author_email="janerik@fnordig.de, pcnoordhuis@gmail.com",
    keywords=["Redis"],
    license="BSD",
    package_dir={"devops_plugins": "devops_plugins"},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
    ],
)
