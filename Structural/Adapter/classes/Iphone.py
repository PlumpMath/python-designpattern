from .Device import Device;

class Iphone(Device):

    def recharge(self):
        print("Iphone is recharging");

    def connect_via_lightning(self):
        print("Connect via Lightning");