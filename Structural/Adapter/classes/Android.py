from .Device import Device;

class Android(Device):

    def recharge(self):
        print("Android is recharging");

    def connect_via_microusb(self):
        print("Connect via Micro USB");