# LojaDeBrinquedos
Trabalho Final para Conclusão de disciplina de Algoritmos

Você foi contratado pela nova empresa que inaugurou no shopping para desenvolver um programa de controle da locação de carrinhos e ursos.
A empresa decidiu organizar melhor, porque percebeu que o controle estava confuso. Este programa deve atender todas as necessidades do
cliente que contratou o serviço: 
Ao executar o programa, deverá ser solicitado o nome do funcionário que irá utilizar o sistema, outro detalhe, sempre que o funcionário 
inicia seu dia de trabalho sua gaveta de dinheiro está sempre vazia, portanto o saldo em caixa na abertura do programa deve ser zero.
O funcionário também deve informar o valor vendido no dia anterior. Depois que o funcionário se identificar no programa deverá aparecer
na tela o menu de opções: 
1 (0,75) - Iniciar brincadeira 
2 (0,50) – Finalizar brincadeira
3 (0,50) – Venda de produtos
4 (0,75) Fechar o caixa 

O funcionário poderá digitar uma dessas opções de menu (só o menu funcionando corretamente vale 0,50) a qualquer momento, portanto elas
sempre devem estar disponíveis na tela, caso for digitado uma opção de menu inválida o programa deve avisar ao usuário com a seguinte 
mensagem "Opção inválida!". Porém se o funcionário escolher uma opção válida o programa deverá funcionar da seguinte forma: 
Opção 1 - Iniciar nova locação 
A empresa possuí 3 Ursos, 3 Carros Elétricos e 3 Caminhões e 4x4.

Como se trata de locação por tempo, o cliente escolhe o brinquedo desejado, paga e começa a brincadeira, o funcionário então realiza o 
seguinte procedimento: registra qual o brinquedo que ele vai andar (1 - Urso, 2 – Carro elétrico, 3 – Caminhão ou 4x4). O tipo do 
brinquedo determina o valor da locação, ou seja, se o brinquedo for um urso o valor da locação será de R$ 25,00, Carro Elétrico R$ 30,00 
e Caminhão ou 4x4 R$ 35,00. Como a empresa tem somente 3 modelos de cada, você deverá controlar se o brinquedo está liberado ou não.

Tipo de Brinquedo: 1 – Urso
Valor da locação do brinquedo: R$ 25,00 
Controle dos Ursos:
0	             1	         2
Brincando	Liberado	Brincando

Neste exemplo o cliente vai brincar com o Urso número 1.
Caso todos os ursos estiverem locados deve informar que antes de nova brincadeira o brinquedo deve ser liberado.

Opção 2 – Finalizar brincadeira
Ao retorno do cliente o funcionário deve informar o tipo de brinquedo e informar qual o código do brinquedo que será liberado.

Opção 3 – Venda de produtos
Nesta opção o funcionário simplesmente irá registrar uma entrada no caixa do valor do produto vendido.

Opção 4 - Fechar o caixa 
Ao final do dia de trabalho o funcionário irá usar esta opção, então o programa deverá apresentar um relatório para conferência do caixa:
    
Fechamento de caixa 
Total movimentado no dia é de: R$ ..... 
Quantia recebida de locação dos Ursos: R$ ..... 
Quantia recebida de locação dos Carros: R$ ..... 
Quantia recebida de locação dos Caminhões e 4x4: R$ ..... 
Quantia recebido em produtos vendidos: R$ .....
Percentual de diferença da entrada atual e do dia anterior: %  
