
def get_channel_feed( c ,type='' ,num=10 ):
    i = c(type)
    data=i.feed(num)

    # print(data["data"]["itemList"])
    # print(len(data["data"]["itemList"]))
    del i
    return data


if __name__ == '__main__':
    pass


