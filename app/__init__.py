from app.config import config_settings
from app.models.user import User
from app.models.vm_server import VMServer


class Application:
    '''
    This is the core of the application module.
    '''
    total_users: int
    vm_servers: [VMServer]
    output: str
    total_uptime: int
    test_mode: bool

    def __init__(self, test=False):
        '''
        :param test: Use this param to return the result value and bypass the writing process.
        '''
        self.vm_servers = []
        self.total_users = 0
        self.output = ''
        self.total_uptime = 0
        self.test_mode = test

    def run(self):
        '''
        Starts the process and simulates the ticks and servers.

        :return: If test is enabled it will return the output text
        '''
        new_users = 1

        while new_users or self.vm_servers:
            self.process_vms_ticks()

            new_users = self.process_new_users()

            users_per_server = [len(server.users) for server in self.vm_servers]

            self.total_uptime += len(users_per_server)

            if not users_per_server:
                users_per_server.append(0)

            self.output += f'{users_per_server}'[1:-1].replace(' ', '') + '\n'

        self.output += f'{self.total_uptime}'

        if self.test_mode:
            return self.output

        with open('outputs/output.txt', 'w') as file:
            file.write(self.output)

    def process_new_users(self) -> int:
        '''
        Get the new users from the queue and pass to the allocation method.

        :return:
        int : total of new users
        '''
        new_users = config_settings.get_next_tick_users()
        for idx in range(new_users):
            self.total_users += 1
            self.allocate_user(User(id=self.total_users))
        return new_users

    def process_vms_ticks(self):
        '''
        Loops all servers updating their tick infos.
        If the server is empty it will be closed
        '''
        for server_idx in range(len(self.vm_servers) - 1, -1, -1):
            self.vm_servers[server_idx].update_tick()

            if not self.vm_servers[server_idx].keep_alive():
                self.close_server(server_idx)

    def close_server(self, server_idx: int):
        '''
        Closes the chosen server.
        :param server_idx: Server position inside the list.
        '''
        self.vm_servers.pop(server_idx)

    def allocate_user(self, user):
        '''
        Sorts the servers descending, avoiding the creationg of unnecessary new servers.
        :param user: new user ready for allocation
        '''
        allocate_new_server = True
        self.vm_servers.sort(key=lambda x: len(x.users), reverse=True)

        for server in self.vm_servers:
            if len(server.users) < config_settings.umax:
                server.update_users(user)
                allocate_new_server = False
                break

        if allocate_new_server:
            self.vm_servers.append(VMServer(len(self.vm_servers) + 1))
            self.vm_servers[len(self.vm_servers) - 1].update_users(user)
