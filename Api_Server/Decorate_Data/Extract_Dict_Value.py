#  路径sting  拿出字典中对应的值
def get_dict_value(dict ,template_path='data/items'):
    temp_list = template_path.split('/')
    for key in temp_list:
        dict = dict[key]
    return dict