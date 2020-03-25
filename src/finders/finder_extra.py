import time
from bs4 import BeautifulSoup
from src.config.selenium_driver import SeleniumDriver
from src.models.diaper import Diaper
from src.finders.finder import Finder


class FinderExtra(Finder):

    URL = "https://www.clubeextra.com.br/secoes/C2475/fraldas?qt=12&ftr=facetSubShelf_ss:2475_Fraldas&p=0&gt=list"

    def __init__(self, driver: SeleniumDriver):
        self._driver = driver.obter_driver(FinderExtra.URL)

    def find(self):
        driver = self._driver
        self.scrollar_pagina_para_carregar_produtos(driver)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        self.obter_info_produtos(soup)
        driver.quit()

    def obter_info_produtos(self, soup)-> list:
        divs = soup.findAll('div', {"class": "container-card"})
        lista = list()
        for card in divs:
            name = card.find('p', {"class": "product-description"})
            price = card.find('p', {"class": "normal-price"})
            price = price if price != None else card.find(
                'p', {"class": "discount-price"})
            image = card.find('img')
            if (image != None and name != None and price != None):
                diaper = Diaper(name.get_text(),price.get_text(), image.get('src'))
                lista.append(diaper)
        return lista

    def scrollar_pagina_para_carregar_produtos(self, driver):
        texto_total_produtos = driver.find_element_by_class_name(
            "filter,ng-binding,ng-scope").text
        while not self.todos_produtos_foram_carregados(texto_total_produtos):
            driver.execute_script("window.scrollBy(0,1000)")
            texto_total_produtos = driver.find_element_by_class_name(
                "filter,ng-binding,ng-scope").text
        time.sleep(20)

    def todos_produtos_foram_carregados(self, texto_total_produtos):
        qtd_carregado = int(texto_total_produtos.split()[1])
        qtd_total = int(texto_total_produtos.split()[3])
        return True if qtd_carregado == qtd_total else False
