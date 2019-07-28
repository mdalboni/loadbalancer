from app.config import config_settings
from app.models import BaseModel


class User(BaseModel):
    '''
    User model class.
    '''
    time_left: int

    def __init__(self, id: int, name=config_settings.dummy_data().name()):
        BaseModel.__init__(self, id, name)
        self.time_left = config_settings.ttask

    def update_process(self) -> int:
        '''
        Updates the time left to end the user process.
        :return: bool
        '''
        self.time_left -= 1
        return self.time_left
