from .AdapterInterface import AdapterInterface
from .Device import Device;

class Recharger:

    def __init__(self, adapter : AdapterInterface , device : Device):
        self.adapter = adapter;
        self.adapter.setDevice(device);

    def do_recharge(self):
        self.adapter.recharge();


