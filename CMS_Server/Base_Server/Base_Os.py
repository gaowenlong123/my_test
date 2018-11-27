import os
# print(os.path.dirname(__file__))
# print(os.path.join(os.path.dirname(__file__)))



def change_path(path="../Yamls/test/test1.yaml"):
    ''' "../Yamls/test/Login.yaml"     根据当前路径获得新路径 '''
    PATH=lambda p : os.path.abspath(
        os.path.join(os.path.dirname(__file__),p)
    )
    return PATH(path)

# print(change_path("../Yamls/test/Login.yaml"))


def write_sys_path(path=''):
    ''' 在该进程中，写进path中  '''
    import sys
    sys.path.append(path)
