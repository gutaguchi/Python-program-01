# Generated by Selenium IDE

from bs4 import BeautifulSoup
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# ----------------------------- classe fastshop ---------------------------------
lista_fast_shop = []

class fast_shop():
  def __init__(self,iphone):
    self.iphone = iphone
    self.driver = webdriver.Chrome('/Users/gustavotaguchi/Desktop/PYTHON/chromedriver')
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def acessa_fast_shop(self):
    self.driver.get("https://www.fastshop.com.br/web/")
    self.driver.set_window_size(1221, 697)
    self.driver.find_element(By.ID, "search-box-id").click()
    #self.driver.find_element(By.ID, "search-box-id").send_keys("iphone 11 pro 64")
    self.driver.find_element(By.ID, "search-box-id").send_keys(self.iphone)
    self.driver.find_element(By.ID, "search-box-id").send_keys(Keys.ENTER)
    time.sleep(5)

  def fechar_nav(self):
    self.driver.close()

# ----------------------------- classe Magazine Luiza ---------------------------------

class magazine():
  def __init__(self, iphone):
    self.iphone = iphone  
    self.driver = webdriver.Chrome('/Users/gustavotaguchi/Desktop/PYTHON/chromedriver')
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def acessa_magazine(self):
    self.driver.get("https://www.magazineluiza.com.br/")
    self.driver.set_window_size(1203, 697)
    time.sleep(10)
    self.driver.find_element(By.ID, "inpHeaderSearch").click()
    time.sleep(10)
    self.driver.find_element(By.ID, "inpHeaderSearch").send_keys(self.iphone)
    time.sleep(4)
    self.driver.find_element(By.ID, "inpHeaderSearch").send_keys(Keys.ENTER)
    self.driver.execute_script("window.scrollTo(0,142)")
    time.sleep(4)

  def fechar_nav(self):
    self.driver.close()
# ----------------------------- classe Apple Store ---------------------------------
class apple():
  
  def __init__(self):
    self.driver = webdriver.Chrome('/Users/gustavotaguchi/Desktop/PYTHON/chromedriver')
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
    
  # Acessa iphone 11 pro
  def acessa_apple_1(self):
    self.driver.get("https://www.apple.com/br/iphone/")
    self.driver.set_window_size(1221, 645)
    self.driver.find_element(By.CSS_SELECTOR, ".chapternav-item-iphone-11-pro .chapternav-icon").click()
    time.sleep(4)
    self.driver.find_element(By.LINK_TEXT, "Comprar").click()
    time.sleep(4)
    self.driver.find_element(By.CSS_SELECTOR, "#Item15_8inch_label > .form-choiceselectorlabel-twocol").click()
    time.sleep(4)
    self.driver.find_element(By.CSS_SELECTOR, "#Item2space_gray_label .ir").click()
    time.sleep(4)
    self.driver.find_element(By.CSS_SELECTOR, "#Item364gb_label .price-point").click()
    time.sleep(4)
    self.driver.execute_script("window.scrollTo(0,755)")
    
    
  # Acessa iphone 11
  def acessa_apple_2(self):
    self.driver.get("https://www.apple.com/br/shop/buy-iphone/iphone-11")
    self.driver.set_window_size(1203, 697)
    time.sleep(4)
    self.driver.find_element(By.CSS_SELECTOR, ".black").click()
    time.sleep(4)
    self.driver.find_element(By.CSS_SELECTOR, "#Item264gb_label small").click()
    self.driver.execute_script("window.scrollTo(0,692)")
    time.sleep(4)
    
    # Acessa iphone XR
  def acessa_apple_3(self):
    self.driver.get("https://www.apple.com/br/shop/buy-iphone/iphone-xr")
    self.driver.set_window_size(1203, 697)
    time.sleep(4)
    self.driver.find_element(By.CSS_SELECTOR, ".black > .ir").click()
    time.sleep(4)
    self.driver.execute_script("window.scrollTo(0,1)")
    time.sleep(4)
    self.driver.find_element(By.CSS_SELECTOR, "#Item264gb_label small").click()
    self.driver.execute_script("window.scrollTo(0,690)")
    time.sleep(4)

  def fechar_nav(self):
    self.driver.close()
  

#-------------------------------------------------------------------------------------


  
resposta = 0
while resposta != 9:
    print('IPHONE - 64GB')
    print('-----------------')
    print('1 - iphone-11-pro')
    print('2 - iphone-11')
    print('3 - iphone-xr')
    print('9 - Sair do programa')

    resposta = int(input('Escolha o modelo ou digite 9 p/ sair (Digite 1, 2 ou 3):'))

    if resposta == 1:
        iphone = 'iphone 11 pro 64'
    elif resposta == 2:
        iphone = 'iphone 11 64'
    else:
        iphone = 'iphone xr 64'


    if resposta != 9:
        print('Consultando...')

#-----tratamento magazine
      
        acesso = magazine(iphone)
        acesso.acessa_magazine()
        site = BeautifulSoup(acesso.driver.page_source, 'html.parser')
        acesso.fechar_nav()

        #pegar o nome do celular
        nome = site.find('div', class_='nm-product-info')
        aux_iphone_magazine = nome.text
       
        nome_iphone_magazine = aux_iphone_magazine.replace('\n', '')
        nome_iphone_magazine =nome_iphone_magazine[16:]
        nome_iphone_magazine =nome_iphone_magazine[:26]
        print(nome_iphone_magazine)

        #pegar o preco do celular
        preco = site.find('div', class_='nm-price-container')
        preco_iphone_magazine = preco.text
        

        
#-----tratamento fastshop
        
        lista_iphone_fastshop = []
        aux_iphone_fastshop = ''
      
        acesso = fast_shop(iphone)
        acesso.acessa_fast_shop()
        site = BeautifulSoup(acesso.driver.page_source, 'html.parser')
        acesso.fechar_nav()
        
        #pegar o nome do celular
        nome = site.find('h3', class_='horizontal-grid-short-description prod-title')
        aux_iphone_fastshop = nome.text
        
        lista_iphone_fastshop = aux_iphone_fastshop.split(',')
        #print(lista_iphone_fastshop)
        nome_iphone_fastshop = lista_iphone_fastshop[0]

        #pegar o preco do celular
        preco = site.find('p', class_='current')
        preco_iphone_fastshop = preco.text

        #tratamento p limpar o preco
        preco_iphone_fastshop = preco_iphone_fastshop.replace('\n', ' ')
        preco_iphone_fastshop = preco_iphone_fastshop.replace(' ', '')
        
        y = 0
        string_new = ''
        
        for i in preco_iphone_fastshop:
            if y != 2 and y < 11:
                string_new = string_new + i
            y += 1
        

#-----tratamento Apple
        if resposta == 1:
            acesso = apple()
            acesso.acessa_apple_1()
            site = BeautifulSoup(acesso.driver.page_source, 'html.parser')
            acesso.fechar_nav()

            nome_celulares = site.find('title')
            nome_celulares_iphone = nome_celulares.text
               


            preco_celulares_iphone = site.find('span', class_='as-price-currentprice')
            preco_celulares_iphone = preco_celulares_iphone.text

            preco_celulares_iphone = preco_celulares_iphone.replace('\n', '')
            preco_celulares_iphone = preco_celulares_iphone.replace(' ', '')
            
        elif resposta == 2:
            acesso = apple()
            acesso.acessa_apple_2()
            site = BeautifulSoup(acesso.driver.page_source, 'html.parser')
            acesso.fechar_nav()

            nome_celulares = site.find('title')
            nome_celulares_iphone = nome_celulares.text
               


            preco_celulares_iphone = site.find('span', class_='as-price-currentprice')
            preco_celulares_iphone = preco_celulares_iphone.text

            preco_celulares_iphone = preco_celulares_iphone.replace('\n', '')
            preco_celulares_iphone = preco_celulares_iphone.replace(' ', '')
            
        elif resposta == 3:
            acesso = apple()
            acesso.acessa_apple_3()
            site = BeautifulSoup(acesso.driver.page_source, 'html.parser')
            acesso.fechar_nav()

            nome_celulares = site.find('title')
            nome_celulares_iphone = nome_celulares.text
               


            preco_celulares_iphone = site.find('span', class_='as-price-currentprice')
            preco_celulares_iphone = preco_celulares_iphone.text

            preco_celulares_iphone = preco_celulares_iphone.replace('\n', '')
            preco_celulares_iphone = preco_celulares_iphone.replace(' ', '')

        else:
            pass


        print('')
        print('     ==========================')
        print('   * FastShop')
        print('     -----------')
        print('     Celular:', nome_iphone_fastshop)
        print('     Preco: ', string_new)
        print('')
        print('   * Apple store BR')
        print('     -----------')
        print('     Celular:', nome_celulares_iphone)
        print('     Preco: ', preco_celulares_iphone)
        print('')
        print('   * Magazine Luize')
        print('     -----------')
        print('     Celular:', nome_iphone_magazine)
        print('     Preco: ', preco_iphone_magazine)
        print('')
        print('')

print('Fim do programa')
