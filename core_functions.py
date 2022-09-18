from os import getenv
import sys
import config.core as core_conf
cmd_to_f={}
def set_config(*args, **kwargs):
    def inner(func):

        global global_conf
        global local_conf
        global cl_args
        global cmd_to_f

        local_conf = core_conf.content['cmd'][sys.argv[1]]
        cmd_to_f[args[0]] = func 
        global_conf = core_conf.content['global_conf']
        cl_args = sys.argv[1:]
        return func   
    return inner


@set_config('s2_dw')
def s2_download():
    '''
    Write your code here.
    This will be executed with 's2_dw' as command line argument.
    _C takes values from config/core.json in cmd--> s2_dw
    '''
    _C = local_conf
    pass


@set_config('s2_ct')
def s2_count():
    '''
    Write your code here.
    This will be executed with 's2_ct' as command line argument.
    _C takes values from config/core.json in cmd--> s2_ct
    '''
    _C = local_conf
    pass


@set_config('debug')
def debug_function():
    '''
    Write your code here.
    This will be executed with 'debug' as command line argument.
    _C takes values from config/core.json in cmd--> debug
    '''
    print('debug')
    _C = local_conf
    pass





 
 
