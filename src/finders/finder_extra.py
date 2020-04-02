import time
from datetime import date

from bs4 import BeautifulSoup

from src.config.selenium_driver import SeleniumDriver
from src.domain.diaper import Diaper
from src.domain.price import Price
from src.finders.finder import Finder


class FinderExtra(Finder):
    URL = "https://www.clubeextra.com.br/secoes/C2475/fraldas?qt=12&ftr=facetSubShelf_ss:2475_Fraldas&p=0&gt=list"
    STORE = "Extra"

    def __init__(self, selenium_driver: SeleniumDriver):
        self._driver = selenium_driver.obter_driver(FinderExtra.URL)

    def find(self):
        print("Iniciando scrapping de fraldas do extra")
        driver = self._driver
        self._scrollar_pagina_para_carregar_produtos()
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        driver.quit()
        return self._obter_info_produtos(soup)

    def _obter_info_produtos(self, soup):
        print("Obtendo informação das Fraldas no HTML")
        divs = soup.findAll('div', {"class": "container-card"})
        lista = list()
        for card in divs:
            sku = card.find_parent('div', {"class": "panel-product"}).find('div', {"class": "sku"})
            name = card.find('p', {"class": "product-description"})
            price = card.find('p', {"class": "normal-price"})
            price = price if price is not None else card.find(
                'p', {"class": "discount-price"})
            image = card.find('img')
            if image is not None and name is not None and price is not None:
                diaper = Diaper(
                    int(sku.get_text()),
                    name.get_text().strip(),
                    image.get('src'),
                    FinderExtra.STORE)
                diaper.add_price(Price(self._retirar_formatacao_moeda(price.get_text()), date.today()))
                lista.append(diaper)
        return lista

    def _scrollar_pagina_para_carregar_produtos(self):
        print("Scrollando pagina até carregar todas as fraldas")
        texto_total_produtos = self._obter_texto_total_produtos()
        while not self._todos_produtos_foram_carregados(texto_total_produtos):
            self._driver.execute_script("window.scrollBy(0,1000)")
            texto_total_produtos = self._obter_texto_total_produtos()
        time.sleep(10)

    def _obter_texto_total_produtos(self):
        return self._driver.find_element_by_class_name(
            "filter,ng-binding,ng-scope").text

    def _todos_produtos_foram_carregados(self, texto_total_produtos):
        qtd_carregado = int(texto_total_produtos.split()[1])
        qtd_total = int(texto_total_produtos.split()[3])
        print(f"Quantidade carregado {qtd_carregado} de {qtd_total}")
        return True if qtd_carregado == qtd_total else False

    def _retirar_formatacao_moeda(self, price_text: str):
        return price_text.split()[1].replace(",", ".")

