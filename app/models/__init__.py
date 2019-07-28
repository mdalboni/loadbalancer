class BaseModel:
    '''
    Default class for the Servers and Users.
    If needed it can be used to track the children classes based on theirs ids and names.
    '''
    id: int
    name: str

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"{self.__class__} [{self.id} | {self.name}]"
