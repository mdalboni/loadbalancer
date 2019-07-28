from faker import Faker


class Error(Exception):
    """
    Custom Exception base class
    """

    def __init__(self, message, errors):
        Exception.__init__(self, message)
        self.errors = errors


class TTaskValueOutOfRange(Error):
    """
    Custom Exception for TTask
    """
    pass


class UMaxValueOutOfRange(Error):
    """
    Custom Exception for UMax
    """
    pass


class Configs:
    """
    Configuration class
    """
    ttask: int = None
    umax: int = None
    user_queue: list = None

    def setup_config(self, file: str):
        """
        Update the configuration parameters for the whole app.
        :param file: relative or absolute path to file
        """
        with open(file, 'r') as file:
            lines = file.read().splitlines()

        self.ttask = int(lines[0])
        self.umax = int(lines[1])
        self.validate_configs()

        self.user_queue = lines[2:]

    def validate_configs(self):
        """
        Check if loaded values are in the expected range
        """
        if not 1 <= self.ttask <= 10:
            raise TTaskValueOutOfRange("[ttask] input is out the expected range of 1 - 10", self.ttask)

        if not 1 <= self.umax <= 10:
            raise UMaxValueOutOfRange("[umax] input is out the expected range of 1 - 10", self.umax)

    def get_next_tick_users(self) -> int:
        if not self.user_queue:
            return 0
        return int(self.user_queue.pop(0))

    def dummy_data(self) -> Faker:
        return Faker('pt_BR')


config_settings = Configs()
