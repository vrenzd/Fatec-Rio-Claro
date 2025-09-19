# Sistema de Gerenciamento do Vestibular FATEC

Sistema para gerenciamento do processo seletivo da FATEC, incluindo inscrições de vestibulandos, cadastro de aplicadores e gestão de aprovados.

## Funcionalidades

- Inscrição e gestão de vestibulandos
- Cadastro de aplicadores de provas
- Cálculo automático de salas necessárias
- Distribuição de candidatos por sala
- Relação candidatos/vaga por curso
- Gestão de alunos aprovados
- Geração de dados fictícios para testes

## Cursos Disponíveis

- Inteligência Artificial
- Gestão ESG

Cada curso possui 40 vagas disponíveis.

## Pré-requisitos

- Python 3.10 ou superior
- Biblioteca Faker (`pip install faker`)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/vestibular-fatec.git
```

2. Instale as dependências:
```bash
pip install faker
```

3. Execute o sistema:
```bash
python vestibular_fatec.py
```

## Menu Principal

1. Inscrever vestibulando
2. Editar dados do vestibulando
3. Cadastrar aplicador
4. Calcular salas necessárias
5. Listar candidatos por sala
6. Relação candidatos por vaga
7. Cadastrar aluno aprovado
8. Listar vestibulandos
9. Listar aplicadores
10. Listar aprovados
11. Gerar dados falsos (Faker)
0. Sair

## Estrutura do Projeto

- vestibular_fatec.py: Arquivo principal com a implementação do sistema
- Queue.py: Implementação da estrutura de dados Lista Ligada

## Regras de Negócio

- Máximo de 30 alunos por sala
- Inscrição só é válida após pagamento do boleto
- Aprovação só é possível para candidatos com inscrição efetivada
- Limite de 40 aprovados por curso


* **Victor Renzzo** - *Desenvolvedor* - [vrenzd](https://github.com/vrenzd)
