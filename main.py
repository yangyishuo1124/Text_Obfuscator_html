class 加密(object):
    def __init__(self, 密钥: str, 内容: str):
        # 密钥和内容长度
        self.密钥 = 密钥
        self.密钥和 = 0
        if self.密钥.isdigit():
            if len(self.密钥) > 5:
                for i in self.密钥:
                    self.密钥和 += int(i)
            else:
                self.密钥和 = int(self.密钥)
        else:
            for i in self.密钥:
                self.密钥和 += int(ord(i))
        self.内容 = 内容
        self.加密结果列表 = []
        self.加密结果 = ''

    def 加密(self):
        for i in self.内容:
            self.加密结果列表.append(chr(ord(i) + self.密钥和))
        for i in self.加密结果列表:
            self.加密结果 += i

    def 输出(self):
        return self.加密结果


class 解密(object):
    def __init__(self,密钥: str,密文: str):
        self.密钥 = 密钥
        self.密钥和= 0
        if self.密钥.isdigit():
            if len(self.密钥) > 5:
                for i in self.密钥:
                    self.密钥和 += int(i)
            else:
                self.密钥和 = int(self.密钥)
        else:
            for i in self.密钥:
                self.密钥和 += int(ord(i))
        self.密文 = 密文
        self.解密结果列表 = []
        self.密文结果 = ''
    def 解密(self):
        for i in self.密文:
            self.解密结果列表.append(chr(ord(i) - self.密钥和))
        for i in self.解密结果列表:
            self.密文结果 += i

    def 输出(self):
        return self.密文结果



def jiamimain(密钥, 内容):
    # 加密
    if len(密钥) >= 8:
        return '密钥长度错误,请重新输入(密钥长度不能大于8)'
    elif len(内容) == 0:
        return '内容不能为空'
    elif len(密钥) == 0:
        return '密钥不能为空'
    else:
        a = 加密(密钥, 内容)
        a.加密()
        return a.输出()


def jiemimain(密钥, 内容):
    # 解密
    if len(密钥) >= 8:
        return '密钥长度错误,请重新输入(密钥长度不能大于8)'
    elif len(内容) == 0:
        return '内容不能为空'
    elif len(密钥) == 0:
        return '密钥不能为空'
    else:
        a = 解密(密钥, 内容)
        a.解密()
        return a.输出()
