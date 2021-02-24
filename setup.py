#!/usr/bin/env python
import os
import re
import sys

from setuptools import setup

sys.path.insert(0, os.path.dirname(__file__))

PACKAGES = [
    'mypackage',
]

REQUIREMENTS = {
    # Installation script (this file) dependencies
    'setup': [
        'setuptools_scm',
    ],
    'install': [
        'numpy',
        'pytest>=3.9,!=6.0.0rc1,!=6.0.0',
        'pytest-cov>=2.10.1',
        'pytest-env',
        'pytest-xdist',
    ]
}

def discover_python_files(paths, ignore):
    """Discover Python files."""
    def _ignore(path):
        """Return True if `path` should be ignored, False otherwise."""
        return any(re.match(pattern, path) for pattern in ignore)

    for path in sorted(set(paths)):
        for root, _, files in os.walk(path):
            if _ignore(path):
                continue
            for filename in files:
                filename = os.path.join(root, filename)
                if (filename.lower().endswith('.py')
                        and not _ignore(filename)):
                    yield filename


setup(
    name='MyPackage',
    version=0.1,
    author="Valeriu Predoi",
    description="An example toy package",
    long_description="bleh",
    long_description_content_type='text',
    url='https://www.flyingpigs.com',
    download_url='https://github.com/ESMValGroup/MyPackage',
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 0 - initial',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    packages=PACKAGES,
    # Include all version controlled files
    include_package_data=True,
    setup_requires=REQUIREMENTS['setup'],
    install_requires=REQUIREMENTS['install'],
    zip_safe=False,
)
