import datetime
class Activation:
    def is_id_active(self , status):
        if status:
            return True
        else:
            return False
class Expiration:
    def __init__(self):
        self.now = datetime.datetime.now()
        self.validity = 2025
    def expiry_check(self):
        if self.validity > self.now.year:
            return "valid"
        else:
            return "invalid"
class Floor:
    def check_floor_access(self , status):
        if status == True:
            return True
        else:
            return False
class Images:
    def click_picture(self):
        print("picture clicked")
    def store_pic_on_dashboard(self):
        print("uploading the pic on the dashboard")
class Attendence:
    def check_in_time(self):
        checkin_time = datetime.datetime.now()
        print("storing the checking time")
        return checkin_time
    def checkout_time(self):
        checkout_time = datetime.datetime.now()
        print("storing the checkout time")
        return checkout_time
class LoggingFacade:
    def __init__(self):
        self.activation = Activation()
        self.expiration = Expiration()
        self.floor = Floor()
        self.images = Images()
        self.attendence = Attendence()
    def login(self , readstatus , floor_access):
        self.activation.is_id_active(readstatus)
        self.expiration.expiry_check()
        self.floor.check_floor_access(floor_access)
        self.images.click_picture()
        self.images.store_pic_on_dashboard()
        self.attendence.check_in_time()
lf = LoggingFacade()
lf.login(True , True)