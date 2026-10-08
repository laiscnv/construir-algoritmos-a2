import datetime
import requests

def cotar():
    cotacoes = [] 
    hoje = datetime.date.today() 
  
    for i in range(365):
        data_atual = hoje - datetime.timedelta(days=i) 
        data_formatada = data_atual.strftime("%m-%d-%Y")

        url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data_formatada}'&$top=100&$format=json"

        try:
            response = requests.get(url) 
            dados = response.json() 

            if dados.get("value") and len(dados["value"]) > 0:
                valor_compra = dados["value"][0]["cotacaoCompra"] 
                cotacoes.append(valor_compra) 
            else:
                cotacoes.append(None)
        except Exception:
            cotacoes.append(None) 

    return cotacoes
