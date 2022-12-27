# WMGW
 
WMGW é um projeto baseado na web que tem como objetivo ser uma biblioteca de filmes,
que apesar de não ser possível assistir filmes no próprio site, o usuário pode descobrir
facilmente qual o próximo filme que irá assistir, pois os filmes são divididos em várias
categorias, facilitando assim a escolha do usuário. Também é possível adicionar filmes à 
lista privada de filmes do usuário.

# Descrição

O projeto foi feito utilizando a linguagem python em conjunto com o framework flask, a 
mesma ensinada no cs50, no entanto, decidi usar em conjunto uma funcionalidade da
própria framework que são os blueprints, como explicado na documentação do flask, serve
para particionar o projeto em diferentes pastas, além das pastas templates e static. Usando 
Essa funcionalidade foi mais simples a organização do código, que ficou com a seguinte 
Organização das pastas: Auth, Main, User, templates e static.

Na pasta Auth se encontram os arquivos relacionados à autenticação do usuário(que a propósito
Nao é obrigatório para acesso ao site), Na pasta User estão os arquivos referentes ao usuário 
que não incluem autenticação. E na pasta Main estão os arquivos referentes a todo o restante 
Do site. Todas as três pastas possuem suas próprias pastas templates e static se necessário.
