# FIAP MBA - CI/CD - Trabalho Final

## TOC (Tabela de Conteúdo)

- [FIAP MBA - CI/CD - Trabalho Final](#fiap-mba---cicd---trabalho-final)
  - [TOC (Tabela de Conteúdo)](#toc-tabela-de-conteúdo)
  - [Integrantes](#integrantes)
  - [Sobre o Projeto](#sobre-o-projeto)
  - [Como funciona o CI/CD](#como-funciona-o-cicd)

## Integrantes

- Lucas Marcolongo (@marcolongol) -- RM 351798
- Guilherme Bitencourt -- RM 350695
- Guilherme Lage -- RM 350842
- Joao Paulo -- RM 352488

## Sobre o Projeto

O projeto esta estruturado em um monorepositório, onde temos 3 projetos:

- `webapp`: Applicacao web em [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- `infra`: Infraestrutura como código utilizando [aws-cdk](https://aws.amazon.com/pt/cdk/)
- `docs`: Documentação do projeto e diagramas em formato de codigo utilizando [diagrams](https://diagrams.mingrammer.com/)

As pastas do projeto estão organizadas da seguinte forma:

```plaintext
.
├── .github
│   ├── renovate.json5                     # Configuração do renovate
│   └── workflows                          # Workflows do Github Actions
│       └── deploy.yml                     # Workflow de deploy
│       └── renovate.yml                   # Workflow de atualização de dependências
├── apps                                   # Projetos do monorepositório (NX)
│   ├── infra                              # Infraestrutura como código
│   ├── webapp                             # Aplicação web
│   └── docs                               # Diagramas e documentação
├── .editorconfig                          # Configuração do editor
├── .gitignore                             # Arquivos ignorados pelo git
├── .prettierrc                            # Configuração do Prettier
├── .python-version                        # Versão do Python
├── buildspec.yaml                         # Configuração do CodeBuild
├── nx.json                                # Configuração do NX
├── package-lock.json                      # Lockfile do NPM
├── package.json                           # Configuração do NPM
├── poetry.lock                            # Lockfile do Poetry
├── poetry.toml                            # Configuração do Poetry
├── pyproject.toml                         # Configuração do Poetry
├── README.md                              # Documentação do projeto
└── task-definition.json                   # Definição de tarefa do ECS

```

Este projeto foi desenvolvido utilizando as seguintes tecnologias:

- [NX](https://nx.dev/)
  NX é uma ferramenta de código aberto que permite compartilhar código entre diferentes projetos, gerenciar dependências e automatizar tarefas de desenvolvimento.

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
  Flask se trata de um framework web minimalista para Python. Ele e projetado para facilitar a construção de aplicativos web rapidamente

- [AWS CDK](https://aws.amazon.com/pt/cdk/)
  AWS CDK é um framework desenvolvimento de software que facilita a definição de aplicativos de infraestrutura em código e provisionamento de recursos na AWS.

- [Diagrams](https://diagrams.mingrammer.com/)
  Diagrams é uma ferramenta que permite a criação de diagramas de infraestrutura como código.

- [Renovate](https://www.whitesourcesoftware.com/free-developer-tools/renovate/)
  Renovate é uma ferramenta que automatiza a atualização de dependências de projetos.

- [Github Actions](https://github.com/features/actions)
  Github Actions é uma ferramenta de automação de fluxos de trabalho.

- [CodeBuild](https://aws.amazon.com/pt/codebuild/)
  CodeBuild é um serviço de compilação totalmente gerenciado que compila código, executa testes e produz artefatos prontos para implantação.

- [ECS](https://aws.amazon.com/pt/ecs/)
  Amazon Elastic Container Service (Amazon ECS) é um serviço de gerenciamento de contêiner altamente escalável e de alta performance que suporta contêineres Docker.

## Como funciona o CI/CD

Este repositorio esta configurado de forma que qualquer alteração no branch `main` irá disparar um pipeline de CI/CD que irá realizar o deploy da aplicação no ECS.

O pipeline de CI/CD é composto por 2 etapas:

- CodeDeploy: Realiza o teste unitário e build da aplicação e reporta o status do commit no Github.
  O arquivo de configuração do CodeDeploy é o [buildspec.yaml](./buildspec.yaml).
  Este arquivo é responsável por realizar o build da aplicação e executar os testes unitários.

- Github Actions: Assim que o CodeDeploy é finalizado com sucesso, o Github Actions é disparado e realiza o deploy da infraestrutura e da aplicação na AWS.
  Os arquivos de configuração do Github Actions estão localizados na pasta [.github/workflows](./.github/workflows).
