#Este código em Python utiliza a biblioteca Selenium para automatizar o envio de mensagens no WhatsApp. Ele carrega uma lista de conversas e uma lista de telefones para enviar as mensagens. A função "maturador" é responsável por escolher aleatoriamente um telefone e uma mensagem, localizar a caixa de pesquisa do WhatsApp, inserir o telefone selecionado, enviar a mensagem e retornar para a caixa de pesquisa para o próximo envio.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
import random

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(60)


#carregar a lista de numeros
conversas = [
    "Olá, como vai?",
    "Tudo bem?",
    "Qual é o seu nome?",
    "Qual é a sua idade?",
    "O que você gosta de fazer?",
    "Você tem algum hobby?",
    "Qual é o seu time do coração?",
    "Qual é a sua banda favorita?",
    "Você gosta de filmes de terror?",
    "Qual é o seu filme favorito?",
    "Você tem algum animal de estimação?",
    "Você gosta de viajar?",
    "Qual é o seu lugar favorito?",
    "Você já visitou algum país estrangeiro?",
    "Você sabe cozinhar?",
    "Qual é o seu prato favorito?",
    "Você gosta de jogar videogame?",
    "Qual é o seu jogo favorito?",
    "Você já leu algum livro interessante?",
    "Qual é o seu autor favorito?",
    "Você gosta de esportes?",
    "Qual é o seu esporte favorito?",
    "Você já praticou algum esporte?",
    "Você gosta de academia?",
    "Qual é o seu exercício favorito?",
    "Você tem algum talento?",
    "Qual é o seu sonho?",
    "Você gosta de música?",
    "Qual é o seu estilo musical favorito?",
    "Qual é a sua música favorita?",
    "Você já foi a algum show?",
    "Você gosta de dançar?",
    "Qual é o seu estilo de dança favorito?",
    "Você já fez aulas de dança?",
    "Você gosta de pintura?",
    "Qual é o seu estilo de arte favorito?",
    "Você já visitou algum museu?",
    "Você gosta de ler notícias?",
    "Qual é o seu site de notícias favorito?",
    "Qual é o seu assunto favorito?",
    "Você gosta de tecnologia?",
    "Qual é o seu gadget favorito?",
    "Você já visitou alguma feira de tecnologia?",
    "Você gosta de carros?",
    "Qual é o seu carro favorito?",
    "Você já dirigiu algum carro interessante?",
    "Você gosta de fotografia?",
    "Qual é o seu tema favorito para fotografar?",
    "Você já visitou algum lugar interessante para fotografar?",
]


#LISTA DE TELEFONES PARA ENVIAR A MENSAGEM 
telefones = ['3197054398','3182583997','3182602401','3184767331']
#ELE VAI CHAMAR OS TELEFONES DE FORMA ALEATORIA



def maturador():
    try:
        numero = random.choice(telefones)
        msg = random.choice(conversas)
        caixa_de_pesquisa = driver.find_element(By.CSS_SELECTOR, "div[title='Caixa de texto de pesquisa']")
        caixa_de_pesquisa.send_keys(numero)
        caixa_de_pesquisa.send_keys(Keys.ENTER)
        time.sleep(2)
        caixa_de_msg = driver.find_element(By.CSS_SELECTOR, "div[title='Mensagem']")
        time.sleep(1)
        caixa_de_msg.send_keys(msg)
        time.sleep(1)
        caixa_de_msg.send_keys(Keys.ENTER)
        time.sleep(1)
        caixa_de_pesquisa.click()
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(5)

        
    except:
        print('AGUARDANDO...')
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(5)

while True:
    maturador()
