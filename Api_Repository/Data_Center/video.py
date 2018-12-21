def template_info(title ,template_type=0):
    '''
    :param title:     标题
    :param template_type:   0 = 小图 1 = 大图 2 = 多图
    :return:
    '''
    if template_type == 0:
        temp = "{\"template_type\":\"small_image\",\"template_title\":\""+title+"\",\"template_title_isSame\":true,\"template_cover\":[\"https://pic.36krcnd.com/201812/21110119/zsam3arqz70vg7nz\"]}"
        pass
    elif template_type == 1:
        temp = "{\"template_type\":\"big_image\",\"template_title\":\""+title+"\",\"template_title_isSame\":true,\"template_cover\":[\"https://pic.36krcnd.com/201812/21115045/w3zkaazep4ahkgzz\"]}"
        pass
    else:
        print('输入的 template_type 错误')
        temp=''

    return temp

class cover:
    one="https://pic.36krcnd.com/201812/21110119/zsam3arqz70vg7nz"
    two="https://pic.36krcnd.com/201812/21115045/w3zkaazep4ahkgzz"

class video_values:
    one={"filesize":7446924,"task_ids":"[\"0ce95baba44b826d3375491ef27ef37d\",\"8eda8daa183748dd706388e084e826a2\",\"10965d3819cee0234fb598977109a71f\"]","url":"https://video.36krcnd.com/201812/21115031/ua5e2xxas1m5c41y.mp4","format":"mp4"}

class web_cover:
    one="https://pic.36krcnd.com/201812/21115015/c6vvpxy2iero37rg"
    two="https://pic.36krcnd.com/201812/21110042/p6dhxaep8nxu4nq2"