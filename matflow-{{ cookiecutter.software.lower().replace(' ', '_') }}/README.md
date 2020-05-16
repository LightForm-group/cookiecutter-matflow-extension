{% set project_slug = cookiecutter.project_name.replace('-', '_') -%}
{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}
{% if is_open_source %}
[![PyPI version](https://img.shields.io/pypi/v/{{ project_slug }}.svg)](https://pypi.python.org/pypi/{{ project_slug }})
[![Documentation Status](https://readthedocs.org/projects/{{ project_slug | replace("_", "-") }}/badge/?version=latest)](https://{{ project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest)
{%- endif %}

{{ cookiecutter.project_short_description }}
{% if is_open_source %}
- Documentation: https://{{ project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}
## Features
- TODO
