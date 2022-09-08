import json
from typing import List, Set, Dict, Union, Any, Callable, Tuple
from xml.dom import ValidationErr
import cerberus as cer # type: ignore
import json
from operator import itemgetter
from pprint import pprint

def _init()->Dict[str,Dict[str,str]]:
    def cerberus_format(entry,rule = {'type': 'string', 'required': True}):
        reformat = {
            'type': 'dict',
            'required': True,
            'schema' : {k:v for k,v in entry.items()}
        }
        reformat['schema']['doc'] = rule
        reformat['schema']['entry_function'] = rule
        return reformat
        
    schema = {
        "function1": {},
        "function2": {
            "option1":{'type': 'integer', 'required': True, 'max':5,'min':2},
            "option2":{'type': 'integer', 'required': True, 'max':5,'min':2}
        },
        "function3": {
            'option1': {'type': 'integer', 'required': True, 'min':1},
            'option2':{'type': 'boolean', 'required': True},
            'option3':{'type': 'boolean', 'required': True},
            'option4':{'type': 'string', 'required': True},
            'option5':{'type': 'list', 'required': True},#!!!!
            'option6':{'type': 'string', 'required': True},
            "option7":{'type': 'integer', 'required': True, 'max':10,'min':1},
        },
        "function4": {},
        "function5": {},
        "debug_function": {}
    }    

    schema = {key:cerberus_format(value) for key,value in schema.items()}
    with open('./config/core.json') as config_file:
            conf = json.load(config_file) #CONFIG FILE
            conf = conf.get('cmd',{})
    validator = cer.Validator()

    validator.schema = schema
    if (not validator.validate(conf, schema)):
        print(validator.errors)
        raise ValidationErr(validator.errors)
    return conf

def _info():
    pprint(_init())

content = _init()
