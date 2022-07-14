
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
    

    










                
        




