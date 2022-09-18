import json
from socket import timeout
from typing import List, Set, Dict, Union, Any, Callable, Tuple
from xml.dom import ValidationErr
import cerberus as cer # type: ignore
import json
from operator import itemgetter
from pprint import pprint

VALIDATE_ENABLED = True

def _init()->Dict[str,Dict[str,str]]:
    def cerberus_format(entry,rule = {'type': 'string', 'required': True}):
        reformat = {
            'type': 'dict',
            'required': True,
            'schema' : {k:v for k,v in entry.items()}
        }
        reformat['schema']['doc'] = rule
        return reformat

    def type_required(_type,required=True):
        return {'type': _type,'required':required}
    schema={
        "s2_dw": {
            "limit": type_required('integer'),
            "geo_files": type_required('list'),
            "time_window": {
                'type': 'dict',
                'required': True,
                'schema': {
                    'start': type_required('list'),
                    'end': type_required('list')
                    },
            },
            "time_delta": type_required('integer'),
            "timeout_sec": type_required('integer'),
            "overwrite": {
                'type': 'dict',
                'required': True,
                'schema': {
                    'flag': type_required('boolean'),
                    'root': type_required('string')
                }
            }
        },
        "s2_ct": {
            "geo_files": type_required('list'),
            "time_window": {
                'type': 'dict',
                'required': True,
                'schema': {
                    'start': type_required('list'),
                    'end': type_required('list')
                },
            },
            "time_delta": type_required('integer'),
        },
        "debug": {}
        }   
    

    schema = {key:cerberus_format(value) for key,value in schema.items()}
    #pprint(schema)
    with open('./config/core.json') as config_file:
        conf = json.load(config_file) #CONFIG FILE
    validator = cer.Validator()

    validator.schema = schema
    if VALIDATE_ENABLED and (not validator.validate(conf['cmd'], schema)):
        print(validator.errors)
        raise ValidationErr(validator.errors) 
    return conf

def _info():
    pprint(_init())

content = _init()
