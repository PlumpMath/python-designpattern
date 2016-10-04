from classes.Recharger import Recharger
from classes.IphoneAdapter import  IphoneAdapter
from classes.Iphone import Iphone;
from classes.Android import Android;
from classes.AndroidAdapter import AndroidAdapter;

# Adapter Pattern
#Purpose : To translate on interface for a class into compatible interface
#An adapter allows classes to work together that normally cound not because of incompatible interface by providing
#its interface to client while using the original interface

iphone =  Iphone();
iphoneAdapter = IphoneAdapter();

android =  Android();
androidAdapter = AndroidAdapter();

#recharger is a client. It does not care about how Iphone Adapter or Android Adapter are implemented.
#It just call function recharge is defined from Adapter Interface

rechargerIphone =  Recharger(iphoneAdapter, iphone);
rechargerIphone.do_recharge();

rechargerAndroid =  Recharger(androidAdapter, android);
rechargerAndroid.do_recharge();
