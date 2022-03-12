# -*- coding: utf-8 -*-
from enum import Enum


class StatusOrcamentoExtendedEnum(Enum):
    @classmethod
    def valores_armazenados(cls):
        return {x[0]: {'descricao': x[1],
                       'taxa_desconto': x[2],
                       'aprovar': x[3],
                       'reprovar': x[4],
                       'finalizar': x[5]
                       }
                for x in list(map(lambda c: c.value, cls))}

    @classmethod
    def descricao_valor(cls, key):
        try:
            return cls.valores_armazenados().get(key).get('descricao')
        except Exception:
            return None

    @classmethod
    def taxa_desconto(cls, key):
        try:
            return cls.valores_armazenados().get(key).get('taxa_desconto')
        except Exception:
            return None

    @classmethod
    def aprovar(cls, key):
        try:
            return cls.valores_armazenados().get(key).get('aprovar')
        except Exception:
            return None

    @classmethod
    def reprovar(cls, key):
        try:
            return cls.valores_armazenados().get(key).get('reprovar')
        except Exception:
            return None

    @classmethod
    def finalizar(cls, key):
        try:
            return cls.valores_armazenados().get(key).get('finalizar')
        except Exception:
            return None


class StatusOrcamento(StatusOrcamentoExtendedEnum):
    # codigo, descricao, taxa_desconto, acao_aprovar, acao_reprovar, acao_finalizar
    Cancelado:      tuple = (0, 'Cancelado', None, None, None, None)
    Em_Aprovacao:   tuple = (1, 'Em Aprovacao', 0.02,
                             'Aprovar', 'Reprovar', None)
    Aprovado:       tuple = (2, 'Aprovado', 0.05, None, None, 'Finalizar')
    Reprovado:      tuple = (3, 'Reprovado', None, None, None, 'Finalizar')
    Finalizado:     tuple = (4, 'Finalizado', None, None, None, None)
