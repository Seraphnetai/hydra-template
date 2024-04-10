import logging
from typing import TYPE_CHECKING, TypedDict

from pydantic import BaseModel

if TYPE_CHECKING:
    from logging import Logger

    from config import {{cookiecutter.main_class_name}}Config


class {{cookiecutter.main_class_name.replace('Validator', '')}}ReportInput(TypedDict):
    """"""

class {{cookiecutter.main_class_name.replace('Validator', '')}}ReportInputDTO(BaseModel):
    """"""


class {{cookiecutter.main_class_name}}:
    """"""
    _logger: 'Logger'
    _config: '{{cookiecutter.main_class_name}}Config'
    _report_input: {{cookiecutter.main_class_name.replace('Validaor', '')}}ReportInput
    _report_input_dto: {{cookiecutter.main_class_name.replace('Validaor', '')}}ReportInputDTO
    _criteria_met: bool

    def __init__(self, cfg: '{{cookiecutter.main_class_name}}Config', logger: 'Logger' = None):
        self._logger = logger if logger is not None else logging.getLogger(__name__)
        self._config = cfg
        self._report_input = {}
        self._criteria_met = True

    def validate(self) -> {{cookiecutter.main_class_name.replace('Validator', '')}}ReportInputDTO:
        """
        """

        return self._report_input_dto
    

    def _get_report_input_dto(self) -> {{cookiecutter.main_class_name.replace('Validator', '')}}ReportInputDTO:
        """
        Tworzy wyjściowy obiekt zawierający wsad do raportu JMC.
        """