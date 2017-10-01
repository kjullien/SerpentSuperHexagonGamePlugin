from serpent.game import Game

from .api.api import SuperHexagonAPI

from serpent.utilities import Singleton


class SerpentSuperHexagonGame(Game, metaclass=Singleton):
    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"

        kwargs["window_name"] = "Super Hexagon"

        kwargs["app_id"] = "221640"
        kwargs["app_args"] = None

        super().__init__(**kwargs)

        self.api_class = SuperHexagonAPI
        self.api_instance = None

    @property
    def screen_regions(self):
        regions = {
            "MENU_MAIN_TITLE": (127, 174, 268, 635),
            "MENU_MAIN_SELECTED": (356, 266, 384, 503),
            "MENU_MAIN_LEFT_ARROW": (411, 79, 332, 160),
            "MENU_MAIN_RIGHT_ARROW": (412, 687, 332, 608),
            "MENU_MAIN_ESC_QUIT": (30, 602, 3, 767),
            "MENU_MAIN_SPACE_SELECT": (455, 214, 473, 556),

            "MENU_OPTIONS_TITLE": (93, 577, 149, 191),
            "MENU_OPTIONS_FULLSCREEN": (184, 216, 204, 553),
            "MENU_OPTIONS_SOUND": (221, 220, 245, 552),
            "MENU_OPTIONS_VSYNC": (262, 228, 287, 545),
            "MENU_OPTIONS_ARCADE": (303, 231, 325, 538),
            "MENU_OPTIONS_ARCADE_SUBTEXT": (436, 16, 472, 752),
            "MENU_OPTIONS_DELETE_RECORDS": (340, 229, 368, 530),
            "MENU_OPTIONS_ESC": (29, 446, 3, 768),

            # I wish I had the patience for the credits...

            "LEVEL_SELECT_TAB_HIGH_SCORES": (27, 17, 4, 291),
            "LEVEL_SELECT_ESC": (4, 448, 26, 764),
            "LEVEL_SELECT_LEVEL_NAME": (80, 131, 137, 577),
            "LEVEL_SELECT_DIFFICULTY": (137, 395, 160, 569),  # only value
            "LEVEL_SELECT_TIME": (162, 394, 186, 599),  # only value
            "LEVEL_SELECT_START": (222, 217, 246, 554),
            # arrows ?

            "GAME_PLAYING_LEVEL": (5, 7, 26, 119),
            "GAME_PLAYING_PROGRESS_BAR": (26, 13, 32, 107),
            "GAME_PLAYING_TIME": (49, 766, 5, 667),  # only value

            "GAME_DEAD_TAB_HIGH_SCORES": (27, 17, 4, 291),
            "GAME_DEAD_ESC_STAGE_SELECT": (26, 468, 4, 765),
            "GAME_DEAD_LEVEL": (206, 250, 164, 1),
            "GAME_DEAD_SHAPE": (210, 102, 231, 251),
            "GAME_DEAD_LAST_TIME": (164, 643, 205, 768),  # only value
            "GAME_DEAD_BEST_TIME": (253, 635, 294, 767), # only value

            # Just learned while doing the regions that there was a high score board...

        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
