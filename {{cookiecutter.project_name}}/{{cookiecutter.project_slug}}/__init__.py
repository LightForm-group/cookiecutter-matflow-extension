'`{{cookiecutter.project_slug}}.__init__.py`'

from functools import partial

from {{cookiecutter.project_slug}}._version import __version__
from {{cookiecutter.project_slug}} import main

from matflow import (
    input_mapper,
    output_mapper,
    cli_format_mapper,
    output_files_mapper,
    func_mapper,
)

input_mapper = partial(input_mapper, software='{{cookiecutter.software_slug}}')
output_mapper = partial(output_mapper, software='{{cookiecutter.software_slug}}')
cli_format_mapper = partial(cli_format_mapper, software='{{cookiecutter.software_slug}}')
output_files_mapper = partial(output_files_mapper, software='{{cookiecutter.software_slug}}')
