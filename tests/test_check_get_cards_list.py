from pokemon_API_project_tests.utils.api_methods import api_method
import allure


def test_check_get_cards(base_url):
    with allure.step("Get cards list"):
        response = api_method.get_cards_list(base_url)

    with allure.step("Check response status code"):
        assert response.status_code == 200

    with allure.step("Check response JSON content length"):
        response = response.json()
        assert len(response) == 5

    with allure.step("Check that page size is default (250 cards per page)"):
        page_size = response['pageSize']
        assert page_size == 250, f'Page size is {page_size} instead of 250.'

    with allure.step("Check that cards amount matches the page size"):
        cards_amount = len(response['data'])
        assert cards_amount == 250, f'Cards amount is {cards_amount} instead of 250.'