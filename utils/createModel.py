# Cria um novo modelo em um app do Django, já o disponibilizando para CRUD no Admin do Djang
# 1. Cria ou edita o arquivo models.py do App com um esqueleto básico do modelo
# 2. Adiciona o modelo ao Admin do Django para poder ser editado
import sys, os, subprocess

def main():
    # verifica os argumentos de chamada do programa e se estรก no diretรณrio certo
    if (len(sys.argv)!=3 or not os.path.isfile('manage.py')) :
        print('error: not enough arguments')
        print('usage: python createModel.py <nomeApp> <nomeModel>')
        exit(2)

    nomeApp = sys.argv[1]
    nomeModel  = sys.argv[2]
    
    if (jaPossuiModel(nomeApp, nomeModel)):
        print('error: model already exists')
        print('usage: python createModel.py <nomeApp> <nomeModel>')
        exit(2)

    print ('Usando App: ' + nomeApp)
    print ('Criando Model: ' + nomeModel)
    alteraArquivoModelApp(nomeApp, nomeModel)
    alteraArquivoAdminApp(nomeApp, nomeModel)
    
    print('Esqueleto do Model criado em: /' +nomeApp + '/models.py')
    print('Model adicionado para CRUD em admin.py. Para criar um usuário, executar: python3 manage.py createsuperuser')
    print('Para ver os tipos de campos, acessar: https://docs.djangoproject.com/en/3.0/ref/models/fields/')
    print('Após implementar a classe, executar os seguintes comandos:')
    print('- python manage.py makemigrations')
    print('- python manage.py migrate')
    
    

#------------------------------------------------------------------------------------------
def alteraArquivoModelApp(nomeApp, nomeModel):
    arquivo = nomeApp + '/models.py'
    destino = open(arquivo, 'a')

    texto = '\n\nclass ' + nomeModel + '(models.Model):\n    def __str__(self):\n        return self.xxx\n'
    destino.write(texto)
    destino.close()
    

#------------------------------------------------------------------------------------------
def alteraArquivoAdminApp(nomeApp, nomeModel):
    arquivo = nomeApp + '/admin.py'
    destino = open(arquivo, 'a')

    texto = '\n\nfrom .models import ' + nomeModel + '\n\nadmin.site.register('+nomeModel+')'
    destino.write(texto)
    destino.close()
    
#------------------------------------------------------------------------------------------    
def jaPossuiModel(nomeApp, nomeModel):
    arquivo = nomeApp + '/models.py'
    conteudo = open(arquivo).read()
    
    if (conteudo.find('class '+nomeModel+'(')>0):
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