from serpent.game_api import GameAPI


class SuperHexagonAPI(GameAPI):

    def __init__(self, game=None):
        super().__init__(game=game)

    def my_api_function(self):
        pass

    class Controls:

        @classmethod
        def go_left(cls):
            api = SuperHexagonAPI.instance
            api.input_controller.tap_key("left")

        @classmethod
        def go_right(cls):
            api = SuperHexagonAPI.instance
            api.input_controller.tap_key("right")

        @classmethod
        def select(cls):
            api = SuperHexagonAPI.instance
            api.input_controller.tap_key("space")

        @classmethod
        def retry(cls):
            api = SuperHexagonAPI.instance
            api.input_controller.tap_key("r")

        @classmethod
        def exit(cls):
            api = SuperHexagonAPI.instance
            api.input_controller.tap_key("esc")