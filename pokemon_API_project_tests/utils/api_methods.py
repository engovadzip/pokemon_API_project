import allure
import json
import logging
import requests
from allure_commons.types import AttachmentType
from random import randint


class APIMethods:
    def attach_logs_and_response_info(self, response):
        allure.attach(body=response.request.url, name="Request URL", attachment_type=AttachmentType.TEXT)
        allure.attach(body=response.request.method, name="Request method", attachment_type=AttachmentType.TEXT)
        allure.attach(body=str(response.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
                      extension='txt')
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response body",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info("Request: " + response.request.url)
        logging.info("Response code: " + str(response.status_code))
        logging.info("Response: " + response.text)

    def get_cards_or_sets_list(self, base_url):
        response = requests.get(url=base_url)
        self.attach_logs_and_response_info(response)
        return response

    def search_cards_or_sets_by_exact_matching_name(self, base_url, search_request):
        response = requests.get(url=base_url + f'?q=!name:{search_request}')
        self.attach_logs_and_response_info(response)
        return response

    def get_card_or_set_by_id(self, base_url, id):
        response = requests.get(url=base_url + f'/{id}')
        self.attach_logs_and_response_info(response)
        return response

    def open_random_page(self, base_url):
        response = requests.get(url=base_url)
        cards_list = response.json()
        on_page = cards_list["count"]
        total_cards = cards_list["totalCount"]
        pages = total_cards // on_page
        last_page_count = total_cards % on_page
        if last_page_count > 0:
            pages += 1

        if pages == 1:
            n = 1
        else:
            n = randint(0, pages - 1)

        response = self.get_cards_or_sets_list(base_url + f'?page={n}')
        opened_page = response.json()["page"]
        assert opened_page == n, f'Opened page is {opened_page} instead of {n}.'
        return response


api_method = APIMethods()
