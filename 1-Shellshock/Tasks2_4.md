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

Como observar, existe uma série de variáveis de ambiente, que são valores que um servidor web envia neste caso para o program CGI, que espelham informação sobre o servidor e não são modificadas e outras que dão informação sobre os utilizadores e podem ser modificados como vimos. Ao usar o comando curl com as opções ```-A``` ```-e``` ```-H``` o atacante pode então injetar o seu próprio conteúdo para as variáveis de ambiente de uma programa CGI alvo.

## Task 4: Getting a Reverse Shell via Shellshock Attack




























