#!/usr/local/bin/python3.7

import sys

def converte_to_list_one(string):
    return [string]

class arquivo_conv_86:
    def __init__(self, nome_arquivo, funcao_convercao=None, separador_linhas="\n"):
        #super().__init__(nome_arquivo, separador_linhas)

        self.__arquivo = open(nome_arquivo, "r", encoding="iso-8859-1")
        self.__separador_linhas = separador_linhas

        self.__linha_zero = self.__arquivo.readline()
        self.__tamanho_linha_zero = len(self.__linha_zero)+1
        self.__linha_zero = self.__linha_zero.rstrip(self.__separador_linhas)

        self.__linha_atual = self.__arquivo.readline()
        self.__tamanho_linha = len(self.__linha_atual)+1
        self.__linha_atual = self.__linha_atual.rstrip(self.__separador_linhas)

        self.__arquivo.seek(0,2)
        self.__tamanho_arquivo = ((self.__arquivo.tell()-self.__tamanho_linha_zero) // self.__tamanho_linha) + 1

        self.__numero_linha_atual = 0
        self.__arquivo.seek(0)

        self.__conversor=funcao_convercao

    def le_linha(self, numero_linha = None):
        if numero_linha != None and numero_linha != self.__numero_linha_atual:
           if numero_linha == 0:
               self.__arquivo.seek(self.__tamanho_linha*numero_linha)
           else:
               self.__arquivo.seek(self.__tamanho_linha_zero+self.__tamanho_linha*(numero_linha-1))
           self.__numero_linha_atual = numero_linha

        if not 0 <= self.__numero_linha_atual < len(self):
            raise IndexError('Index out of range')

        # Checar se náo é a última já carregada, se for deixa a mesma sem ler novamente
        self.__linha_atual = self.__arquivo.readline().rstrip(self.__separador_linhas)

        if self.__conversor != None:
            self.__linha_atual = self.__conversor(self.__arquivo.readline().rstrip(self.__separador_linhas))

        self.__numero_linha_atual += 1

        return self.__linha_atual

    def fecha_arquivo(self):
        if not self.__arquivo.closed:
            self.__arquivo.close()

    def __len__(self):
        return self.__tamanho_arquivo

    def __getitem__(self, chave):
        if isinstance(chave, slice):
            start, stop, step = chave.indices(len(self))

            #return Seq([self[i] for i in range(start, stop, step)])
            return [self[i] for i in range(start, stop, step)]
        elif isinstance(chave, int):
            return self.le_linha(chave)

    def __del__(self):
        self.fecha_arquivo()

if __name__ == "__main__" :
    # Testes

    arquivo_flavio = arquivo_conv_86("/portaloptrib/TESHUVA/sparta/DEV/arquivos/clone2/ajuste_cadastral_clone2/portaloptrib/TESHUVA/sparta/PROD/entradas/conv86/SP/pleito_202011_versao_202011_escopo_2016_corrigido/202011EN_corrigido.txt", converte_to_list_one)

    print (len(arquivo_flavio))

    print(arquivo_flavio[1702360])

    #for linha in arquivo_flavio:
    #    print(f"TLinha: {linha}")
    #.    print(f"TLinha: {len(linha)}")

    #arquivo_flavio = arquivo_conv_86("teste.txt")
    #print(arquivo_flavio[:2])
    #if "Flavio" in arquivo_flavio:
    #  print("Tem")
    #else:
    #  print("Não tem")

    #print(arquivo_flavio[10])

    arquivo_flavio.fecha_arquivo()

