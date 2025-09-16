README.md
<p align="center"><img src="https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg" width="200" alt="Logotipo do Laravel"></p>

<h1 align="center">CIATRON Estoque</h1>

<p align="center"> <a href="https://github.com/laravel/framework/actions"><img src="https://github.com/laravel/framework/workflows/tests/badge.svg" alt="Status da construção"></a> <a href="https://packagist.org/pacotes/laravel/framework"><img src="https://img.shields.io/packagist/dt/laravel/framework" alt="Total de downloads"></a> <a href="https://packagist.org/pacotes/laravel/framework"><img src="https://img.shields.io/packagist/v/laravel/framework" alt="Última versão estável"></a> <a href="https://packagist.org/pacotes/laravel/framework"><img src="https://img.shields.io/packagist/l/laravel/framework" alt="Licença"></a> </p>

Visão Geral do Projeto

Este é um sistema de controle de estoque completo, projetado para gerenciar produtos de forma eficiente. O projeto é dividido em duas partes: um backend robusto em API, construído sobre o framework Laravel, e um frontend com uma aplicação desktop nativa em Python.

Este projeto está em constante evolução, com planos para absorver a gestão de vendas e, futuramente, se integrar com a SEFAZ para emissão de notas fiscais.

Tecnologias Utilizadas
Backend (API)
Laravel: Framework PHP para o desenvolvimento da API.

MySQL: Banco de dados relacional para armazenamento de dados.

XAMPP: Ambiente de desenvolvimento local (Apache e MySQL).

Frontend (Aplicação Desktop)
Python: Linguagem de programação para a interface de usuário.

Tkinter: Biblioteca padrão do Python para criação de interfaces gráficas.

Solicitações: Biblioteca Python para comunicação com a API (solicitações HTTP).

PyInstaller: Ferramenta usada para empacotar a aplicação Python em um arquivo executável (.exe).

Inno Setup: Ferramenta futura para criar um instalador único do projeto, garantindo uma distribuição profissional.

Pillow: Biblioteca Python essencial para o PyInstaller, usada para processar e integrar o ícone personalizado (.ico) na aplicação.

Funcionalidades (CRUD)
O sistema permite que o usuário realize as seguintes operações:

Create (Criar): Adicionar novos produtos ao estoque.

Read (Ler): Visualizar todos os produtos do estoque.

Update (Atualizar): Modificar as informações de um produto existente.

Delete (Excluir): Remover produtos do estoque.

Como Usar
1. Configurar o Backend (Servidor)
Certifique-se de que o XAMPP está instalado e que os módulos Apache e MySQL estão em execução.

Importe a base de dados para o MySQL.

Inicie a API do Laravel. O endereço do servidor deve ser fixado em http://192.168.0.100:8000.

2. Usar a Aplicação Frontend (Cliente)
A aplicação é executada a partir de um único arquivo CIATRON Estoque.exe.

Um atalho de execução é criado com o ícone app_icon.ico para facilitar o acesso do usuário.

A máquina cliente deve estar na mesma rede local que o servidor.

No futuro, um instalador será fornecido para automatizar a instalação em novas máquinas.

Planos Futuros
Gestão de Vendas: O projeto será expandido para incluir um módulo de vendas, que irá absorver os dados do estoque.

Integração com a SEFAZ: Planeja-se a integração com a SEFAZ para emissão de notas fiscais eletrônicas, tornando o sistema compatível com as exigências fiscais.

Como Contribuir
O projeto está aberto a novos desenvolvedores que queiram participar e contribuir com a sua evolução. Se você tem interesse em fazer parte deste time, sinta-se à vontade para entrar em contato. Suas ideias e contribuições são muito bem-vindas!

Contato
Desenvolvedor: Leandro Machado

Licença
O framework Laravel é um software de código aberto licenciado sob alicença MIT.
