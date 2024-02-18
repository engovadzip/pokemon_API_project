from allure_commons.types import AttachmentType
from pokemon_API_project_tests.utils.api_methods import api_method
from pokemon_API_project_tests.utils.browser_actions import browser_action
from random import randint
import allure


def test_get_set_by_id(sets_url):
    with allure.step("Get cards list"):
        response = api_method.get_cards_or_sets_list(sets_url)

        with allure.step("Check response status code"):
            assert response.status_code == 200, f"Response status code is {response.status_code} instead of 200."

        with allure.step("Check that page size is default (250 objects per page)"):
            response = response.json()
            page_size = response['pageSize']
            assert page_size == 250, f'Page size is {page_size} instead of 250.'

    with allure.step("Open random page"):
        response = api_method.open_random_page(sets_url)
        response = response.json()

    with allure.step("Get random set id"):
        objects_on_page = response['count']
        n = randint(0, objects_on_page - 1)
        checked_card = response["data"][n]
        set_id = checked_card['id']
        allure.attach(set_id, name='Set id', attachment_type=AttachmentType.TEXT)

    with allure.step("Get set info by set id"):
        response = api_method.get_card_or_set_by_id(sets_url, set_id)

        with allure.step("Check response status code"):
            assert response.status_code == 200, f"Response status code is {response.status_code} instead of 200."

    with allure.step("Check that set found by id is the same as set with its id in sets list"):
        response = response.json()
        card_found_by_id = response["data"]
        assert checked_card == card_found_by_id, "An error occurred while searching for a set by id."
