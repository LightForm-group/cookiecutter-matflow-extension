'`{{ cookiecutter.project_name.replace("-", "_") }}.__init__.py`'

from functools import partial

from {{ cookiecutter.project_name.replace('-', '_') }}._version import __version__

from matflow import (
    input_mapper,
    output_mapper,
    cli_format_mapper,
    register_output_file,
    func_mapper,
    software_versions,
)

SOFTWARE = '{{ cookiecutter.software.lower().replace(" ", "_").replace("-", "_") }}'

input_mapper = partial(input_mapper, software=SOFTWARE)
output_mapper = partial(output_mapper, software=SOFTWARE)
cli_format_mapper = partial(cli_format_mapper, software=SOFTWARE)
register_output_file = partial(register_output_file, software=SOFTWARE)
func_mapper = partial(func_mapper, software=SOFTWARE)
software_versions = partial(software_versions, software=SOFTWARE)

# Import any modules that contain functions decorated by the matflow function decorators.
# This import must come after the above `partial`s.
from {{ cookiecutter.project_name.replace('-', '_') }} import main
