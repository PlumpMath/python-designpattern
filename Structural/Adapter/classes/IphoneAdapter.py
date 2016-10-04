from .AdapterInterface import AdapterInterface
from .Iphone import Iphone


class IphoneAdapter(AdapterInterface):

    def setDevice(self, device: Iphone):
        self.device = device;

    def recharge(self):
        self.device.connect_via_lightning();
        self.device.recharge();
