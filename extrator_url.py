class ExtratorURL:
    def __init__(self,url_teste):
        self.url = self.sanitiza_url(url_teste)
        self.valida_url()
        self.valida_url_base()


    def sanitiza_url(self,url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
    
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def valida_url_base(self):
        url_base = self.get_url_base()
        if not url_base.endswith("cambio") or not url_base.startswith("https") :
            raise ValueError("A URL não está correta")
        
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


#extrator_url = ExtratorURL(None)
extrator_url = ExtratorURL("https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)

