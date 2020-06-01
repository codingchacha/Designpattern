# your code goes here"""For building room there are certain rules
  1) Base 2 ) pillar 3) Floor 4 ) Windows 5) Marble
   Base , Pillar and floor having the same structure
   but windows and marble can be different from all he floors
   Design the api
         Note order from a to f cannot vary """

class AbstractRoom(ABC):
    def base(self):
        print("base is same for all type of room")
    def pillar(self , height , color):
        print("pillar is of same {}  and {}".format(height , color))

    def floor(self , color):
        print("All rooms are of same color {}".format(color))
    def windows(self):
        print("orthodox roman windows")
    def marble(self):
        print("Makrana Marble")


class Room(AbstractRoom):
    def windows(self):
        print("modern windows with glass pane")

    def marble(self):
        print("italic modern marble")


class Client:
    def __init__(self , room):
        self.room = room
    def get_room_design(self , color , height):
        self.room.base()
        self.room.pillar(height , color)
        self.room.floor(color)
        self.room.windows()
        self.room.marble()

room_obj = Room()
c = Client(room_obj)
c.get_room_design("white" , 14)