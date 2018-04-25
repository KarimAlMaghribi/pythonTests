import abc


class Connector:


    """@abc.abstractmethod
    def connect(self):
        pass
    """
    
    @abc.abstractmethod
    def save(self, item):
        pass
    

    @abc.abstractmethod
    def load_all(self):
        pass
    
    
    @abc.abstractmethod
    def load_by_id(self, id):
        pass

    
    @abc.abstractmethod
    def update_item(self, item):
        pass


    @abc.abstractmethod
    def get_last_id(self):
        pass


    @abc.abstractmethod
    def get_done_items(self):
        pass    
    
    
    """@abc.abstractmethod
    def close(self):
        pass"""

   

