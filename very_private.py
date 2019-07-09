class Tresor(object):
    def __init__(self):
        self.__secret = 'very secret'

    def __getattribute__(self, attr):
        if attr == '_Tresor__secret' or attr == '__secret':
            return ':-('
        return super(Tresor, self).__getattribute__(attr)

    def __dict__(self):
        return {}

    def get_x(self, secret):
        if secret == 'hugo':
            return super(Tresor, self).__getattribute__('_Tresor__secret')


hugo = Tresor()
