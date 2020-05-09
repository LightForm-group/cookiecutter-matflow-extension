'`{{cookiecutter.project_slug}}.__init__.py`'

from functools import partial

from {{cookiecutter.project_slug}}._version import __version__

from matflow import (
    input_mapper,
    output_mapper,
    cli_format_mapper,
    register_output_file,
    func_mapper,
)

input_mapper = partial(input_mapper, software='{{cookiecutter.software_slug}}')
output_mapper = partial(output_mapper, software='{{cookiecutter.software_slug}}')
cli_format_mapper = partial(cli_format_mapper, software='{{cookiecutter.software_slug}}')
register_output_file = partial(register_output_file, software='{{cookiecutter.software_slug}}')
func_mapper = partial(func_mapper, software='{{cookiecutter.software_slug}}')

# This import must come after assigning the partial functions:
from {{cookiecutter.project_slug}} import main
