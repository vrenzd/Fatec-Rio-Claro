from Queue import ListaLigada
from faker import Faker
import random

# 1) Estrutura pra armazenar dados dos vestibulandos
class Vestibulando:
    numero_sequencial = 0
    
    def __init__(self, nome, cpf, opcao_curso, inscricao_efetivada=False):
        Vestibulando.numero_sequencial += 1
        self.numero_inscricao = Vestibulando.numero_sequencial
        self.nome = nome
        self.cpf = cpf
        self.opcao_curso = opcao_curso  # 'Inteligência Artificial' ou 'Gestão ESG'
        self.inscricao_efetivada = inscricao_efetivada  # True se boleto pago
    
    def __str__(self):
        status = 'Efetivada' if self.inscricao_efetivada else 'Não efetivada'
        return f'Inscrição: {self.numero_inscricao} | Nome: {self.nome} | CPF: {self.cpf} | Curso: {self.opcao_curso} | Status: {status}'


# 2) estrutura pra cadastrar aplicadores das provas
class Aplicador:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
    
    def __str__(self):
        return f'Nome: {self.nome} | Cargo: {self.cargo}'


# 3) estrutura pra alunos aprovados
class AlunoAprovado:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    def __str__(self):
        return f'Nome: {self.nome} | CPF: {self.cpf}'


class SistemaVestibular:
    def __init__(self):
        self.vestibulandos = ListaLigada()
        self.aplicadores = ListaLigada()
        self.aprovados_ia = ListaLigada()
        self.aprovados_esg = ListaLigada()
        self.VAGAS_POR_CURSO = 40 # Definindo o número de vagas como uma constante
        self.fake = Faker('pt_BR') # Inicializa o Faker para português do Brasil

    
    # 1) inscrever vestibulando
    def inscrever_vestibulando(self, nome, cpf, opcao_curso, boleto_pago=False):
        if opcao_curso not in ['Inteligência Artificial', 'Gestão ESG']:
            print('Opção de curso inválida! Use "Inteligência Artificial" ou "Gestão ESG"')
            return False
        
        vestibulando = Vestibulando(nome, cpf, opcao_curso, boleto_pago)
        self.vestibulandos.adicionar(vestibulando)
        print(f'Vestibulando inscrito com sucesso! Número de inscrição: {vestibulando.numero_inscricao}')
        return True
    
    # 2) editar dados do vestibulando
    def editar_vestibulando(self, numero_inscricao):
        vestibulando = None
        for v in self.vestibulandos:
            if v.numero_inscricao == numero_inscricao:
                vestibulando = v
                break

        if not vestibulando:
            print('Número de inscrição não encontrado!')
            return False
        
        print(f'Dados atuais: {vestibulando}')
        
        novo_nome = input('Novo nome (Enter para manter atual): ').strip()
        if novo_nome:
            vestibulando.nome = novo_nome
        
        novo_cpf = input('Novo CPF (Enter para manter atual): ').strip()
        if novo_cpf:
            vestibulando.cpf = novo_cpf
        
        print('Opções de curso: 1 - Inteligência Artificial, 2 - Gestão ESG')
        opcao = input('Nova opção de curso (Enter para manter atual): ').strip()
        if opcao == '1':
            vestibulando.opcao_curso = 'Inteligência Artificial'
        elif opcao == '2':
            vestibulando.opcao_curso = 'Gestão ESG'
        
        print('Dados atualizados com sucesso!')
        return True
    
    # 3) cadastrar aplicador
    def cadastrar_aplicador(self, nome, cargo):
        aplicador = Aplicador(nome, cargo)
        self.aplicadores.adicionar(aplicador)
        print(f'Aplicador cadastrado: {aplicador}')
        return True
    
    # 4) calcular número de salas necessárias
    def calcular_salas_necessarias(self):
        candidatos_efetivados = 0
        for vestibulando in self.vestibulandos:
            if vestibulando.inscricao_efetivada:
                candidatos_efetivados += 1
        
        salas_necessarias = (candidatos_efetivados + 29) // 30  # Arredonda pra cima
        print(f'Candidatos com inscrição efetivada: {candidatos_efetivados}')
        print(f'Salas necessárias: {salas_necessarias}')
        return salas_necessarias
    
    # 5) elaborar lista de candidatos por sala
    def listar_candidatos_por_sala(self):
        candidatos_efetivados = []
        for vestibulando in self.vestibulandos:
            if vestibulando.inscricao_efetivada:
                candidatos_efetivados.append(vestibulando)
        
        if not candidatos_efetivados:
            print('Nenhum candidato com inscrição efetivada!')
            return
        
        sala_atual = 1
        candidatos_na_sala = 0
        
        print(f'\n=== DISTRIBUIÇÃO POR SALAS ===')
        print(f'SALA {sala_atual}:')
        
        for vestibulando in candidatos_efetivados:
            if candidatos_na_sala == 30:
                sala_atual += 1
                candidatos_na_sala = 0
                print(f'\nSALA {sala_atual}:')
            
            print(f'  {vestibulando.nome} - {vestibulando.opcao_curso}')
            candidatos_na_sala += 1
    
    # 6) relação candidatos por vaga
    def relacao_candidatos_por_vaga(self):
        #contadores pra todas as inscrições
        total_ia = 0
        total_esg = 0
        
        #contadores pra inscrições efetivadas
        efetivadas_ia = 0
        efetivadas_esg = 0
        
        for vestibulando in self.vestibulandos:
            if vestibulando.opcao_curso == 'Inteligência Artificial':
                total_ia += 1
                if vestibulando.inscricao_efetivada:
                    efetivadas_ia += 1
            elif vestibulando.opcao_curso == 'Gestão ESG':
                total_esg += 1
                if vestibulando.inscricao_efetivada:
                    efetivadas_esg += 1
        
        
        print(f'\n=== RELAÇÃO CANDIDATOS POR VAGA ===')
        print(f'INTELIGÊNCIA ARTIFICIAL:')
        print(f'Todas as inscrições: {total_ia} candidatos para {self.VAGAS_POR_CURSO} vagas')
        print(f'Relação: {total_ia/self.VAGAS_POR_CURSO:.2f} candidatos por vaga')
        print(f'Inscrições efetivadas: {efetivadas_ia} candidatos para {self.VAGAS_POR_CURSO} vagas')
        print(f'Relação: {efetivadas_ia/self.VAGAS_POR_CURSO:.2f} candidatos por vaga')
        
        print(f'\nGESTÃO ESG:')
        print(f'Todas as inscrições: {total_esg} candidatos para {self.VAGAS_POR_CURSO} vagas')
        print(f'Relação: {total_esg/self.VAGAS_POR_CURSO:.2f} candidatos por vaga')
        print(f'Inscrições efetivadas: {efetivadas_esg} candidatos para {self.VAGAS_POR_CURSO} vagas')
        print(f'Relação: {efetivadas_esg/self.VAGAS_POR_CURSO:.2f} candidatos por vaga')
    
    # 7) cadastrar alunos aprovados
    def cadastrar_aprovado(self, numero_inscricao):
        vestibulando = None
        for v in self.vestibulandos:
            if v.numero_inscricao == numero_inscricao:
                vestibulando = v
                break

        if not vestibulando:
            print('Número de inscrição não encontrado!')
            return False
        
        if not vestibulando.inscricao_efetivada:
            print('Candidato não pode ser aprovado pois a inscrição não está efetivada!')
            return False
        
        aluno_aprovado = AlunoAprovado(vestibulando.nome, vestibulando.cpf)
        
        if vestibulando.opcao_curso == 'Inteligência Artificial':
            if len(self.aprovados_ia) >= self.VAGAS_POR_CURSO:
                print('Número máximo de aprovados para Inteligência Artificial já atingido!')
                return False
            self.aprovados_ia.adicionar(aluno_aprovado)
            print(f'Aluno aprovado em Inteligência Artificial: {aluno_aprovado}')
        else:  # Gestão ESG
            if len(self.aprovados_esg) >= self.VAGAS_POR_CURSO:
                print('Número máximo de aprovados para Gestão ESG já atingido!')
                return False
            self.aprovados_esg.adicionar(aluno_aprovado)
            print(f'Aluno aprovado em Gestão ESG: {aluno_aprovado}')
        
        return True
    
    def listar_aprovados(self):
        print(f'\n=== ALUNOS APROVADOS ===')
        print(f'INTELIGÊNCIA ARTIFICIAL ({len(self.aprovados_ia)}/{self.VAGAS_POR_CURSO}):')
        for aprovado in self.aprovados_ia:
            print(f'  {aprovado}')
        
        print(f'\nGESTÃO ESG ({len(self.aprovados_esg)}/{self.VAGAS_POR_CURSO}):')
        for aprovado in self.aprovados_esg:
            print(f'  {aprovado}')
    
    #métodos auxiliares pra listagem
    def listar_vestibulandos(self):
        print(f'\n=== LISTA DE VESTIBULANDOS ===')
        for vestibulando in self.vestibulandos:
            print(vestibulando)
    
    def listar_aplicadores(self):
        print(f'\n=== LISTA DE APLICADORES ===')
        for aplicador in self.aplicadores:
            print(aplicador)

    def gerar_dados_falsos(self, num_vestibulandos=5, num_aplicadores=2):
        print(f'\nGerando {num_vestibulandos} vestibulandos falsos...')
        for _ in range(num_vestibulandos):
            nome = self.fake.name()
            cpf = self.fake.cpf()
            opcao_curso = random.choice(['Inteligência Artificial', 'Gestão ESG'])
            inscricao_efetivada = self.fake.boolean(chance_of_getting_true=70)
            self.inscrever_vestibulando(nome, cpf, opcao_curso, inscricao_efetivada)
        
        print(f'\nGerando {num_aplicadores} aplicadores falsos...')
        for _ in range(num_aplicadores):
            nome = self.fake.name()
            cargo = self.fake.job()
            self.cadastrar_aplicador(nome, cargo)
        print('\nDados falsos gerados com sucesso!')


#menu principal
def menu_principal():
    sistema = SistemaVestibular()
    
    while True:
        print('\n' + '='*50)
        print('SISTEMA DE GERENCIAMENTO DO VESTIBULAR FATEC')
        print('='*50)
        print('1. Inscrever vestibulando')
        print('2. Editar dados do vestibulando')
        print('3. Cadastrar aplicador')
        print('4. Calcular salas necessárias')
        print('5. Listar candidatos por sala')
        print('6. Relação candidatos por vaga')
        print('7. Cadastrar aluno aprovado')
        print('8. Listar vestibulandos')
        print('9. Listar aplicadores')
        print('10. Listar aprovados')
        print('11. Gerar dados falsos (Faker)')
        print('0. Sair')
        
        opcao = input('\nEscolha uma opção: ').strip()
        
        match opcao:
            case '1':
                nome = input('Nome do vestibulando: ').strip()
                cpf = input('CPF: ').strip()
                print('Opções de curso:')
                print('1 - Inteligência Artificial')
                print('2 - Gestão ESG')
                curso_opcao = input('Escolha o curso (1 ou 2): ').strip()
                
                if curso_opcao == '1':
                    curso = 'Inteligência Artificial'
                elif curso_opcao == '2':
                    curso = 'Gestão ESG'
                else:
                    print('Opção inválida!')
                    continue
                boleto = input('Boleto pago? (s/n): ').strip().lower()
                boleto_pago = boleto == 's'
                
                sistema.inscrever_vestibulando(nome, cpf, curso, boleto_pago)
            case '2':
                try:
                    num_inscricao = int(input('Número da inscrição: '))
                    sistema.editar_vestibulando(num_inscricao)
                except ValueError:
                    print('Número de inscrição inválido!')
            case '3':
                nome = input('Nome do aplicador: ').strip()
                cargo = input('Cargo na FATEC: ').strip()
                sistema.cadastrar_aplicador(nome, cargo)
            case '4':
                sistema.calcular_salas_necessarias()
            case '5':
                sistema.listar_candidatos_por_sala()
            case '6':
                sistema.relacao_candidatos_por_vaga()
            case '7':
                try:
                    num_inscricao = int(input('Número da inscrição do aprovado: '))
                    sistema.cadastrar_aprovado(num_inscricao)
                except ValueError:
                    print('Número de inscrição inválido!')  
            case '8':
                sistema.listar_vestibulandos()
            case '9':
                sistema.listar_aplicadores()
            case '10':
                sistema.listar_aprovados()   
            case '11':
                try:
                    num_vest = int(input('Quantos vestibulandos falsos deseja gerar? (Padrão: 5): ') or '5')
                    num_apl = int(input('Quantos aplicadores falsos deseja gerar? (Padrão: 2): ') or '2')
                    sistema.gerar_dados_falsos(num_vest, num_apl)
                except ValueError:
                    print('Entrada inválida. Usando valores padrão.')
                    sistema.gerar_dados_falsos()
            case '0':
                print('Encerrando o sistema...')
                break    
            case _:
                print('Opção inválida!')

menu_principal()

