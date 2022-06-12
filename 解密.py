#  -*-coding=utf-8-*-
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


if __name__ == '__main__':
    密钥 = input('请输入密钥：')
    内容 = input('请输入内容：')
    解密 = 解密(密钥, 内容)
    解密.解密()
    print(解密.输出())
