#Você foi contratado pela nova empresa que inaugurou no shopping para desenvolver um programa de controle da locação de carrinhos e ursos.
#A empresa decidiu organizar melhor, porque percebeu que o controle estava confuso. Este programa deve atender todas as necessidades do
#cliente que contratou o serviço: 
#Ao executar o programa, deverá ser solicitado o nome do funcionário que irá utilizar o sistema, outro detalhe, sempre que o funcionário 
#inicia seu dia de trabalho sua gaveta de dinheiro está sempre vazia, portanto o saldo em caixa na abertura do programa deve ser zero.
#O funcionário também deve informar o valor vendido no dia anterior. Depois que o funcionário se identificar no programa deverá aparecer
#na tela o menu de opções: 
#1 (0,75) - Iniciar brincadeira 
#2 (0,50) – Finalizar brincadeira
#3 (0,50) – Venda de produtos
#4 (0,75) Fechar o caixa 

#O funcionário poderá digitar uma dessas opções de menu (só o menu funcionando corretamente vale 0,50) a qualquer momento, portanto elas
#sempre devem estar disponíveis na tela, caso for digitado uma opção de menu inválida o programa deve avisar ao usuário com a seguinte 
#mensagem "Opção inválida!". Porém se o funcionário escolher uma opção válida o programa deverá funcionar da seguinte forma: 
#Opção 1 - Iniciar nova locação 
#A empresa possuí 3 Ursos, 3 Carros Elétricos e 3 Caminhões e 4x4.

#Como se trata de locação por tempo, o cliente escolhe o brinquedo desejado, paga e começa a brincadeira, o funcionário então realiza o 
#seguinte procedimento: registra qual o brinquedo que ele vai andar (1 - Urso, 2 – Carro elétrico, 3 – Caminhão ou 4x4). O tipo do 
#brinquedo determina o valor da locação, ou seja, se o brinquedo for um urso o valor da locação será de R$ 25,00, Carro Elétrico R$ 30,00 
#e Caminhão ou 4x4 R$ 35,00. Como a empresa tem somente 3 modelos de cada, você deverá controlar se o brinquedo está liberado ou não.

#Tipo de Brinquedo: 1 – Urso
#Valor da locação do brinquedo: R$ 25,00 
#Controle dos Ursos:
#0	             1	         2
#Brincando	Liberado	Brincando

#Neste exemplo o cliente vai brincar com o Urso número 1.
#Caso todos os ursos estiverem locados deve informar que antes de nova brincadeira o brinquedo deve ser liberado.

#Opção 2 – Finalizar brincadeira
#Ao retorno do cliente o funcionário deve informar o tipo de brinquedo e informar qual o código do brinquedo que será liberado.

#Opção 3 – Venda de produtos
#Nesta opção o funcionário simplesmente irá registrar uma entrada no caixa do valor do produto vendido.

#Opção 4 - Fechar o caixa 
#Ao final do dia de trabalho o funcionário irá usar esta opção, então o programa deverá apresentar um relatório para conferência do caixa:
    
#Fechamento de caixa 
#Total movimentado no dia é de: R$ ..... 
#Quantia recebida de locação dos Ursos: R$ ..... 
#Quantia recebida de locação dos Carros: R$ ..... 
#Quantia recebida de locação dos Caminhões e 4x4: R$ ..... 
#Quantia recebido em produtos vendidos: R$ .....
#Percentual de diferença da entrada atual e do dia anterior: %   
from logging import exception
import time
import locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.utf8')
saldoCaixa=0
urso=['liberado','liberado','liberado']
carroEletrico = ['liberado','liberado','liberado']
caminhao=['liberado','liberado','liberado']
opcao=1
somaUrso=0
somaCarro=0
somaCaminhao=0
venda=0
somaVenda=0

nomeFuncionario=input('Informe seu nome: ')
try:
    saldoDiaAnterior=float(input('Informe o valor vendido no dia anterior: '))
except Exception:        
        print('\033[1;30;41mPor favor, digite um número e não uma letra.Lembre de separar as casas decimais utilizando ponto(.)\033[m') 
        saldoDiaAnterior=float(input('Informe o valor vendido no dia anterior: '))       
           
while opcao <999999999 :
    print()
    print('MENU')
    print('1 - Iniciar brincadeira\n2 – Finalizar brincadeira\n3 – Venda de produtos\n4 - Fechar o caixa')
    
    try:
        opcao = int(input('Informe a opção desejada: '))
    except Exception:
        print()
        print('\033[1;30;41mPor favor, digite um número e não uma letra\033[m')
        continue
    print()    

    if opcao ==1:
        print()          
        print("1- Urso");
        print("2- Carro Eletrico");
        print("3- Caminhao 4x4\n");
        try:
            brinquedo=int(input("Informe o brinquedo escolhido: ")) 
        except Exception:
            print()
            print('\033[1;30;41mPor favor, digite um número e não uma letra\033[m')     
            continue  
        print()    

        if brinquedo == 1:
            somaUrso+=25
            print('Brinquedo Escolhido: Urso')
            print('Valor hora R$: 25,00')
            print()
            print(f"\033[1;30;47m{'CONTROLE':^20}\033[m")
            for i in range(3):                   
                if urso[i]=='liberado':                 
                   print(f"\033[0;32;40m{'Brinquedo':<10} {i} {'liberado':>5}\033[m")            
                else:                   
                    print(f"\033[7;30;41m{'Brinquedo':<10} {i} {'brincando':>5}\033[m")                   
                 
            print()                       
            if urso[0] =='brincando' and urso[1] == 'brincando' and urso[2]== 'brincando':
                print('\033[0;30;41mTodos os Ursos estão em uso, aguarde algum brinquedo ser liberado ou escolha outro brinquedo.\033[m')
                print('voltando ao menu inicial...aguarde...')
                time.sleep(3)
            try:    
                opcaoUrso=int(input('Informe qual opção de brinquedo você deseja: ')) 
            except Exception:
                print()
                print('\033[1;30;41mPor favor, digite um número e não uma letra\033[m')  
                continue   
            if urso[opcaoUrso] == 'brincando':
                print('\033[7;30;41mBRINQUEDO  ESTÁ SENDO UTILIZADO! POR FAVOR REPITA OPERAÇÃO.\033[m')
            else:
                urso[opcaoUrso]='brincando'                            
            print()   
                

        if brinquedo == 2:
            somaCarro+=30
            print('Brinquedo Escolhido: Carro elétrico')
            print('Valor hora R$: 30,00')
            print()
            print(f"\033[1;30;47m{'CONTROLE':^20}\033[m")
            for i in range(3):                    
                if carroEletrico[i]=='liberado':                 
                   print(f"\033[0;32;40m{'Brinquedo':<10} {i} {'liberado':>5}\033[m")            
                else:                   
                    print(f"\033[7;30;41m{'Brinquedo':<10} {i} {'brincando':>5}\033[m")                    
                 
            print()            
            if carroEletrico[0] =='brincando' and carroEletrico[1] == 'brincando' and carroEletrico[2]== 'brincando':
                     print('\033[0;30;41mTodos os carros elétricos estão em uso, aguarde algum brinquedo ser liberado ou escolha outro brinquedo.\033[m')
                     print('voltando ao menu inicial...aguarde...')
                     time.sleep(3)
            try:         
                opcaoCarroEletrico=int(input('Informe qual opção de brinquedo você deseja: '))
            except Exception:
                print()
                print('\033[1;30;41mPor favor, digite um número e não uma letra\033[m') 
                continue   
            if carroEletrico[opcaoCarroEletrico] == 'brincando':
                print('\033[7;30;41mBRINQUEDO  ESTÁ SENDO UTILIZADO! POR FAVOR REPITA OPERAÇÃO.\033[m')
            else:
                carroEletrico[opcaoCarroEletrico]='brincando'
            print()
        if brinquedo == 3:
            somaCaminhao+=35
            print('Brinquedo Escolhido: Caminhão 4x4')
            print('Valor hora R$: 35,00')
            print()
            print(f"\033[1;30;47m{'CONTROLE':^20}\033[m")  
                   
            print()
            for i in range(3):                
                if caminhao[i]=='liberado':                 
                    print(f"\033[0;32;40m{'Brinquedo':<10} {i} {'liberado':>5}\033[m")            
                else:                   
                    print(f"\033[7;30;41m{'Brinquedo':<10} {i} {'brincando':>5}\033[m")                    
                 
            print()            
            if caminhao[0] =='brincando' and caminhao[1] == 'brincando' and caminhao[2]== 'brincando':
                     print('\033[0;30;41mTodos os caminhões estão em uso, aguarde algum brinquedo ser liberado ou escolha outro brinquedo.\033[m') 
                     print('voltando ao menu inicial...aguarde...')         
                     time.sleep(3)
            try:         
                opcaoCaminhao=int(input('Informe qual opção de brinquedo você deseja: '))
            except Exception:
                print()
                print('\033[1;30;41mPor favor, digite um número e não uma letra\033[m')    
                continue
            if  caminhao[opcaoCaminhao] == 'brincando':
                print('\033[7;30;41mBRINQUEDO  ESTÁ SENDO UTILIZADO! POR FAVOR REPITA OPERAÇÃO.\033[m')
            else:
                caminhao[opcaoCaminhao]='brincando'  

    if opcao ==2:
        print()          
        print("1- Urso");
        print("2- Carro Eletrico");
        print("3- Caminhao 4x4\n");      
        try:  
            brinquedo=int(input("Informe o brinquedo a ser liberado: ")) 
        except Exception:
            print()
            print('\033[1;30;41mPor favor, digite um número e não uma letra\033[m')  
            continue  
        
        if brinquedo == 1:
            print(f"\033[1;30;47m{'CONTROLE':^20}\033[m")
            for i in range(3):                
                if urso[i]=='liberado':                 
                    print(f"\033[0;32;40m{'Brinquedo':<10} {i} {'liberado':>5}\033[m")            
                else:                   
                    print(f"\033[7;30;41m{'Brinquedo':<10} {i} {'brincando':>5}\033[m")                                    
                 
            print()
            try:
                opcaoUrso=int(input('Informe qual opção de brinquedo você deseja liberar: '))
            except Exception:
                print()
                print('\033[1;30;41mPor favor, digite um número e não uma letra\033[m')  
                continue  
            if urso[opcaoUrso] == 'liberado':
                print('\033[7;30;41mBRINQUEDO NÃO ESTÁ SENDO UTILIZADO! POR FAVOR REPITA OPERAÇÃO.\033[m')
            else:
                urso[opcaoUrso]='liberado'            
            print()
        if brinquedo == 2:
            print(f"\033[1;30;47m{'CONTROLE':^20}\033[m")
            for i in range(3):                
                if carroEletrico[i]=='liberado':                 
                    print(f"\033[0;32;40m{'Brinquedo':<10} {i} {'liberado':>5}\033[m")            
                else:                   
                    print(f"\033[7;30;41m{'Brinquedo':<10} {i} {'brincando':>5}\033[m")                      
                 
            print()
            try:
                opcaoCarroEletrico=int(input('Informe qual opção de brinquedo você deseja liberar: '))
            except Exception:
                print()
                print('\033[1;30;41mPor favor, digite um número e não uma letra\033[m')   
                continue 
            if carroEletrico[opcaoCarroEletrico] == 'liberado':
                print('\033[7;30;41mBRINQUEDO NÃO ESTÁ SENDO UTILIZADO! POR FAVOR REPITA OPERAÇÃO.\033[m')
            else:
                carroEletrico[opcaoCarroEletrico]='liberado'
            carroEletrico[opcaoCarroEletrico]='liberado'                      
            print()
        
        if brinquedo == 3:    
            print(f"\033[1;30;47m{'CONTROLE':^20}\033[m")        
            for i in range(3):  
                if caminhao[i]=='liberado':              
                 print(f"\033[0;32;40m{'Brinquedo':<10} {i} {'liberado':>5}\033[m")            
                else:                   
                    print(f"\033[7;30;41m{'Brinquedo':<10} {i} {'brincando':>5}\033[m")                     
                 
            print()
            try:
                opcaoCaminhao=int(input('Informe qual opção de brinquedo você deseja liberar: '))
            except Exception:
                print()
                print('\033[1;30;41mPor favor, digite um número e não uma letra\033[m') 
                continue   
            if caminhao[opcaoCaminhao] == 'liberado':
                print('\033[7;30;41mBRINQUEDO NÃO ESTÁ SENDO UTILIZADO! POR FAVOR REPITA OPERAÇÃO.\033[m')
            else:
                caminhao[opcaoCaminhao]='liberado'
            
    if opcao ==3:
        try:
            venda=float(input('Informe o valor da venda: '))
        except Exception:
            print()
            print('\033[1;30;41mUtilize ponto(.) para separar as casas decimais!\033[m')  
            continue  
        somaVenda+=venda

    if opcao ==4:
        totalDia=somaUrso+somaCarro+somaCaminhao+somaVenda
        totaDiaEmReais=locale.currency(totalDia)
        somaUrsoEmReais=locale.currency(somaUrso)
        somaCarroEmReais=locale.currency(somaCarro)
        somaCaminhaoEmReais=locale.currency(somaCaminhao)
        somaVendaEmReais=locale.currency(somaVenda)
        saldoDiaAnteriorEmReais=locale.currency(saldoDiaAnterior)
        print(f"\033[1;30;47m{'RELATÓRIO DE FECHAMENTO':^100}\033[m")
        print(f"{'Total movimentado no dia anterior':<50} {saldoDiaAnteriorEmReais:>40}")
        print(f"{'Total movimentado no dia atual':<50} {totaDiaEmReais:>40}")
        print(f"{'Valor recebido em locação dos ursos':<50} {somaUrsoEmReais:>40}")
        print(f"{'Valor recebido em locação dos carros elétricos':<50} {somaCarroEmReais:>40}")
        print(f"{'Valor recebido em locação dos Caminhões':<50} {somaCaminhaoEmReais:>40}")
        print(f"{'Valor recebido em produtos vendidos':<50} {somaVendaEmReais:>40}")
        if saldoDiaAnterior>=totalDia:
            Diferenca=((saldoDiaAnterior-totalDia)/saldoDiaAnterior)*-100;
        else:
            Diferenca=((totalDia-saldoDiaAnterior)/totalDia)*100;
        print(f"{'Diferença entre saldo atual e saldo do dia anterior em %:':<50} {Diferenca:>33.2f}")

    if opcao <=0 or opcao >=5:        
        print('\033[1;30;41mPor favor, digite um número válido conforme menu de opções\033[m')  
        continue  
    

    










                
        




