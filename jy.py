import os
from socket import close
from pandas import ExcelWriter
import time
import pandas as pd
from selenium import webdriver
import urllib.request

url_login= "https://www.joyasnevada.cl/log"
# login_data= {'email':'c.illanes.d@gmail.com', 'password':'vamosasermillonarios'}

br = webdriver.Chrome('C:\laragon\www\chromedriver_win32 (98.0.4)\chromedriver.exe')
# br.get(url_login)
br.get(r'C:\Users\Carlos\Google Drive\joya\Pedido N°23149 _ Mi cuenta _ Joyas de Plata por Mayor - Joyas Nevada.html')
#saltar el popUp
# try:
#         br.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/button').click()
#         br.find_element_by_xpath( '/html/body/div[2]/div/div[1]/div/button').click()
#         br.find_element_by_xpath('/html/body').click()
# except:
#     pass
# #login
# br.find_element_by_name('email').send_keys('c.illanes.d@gmail.com')
# br.find_element_by_name('password').send_keys('vamosasermillonarios')
# br.find_element_by_xpath('//*[@id="tt-pageContent"]/div[2]/div/div/div/div[2]/div/div/form/div[3]/div[1]/div/button').click()
# time.sleep(1)
# br.get('https://www.joyasnevada.cl/mi-cuenta/pedido/id/23149/')
time.sleep(1)
# br.get(r'C:\Users\Carlos\Google Drive\joya\Pedido N°23149 _ Mi cuenta _ Joyas de Plata por Mayor - Joyas Nevada2.html')

# time.sleep(2)
br.find_element_by_xpath('/html/body').click()
lista =[]
#obtener de la pagina de pedidos un set() con los link de los productos
# elems = br.find_element_by_class_name('boxCarro') and br.find_elements_by_xpath("//a[@href]")
# for elem in elems:
#     if elem not in lista:
#         lista.append(elem.get_attribute("href"))

# El range es el n° del Div al que tiene que hacer referencia, cambia depende del numero de item en el pedido, al parecer siempre empieza en 5
for i in range(5,53):
    page = br.find_element_by_xpath('//*[@id="tt-pageContent"]/div/div/div/div/div/div['+str(i)+']/div[1]/a').get_attribute("href")
    lista.append(page)


print("lista tiene : ",len(lista))
myset= set(lista)
print("el set tiene : ",len(myset))
# print(myset)
l2 = [] # lista de paginas que no se pudieron cargar{}
producto =[]
price_det=[] 
price_w=[]
codes=[]
descripcion=[]
descr_larg=[]
categoria=[]
pag=[]
imges=[]
segunda_fot=[]
imagen_chic=[]
# def url(x):
#     return x
#iterar por cada producto, sacar los datos de interes y registrar en el excel productos.xlsx
for page in myset:
    br.get(page)
    # click en el popUp
    try:
        br.find_element_by_xpath( '/html/body/div[2]/div/div[1]/div/button').click()
        br.find_element_by_xpath('/html/body').click()
    except:
        pass
    
# 
    if br.current_url == "https://www.joyasnevada.cl/404":
        l2.append(page) 
        pass

    else:
        time.sleep(1)
        product_name =br.find_element_by_xpath('//*[@id="tt-pageContent"]/div[2]/div[2]/div/div[2]/div/h1').text
        
        price_detail= br.find_element_by_xpath('//*[@id="precio-detalle"]').text
        price_wh=br.find_element_by_xpath('//*[@id="producto-precio"]/span[1]').text
        code=br.find_element_by_xpath('//*[@id="tt-pageContent"]/div[2]/div[2]/div/div[2]/div/div[2]/ul/li').text

        descrip=br.find_element_by_xpath('//*[@id="tt-pageContent"]/div[2]/div[2]/div/div[2]/div/div[5]/div/ul/li[1]').text
        try: #intenta acceder a la descripción larga y a la segunda foto
            descr_larga = br.find_element_by_xpath('//*[@id="tt-pageContent"]/div[2]/div[2]/div/div[2]/div/div[5]/div/ul/li[3]').text
            descr_larg.append(descr_larga)
            segunda_foto = br.find_elements_by_xpath('//*[@id="smallGallery"]/div/div/li[2]/a').get_attribute("data-zoom-image")
            segunda_fot.append(segunda_foto)
        except : 
            descr_larg.append('descr_larga')
            pass # sí no encuentra la desripcion larga pasa de largo
        #guardar los datos en las listas que voy a ocupar para registrar en el excel
        category=br.find_element_by_xpath('//*[@id="tt-pageContent"]/div[2]/div[2]/div/div[2]/div/div[5]/div/ul/li[2]/a').text
        producto.append(product_name)
        price_det.append(price_detail)
        price_w.append(price_wh)
        codes.append(code)
        descripcion.append(descrip)
        pag.append(page)
        
        categoria.append(category)
        
            
    
    
    
    #    Registrar en el excel
    data= [producto,price_det,price_w,codes,descripcion, descr_larg,categoria,pag]
    data_names= ['producto','price_det','price_w','codes','descripcion','descripcion larga','categoria', 'pag']
    df= pd.DataFrame(data=data, index=data_names)
    df2= pd.DataFrame(l2)
    df3= pd.DataFrame(segunda_fot)
    # df4= pd.DataFrame(imagen_chic)
    writer = ExcelWriter(r'C:\laragon\www\scrap\jy\productos.xlsx')
    df.to_excel(writer, 'Productos', index=True)
    df2.to_excel(writer, 'productos que no se cargaron', index=False)
    df3.to_excel(writer, 'tienen 2 fotos', index=False)
    # df4.to_excel(writer, imagen_chic)
    writer.save()
    time.sleep(1)




br.close()



