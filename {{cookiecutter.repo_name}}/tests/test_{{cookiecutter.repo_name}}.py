import pytest

from {{cookiecutter.repo_name}} import {{cookiecutter.main_class_name}}
from {{cookiecutter.repo_name}}.config import register_config_scheme

from hydra import compose, initialize

register_config_scheme()


def test_init():
    with initialize(version_base=None, config_path="../{{cookiecutter.repo_name}}/config"):
        cfg = compose(config_name="default_config", overrides=[]) # f"...={...}"
    {{cookiecutter.repo_name}} = {{cookiecutter.main_class_name}}(cfg)
    assert isinstance({{cookiecutter.repo_name}}, {{cookiecutter.main_class_name}})