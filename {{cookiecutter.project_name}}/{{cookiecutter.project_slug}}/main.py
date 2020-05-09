'`{{cookiecutter.project_slug}}.main.py`'

from {{ cookiecutter.project_slug }} import (
    input_mapper,
    output_mapper,
    cli_format_mapper,
    register_output_file,
    func_mapper,
)
