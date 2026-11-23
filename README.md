# Organiza Festa

## Sobre o projeto

O **Organiza Festa** é um sistema desenvolvido em **Python** para auxiliar no planejamento e organização de eventos.

O sistema foi desenvolvido para facilitar o controle de informações importantes de uma festa ou evento, como:

- Dados do evento;
- Convidados;
- Orçamento disponível;
- Tarefas e seus respectivos custos;
- Data e localização;
- Controle dos gastos;
- Sugestões personalizadas de acordo com o evento.

O projeto possui funcionamento por **terminal (CLI)** e utiliza arquivos `.csv` para manter os dados salvos.

---

## Objetivo

O objetivo do sistema é facilitar a organização de eventos, permitindo que o usuário cadastre e gerencie as principais informações necessárias para o planejamento de uma festa.

O sistema busca evitar problemas relacionados ao controle de tarefas, orçamento e informações do evento.

---

## Funcionalidades

### Gerenciamento de eventos

O sistema permite:

- Cadastrar eventos;
- Visualizar eventos cadastrados;
- Editar informações de eventos;
- Excluir eventos.

As informações de um evento incluem:

- ID;
- Nome;
- Tipo de evento;
- Data;
- Local;
- Orçamento disponível;
- Quantidade de convidados.

### Tarefas e orçamento

O usuário pode cadastrar tarefas relacionadas a um evento, como:

- Decoração;
- Buffet;
- Música;
- Fotografia;
- Entre outras.

Cada tarefa possui um custo, permitindo acompanhar os gastos do evento e calcular o orçamento restante.

### Contagem regressiva

Ao consultar um evento, o sistema pode informar quantos dias faltam para a realização do evento.

### Armazenamento de dados

Os dados são armazenados em arquivos `.csv`, permitindo que as informações continuem disponíveis mesmo após o encerramento do programa.

Os principais arquivos utilizados são:

- `eventos.csv`
- `tarefas.csv`

### Sugestões personalizadas

O sistema pode apresentar sugestões de acordo com informações do evento, como:

- Tipo de evento;
- Quantidade de convidados.

### Funcionalidade Extra 

Lista de convidados com confirmação de presença: cadastrar nome e se confirmou. Combina com o enunciado, que cita controle de convidados e usa o nº de convidados nas sugestões.

---

## Estrutura do projeto

```text
Organiza_Festa/
│
├── main.py
│
├── src/
│   ├── eventos.py
│   ├── tarefas.py
│   ├── arquivos.py
│   ├── sugestoes.py
│   └── utils.py
│
├── dados/
│   ├── eventos.csv
│   └── tarefas.csv
│
└── README.md
```

### `main.py`

Responsável pelo funcionamento principal do sistema, incluindo o menu e a interação com o usuário.

### `src/eventos.py`

Contém as funções relacionadas ao gerenciamento dos eventos, como cadastro, consulta, edição e exclusão.

### `src/tarefas.py`

Responsável pelo gerenciamento das tarefas e dos custos associados aos eventos.

### `src/arquivos.py`

Responsável pela persistência dos dados, realizando a gravação e leitura das informações nos arquivos `.csv`.

### `src/sugestoes.py`

Responsável pelas sugestões personalizadas de acordo com as características do evento.

### `src/convidados.py`

Responsável pela incrementação da funcionalidade extra de convidados, onde monta um menu para cadastrar, remover, listar, alterar o status de presença e ver o resumo de custo por convidado.

### `dados/`

Armazena os arquivos `.csv` utilizados pelo sistema para manter os registros.

---

## Tecnologias utilizadas

- **Python**
- **Arquivos CSV**
- **Git e GitHub**
- Execução pelo **terminal**

O projeto utiliza recursos nativos do Python e segue as restrições estabelecidas para o desenvolvimento da atividade.

---

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/chico-acioli/projeto-FP
```

### 2. Entre na pasta do projeto

```bash
cd projeto-FP
```

### 3. Execute o programa

```bash
python main.py
```

O sistema será iniciado no terminal.

---

## Como utilizar

Após iniciar o programa, o usuário deverá utilizar o menu apresentado no terminal para escolher a operação desejada.

De acordo com as opções disponíveis, será possível:

1. Cadastrar um evento;
2. Consultar eventos;
3. Editar eventos;
4. Excluir eventos;
5. Cadastrar tarefas;
6. Consultar tarefas;
7. Gerenciar os custos do evento;
8. Consultar informações e sugestões.

Os dados cadastrados são armazenados nos arquivos da pasta `dados`.

---

## Formato dos dados

### `eventos.csv`

Os eventos são armazenados utilizando campos separados por `;`.

Exemplo:

```text
id;nome;tipo;data;local;orcamento;convidados
1;Aniversario;Aniversario;20/12/2026;Salao;5000;50
```

### `tarefas.csv`

As tarefas são armazenadas utilizando:

```text
id;id_evento;nome;custo
1;1;Buffet;1500
2;1;Decoracao;800
```

O campo `id_evento` permite relacionar uma tarefa ao evento correspondente.

---

## Desenvolvimento em equipe

O projeto foi desenvolvido em equipe utilizando **GitHub** para controle de versão e organização do código.

Cada integrante contribui para diferentes partes do sistema, mantendo os módulos separados para facilitar o desenvolvimento, a integração e a manutenção do projeto.

---

## Observações

- O sistema funciona através do terminal.
- Os dados devem ser mantidos nos arquivos da pasta `dados`.
- Os arquivos `.csv` são utilizados para garantir a persistência das informações.
- O projeto foi desenvolvido seguindo as especificações propostas para a atividade.

---

## Projeto acadêmico

Projeto desenvolvido para fins acadêmicos como parte da disciplina de programação.

**Projeto:** Organiza Festa – Sistema de Planejamento de Eventos  
**Linguagem:** Python  
**Armazenamento:** CSV  
**Interface:** Terminal (CLI)