# Agiliza a criaçãod e Views no Django
# 1. Cria ou altera o diretório de Templates da aplicação para incluir um HTML para a view
# 2. Cria um HTML simples para a View
# 3. Adiciona a view no arquivo de views.py da aplicação
# 4. Altera o arquivo de URLs do app, adicionando a View criada.
import sys, os, subprocess

def main():
    # verifica os argumentos de chamada do programa e se estรก no diretรณrio certo
    if (len(sys.argv)!=3 or not os.path.isfile('manage.py')) :
        print('error: not enough arguments')
        print('usage: python createView.py <nomeApp> <nomeView>')
        exit(2)

    nomeApp = sys.argv[1]
    nomeView  = sys.argv[2]
    
    if (jaPossuiView(nomeApp, nomeView)):
        print('error: view already exists')
        print('usage: python createView.py <nomeApp> <nomeView>')
        exit(2)

    print ('Usando App: ' + nomeApp)
    print ('Criando view: ' + nomeView)
    criaDiretorioTemplates(nomeApp)
    criaArquivoHTMLView(nomeApp, nomeView)
    alteraArquivoViews(nomeApp, nomeView)
    alteraArquivoURLsApp(nomeApp, nomeView)
    
    print('Execute o servidor e adicione o seguinte caminho no final: /' +nomeApp + '/' + nomeView )
    

#------------------------------------------------------------------------------------------
def criaDiretorioTemplates(nomeApp):
    diretorio = nomeApp + '/templates'
    if not os.path.exists(diretorio):
        os.mkdir(diretorio)
    diretorio = diretorio + '/' + nomeApp
    if not os.path.exists(diretorio):
        os.mkdir(diretorio)
    
#------------------------------------------------------------------------------------------
def criaArquivoHTMLView(nomeApp, nomeView):
    arquivo = nomeApp + '/templates/' + nomeApp + '/' + nomeView + '.html'
    destino = open(arquivo, 'w+')
    destino.write('<html>\n\t<body>\n\t\tIncluir seu Texto HTML na View <b>' + nomeView + '</b>\n\t\t<br><br>\n\t\tTexto: {{nome}}\n\t</body>\n<html>')
    destino.close()
    print('Criado arquivo de template: ' + arquivo)
    
#------------------------------------------------------------------------------------------
def alteraArquivoViews(nomeApp, nomeView):
    arquivo = nomeApp + '/views.py'
    destino = open(arquivo, 'a')
    texto = '\ndef ' + nomeView + '(request):\n    name=\'Você pode me alterar na view.\'\n    return render(request, "' + nomeApp + '/' +nomeView + '.html", {\'nome\':name})\n\n'
    destino.write(texto)
    destino.close()
    print('Arquivo Views do App alterado: ' + arquivo)

#------------------------------------------------------------------------------------------
def alteraArquivoURLsApp(nomeApp, nomeView):
    arquivo = nomeApp + '/urls.py'
    
    conteudo = open(arquivo).read()
    conteudo = insereTextoConfig(conteudo, 'urlpatterns', 'url(r\'^'+nomeView+'/\', views.'+nomeView+', name="'+ nomeView +'")')
    
    destino = open(arquivo, 'w+')
    destino.write(conteudo)
    destino.close()
    print('Arquivo de URLs do App alterado: ' + arquivo)
    
#------------------------------------------------------------------------------------------    
def jaPossuiView(nomeApp, nomeView):
    arquivo = nomeApp + '/views.py'
    conteudo = open(arquivo).read()
    
    if (conteudo.find(' '+nomeView+'(')>0):
        
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