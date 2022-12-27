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

OBS: Em alguns arquivos html é referenciado a pasta /static/posters, essa pasta não está no github
pois nela estão os quase 65000 posters do site, por isso optei por não fazer o upload dessa pasta.

Decidi não usar uma API para esse projeto, pois ele não tem o objetivo de ser publicado, e sim ser uma
possibilidade de aprendizado pondo a mão na massa em um projeto relativamente grande, e criar o banco 
de dados e alimentá-lo do zero é algo bem mais desafiador do que usar uma API.

Sobre o banco de dados do projeto
O banco de dados desse projeto, com o nome database.db que é referenciado em alguns arquivos do projeto,
trata-se de um banco de dados sqlite3 e não está no github devido ao seu tamanho. Ele foi criado e
alimentado do zero, utilizando os dados do dataset do imdb. Ao rodar .schema no banco o resultado é o 
seguinte:
"CREATE TABLE people(id TEXT PRIMARY KEY, name TEXT NOT NULL, professions TEXT, knownForTitles TEXT);
CREATE TABLE movies(id TEXT PRIMARY KEY, title TEXT NOT NULL, year INTEGER, genres TEXT);
CREATE TABLE ratings(id INTEGER NOT NULL, averageRating REAL, numVotes INTEGER, FOREIGN KEY(id) REFERENCES movies(id));
CREATE TABLE producers(id TEXT NOT NULL, directors TEXT, writers TEXT);
CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT NOT NULL, hash TEXT NOT NULL);
CREATE TABLE users_lists(id INTEGER PRIMARY KEY, list TEXT);"


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
este arquivo css para estilizar as paginas, todo o espaçamento, efeitos hover e tamanhos das divs são 
definidos aqui.

static/Logo.png, Logo2.png, fire.jpg, poster_not_found.jpg
Imagens usadas no projeto, Logo.png é a logo principal do projeto, Logo2.png é a mini-logo que aparece na aba do 
navegador, fire.jpg é o plano de fundo do site, e poster_not_found.jpg é a imagem usada quando o filme não 
possui poster.

static/swiper.js, swiperAuto.js, usrModal.js
Arquivos javascript para fazer os carroseis do site funcionarem, tanto o carrossel de oscars quanto os de 
cada categoria
na pagina principal.

static/imgs/
Pasta que contem as imagems que são mostradas no carrosel de oscars, em que cada imagem tem o nome do id 
do filme a que ela se refere.

O restante das pastas segue o seguinte padrão:
Pasta_blueprint/__init__.py ,Pasta_blueprint/templates/, Pasta_blueprint/[nome da blueprint]_utils.py

__init__.py de cada pasta
Arquivo principal de cada blueprint, onde a blueprint é definida, e onde as funções que retornam uma pagina 
para o usuário são definidas. Para as funções presentes aqui funcionarem é necessário importar as funções 
presentes em [nome da blueprint]_utils.py.

[nome da blueprint]_utils.py em cada pasta
Arquivo onde as funções que realizam ou não alguma ação no banco de dados são definidas, todas as funções 
presentes nesse arquivo não são executadas diretamente, e sim chamadas por __init__.py.

/templates/ de cada pasta
Pasta onde ficam os arquivos .html de cada blueprint, onde alguns possuem um html chamado base_[nome da blueprint].html, 
que funciona como o base.html do projeto, porém apenas para essa pagina, e ela também estende o que há em base.html.

*Auth/login_required.py
Arquivo que possue a função para verificar se o usuário está logado, e caso não redirecionar para a pagina de login.
Essa função é importada sempre que em algum ponto do projeto seja necessário o usuário estar logado.



