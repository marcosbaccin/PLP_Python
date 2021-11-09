# -*- coding: utf-8 -*-

class CalculadorDeImposto(object):

    def realiza_calculo(self, orcamento):
        imposto_calculado = orcamento.valor * 0.1


if __name__ == '__main__':
    from Orcamento import Orcamento

    calculador = CalculadorDeImposto()
    orcamento = Orcamento(500)
    calculador.realiza_calculo(orcamento)
