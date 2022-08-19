"""
it is used to share implementation between multiple different objects
"""
import abc

class AbstractResourceFetcher(abc.ABC):
    abc.abstractmethod
    def fetch(self):
        """it is used to fetch data"""
        
class textFetcher(AbstractResourceFetcher):
    def fetch(self):
        print("fetch from text")
        

class webFetcher(AbstractResourceFetcher):
    def fetch(self):
        print("fetch from Web")
        

class user:
    def __init__(self, implement) -> None:
        self._implement =implement
    
    def show(self):
        self._implement.fetch()
        

text = user(textFetcher())
web = user(webFetcher())
text.show()
print("---") 
web.show()   
