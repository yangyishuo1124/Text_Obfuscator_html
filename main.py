class jiami(object):
    def __init__(self, key: str, data: str):
        # 密钥和内容长度
        self.key = key
        self.key_add = 0
        if self.key.isdigit():
            if len(self.key) > 5:
                for i in self.key:
                    self.key_add += int(i)
            else:
                self.key_add = int(self.key)
        else:
            for i in self.key:
                self.key_add += int(ord(i))
        self.data = data
        self.jiami_result_list = []
        self.jiami_result = ''

    def jiami(self):
        for i in self.data:
            self.jiami_result_list.append(chr(ord(i) + self.key_add))
        for i in self.jiami_result_list:
            self.jiami_result += i

    def result(self):
        return self.jiami_result


class jiemi(object):
    def __init__(self, key: str, data: str):
        self.key = key
        self.key_add = 0
        if self.key.isdigit():
            if len(self.key) > 5:
                for i in self.key:
                    self.key_add += int(i)
            else:
                self.key_add = int(self.key)
        else:
            for i in self.key:
                self.key_add += int(ord(i))
        self.data = data
        self.jiemi_result_list = []
        self.jiemi_result = ''

    def jiemi(self):
        for i in self.data:
            try:
                self.jiemi_result_list.append(chr(ord(i) - self.key_add))
            except ValueError:
                self.jiemi_result = '输入的内容不是密文'
                break
        for i in self.jiemi_result_list:
            self.jiemi_result += i

    def result(self):
        return self.jiemi_result


def jiamimain(key, data):
    # jiami
    if len(key) >= 8:
        return '密钥长度错误,请重新输入(密钥长度不能大于8)'
    elif len(data) == 0:
        return '内容不能为空'
    elif len(key) == 0:
        return '密钥不能为空'
    else:
        a = jiami(key, data)
        a.jiami()
        return a.result()


def jiemimain(key, data):
    # jiemi
    if len(key) >= 8:
        return '密钥长度错误,请重新输入(密钥长度不能大于8)'
    elif len(data) == 0:
        return '内容不能为空'
    elif len(key) == 0:
        return '密钥不能为空'
    else:
        a = jiemi(key, data)
        a.jiemi()
        return a.result()
