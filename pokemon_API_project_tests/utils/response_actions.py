from random import choice


class ResponseActions:
    def get_random_card_link(self, response):
        random_card = choice(response["data"])
        image_link = random_card["images"]["large"]
        return image_link

    def check_search_results_exact_match_search_request(self, response, search):
        n = len(response['data'])
        for i in range(n):
            pokemon_name = response['data'][i]['name']
            assert search.lower() == pokemon_name.lower(), (f'Search request: "{search}", '
                                                            f'one of search results: "{pokemon_name}".')


response_action = ResponseActions()