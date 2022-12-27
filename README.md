# WMGW
 
WMGW é um projeto baseado na web que tem como objetivo ser uma biblioteca de filmes,
que apesar de não ser possível assistir filmes no próprio site, o usuário pode descobrir
facilmente qual o próximo filme que irá assistir, pois os filmes são divididos em várias
categorias, facilitando assim a escolha do usuário. Também é possível adicionar filmes à 
lista privada de filmes do usuário.

# Descrição

O projeto foi feito utilizando a linguagem python em conjunto com o framework flask, a 
mesma ensinada no cs50, junto com html, css e javascript.
Também foi feito uso de bootstrap para algumas estilizações do site, porém também escrevi
várias propriedades css do zero para o site.
Decidi usar uma funcionalidade da própria framework que são os blueprints, que como é explicado
na documentação do flask, serve para particionar o projeto em diferentes pastas, além das pastas
templates e static, para facilitar na organização do projeto. Usando essa funcionalidade a organização
e desenvolvimento do projeto foi facilitada, que ficou com a seguinte organização das pastas:
Auth, Main, User, templates e static.

Na pasta Auth se encontram os arquivos relacionados à autenticação do usuário(que a propósito
Nao é obrigatório para acesso ao site), Na pasta User estão os arquivos referentes ao usuário 
que não incluem autenticação. E na pasta Main estão os arquivos referentes a todo o restante 
Do site. Todas as três pastas possuem suas próprias pastas templates e static se necessário.

Função de cada arquivo do projeto

Arquivo app.py
Arquivo responsável por interligar todos os blueprints do projeto, e também é o responsável por iniciar
a aplicação. Todos os arquivos que retornam uma pagina para o usuário passam pelo app.py, e quando necessário
ele manda uma requisição de um blueprint para outro. Sua outra função é armazenar dados no navegador do
usuário, como por exemplo manter ele logado apos fechar e abrir o site.

templates/base.html
html base para todos os outros arquivos html do projeto, aqui são feitas as importações de scripts locais ou 
externos, como o bootstrap por exemplo, aqui é escrito a base da aparencia do projeto como a navbar e a área 
á ser alterada pelos demais arquivos html do projeto através de jinja templates.

static/style.css
Arquivo css com todas as propriedades definidas localmente do site, todos os blueprints do projeto utilizam
este arquivo css para estilizar as paginas, 


