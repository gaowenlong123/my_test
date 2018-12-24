def template_info(title , type=0):
    '''
    :param title:
    :param type: 0 初始化  1 正常
    :return:
    '''
    if type == 0:
        return "{\"template_type\":\"small_image\",\"template_title\":\"" + title+ "\",\"template_title_isSame\":true,\"template_cover\":[]}"
    else:
        return "{\"template_type\":\"small_image\",\"template_title\":\""+title+"\",\"template_title_isSame\":true,\"template_cover\":[\"https://pic.36krcnd.com/201812/24084912/v5ybx4h2du0tsbj7\"]}"


class audio:
    audio_values={"filesize":2370044,"task_ids":"[\"3c5519e129670e09367cfe40bce02135\",\"6dcb7243b2d25620eef7526e83d98741\",\"aaa68904eeb4cc3f4f8e16d6829f7659\"]","url":"https://audio.36krcnd.com/201812/24084805/qb1mncy419cicql0.wav","format":"wav"}
    cover="https://pic.36krcnd.com/201812/24084912/v5ybx4h2du0tsbj7"
