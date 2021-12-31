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
        logger.debug(mensagens.INICIO_LOAD_CALCULO)
        self.load_servico()

    def load_servico(self):
        """"
        Carrega o servico
        """

        logger.debug(mensagens.FIM_LOAD_CALCULO)

    def executar_calc_equacao(self, index):
        response = {}

        logger.debug(mensagens.INICIO_CALCULO)
        start_time = time.time()
        response_predicts = self.encontrar_raizes(index['a'], index['b'], index['c'])

        logger.debug(mensagens.FIM_CALCULO)
        logger.debug(f"Fim dos cálculos em {time.time()-start_time}")
        response = {
                    "Resultado da operação": response_predicts}

        return response

    def encontrar_raizes(self, a, b, c):

        logger.debug('Iniciando o cálculo...')
        
        delta = ((math.pow(2,b)) - 4 * a * c)

        if delta < 0: sqrt = 0
        else: sqrt = (math.sqrt(delta))
        
        x1 = (- b + sqrt)/(2* a)
        x2 = (- b - sqrt)/(2* a)

        response = "x1 = " + str(str(x1) + ", " + "x2 = " +  str(x2))

        return response