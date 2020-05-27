# Facilita a criação de apps para o Django.
# 1. Cria a aplicação no Django
# 2. Insere a aplicação nas URLs do Projeto
# 3. Insere a aplicação como uma aplicação do Django em settings.py
# 4. Cria um arquivo de URLs para o Projeto

import sys, os, subprocess

def main():
    # verifica os argumentos de chamada do programa e se está no diretório certo
    if (len(sys.argv)!=3 or not os.path.isfile('manage.py')) :
        print('error: not enough arguments')
        print('usage: python createDjango.py <nomeServidor> <nomeNovoApp>')
        exit(2)

    nomeServidor = sys.argv[1]
    nomeNovoApp  = sys.argv[2]
    
    if (existeApp(nomeNovoApp)):
        print('error: app already exists')
        exit(2)

    djangoSettings = nomeServidor+'/settings.py'
    if (not os.path.isfile(djangoSettings)):
        print('error: cannot find django setting file:' + djangoSettings)
        exit(2)

    print ('Criando app: ' + nomeNovoApp)
    criaApp(nomeServidor, nomeNovoApp)
    print ('Criando arquivos de URL no App')
    criaArquivoUrlsApp(nomeNovoApp)
    print ('Alterando arquivo de configuração: ' + djangoSettings )
    alteraSettings(djangoSettings, nomeNovoApp)
    print ('Alterando arquivo URL do Projeto')
    alteraUrlsDoProjeto(nomeServidor, nomeNovoApp)

#------------------------------------------------------------------------------------------
def criaApp(nomeServidor, nomeNovoApp):
    process = subprocess.Popen(['python', 'manage.py', 'startapp', nomeNovoApp],
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

#------------------------------------------------------------------------------------------
def alteraSettings(djangoSettings, nomeNovoApp):
    arquivo = open(djangoSettings).read()

    arquivo = insereTextoConfig(arquivo, 'INSTALLED_APPS', '\''+nomeNovoApp+'\'')

    destino = open(djangoSettings, 'w+')
    destino.write(arquivo)
    destino.close()

#------------------------------------------------------------------------------------------
def criaArquivoUrlsApp(nomeApp):
    destino = open(nomeApp+'/urls.py', 'w+')
    destino.write('from django.conf.urls import url, include\n')
    destino.write('from django.contrib import admin\n')
    destino.write('from . import views\n\n')
    destino.write('urlpatterns = [\n\n]')
    destino.close()

#------------------------------------------------------------------------------------------
def alteraUrlsDoProjeto(nomeServidor, nomeNovoApp):
    nomeArq = nomeServidor + '/urls.py'
    arquivo = open(nomeArq).read()
    
    if (arquivo.find('\nfrom django.urls import include, path')==-1):
        arquivo = '\nfrom django.urls import include, path\n' + arquivo
    
    arquivo = insereTextoConfig(arquivo, 'urlpatterns', 'path(\''+nomeNovoApp+'/\', include(\''+nomeNovoApp+'.urls\'))')

    destino = open(nomeArq, 'w+')
    destino.write(arquivo)
    destino.close()
    
#------------------------------------------------------------------------------------------
def existeApp(nomeApp):
    if os.path.exists(nomeApp):
        return True
    return False

#------------------------------------------------------------------------------------------
def insereTextoConfig(texto, variavel, inclusao):
    inicio = texto.find(variavel)
    fim = texto.find(']', inicio)
    return texto[:fim] + '\t'+inclusao+',\r\n' + texto[fim:]

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()