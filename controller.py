from distutils.command.config import config
from os import getenv
import sys
import config
#print(config.entry['conf1'])
#print(config.global_conf)
cmd_to_f={}

def _help():
    print(f'\nCOMMANDS LIST:\n')
    for elem in config.conf_list:
        print('##################################\n')
        print(f'Function name:\n{elem}\n')
        print(f'Description:\n{config.entry[elem]["doc"]}\n')
    print('##################################\n')
    exit()

def set_config(*args, **kwargs):
    def inner(func):

        global global_conf
        global local_conf
        global cl_args
        global cmd_to_f
        cla_1 = None
        try:
            cla_1 = sys.argv[1]
        except IndexError as e:
            _help()
        local_conf = config.entry[cla_1]
        cmd_to_f[args[0]] = func 
        global_conf = config.global_conf
        cl_args = sys.argv[1:]
        return func   
    return inner


@set_config('function1')
def s2_download():
    '''
    Write your code here.
    This will be executed with 'function1' as command line argument.
    _LOC takes values from config/function1/value.json
    _GLB takes values from config/global.json
    _CLA takes line arguments
    '''
    _LOC = local_conf
    _GLB = global_conf
    _CLA = cl_args
    pass


@set_config('function2')
def s2_count():
    '''
    Write your code here.
    This will be executed with 'function2' as command line argument.
    _LOC takes values from config/function2/value.json
    _GLB takes values from config/global.json
    _CLA takes line arguments
    '''
    _LOC = local_conf
    _GLB = global_conf
    _CLA = cl_args
    pass


@set_config('debug')
def debug_function():
    '''
    Write your code here.
    This will be executed with 'debug' as command line argument.
    _LOC takes values from config/debug/value.json
    _GLB takes values from config/global.json
    _CLA takes line arguments

    '''
    print('debug')
    _LOC = local_conf
    _GLB = global_conf
    _CLA = cl_args
    pass





 
 
