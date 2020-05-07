'`{{cookiecutter.project_slug}}.main.py`'

from {{ cookiecutter.project_slug }} import (
    input_mapper,
    output_mapper,
    cli_format_mapper,
    output_files_mapper,
    func_mapper,
)
