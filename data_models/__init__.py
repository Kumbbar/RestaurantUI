import json

from pydantic import BaseModel
from pydantic_core import ValidationError

from services.requests import RequestMethod


class BaseDataModel(object):
    url: str
    pydantic_model = BaseModel
    data_list_attr = 'results'

    def __init__(self, page, extra_url='', **kwargs):
        self.page_link = page
        self.extra_url = extra_url
        self.data = self.__get_data(**kwargs)

    @property
    def result_list(self):
        return getattr(self.data, self.__class__.data_list_attr, [])

    def __get_pydantic_response(self, **kwargs):
        response = self.page_link.current_view.auth_service.send_closed_request(
            RequestMethod.GET,
            f'{self.__class__.url}{self.extra_url}',
            **kwargs
        )
        if not response.ok:
            raise ConnectionError('Server unavailable')
        data = self.__validate_response(response)
        return data

    def __get_data(self, **kwargs):
        return self.__get_pydantic_response(**kwargs)


    def __validate_response(self, response):
        try:
            return self.__class__.pydantic_model.model_validate_json(
                json.dumps(response.json())
            )
        except ValidationError:
            return dict()