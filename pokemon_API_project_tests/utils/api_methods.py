import allure
import json
import logging
import requests
from allure_commons.types import AttachmentType

class APIMethods:
    def get_cards_list(self, base_url):
        response = requests.get(url=base_url)
        allure.attach(body=response.request.url, name="Request URL", attachment_type=AttachmentType.TEXT)
        allure.attach(body=response.request.method, name="Request method", attachment_type=AttachmentType.TEXT)
        allure.attach(body=str(response.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
                      extension='txt')
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response body",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info("Request: " + response.request.url)
        logging.info("Response code " + str(response.status_code))
        logging.info("Response: " + response.text)
        return response

    def search_cards_by_exact_matching_name(self, base_url, search_request):
        response = requests.get(url=base_url + f'?q=!name:{search_request}')
        allure.attach(body=response.request.url, name="Request URL", attachment_type=AttachmentType.TEXT)
        allure.attach(body=response.request.method, name="Request method", attachment_type=AttachmentType.TEXT)
        allure.attach(body=str(response.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
                      extension='txt')
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response body",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info("Request: " + response.request.url)
        logging.info("Response code " + str(response.status_code))
        logging.info("Response: " + response.text)
        return response


api_method = APIMethods()
