# your code goes here""" We have to build an api for searching Primary search and bInary search we need to design 
 our api in such a way that during run time that we can use any of them """
class SortAbstract(ABC):
    @abstractmethod
    def search(self , array):
        pass

class Primary_Search(SortAbstract):
    def search(self , array , key):
        for index , element in enumerate(0 , len(array)):
            if elem == key:
                return index
        return False
class Binary_Search(SortAbstract):
    def search(self , array , key):
        start = 0
        end = len(array) - 1
        while(start <= end):
            mid = (start + end) // 2
            if array[mid] == key:
                return mid
            elif array[mid] < key:
                start = mid + 1
            else:
                end = mid - 1
        return False
class Context:
    def __init__(self , strategy):
        self.strategy = strategy
    def search(self , array , key):
        return self.strategy.search(array , key)


class Client:
    def main(self , array , key):
        search = Primary_Search()
        smart_search = Binary_Search()
        c = Context(smart_search)
        return c.search(array , key)
client = Client()
print(client.main([1,4,8,12,13,20,25,31,100] ,31))