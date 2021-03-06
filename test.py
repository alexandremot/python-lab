
class Carta(object):

        naipes = 'paus ouros copas espadas'.split()
        valores = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

        def __init__(self, valor, naipe):
                self.valor = valor
                self.naipe = naipe

        def __repr__(self):
                return 'Carta (%r, %r)' % (self.valor, self.naipe)

        def __str__(self):
                return self.valor + ' de ' + self.naipe


        @classmethod
        def todas(cls):
                return [cls(v, n) for n in cls.naipes for v in cls.valores]