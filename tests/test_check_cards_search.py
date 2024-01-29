from pokemon_API_project_tests.utils.api_methods import api_method
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
