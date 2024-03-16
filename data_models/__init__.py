import json

from pydantic import BaseModel

from services.requests import RequestMethod


class BaseDataModel(object):
    url: str
    pydantic_model = BaseModel
    data_list_attr = 'results'

    def __init__(self, page, **kwargs):
        self.page_link = page
        self.data = self.__get_data(**kwargs)

    @property
    def result_list(self):
        return getattr(self.data, self.__class__.data_list_attr)

    def __get_pydantic_response(self, **kwargs):
        response = self.page_link.current_view.auth_service.send_closed_request(
            RequestMethod.GET,
            self.__class__.url,
            **kwargs
        )
        if not response.ok:
            raise ConnectionError('Server unavailable')
        data = self.__validate_response(response)
        return data

    def __get_data(self, **kwargs):
        return self.__get_pydantic_response(**kwargs)

    def __validate_response(self, response):
        return self.__class__.pydantic_model.model_validate_json(
            json.dumps(response.json())
        )