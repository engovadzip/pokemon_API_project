from allure_commons.types import AttachmentType
from pokemon_API_project_tests.utils.api_methods import api_method
from pokemon_API_project_tests.utils.browser_actions import browser_action
from pokemon_API_project_tests.utils.response_actions import response_action
import allure


def test_check_cards_search_by_exact_matching_name(cards_url, search):
    with allure.step("Get cards list by search request"):
        response = api_method.search_cards_or_sets_by_exact_matching_name(cards_url, search)

    with allure.step("Check response status code"):
        assert response.status_code == 200, f"Response status code is {response.status_code} instead of 200."

    with allure.step("Check that response' Pokemon names exact match search request"):
        response = response.json()
        response_action.check_search_results_exact_match_search_request(response, search)

    with allure.step("Open random card from search results in browser"):
        image_link = response_action.get_random_card_link(response)

        browser = browser_action.setup_browser()
        browser_action.open_link(browser, image_link)

        if browser_action.element_is_present(browser, '//img'):
            allure.attach(browser.get_screenshot_as_png(), name=f'One of the cards found by search request "{search}"',
                          attachment_type=AttachmentType.PNG)
            allure.attach(image_link, name='Card link', attachment_type=AttachmentType.TEXT)
            browser_action.quit_browser(browser)
        else:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            browser_action.quit_browser(browser)
            assert False, "Error while loading card."
