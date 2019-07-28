from faker import Faker


class Error(Exception):
    def __init__(self, message, errors):
        Exception.__init__(self, message)
        self.errors = errors


class TTaskValueOutOfRange(Error):
    pass


class UMaxValueOutOfRange(Error):
    pass


class Configs:
    ttask: int = None
    umax: int = None
    tick: int = None  # TODO thread using seconds as ticks

    def setup_config(self, file):
        with open(file, 'r') as file:
            lines = file.read().splitlines()

        self.ttask = int(lines[0])
        self.umax = int(lines[1])
        self.validate_configs()
        self.next_ticks = lines[2:]

    def validate_configs(self):
        if not 1 <= self.ttask <= 10:
            raise TTaskValueOutOfRange("[ttask] input is out the expected range of 1 - 10", self.ttask)

        if not 1 <= self.umax <= 10:
            raise UMaxValueOutOfRange("[umax] input is out the expected range of 1 - 10", self.umax)

    def get_next_tick_users(self) -> int:
        if not self.next_ticks:
            return 0
        return int(self.next_ticks.pop(0))

    def dummy_data(self) -> Faker:
        return Faker('pt_BR')


config_settings = Configs()
