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

Dado que este lab está a ser produzido num docker container sem a presença de uma máquina virtual seed usar o browser para identificar quais variáveis de ambiente são definidas por este não pode ser realizado, a equipa apenas vai demonstrar neste relatório a tarefa envolvendo o uso do comando **curl**.

### Task 2.A: Using Curl

Tendo como objetivo de definir a informação relativa a variáveis do ambiente para valores arbitrários, o comando **curl** permite aos users manipular campos num pedido HTTP utilizando certas opções.


Se a opção ```-v``` estiver especificada então é imprimido o cabeçalho do pedido HTTP:

![-v option on curl](https://github.com/Fernando-A-Rocha/FEUP-SSI/blob/main/1-Shellshock/Screenshots/2_A_curl_v_option.png?raw=true)


















