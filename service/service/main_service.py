import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd
import numpy as np
import math

# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class CalcEquacaoService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_servico()

    def load_servico(self):
        """"
        Carrega o servico
        """

        logger.debug(mensagens.FIM_LOAD_SERVICO)

    def executar_calc_equacao(self, index):
        response = {}

        logger.debug(mensagens.INICIO_SERVICO)
        start_time = time.time()

        response_predicts = self.encontrar_raizes((index['a'], index['b'], index['c']))

        logger.debug(mensagens.FIM_SERVICO)
        logger.debug(f"Fim de todas as predições em {time.time()-start_time}")
        response = {
                    "Resultado da operacao": response_predicts}

        return response

    def encontrar_raizes(self, a, b, c):

        logger.debug('Iniciando a solucao...')
        a = a[0]
        b = b[0]
        c = c[0]

        delta = (b**2 - 4 * a * c)

        sqrt = delta**(1/2)

        x1 = (- b + sqrt/2* a)
        x2 = (- b - sqrt/2* a)

        response = int(str(x1) + ',' + str(x2))
        # response = a + b + c

        print(response)

        return response