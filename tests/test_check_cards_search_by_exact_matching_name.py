from allure_commons.types import AttachmentType
from random import randint
from pokemon_API_project_tests.utils.api_methods import api_method
from pokemon_API_project_tests.utils.browser_actions import browser_action
from selenium import webdriver
import allure


def test_check_cards_search_by_exact_matching_name(base_url, search):
    with allure.step("Get cards list by search request"):
        response = api_method.search_cards_by_exact_matching_name(base_url, search)

    with allure.step("Check response status code"):
        assert response.status_code == 200

    with allure.step("Check first result's Pokemon name"):
        response = response.json()
        pokemon_name = response['data'][0]['name']
        assert search.lower() == pokemon_name.lower()

    with allure.step("Open random card from search results in browser if possible"):
        cards_amount = len(response['data'])
        n = randint(0, cards_amount - 1)
        image_link = response["data"][n]["images"]["large"]
        browser = webdriver.Chrome()
        browser.get(image_link)

        def quit_browser():
            browser.close()
            browser.quit()

        if browser_action.element_is_present(browser, '//img'):
            allure.attach(image_link, name=f'Random card found by search request "{search}"', attachment_type=AttachmentType.TEXT)
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            quit_browser()
        else:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            quit_browser()
            assert False, "Error while loading card."
