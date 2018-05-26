# Scrapy Profile Crawler

Este crawler é capaz de obter a lista de amigos de um perfil público no Facebook
utilizando o modulo Scrapy do Python. Com ele é possível definir via linha de
comando as informações necessárias para fazer a raspagem e compatível com MongoDB.

## Justificativas
O módulo escolhido foi o Scrapy por ser uma ferramenta pensada para agir em escala.
Com pouco trabalho é possível fazer deploy para o scrapinghub.com que possui uma API
full capaz de controlar nos detalhes a execução do Crawler. Além disso o Scrapy possui
uma ótima organização para controlar as requisições (configuração de proxys, ações de acordo dom status), controlar o pipeline do item raspado e exportar as informações.

Por ser um módulo incapaz de renderizar JS, optei por usar a versão básica do Facebook
encontrada em (m.facebook.com), mas é possível extender para o uso de JS com o Splash,
um serviço de renderização de JS feito em Lua pelo pessoal quem mantém o Scrapy.

Além disso, é possível controlar as ações dos crawlers em cluster, com o projeto
Scrapy Cluster (https://github.com/istresearch/scrapy-cluster).

## Começando

Essas instruções farão com que você tenha uma cópia do projeto em execução na sua máquina local.
