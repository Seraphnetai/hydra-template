from dataclasses import dataclass

from hydra.core.config_store import ConfigStore


@dataclass
class {{cookiecutter.main_class_name}}Config:
    """"""


def register_config_scheme() -> None:
    """Rejestruje domyślny schemat konfiguracji"""
    cs = ConfigStore.instance()
    cs.store(name="default_config_schema", node={{cookiecutter.main_class_name}}Config)