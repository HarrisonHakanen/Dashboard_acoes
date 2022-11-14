import math
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense, LSTM, Dropout
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import datetime
import dateutil.parser
import math
import plotly.express as px

class Acao:
    
    def _init_(self,ticker:str,negociacoes_mes:list,negociacoes_param:list,fechamento:list,sazonalidade_param:list,sazonalidade_mes:list):
    
        self.ticker = ticker
        self.negociacoes_mes = negociacoes_mes
        self.negociacoes_param = negociacoes_param
        self.fechamento = fechamento
        self.sazonalidade_mes = sazonalidade_mes
        self.sazonalidade_param = sazonalidade_param
        
        
    
def create_df(df,steps=1):
    
    dataX,dataY = [],[]
    
    for i in range(len(df)-steps-1):
        a = df[i:(i+steps),0]
        dataX.append(a)
        dataY.append(df[i+steps,0])
    return np.array(dataX),np.array(dataY)


def prever_valor_media(array,dias_anteriores):
    
    diferenca_pelo_min = array.tail(dias_anteriores).mean() - array.tail(dias_anteriores).min()
    diferenca_pelo_max = array.tail(dias_anteriores).mean() - array.tail(dias_anteriores).max()
    media = array.tail(dias_anteriores).mean() 
    
    
    if(diferenca_pelo_min<0):
        diferenca_pelo_min *= -1

    if(diferenca_pelo_max<0):
        diferenca_pelo_max *= -1
        
    ate = media-diferenca_pelo_max
    
    
    return media
        
        

#PREVE O VALOR DA PRÓXIMA ALTA OU DA PRÓXIMA BAIXA, DEPENDE DO ARRAY QUE SERÁ PASSADO        
def prever_valor_lstm(array,dias_anteriores,dias_previsao,epocas):

    if len(array) < 130:
        dias_anteriores = 10
        
    
    dias_retorno = dias_anteriores
    
    dias_previsao = dias_previsao
    

    qtd_linhas = len(array)

    qtd_linhas_treino = round(.70*qtd_linhas)


    qtd_linhas_teste = qtd_linhas-qtd_linhas_treino

    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(array)

    #Separa em treino e teste

    train = df_scaled[:qtd_linhas_treino]
    test = df_scaled[qtd_linhas_treino:qtd_linhas_treino+qtd_linhas_teste]




    #gerando dados de treino e de teste

    steps = dias_retorno

    X_train,Y_train = create_df(train,steps)
    X_teste,Y_teste = create_df(test,steps)
    
    
    if(len(X_train)>0):

        #print('Treino x: ',X_train.shape,' Treino y: ',Y_train.shape)
        #print('Teste x: ',X_teste.shape,' Teste y: ',Y_teste.shape)

        """Esse 1 significa a quantidade de features o modelo tem"""
        X_train = X_train.reshape(X_train.shape[0],X_train.shape[1],1)
        X_teste = X_teste.reshape(X_teste.shape[0],X_teste.shape[1],1)




        #montando a rede
        model = Sequential()
        model.add(LSTM(35,return_sequences=True,input_shape=(steps,1)))
        model.add(LSTM(35,return_sequences=True))
        model.add(LSTM(35))
        model.add(Dropout(0.2))
        model.add(Dense(1))

        model.compile(optimizer='adam',loss='mse')
        #model.summary()

        validation = model.fit(X_train,Y_train,validation_data=(X_teste,Y_teste),epochs=epocas,batch_size=dias_retorno,verbose=0)
        
        length_test = len(test)

        days_input_steps = length_test - steps
        #print("Tamanho do test: ",length_test)
        #print("Quantidade de dias retornados: ",days_input_steps)

        input_steps = test[days_input_steps:]
        input_steps = np.array(input_steps).reshape(1,-1)
        #input_steps

        #Transformar em lista
        list_output_steps = list(input_steps)
        list_output_steps = list_output_steps[0].tolist()
        #list_output_steps

        pred_output =[]
        i = 0
        n_future = 1

        while(i<n_future):
            if(len(list_output_steps)>steps):
                input_steps = np.array(list_output_steps[1:])
                #print("{} dia. Valores de entrada -> {}".format(i,input_steps))
                input_steps = input_steps.reshape(1,-1)
                input_steps = input_steps.reshape((1,steps,1))
                pred = model.predict(input_steps,verbose=0)
                #print("{} dia. Valor previsto {}".format(i,pred))
                list_output_steps.extend(pred[0].tolist())
                list_output_steps = list_output_steps[1:]
                pred_output.extend(pred.tolist())
                i=i+1
            else:
                input_steps = input_steps.reshape((1,steps,1))
                pred = model.predict(input_steps, verbose=0)
                #print(pred[0])
                list_output_steps.extend(pred[0].tolist())
                #print(len(list_output_steps))
                pred_output.extend(pred.tolist())
                i=i+1

        #print(pred_output)

        prev = scaler.inverse_transform(pred_output)
        prev = np.array(prev).reshape(1,-1)
        #proxima_alta = list(prev)
        proxima_alta = prev[0].tolist()

    return proxima_alta    



def High_Low(acao_df,h_l,pulo):
    
    quantos_em_quantos = pulo
    controlador = 0
    dados = pd.DataFrame()

    while(quantos_em_quantos<len(acao_df)):

        if (controlador)==0:
  
            if(h_l==1):
                dados =[[[acao_df['Date'][acao_df['Close'][:quantos_em_quantos].idxmax()]],acao_df['Close'][:quantos_em_quantos].max()]]
            else:
                dados =[[[acao_df['Date'][acao_df['Close'][:quantos_em_quantos].idxmin()]],acao_df['Close'][:quantos_em_quantos].min()]]
            
            controlador = 1

        else:    
            if(h_l==1):
                dados.append([[acao_df['Date'][acao_df['Close'][quantos_em_quantos:quantos_em_quantos+pulo].idxmax()]],acao_df['Close'][quantos_em_quantos:quantos_em_quantos+pulo].max()])
            else:
                dados.append([[acao_df['Date'][acao_df['Close'][quantos_em_quantos:quantos_em_quantos+pulo].idxmin()]],acao_df['Close'][quantos_em_quantos:quantos_em_quantos+pulo].min()])
            

            quantos_em_quantos+=pulo
            
    dados = pd.DataFrame(dados,columns=['Date','Close'])
    
    return dados




def High_low2(acao_df,h_l):

    acao_df['Date'] = pd.to_datetime(acao_df['Date'],format='%Y-%m-%d')

    acao_df = acao_df.set_index(pd.DatetimeIndex(acao_df['Date']))
    
    
    i = 0

    anos = list()
    meses = list()
    while(i<len(acao_df)):

        anos.append(acao_df["Date"][i].year)
        meses.append(acao_df["Date"][i].month)
        i+=1

    anos = list(dict.fromkeys(anos))
    meses = list(dict.fromkeys(meses))
    

    anos.sort(reverse=False)
    meses.sort(reverse=False)


    i = 0
    i_ano = 0
    i_mes = 0

    controlador = 0

    
    dados = pd.DataFrame()


    while(i<len(acao_df)):


        while(i_ano<len(anos)):

            while(i_mes<len(meses)):

                if(controlador == 0):
                    
                    if(h_l == 0):
                        close = acao_df[str(anos[i_ano])+"-"+str(meses[i_mes]):str(anos[i_ano])+"-"+str(meses[i_mes])]["Close"].min()
                        date =acao_df[str(anos[i_ano])+"-"+str(meses[i_mes]):str(anos[i_ano])+"-"+str(meses[i_mes])][acao_df["Close"]==close].index.values
                        
                        dados = [[close,date]]

                    elif(h_l==1):
                        close = acao_df[str(anos[i_ano])+"-"+str(meses[i_mes]):str(anos[i_ano])+"-"+str(meses[i_mes])]["Close"].max()
                        date =acao_df[str(anos[i_ano])+"-"+str(meses[i_mes]):str(anos[i_ano])+"-"+str(meses[i_mes])][acao_df["Close"]==close].index.values
                        
                        dados = [[close,date]]

               
                    controlador=1
                else:

                    if(h_l==0):
                        close = acao_df[str(anos[i_ano])+"-"+str(meses[i_mes]):str(anos[i_ano])+"-"+str(meses[i_mes])]["Close"].min()
                        date =acao_df[str(anos[i_ano])+"-"+str(meses[i_mes]):str(anos[i_ano])+"-"+str(meses[i_mes])][acao_df["Close"]==close].index.values

                    elif(h_l==1):
                        close = acao_df[str(anos[i_ano])+"-"+str(meses[i_mes]):str(anos[i_ano])+"-"+str(meses[i_mes])]["Close"].max()
                        date =acao_df[str(anos[i_ano])+"-"+str(meses[i_mes]):str(anos[i_ano])+"-"+str(meses[i_mes])][acao_df["Close"]==close].index.values


                    if(not math.isnan(close)):

                        if(len(date)>1):
                            date2 = date[0]

                            date = list()
                            date = [date2]

                        dados.append([close,date])
                        #dados.append([close])

                i_mes+=1


            i_mes = 0
            i_ano+=1

        i+=1
    dados = pd.DataFrame(dados,columns=['Close','Date'])

    return dados


def dados_lucro(altas_np,baixas_np):

    tamanho = 0
    diferencas = list()
    datas = list()
    data_compra = list()
    data_venda = list()
    valor_compra = list()
    valor_venda = list()
    lucro = list()
    
    
    if(len(altas_np)==len(baixas_np)):

        tamanho = len(altas_np)

    i = 0

    controlador = 0

    
    primeiro_ciclo = 0

    while(i<tamanho):
        
        if(len(baixas_np[i][1])==1):
            
            if(primeiro_ciclo == 0):

                b = baixas_np[i][1][0]

                vlr_c = baixas_np[i][0]

                a = altas_np[i][1][0]
                
                primeiro_ciclo+=1

            else:

                if(controlador == 0):
                    b = baixas_np[i][1][0]
                    vlr_c = baixas_np[i][0]
                    a = altas_np[i][1][0]
                else:
                    a = altas_np[i][1][0]



            if(b<a):

                lucro.append(altas_np[i][0] - vlr_c)

                data_venda.append(altas_np[i][1][0])

                valor_venda.append(altas_np[i][0])

                data_compra.append(b)

                valor_compra.append(vlr_c)    
                
                
                controlador = 0
            else:

                controlador = 1

        i+=1

    dados= list(zip(data_compra,valor_compra,data_venda,valor_venda,lucro))

    negocios = pd.DataFrame(dados,columns=["Data compra","Valor compra","Data venda","Valor venda","Lucro"])

    return negocios



def GetAcoes(tickers,todas_acoes,data_inicio=0,data_fim=0):

    contador = 0
    
    lista_de_acoes = list()
    
    cont = 0
    
    if(todas_acoes==0):
        tickers = pd.DataFrame(tickers,columns=["Acoes"])
    

    for ticker in tickers["Acoes"]:
        
        if(contador<10):

            print(ticker)
            
            acao = yf.download(ticker)
            
            if(not data_inicio != 0 and data_fim != 0):
                print("oi")
                acao = acao[data_inicio:data_fim]
            
            acao_df = acao.rename_axis('Date').reset_index()
            
            
            acao_df = acao_df[['Date','Close','Open','High','Low']]
            
            '''OBJETO AÇÃO'''
            acao = Acao()
            acao.ticker = ticker

            
            
            '''ANALISE MENSAL'''
            altas_mes_df = High_low2(acao_df,1)
            baixas_mes_df = High_low2(acao_df,0)
            
            altas_mes_np = altas_mes_df.to_numpy()
            baixas_mes_np = baixas_mes_df.to_numpy()
            
            altas_mes_df = altas_mes_df.dropna()
            baixas_mes_df = baixas_mes_df.dropna()
            
            altas_mes_df = altas_mes_df.rename({"Close":"Fechamento alta","Date":"Data alta"},axis=1)
            baixas_mes_df = baixas_mes_df.rename({"Close":"Fechamento baixa","Date":"Data baixa"},axis=1)
            
            #print(type(baixas_mes_df["Data baixa"]))
            datas_baixas_normalizadas_mes = list()
            datas_altas_normalizadas_mes = list()
    
            j=0
            while j< len(baixas_mes_df["Data baixa"]):
                
                #print(baixas_mes_df["Data baixa"].values[j][0])
                datas_baixas_normalizadas_mes.append(baixas_mes_df["Data baixa"].values[j][0])
                datas_altas_normalizadas_mes.append(altas_mes_df["Data alta"].values[j][0])
                
                j+=1
        
            baixas_mes_df["Data baixa"] = datas_baixas_normalizadas_mes 
            altas_mes_df["Data alta"] = datas_altas_normalizadas_mes
            
            
            dados= list(zip(baixas_mes_df["Fechamento baixa"],baixas_mes_df["Data baixa"].values,altas_mes_df["Fechamento alta"],altas_mes_df["Data alta"].values))
            acao.sazonalidade_mes = pd.DataFrame(dados,columns=["Fechamento baixa","Data baixa","Fechamento alta","Data alta"])            
            
            acao.negociacoes_mes = dados_lucro(altas_mes_np,baixas_mes_np)
            acao.negociacoes_mes["Taxa retorno"] = np.log(acao.negociacoes_mes["Valor venda"]/acao.negociacoes_mes["Valor compra"])*100
            
            
            
            '''ANALISE POR PARAMETRO'''
            altas_param_df = High_Low(acao_df,1,15)
            baixas_param_df = High_Low(acao_df,0,15)
            
            altas_param_df = altas_param_df.iloc[:,[1,0]]
            baixas_param_df = baixas_param_df.iloc[:,[1,0]]
            
            altas_param_np = altas_param_df.to_numpy()
            baixas_param_np = baixas_param_df.to_numpy()
            
            altas_param_df = altas_param_df.rename({"Close":"Fechamento alta","Date":"Data alta"},axis=1)
            baixas_param_df = baixas_param_df.rename({"Close":"Fechamento baixa","Date":"Data baixa"},axis=1)
            
            datas_baixas_normalizadas = list()
            datas_altas_normalizadas = list()
            
            j=0
            while j< len(baixas_param_df):
                
                
                dia= baixas_param_df['Data baixa'][j][0].day
                mes = baixas_param_df['Data baixa'][j][0].month
                ano = baixas_param_df['Data baixa'][j][0].year
                
                datas_baixas_normalizadas.append(pd.to_datetime(str(ano)+"-"+str(mes)+"-"+str(dia),format='%Y-%m-%d'))
                
                dia = altas_param_df['Data alta'][j][0].day
                mes = altas_param_df['Data alta'][j][0].month
                ano = altas_param_df['Data alta'][j][0].year
                
                datas_altas_normalizadas.append(pd.to_datetime(str(ano)+"-"+str(mes)+"-"+str(dia),format='%Y-%m-%d'))
                
                j+=1
                        
            baixas_param_df['Data baixa'] = datas_baixas_normalizadas 
            
            altas_param_df['Data alta'] = datas_altas_normalizadas
            
            
            dados= list(zip(baixas_param_df["Fechamento baixa"],baixas_param_df["Data baixa"].values,altas_param_df["Fechamento alta"],altas_param_df["Data alta"].values))
            acao.sazonalidade_param = pd.DataFrame(dados,columns=["Fechamento baixa","Data baixa","Fechamento alta","Data alta"])
               
            acao.negociacoes_param = dados_lucro(altas_param_np,baixas_param_np)
            acao.negociacoes_param["Taxa retorno"] = np.log(acao.negociacoes_param["Valor venda"]/acao.negociacoes_param["Valor compra"])*100
            
            acao.fechamento = acao_df.set_index("Date")
            
            lista_de_acoes.append(acao)
            
            #contador += 1
        else:
            break
        
    return lista_de_acoes


def PesquisaAcao(acao_pesquisada, info):
    
    i = 0
    achou = 0
    tail = 0
    acao_pesquisada_info = pd.DataFrame()

    if(tail<len(info)):

        while(i<len(info)):

            if(info[i][1] == acao_pesquisada):
                acao_pesquisada_info = info[i][0]

                acao_pesquisada_info["Taxa retorno"] = np.log(acao_pesquisada_info["Valor venda"]/acao_pesquisada_info["Valor compra"])*100
                
                achou = 1

            if(achou==1):
              break
            i+=1
    else:

        print("O valor de tail deve ser menor que ",len(info))  
    
    return acao_pesquisada_info


def Prever_negociacoes_lstm_param(ticker,info,dias_anteriores = 10,tipo="compra_venda"):

    i = 0
    
    while(i<len(info)):

        if(ticker == info[i].ticker):
            
            if(tipo=="compra_venda"):
                compra_prevista_lstm = prever_valor_lstm(pd.DataFrame(info[i].negociacoes_param["Valor compra"]),dias_anteriores,1,180)
                venda_prevista_lstm = prever_valor_lstm(pd.DataFrame(info[i].negociacoes_param["Valor venda"]),dias_anteriores,1,180)
            
            elif(tipo=="alta_baixa"):
                compra_prevista_lstm = prever_valor_lstm(pd.DataFrame(info[i].baixas_param["Close"]),dias_anteriores,1,180)
                venda_prevista_lstm = prever_valor_lstm(pd.DataFrame(info[i].altas_param["Close"]),dias_anteriores,1,180)

        i+=1
    
    return [compra_prevista_lstm, venda_prevista_lstm]

def Prever_negociacoes_media_param(ticker,info,dias_anteriores=10,tipo="compra_venda"):
    
    
    i = 0

    while(i<len(info)):

        if(ticker == info[i].ticker):
            
            if(tipo=="compra_venda"):
                compra_prevista_media = prever_valor_media(info[i].negociacoes_param["Valor compra"],dias_anteriores)
                venda_prevista_media = prever_valor_media(info[i].negociacoes_param["Valor venda"],dias_anteriores)
            
            elif(fipo=="alta_baixa"):
                compra_prevista_media = prever_valor_media(info[i].baixas_param["Close"],dias_anteriores)
                venda_prevista_media = prever_valor_media(info[i].altas_param["Close"],dias_anteriores)
                
        i+=1

    
    
    return [compra_prevista_media,venda_prevista_media]



def PesquisarAcoes(lista_de_acoes):


    info = GetAcoes(lista_de_acoes,0)
    
    neg_param = pd.DataFrame()
    neg_mes = pd.DataFrame()

    sazon_param = pd.DataFrame()
    sazon_mes = pd.DataFrame()

    fechamento = pd.DataFrame()

    i = 0
    while i< len(info):   
        
        info[i].negociacoes_param["ticker"] = info[i].ticker
        info[i].negociacoes_mes["ticker"] = info[i].ticker
        info[i].sazonalidade_param["ticker"] = info[i].ticker
        info[i].sazonalidade_mes["ticker"] = info[i].ticker
        info[i].fechamento["ticker"] = info[i].ticker
        
        
        neg_param=pd.concat([neg_param,info[i].negociacoes_param])
        neg_mes = pd.concat([neg_mes,info[i].negociacoes_mes])
                             
        sazon_param = pd.concat([sazon_param,info[i].sazonalidade_param])
        sazon_mes = pd.concat([sazon_mes,info[i].sazonalidade_mes])
        
        fechamento = pd.concat([fechamento,info[i].fechamento])


        i+=1

    '''
    neg_param.to_csv("ng_param.csv")
    neg_mes.to_csv("ng_mes.csv")
    sazon_param.to_csv("sazon_param.csv")
    sazon_mes.to_csv("sazon_mes.csv")
    '''

    return neg_param,neg_mes,sazon_param,sazon_mes,fechamento