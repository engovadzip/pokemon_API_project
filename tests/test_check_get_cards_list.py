from pokemon_API_project_tests.utils.api_methods import api_method
import allure


@allure.story("Check GET cards list")
def test_check_get_cards_list(cards_url):
    with allure.step("Get cards list"):
        response = api_method.get_cards_or_sets_list(cards_url)

    with allure.step("Check response status code"):
        assert response.status_code == 200, f"Response status code is {response.status_code} instead of 200."

    with allure.step("Check response JSON content length"):
        response = response.json()
        assert len(response) == 5, f"Response length is {len(response)} instead of 5."

    with allure.step("Check that page size is default (250 cards per page)"):
        page_size = response['pageSize']
        assert page_size == 250, f'Page size is {page_size} instead of 250.'

    with allure.step("Check that cards amount matches the page size"):
        cards_count_in_data = len(response['data'])
        cards_on_page = response['count']
        assert cards_count_in_data == cards_on_page, (f'Cards amount in "data" is {cards_count_in_data}. '
                                             f'Cards amount in "count" is {cards_on_page}.')
