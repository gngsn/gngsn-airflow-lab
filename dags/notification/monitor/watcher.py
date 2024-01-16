import logging


class Watcher:
    @classmethod
    def not_implement_yet_warning(cls):
        logging.WARN("아직 구현되지 않은 기능입니다.")
