from app.config import config_settings
from app.models import BaseModel
from app.models.user import User


class VMServer(BaseModel):
    '''
    Server model class
    '''
    uptime: int
    users: [User]

    def __init__(self, id: int, name: str = config_settings.dummy_data().file_name(), users: [User] = None):
        BaseModel.__init__(self, id, name)
        self.uptime = 0
        self.users = users if users else []

    def __lt__(self, size) -> bool:
        '''
        Sets the expected behavior when sorting the servers.
        :param size:
        :return: bool
        '''
        return len(self.users) < len(size)

    def update_users(self, new_users: User):
        '''
        Adds a new user to the server.
        :param new_users: User
        :return:
        '''
        self.users.append(new_users)

    def update_tick(self):
        '''
        Updates all users process countdown.
        '''
        for idx in range(len(self.users) - 1, -1, -1):
            if not self.users[idx].update_process():
                self.users.pop(idx)
        self.uptime += 1

    def keep_alive(self) -> bool:
        '''
        Check the users lists.
        Returns if the server is empty or not.
        :return: bool
        '''
        return True if self.users else False
