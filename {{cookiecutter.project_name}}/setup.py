"""Pip installation script."""

import os
import re
from setuptools import find_packages, setup


def get_version():

    ver_file = '{{cookiecutter.project_slug}}/_version.py'
    with open(ver_file) as handle:
        ver_str_line = handle.read()

    ver_pattern = r'^__version__ = [\'"]([^\'"]*)[\'"]'
    match = re.search(ver_pattern, ver_str_line, re.M)
    if match:
        ver_str = match.group(1)
    else:
        msg = 'Unable to find version string in "{}"'.format(ver_file)
        raise RuntimeError(msg)

    return ver_str


def get_long_description():
    readme_file = 'README.md'
    with open(readme_file, encoding='utf-8') as handle:
        contents = handle.read()
    return contents


def get_changelog():
    changelog_file = 'CHANGELOG.md'
    with open(changelog_file, encoding='utf-8') as handle:
        contents = handle.read()
    return contents

{% set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Mozilla Public License 2.0 (MPL 2.0)': 'OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)'
} %}
setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Operating System :: OS Independent',
        {%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
        {%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="{{ cookiecutter.project_short_description }}",
    entry_points="""
        [matflow.extension]
        {{ cookiecutter.software_slug }}={{ cookiecutter.project_slug }}
    """,
    install_requires=[
        'matflow',
    ],
    {%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
    {%- endif %}
    long_description=get_long_description() + '\n\n' + get_changelog(),
    long_description_content_type='text/markdown',
    keywords='matflow, materials-science, computational-workflow',
    name='{{ cookiecutter.project_name }}',
    packages=find_packages(),    
    {%- if cookiecutter.github_org is defined %}
    project_urls={
        'GitHub': 'https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.project_name }}'
    },
    {%- else %}
    project_urls={
        'GitHub': 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}'
    },
    {%- endif %}
    version=get_version(),
    zip_safe=True,
)
