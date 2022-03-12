# -*- coding: utf-8 -*-
"""
    
"""
def IPVX(metodo_ou_funcao):
    def wrapper(self, *args, **kwargs):
        return metodo_ou_funcao(self, *args, **kwargs) + 50.0
    return wrapper
