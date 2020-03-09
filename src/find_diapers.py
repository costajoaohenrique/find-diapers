
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def todos_produtos_foram_carregados(texto_total_produtos):
    qtd_carregado = int(texto_total_produtos.split()[1])
    qtd_total = int(texto_total_produtos.split()[3])
    return True if qtd_carregado == qtd_total else False


option = Options()
option.headless = False
driver = webdriver.Firefox(options=option)

driver.get("https://www.clubeextra.com.br/secoes/C2475/fraldas?qt=12&ftr=facetSubShelf_ss:2475_Fraldas&p=0&gt=list")
driver.implicitly_wait(20)  # in seconds

texto_total_produtos = driver.find_element_by_class_name("filter,ng-binding,ng-scope").text
print(texto_total_produtos)

while not todos_produtos_foram_carregados(texto_total_produtos):
    driver.execute_script("window.scrollBy(0,1000)")
    texto_total_produtos = driver.find_element_by_class_name("filter,ng-binding,ng-scope").text

print(driver.find_element_by_class_name("filter,ng-binding,ng-scope").text)

html_content = driver.page_source

soup = BeautifulSoup(html_content, 'html.parser')

divs = soup.findAll('div', {"class": "container-card"})

print(len(divs))

driver.quit()
