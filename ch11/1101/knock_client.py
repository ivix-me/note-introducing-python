# -*- coding: utf-8 -*-


from twisted.internet import reactor, protocol


class KnockClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write('叮咚'.encode('utf-8'))

    def dataReceived(self, data):
        if data.startswith('谁在那？'.encode('utf-8')):
            response = '消失中'.encode('utf-8')
            self.transport.write(response)
        else:
            self.transport.loseConnection()
            reactor.stop()


class KnockFactory(protocol.ClientFactory):
    protocol = KnockClient


if __name__ == '__main__':
    f = KnockFactory()
    reactor.connectTCP('localhost', 58888, f)
    reactor.run()
