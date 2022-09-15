import config.core as core_conf
import sys
import core_functions

CMD_CONF = core_conf.content['cmd']


def controller(cl_args):
    entry_function = core_functions.cmd_to_f.get(cl_args[0],'CMD_NOT_FOUND')
    if entry_function=='CMD_NOT_FOUND':
        raise Exception(entry_function)
    entry_function()

def _help():
    print(f'\nCOMMANDS LIST:\n')
    for cmd_name,content in CMD_CONF.items():
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
