from allure_commons.types import AttachmentType
from pokemon_API_project_tests.utils.api_methods import api_method
from random import randint
import allure
import json


def test_check_card_info_by_id(base_url):
    with allure.step("Get cards list"):
        response = api_method.get_cards_list(base_url)

        with allure.step("Check response status code"):
            assert response.status_code == 200

        with allure.step("Check that page size is default (250 cards per page)"):
            response = response.json()
            page_size = response['pageSize']
            assert page_size == 250, f'Page size is {page_size} instead of 250.'

    with allure.step("Get random card info"):
        n = randint(0, page_size - 1)
        checked_card = response["data"][n]
        card_id = checked_card['id']
        allure.attach(body=json.dumps(checked_card, indent=4, ensure_ascii=True), name="Random card info",
                      attachment_type=AttachmentType.JSON, extension="json")

    with allure.step("Get card info by card id"):
        response = api_method.get_card_by_id(base_url, card_id)

        with allure.step("Check response status code"):
            assert response.status_code == 200

    with allure.step("Check that card found by id is the same as card with its id in cards list"):
        response = response.json()
        card_found_by_id = response["data"]
        allure.attach(body=json.dumps(card_found_by_id, indent=4, ensure_ascii=True), name="Card found by id",
                      attachment_type=AttachmentType.JSON, extension="json")
        assert checked_card == card_found_by_id
