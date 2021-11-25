# Python-InfoSec

Linguagem Simplista - Fácil Desesnvolvimento

Menos Linhas de Código

Linguagem OO

APi's e Bibliotecas Prontas para Redes, Web, Etc

Multiplataforma

A área tem como objetivo assegurar que todos os dados de uma ou mais 
informações estejam sempre confidenciais, íntegros e disponíveis em 
qualquer meio de comunicação.

-Pilares - Princípios

*Integridade
Proteger a informação contra alterações indevidas.

*Confidencialidade
Visa manter uma informação confidencial.

*Disponibilidade
Garantir a disponibilidade dos recursos, informações sempre disponíveis. 

'Identificação
Identificar uma entidade.

'Autenticação
Verificar a entidade e suas credenciais.

'Autorização
Autorizar a entidade dentro de um sistema.

'Não Repúdio
Evitar que uma entidade negue suas ações em um sistema.

Métodos de Scan
Um Scanner de portas pode usar diversos métodos para varrer
a rede, desde o mais simples até métodos evasivos que são aqueles
que fazem menos "barulho" no alvo.

TCP Scan - Varredura mais utilizada em todos Port Scanners, equivale
a uma requisição(Handshake) para cada porta definida, este tipo de 
varredura é considerada "barulhenta", ou seja, é de fácil detecção.

UDP Scan - Este tipo de varredura descobre serviços UDP rodando na
rede, ou seja, as portas UDP abertas.
Portas UDP abertas podem detectar que há serviços VoIP, Streaming
de Vídeo e outros rodando em uma rede.

SYN Scan - Este tipo de varredura é considerada Stealth("furtiva"),
pois é menos barulhenta devido ao tipo de requisição TC`que ela faz,
sem completar a conexão com o alvo.