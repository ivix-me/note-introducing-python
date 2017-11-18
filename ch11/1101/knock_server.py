# -*- coding: utf-8 -*-


from twisted.internet import protocol, reactor


class Knock(protocol.Protocol):
    def dataReceived(self, data):
        print('客户端：', data.decode('utf-8'))
        if data.startswith('叮咚'.encode('utf-8')):
            response = '谁在那？'.encode('utf-8')
        else:
            response = data + '谁？'.encode('utf-8')
        print('服务端：', response.decode('utf-8'))
        self.transport.write(response)


class KnockFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Knock()


reactor.listenTCP(58888, KnockFactory())
reactor.run()

# /opt/env/intro-python/bin/python /home/ivix/PycharmProjects/IntroducingPython/ch11/1101/knock_server.py
# 客户端： 叮咚
# 服务端： 谁在那？
# 客户端： 消失中
# 服务端： 消失中谁？
