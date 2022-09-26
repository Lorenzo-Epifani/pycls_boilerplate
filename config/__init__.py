from importlib.resources import path
from importlib import import_module
import os 
import json

this_dirname = os.path.dirname(__file__)
global_conf=None
with open(f'{this_dirname}/global_conf.json') as g_f:
    global_conf=json.load(g_f)
conf_list=[a for a in os.walk(this_dirname)][0][1]
if '__pycache__' in conf_list: conf_list.remove('__pycache__')
#paths = [f'{this_dirname}/{name}' for name in conf_list]
entry={}
validation={}
for module_name in conf_list:
    mod=import_module(f'config.{module_name}.validator','.')
    for elem in conf_list:
        entry[module_name]=mod.content
        validation[module_name]=mod.validation
    
