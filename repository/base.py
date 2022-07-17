from abc import ABC, abstractmethod
from database.session import Session


class BaseRepository(ABC):
    def __init__(self, session: Session):
        self.session: Session = session

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def update(self, id, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()
