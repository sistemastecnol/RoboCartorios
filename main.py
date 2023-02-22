from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import easygui
import time
import csv
driver = webdriver.Firefox()
driver.get("https://registradores.onr.org.br/CartorioNacional/CartorioNacional.aspx")
driver.maximize_window()
delay = 3
time.sleep(10)

CbbEstados= Select(driver.find_element(By.NAME, "ddlListaEstados"))
CbbEstados.select_by_index(26)
time.sleep(1)
lblestados = driver.find_element(By.ID, "ddlListaEstados")
estado = lblestados.get_property('value')

time.sleep(4)

cbbCidades= Select(driver.find_element(By.NAME, "ddlListaCidades"))
contadorCidades=int(len(cbbCidades.options))
#contadorCidades=270
iterador = 1
time.sleep(4)
for i in range(contadorCidades-1):
    cbbCidades = Select(driver.find_element(By.NAME, "ddlListaCidades"))
    cbbCidades.select_by_index(iterador)
    lblcidades = driver.find_element(By.ID, "ddlListaCidades")
    cidades = lblcidades.get_property('value')
    cbbCartorios1 = Select(driver.find_element(By.NAME, "ddlListaCartorios"))
    contadorCartorios = int(len(cbbCartorios1.options))
    iteradorCartorios = 1
    if contadorCartorios == 0:
        iterador = iterador + 1
        continue
    time.sleep(3)
    for i in range(contadorCartorios-1):
        cbbCartorios = Select(driver.find_element(By.NAME, "ddlListaCartorios"))
        cbbCartorios.select_by_index(iteradorCartorios)

        try:
            element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "lblRazao"))

            )
            lblRazao = driver.find_element(By.ID, "lblRazao")
            Razao = lblRazao.get_attribute("innerHTML")
            lblReponsavel = driver.find_element(By.ID, "lblResponsavel")
            responsavel = lblReponsavel.get_attribute("innerHTML")
            lblRua = driver.find_element(By.ID, "lblLogradouro")
            Rua = lblRua.get_attribute("innerHTML")
            lblNumero = driver.find_element(By.ID, "lblNumero")
            Numero = lblNumero.get_attribute("innerHTML")
            lblBairro = driver.find_element(By.ID, "lblBairro")
            Bairro = lblBairro.get_attribute("innerHTML")
            lblCEP = driver.find_element(By.ID, "lblCep")
            CEP = lblCEP.get_attribute("innerHTML")
            lblDDD = driver.find_element(By.ID, "lblDDDTelefone")
            DDD = lblDDD.get_attribute("innerHTML")
            lblTelefone = driver.find_element(By.ID, "lblTelefone")
            Telefone = lblTelefone.get_attribute("innerHTML")
            lblEmail = driver.find_element(By.ID, "lblEmail")
            Email = lblEmail.get_attribute("innerHTML")
            lblSite = driver.find_elements(By.TAG_NAME, 'li')
            Site = lblSite[73].get_attribute('textContent').replace('\n', '').replace(
                'Site:                                              ', '').replace(
                '                                            ', ' ').replace('                                 ', '')
            Servicos = lblSite[74].get_attribute('textContent').replace('\n', '').replace(
                'Serviços ativados ao cartório:                       ', '').replace(
                '                                                 ', '')
            assert "No results found." not in driver.page_source
            header = ['Razao', 'Responsavel', 'Rua', 'Numero', 'Cep', 'DDD', 'Telefone', 'Email', 'Site', 'Serviços']
            data = [estado, cidades, Razao, responsavel, Rua, Numero, CEP, Bairro, DDD, Telefone, Email, Site, Servicos]

            with open('cartorios.csv', 'a', newline='', encoding='UTF8') as f:
                writer = csv.writer(f)
                # writer.writerow(header)
                writer.writerow(data)

            iteradorCartorios = iteradorCartorios + 1

        except:
             print('erro')
    iterador = iterador + 1
driver.close()
easygui.msgbox("Processo Finalizado!", title="Robô cartórios")