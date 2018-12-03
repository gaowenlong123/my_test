#接口的基类

class Interface():
    def __init__(self):
        self._auther='gao'
        self._FixBody=[]
        self._error_times=0
        self._error_frequency=[]
        self._error_reason=[]

        self._request_type='post'

        self.request_data={}
        self.response_data={}


    @property
    def auther(self):
        return self._auther

    @property
    def FixBody(self):
        return self._FixBody

    @property
    def Error_Times(self):
        return self._error_times

    @property
    def Error_Frequency(self):
        return self._error_frequency

    @property
    def Error_Reason(self):
        return self._error_reason

    @property
    def RequestType(self):
        return self._request_type




a=Interface()
print()

