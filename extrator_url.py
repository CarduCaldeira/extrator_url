import re
class ExtratorURL:
    def __init__(self,url_teste):
        self.url = self.sanitiza_url(url_teste)
        self.valida_url()

    def sanitiza_url(self,url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        busca = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = busca.match(self.url)

        if not match:
            raise ValueError('A URL não é válida')
    
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base
        
    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro   = self.get_url_parametros().find(parametro_busca)
        indice_valor       = indice_parametro + len(parametro_busca)+1
        indice_e_comercial = self.get_url_parametros().find("&",indice_valor)
        if  indice_e_comercial == -1:
            return self.get_url_parametros()[indice_valor:]
        else:
            return  self.get_url_parametros()[indice_valor:indice_e_comercial]

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return "O link é: "+ self.url +"\n" + "A base do Link é: " + self.get_url_base() +"\n" +"Os parametros do link são: "+  self.get_url_parametros()

    def __eq__(self,objeto):
        return self.url == objeto.url
        

#extrator_url = ExtratorURL(None)
extrator_url = ExtratorURL("https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
extrator_url2 = ExtratorURL("https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")

valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
print(len(extrator_url))
print(extrator_url)
if extrator_url == extrator_url2:
    print("É igual")

""" 
Em valida_url usei expressoes regulares para verificar se o link estava de uma forma valida, outro exemplo
de uso de expressoes regulares é a verificação e extração de um CEP em um texto. Como no exemplo a seguir:

import re

endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120"
padrao   = re.compile("[0123456789]{5}[-]?[123456789]{3})
busca    = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)

Na linha 70 poderiamos substituir [0123456789] por [0-9], 
{5} pode ser substituido por [0-9] escrito 5 vezes
e ? por {0,1}.

Além disso, padrao.search(endereco) retorna um booleano, 
que é True caso encontre o padrão especificado em re.compile.
Para extrair o cep da string, usamos o comando .group() na linha 74.
"""