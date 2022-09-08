import config.core as core_conf
import sys
import core_functions

CORE_CONF = core_conf.content


def controller(cl_args):
    #TODO you can pass cl_args to the entry function
    cmd_item = CORE_CONF.get(cl_args[0],'CMD_NOT_FOUND')
    if cmd_item=='CMD_NOT_FOUND':
        raise Exception(cmd_item)

    entry_function = getattr(core_functions,cmd_item['entry_function'])
    entry_function(cl_args[1:])

def _help():
    print(f'\nCOMMANDS LIST:\n')
    for cmd_name,content in CORE_CONF.items():
        print('##################################\n')
        print(f'Function name:\n{cmd_name}\n')
        print(f'Description:\n{content["doc"]}\n')
    print('##################################\n')

if __name__ == '__main__':
    cl_args=sys.argv[1:]

    if len(cl_args)==0:
        print('Choose a command')
        _help()
        exit()

    #plt.ion()
    controller(cl_args)
