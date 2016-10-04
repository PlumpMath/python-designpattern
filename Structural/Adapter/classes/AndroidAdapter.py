from .AdapterInterface import AdapterInterface
from .Android import Android


class AndroidAdapter(AdapterInterface):

    def setDevice(self, device: Android):
        self.device = device;

    def recharge(self):
        self.device.connect_via_microusb();
        self.device.recharge();
