import os
import time
from selenium import webdriver
import pandas as pd
import urllib3

br= webdriver.Chrome(r'C:\laragon\www\chromedriver_win32 (98.0.4)\chromedriver.exe')

url= ["https://www.joyasnevada.cl/producto/51196-colgante-corazon-flor-circones-multicolor/",
"https://www.joyasnevada.cl/producto/29886-cadena-ovalos-rolo/",
"https://www.joyasnevada.cl/producto/45645-pulsera-ajustable-infinito-karma-circones/",
"https://www.joyasnevada.cl/producto/31406-pulsera-grumet-facetada/",
"https://www.joyasnevada.cl/producto/15970-cadena-veneciana/",
"https://www.joyasnevada.cl/producto/48804-pulsera-chakra-svadhisthana/",
"https://www.joyasnevada.cl/producto/36031-cadena-espiral/",
"https://www.joyasnevada.cl/producto/50827-colgante-llamador-de-angeles-14-mm/",
"https://www.joyasnevada.cl/producto/49010-anillo-constelacion-circones-signo-sagitario/",
"https://www.joyasnevada.cl/producto/51288-conjunto-corazon-circones/",
"https://www.joyasnevada.cl/producto/51084-conjunto-corazon-infinito-circones/",
"https://www.joyasnevada.cl/producto/50045-aro-trepador-mariposa-circones-por-unidad/",
"https://www.joyasnevada.cl/producto/45712-aro-desigual-simbolos-circones/",
"https://www.joyasnevada.cl/producto/17456-pulsera-grumet/",
"https://www.joyasnevada.cl/producto/16493-cadena-veneciana/",
"https://www.joyasnevada.cl/producto/50838-colgante-yin-yang-esmaltado-circones-naranja/",
"https://www.joyasnevada.cl/producto/50949-collar-infinito-circones/",
"https://www.joyasnevada.cl/producto/51091-conjunto-corazon-circon-amatista/",
"https://www.joyasnevada.cl/producto/50965-collar-corazon-circones/",
"https://www.joyasnevada.cl/producto/36788-anillo-doble-corazon-midi-del-deseo-circones/",
"https://www.joyasnevada.cl/producto/51072-conjunto-corazones/",
"https://www.joyasnevada.cl/producto/49286-argolla-huggie-yin-yang-circones-onix-12/",
"https://www.joyasnevada.cl/producto/49702-argolla-corte-cuadrado-14-mm/",
"https://www.joyasnevada.cl/producto/39123-aro-bidu-simbolo-de-la-paz/",
"https://www.joyasnevada.cl/producto/48915-aro-trepador-patitas/",
"https://www.joyasnevada.cl/producto/18234-cadena-cartier/",
"https://www.joyasnevada.cl/producto/50843-set-collar-y-aro-llave-circones/",
"https://www.joyasnevada.cl/producto/50728-colgante-mandala/",
"https://www.joyasnevada.cl/producto/50821-colgante-llamador-de-angeles-flor-de-loto-13-mm/",
"https://www.joyasnevada.cl/producto/17010-conjunto-mandala/",
"https://www.joyasnevada.cl/producto/15987-cadena-singapur/",
"https://www.joyasnevada.cl/producto/50337-anillo-cadena-cruz-circones/",
"https://www.joyasnevada.cl/producto/43247-pulsera-cartier-facetada/",
"https://www.joyasnevada.cl/producto/51167-pulsera-corazon-infinito-circones/",
"https://www.joyasnevada.cl/producto/50515-aro-delfin-circones-y-esferas-por-unidad/",
"https://www.joyasnevada.cl/producto/8589-aro-perla-8-mm/",
"https://www.joyasnevada.cl/producto/49003-anillo-constelacion-circones-signo-tauro/",
"https://www.joyasnevada.cl/producto/34322-aro-karma-con-circones/",

]
imagen_chic =[]




for e in url:
    br.get(e)
    product_name =br.find_element_by_xpath('//*[@id="tt-pageContent"]/div[2]/div[2]/div/div[2]/div/h1').text


    try :
        carpeta= '../'+product_name
        os.mkdir(carpeta)
        imagen_principal= br.find_element_by_xpath('/html/body/div[9]/div/div').value_of_css_property("background-image")
    
        print("esto es imagen principal",imagen_principal[5:-2])
        
        urllib3.request.urlretrieve(imagen_principal[5:-2], carpeta)
        time.sleep(1)
        imagen_chica= br.find_element_by_xpath('//*[@id="smallGallery"]/div/div/li/a').get_attribute('data-image')
        imagen_chic.append(product_name)
        urllib3.request.urlretrieve(imagen_chica, carpeta)
                
    except :
        print(e ,'no se pudo guardar')
