#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Kyle Alexander Coffey",
    author_email='me@mail.phytolizer.dev',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    description="Pink Doom is Doom, but in Python/Pygame!",
    entry_points={
        'console_scripts': [
            'pink_doom=pink_doom.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pink_doom',
    name='pink_doom',
    packages=find_packages(include=['pink_doom', 'pink_doom.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Phytolizer/pink_doom',
    version='0.1.0',
    zip_safe=False,
)
