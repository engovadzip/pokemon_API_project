from allure_commons.types import AttachmentType
from pokemon_API_project_tests.utils.api_methods import api_method
from pokemon_API_project_tests.utils.browser_actions import browser_action
from random import randint
import allure


@allure.story("Check GET card by id")
def test_get_card_by_id(cards_url):
    with allure.step("Get cards list"):
        response = api_method.get_cards_or_sets_list(cards_url)

        with allure.step("Check response status code"):
            assert response.status_code == 200, f"Response status code is {response.status_code} instead of 200."

        with allure.step("Check that page size is default (250 objects per page)"):
            response = response.json()
            page_size = response['pageSize']
            assert page_size == 250, f'Page size is {page_size} instead of 250.'

    with allure.step("Open random page"):
        response = api_method.open_random_page(cards_url)
        response = response.json()

    with allure.step("Get random card id"):
        objects_on_page = response['count']
        n = randint(0, objects_on_page - 1)
        checked_card = response["data"][n]
        card_id = checked_card['id']
        allure.attach(card_id, name='Card id', attachment_type=AttachmentType.TEXT)

    with allure.step("Get card info by card id"):
        response = api_method.get_card_or_set_by_id(cards_url, card_id)

        with allure.step("Check response status code"):
            assert response.status_code == 200, f"Response status code is {response.status_code} instead of 200."

    with allure.step("Check that card found by id is the same as card with its id in cards list"):
        response = response.json()
        card_found_by_id = response["data"]
        assert checked_card == card_found_by_id, "An error occurred while searching for a card by id."

    with allure.step("Open card in browser"):
        image_link = card_found_by_id["images"]["large"]

        browser = browser_action.setup_browser()
        browser_action.open_link(browser, image_link)

        if browser_action.element_is_present(browser, '//img'):
            allure.attach(browser.get_screenshot_as_png(), name=f'Card found by id "{card_id}"',
                          attachment_type=AttachmentType.PNG)
            allure.attach(image_link, name='Card image link', attachment_type=AttachmentType.TEXT)
            browser_action.quit_browser(browser)
        else:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            browser_action.quit_browser(browser)
            assert False, "Error while loading card."
