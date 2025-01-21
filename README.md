### **Resumo do Projeto:**

Este projeto é uma **API RESTful** desenvolvida utilizando **Django** e **Django REST Framework (DRF)**, com o foco em fornecer uma interface para gerenciar eventos e participantes. A API permite que **organizadores** criem, editem e visualizem eventos, enquanto **participantes** podem se inscrever nos eventos. A aplicação foi estruturada para funcionar de maneira escalável, com autenticação segura usando **JSON Web Tokens (JWT)**.

Além disso, o projeto foi configurado para ser executado dentro de **containers Docker**, o que facilita o processo de desenvolvimento, testes e deployment, garantindo um ambiente de execução isolado e consistente.

### **Funcionalidades Principais da API:**

1. **Gestão de Eventos**:
   - **Organizadores** podem criar, listar, editar e excluir eventos.
   - **Campos de Evento** incluem: nome, data de início e término, local, e descrição.
   - A API permite que os organizadores obtenham, modifiquem ou removam os eventos que criaram, com **filtragem e paginação** para facilitar a navegação.

2. **Gestão de Participantes**:
   - **Participantes** podem se inscrever nos eventos através da API.
   - Cada inscrição é associada a um evento, e os participantes fornecem informações como nome, email e data de inscrição.

3. **Autenticação de Usuário**:
   - Utilização do sistema de autenticação integrado do Django para criar **superusuários** e **usuários comuns**.
   - **JSON Web Tokens (JWT)** são utilizados para autenticação, permitindo sessões seguras e escaláveis sem a necessidade de armazenar informações no servidor.
   - A API está protegida por autenticação JWT, onde o usuário precisa fornecer um token válido para acessar os endpoints protegidos.

4. **Permissões e Autorização**:
   - **Permissões personalizadas** foram criadas para garantir que apenas o organizador de um evento tenha acesso para editar ou visualizar os eventos que criou.
   - **Superusuário** tem acesso completo para administrar a API e todos os seus recursos.

5. **Filtragem e Paginamento**:
   - A API permite **filtragem avançada** de eventos e participantes usando **DJ-RQL** (Django Relational Query Language), facilitando a busca de eventos por parâmetros como nome, data de início, e participantes.
   - **Paginamento** está configurado para limitar o número de itens por página, o que melhora a performance ao lidar com grandes volumes de dados.

### **Tecnologias Utilizadas:**

1. **Django**:
   - Framework web robusto para o desenvolvimento de aplicações, utilizado para criar a estrutura da API, gerenciar models, views, URLs e a administração.

2. **Django REST Framework (DRF)**:
   - Framework para construir APIs RESTful em Django. Ele fornece ferramentas para criar serializadores, viewsets e rotas de maneira rápida e fácil.
   - Utilizado para criar a API que manipula eventos, participantes e autenticação de usuários.

3. **PostgreSQL**:
   - Banco de dados relacional utilizado para armazenar informações dos eventos, participantes e usuários.
   - Conectado à aplicação via Django ORM (Object-Relational Mapping) para facilitar o gerenciamento de dados.

4. **JWT (JSON Web Token)**:
   - Utilizado para autenticação de usuários na API. O **`rest_framework_simplejwt`** é integrado para gerenciar tokens de acesso e refresh.
   - Isso permite que a API seja escalável e que a autenticação seja sem estado, onde o servidor não precisa manter informações sobre o usuário entre as requisições.

5. **DJ-RQL**:
   - **Django Relational Query Language**: Biblioteca para realizar filtragem avançada em consultas Django. A API pode filtrar eventos e participantes de maneira dinâmica e eficiente com base em parâmetros fornecidos na URL da requisição.

6. **Docker**:
   - O projeto foi configurado para rodar dentro de **containers Docker**, o que garante um ambiente de execução consistente e isolado, independentemente de onde a aplicação está sendo executada.
   - **Dockerfile**: Define a imagem Docker para a aplicação Django, com todos os pacotes e dependências necessários, além da configuração do servidor.
   - **Docker Compose**: Usado para orquestrar múltiplos containers (um para o Django e outro para o PostgreSQL), facilitando a execução da aplicação em ambientes de desenvolvimento, teste ou produção.

7. **Outras Ferramentas**:
   - **Comandos Customizados do Django**: Foi implementado um comando para criar automaticamente um **usuário admin** após as migrações do banco de dados, facilitando a configuração inicial do sistema.
   - **Permissões Customizadas**: Permissões específicas foram criadas para garantir que apenas o organizador de um evento tenha acesso a editar ou visualizar os eventos que criou, utilizando a classe `EventoOrganizadorPermission`.

### **Docker e Containers no Projeto**:

1. **Dockerfile**:
   - O **Dockerfile** define a imagem do Docker para a aplicação Django, especificando a instalação das dependências, a configuração do ambiente e o comando para rodar o servidor da aplicação.
   
2. **Docker Compose**:
   - O **Docker Compose** foi utilizado para gerenciar os múltiplos containers necessários para a aplicação:
     - **Container para o PostgreSQL**: Este container roda o banco de dados PostgreSQL, armazenando as informações dos eventos e participantes.
     - **Container para o Django**: O container que executa o servidor Django e expõe a API na porta configurada (8000).
   
3. **Vantagens do Uso de Docker**:
   - **Ambiente Consistente**: Com Docker, todos os desenvolvedores e ambientes de produção usam o mesmo ambiente de execução, eliminando problemas de "funciona na minha máquina".
   - **Facilidade de Setup e Deploy**: Novos desenvolvedores podem rodar o projeto localmente com um único comando, sem a necessidade de configurar manualmente o banco de dados ou outras dependências.
   - **Isolamento de Dependências**: O Docker garante que as dependências de cada serviço (Django, PostgreSQL) não entrem em conflito com outras partes do sistema operacional ou outras aplicações.
   - **Escalabilidade**: Docker facilita a escalabilidade da aplicação, permitindo adicionar mais containers conforme a necessidade, especialmente útil em ambientes de produção.

### **Conclusão:**

Este projeto é uma **API RESTful** construída com **Django** e **Django REST Framework**, permitindo que organizadores gerenciem eventos e que participantes se inscrevam nesses eventos. A autenticação é feita utilizando **JSON Web Tokens (JWT)**, garantindo uma solução segura e escalável.

O uso de **Docker** e **Docker Compose** permite que a aplicação rode de forma isolada e consistente em diferentes ambientes, tornando o desenvolvimento, testes e deployment mais simples e eficientes. O projeto oferece uma estrutura robusta e facilmente escalável para gerenciar eventos e inscrições de forma eficiente.
