import hydra

from config import {{cookiecutter.main_class_name}}Config, register_config_scheme
from {{cookiecutter.repo_name}} import {{cookiecutter.main_class_name}}

register_config_scheme()

@hydra.main(version_base=None, config_path="config", config_name="default_config")
def main(cfg: {{cookiecutter.main_class_name}}Config):
    """"""


if __name__ == "__main__":
    main()
