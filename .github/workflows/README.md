# Github Actions Workflows

## TOC (Tabela de Conteúdo)

- [Github Actions Workflows](#github-actions-workflows)
  - [TOC (Tabela de Conteúdo)](#toc-tabela-de-conteúdo)
  - [Workflows](#workflows)
    - [Renovate](#renovate)
    - [Deploy](#deploy)

## Workflows

### Renovate

O workflow `renovate` é responsável por atualizar as dependências do projeto. Ele é executado diariamente e verifica se há atualizações disponíveis para as dependências do projeto.

[Renovate](https://docs.renovatebot.com/) é uma ferramenta que automatiza a atualização de dependências em projetos. Ele verifica diariamente se há atualizações disponíveis para as dependências do projeto e cria pull requests automaticamente para atualizar as dependências.

### Deploy

O workflow `deploy` é responsável por realizar o deploy da aplicação. Ele é executado sempre que um push é realizado na branch `main`.

O workflow de deploy é composto pelas seguintes etapas:

1. **Check commit status**: Verifica o status do commit reportado pelo CodeBuild e aguarda até que o status seja `SUCCESS`.

2. **Checkout code**: Realiza o checkout do código da branch `main`.

3. **Configure AWS credentials**: Configura as credenciais da AWS para realizar o deploy da aplicação.

4. **Login to Amazon ECR**: Realiza o login no Amazon ECR para autenticar o Docker.

5. **Setup Node.js**: Configura o ambiente Node.js.

6. **Install poetry**: Instala o poetry.

7. **Install dependencies**: Instala as dependências do projeto.

8. **Deploy CDK**: Realiza o deployment da infraestrutura utilizando o AWS CDK.

9. **Build and push Docker image**: Realiza o build e push da imagem Docker para o Amazon ECR.

10. **Retrieve Image URI**: Recupera a URI da imagem Docker gerada.

11. **Fill in the new image ID in the Amazon ECS task definition**: Preenche o ID da nova imagem no template do arquivo de definição de tarefa do Amazon ECS.

12. **Deploy Amazon ECS task definition**: Realiza o deploy da nova definição de tarefa do Amazon ECS.
