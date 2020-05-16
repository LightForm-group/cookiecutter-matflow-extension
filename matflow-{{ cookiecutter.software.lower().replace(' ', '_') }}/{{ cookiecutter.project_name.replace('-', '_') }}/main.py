'`{{ cookiecutter.project_name.replace("-", "_") }}.main.py`'

from {{ cookiecutter.project_name.replace('-', '_') }} import (
    input_mapper,
    output_mapper,
    cli_format_mapper,
    register_output_file,
    func_mapper,
    software_versions,
)
