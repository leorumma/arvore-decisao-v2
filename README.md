# arvore-decisao-parte2
O objetivo desta tarefa é realizar um conjunto de experimentos usando o método de árvore de decisão e um dataset escolhido no site kaggle (https://www.kaggle.com/datasets). A base deve ter mais de 500 instâncias.


Deve ser entregue no classroom um relatório contendo as seguintes informações:

1- descrição do dataset selecionado: informe o número de instâncias do dataset, os atributos, assim como seus respectivos tipos e os valores que cada atributo pode assumir;

2- defina um experimento base: informe quais atributos do dataset serão considerados (você pode usar todos ou selecionar apenas alguns - neste caso justifique sua decisão); informe os parâmetros usados neste experimento (como o dataset será dividido em treinamento/teste; no caso de usar k-fold, qual o valor de k foi escolhido, qual função será usada para escolher o atributo durante a construção da árvore - gini ou entropia; como é feita a avaliação da árvore gerada que será, etc ).

3- explore alternativas para melhorar os resultados obtidos: faça isso mudando os parâmetros usados no experimento base e/ou fazendo podas na árvore resultante. Justifique a alteração e o que você esperava que acontecesse quando decidiu fazer a alteração do parâmetro e qual o resultado obtido. Compare seus resultados com o experimento base.

4- compare os resultados que você obteve na base que você escolheu com os obtidos por outros métodos e que estejam disponíveis no kaggle.

Os códigos usados nos seus experimentos também devem ser entregues.

#Instalar dependencias, jupyter notebook e todas as configurações necessarias para executar o projeto. 
Antes, sera necessario ter instalado o python3 e o pip(que vem dentro da instalação do python3)

Execute o comando dentro da pasta do projeto.

pip install -r requirements.txt


# Configuração Google colab para local runtime 

Setup instructions
In order to allow Colaboratory to connect to your locally running Jupyter server, you'll need to perform the following steps.

Step 1: Install Jupyter
Install Jupyter on your local machine.

Step 2: Install and enable the jupyter_http_over_ws jupyter extension (one-time)
The jupyter_http_over_ws extension is authored by the Colaboratory team and available on GitHub.

pip install jupyter_http_over_ws

jupyter serverextension enable --py jupyter_http_over_ws

Step 3: Start server and authenticate
New notebook servers are started normally, though you will need to set a flag to explicitly trust WebSocket connections from the Colaboratory frontend.

jupyter notebook --NotebookApp.allow_origin='https://colab.research.google.com' --port=8888 --NotebookApp.port_retries=0
    
Once the server has started, it will print a message with the initial backend URL used for authentication. Make a copy of this URL as you'll need to provide this in the next step.

Step 4: Connect to the local runtime
In Colaboratory, click the "Connect" button and select "Connect to local runtime...". Enter the URL from the previous step in the dialog that appears and click the "Connect" button. After this, you should now be connected to your local runtime.

# Utilize o github como repositorio e para controle de versão do notebook diretamente no front end do google colab
![Capturar](https://user-images.githubusercontent.com/21993550/178114681-d810653b-ca8f-4e9d-a80b-978f3c3e8689.PNG)

