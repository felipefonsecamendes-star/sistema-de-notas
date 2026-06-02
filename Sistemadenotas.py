
alunos = []


def adicionar_aluno(nome, notas):
    """
    Adiciona um novo aluno ao sistema.

    Parâmetros:
        nome (str): Nome do aluno
        notas (list): Lista de notas (float) do aluno

    Retorna:
        dict: Dicionário com os dados do aluno cadastrado
    """
    aluno = {
        "nome": nome.strip().title(),
        "notas": notas.copy(),
        "media": sum(notas) / len(notas) if notas else 0.0
    }
    alunos.append(aluno)
    return aluno


def listar_alunos():
    """
    Retorna a lista completa de alunos cadastrados.

    Retorna:
        list: Lista de dicionários com dados dos alunos
    """
    return alunos.copy()


def media_turma():
    """
    Calcula a média geral da turma com base nas médias individuais.

    Retorna:
        float: Média geral da turma
        None: Se não houver alunos cadastrados
    """
    if not alunos:
        return None

    soma_medias = sum(aluno["media"] for aluno in alunos)
    return soma_medias / len(alunos)



def buscar_aluno(nome):
    """Busca um aluno pelo nome (case insensitive)."""
    nome_busca = nome.strip().lower()
    for aluno in alunos:
        if aluno["nome"].lower() == nome_busca:
            return aluno
    return None


def remover_aluno(nome):
    """Remove um aluno pelo nome. Retorna True se removido, False se não encontrado."""
    global alunos
    nome_busca = nome.strip().lower()
    alunos_originais = alunos[:]
    alunos = [a for a in alunos if a["nome"].lower() != nome_busca]
    return len(alunos) < len(alunos_originais)


def situacao_aluno(media):
    """Retorna a situação do aluno com base na média."""
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"


def formatar_nota(nota):
    """Formata uma nota para exibição com 1 casa decimal."""
    return f"{nota:.1f}"


def exibir_cabecalho(titulo):
    """Exibe um cabeçalho formatado."""
    print()
    print("=" * 50)
    print(f"  {titulo}")
    print("=" * 50)


def exibir_aluno(aluno):
    """Exibe os dados formatados de um aluno."""
    notas_str = ", ".join(formatar_nota(n) for n in aluno["notas"])
    situacao = situacao_aluno(aluno["media"])
    print(f"  Nome:   {aluno['nome']}")
    print(f"  Notas:  [{notas_str}]")
    print(f"  Média:  {formatar_nota(aluno['media'])}")
    print(f"  Status: {situacao}")


def exibir_lista_alunos():
    """Exibe a lista de todos os alunos cadastrados."""
    lista = listar_alunos()

    if not lista:
        print("  Nenhum aluno cadastrado.")
        return

    print(f"  {'Nº':<4} {'Nome':<25} {'Média':<8} {'Status':<15}")
    print("  " + "-" * 55)

    for i, aluno in enumerate(lista, 1):
        situacao = situacao_aluno(aluno["media"])
        print(f"  {i:<4} {aluno['nome']:<25} {formatar_nota(aluno['media']):<8} {situacao:<15}")


def exibir_media_turma():
    """Exibe a média geral da turma."""
    media = media_turma()

    if media is None:
        print("  Não há alunos cadastrados para calcular a média.")
        return

    print(f"  Total de alunos: {len(alunos)}")
    print(f"  Média da turma:  {formatar_nota(media)}")

    # Estatísticas adicionais
    aprovados = sum(1 for a in alunos if a["media"] >= 7.0)
    recuperacao = sum(1 for a in alunos if 5.0 <= a["media"] < 7.0)
    reprovados = sum(1 for a in alunos if a["media"] < 5.0)

    print()
    print(f"  Aprovados:     {aprovados} ({aprovados/len(alunos)*100:.1f}%)")
    print(f"  Recuperação:   {recuperacao} ({recuperacao/len(alunos)*100:.1f}%)")
    print(f"  Reprovados:    {reprovados} ({reprovados/len(alunos)*100:.1f}%)")


def ler_nome():
    """Lê e valida o nome do aluno."""
    while True:
        nome = input("  Nome do aluno: ").strip()
        if nome:
            return nome
        print("  [ERRO] O nome não pode estar vazio.")


def ler_notas():
    """Lê e valida as notas do aluno."""
    notas = []
    print("  Digite as notas (pressione Enter sem valor para encerrar):")

    while True:
        entrada = input(f"    Nota {len(notas) + 1}: ").strip()

        if not entrada:
            if len(notas) == 0:
                print("    [ERRO] Pelo menos uma nota é necessária.")
                continue
            break

        try:
            nota = float(entrada.replace(",", "."))
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("    [ERRO] A nota deve estar entre 0 e 10.")
        except ValueError:
            print("    [ERRO] Valor inválido. Digite um número.")

    return notas


def menu_interativo():
    """
    Executa o menu interativo do sistema de notas.
    Permite ao usuário navegar pelas funcionalidades do sistema.
    """
    while True:
        exibir_cabecalho("SISTEMA DE NOTAS - MENU PRINCIPAL")
        print("  [1] Adicionar Aluno")
        print("  [2] Listar Alunos")
        print("  [3] Média da Turma")
        print("  [4] Buscar Aluno")
        print("  [5] Remover Aluno")
        print("  [0] Sair")
        print("=" * 50)

        opcao = input("  Escolha uma opção: ").strip()

        if opcao == "1":
            # Adicionar Aluno
            exibir_cabecalho("ADICIONAR ALUNO")
            nome = ler_nome()
            notas = ler_notas()
            aluno = adicionar_aluno(nome, notas)
            print()
            print(f"  ✓ Aluno '{aluno['nome']}' cadastrado com sucesso!")
            print(f"    Média: {formatar_nota(aluno['media'])}")

        elif opcao == "2":
            # Listar Alunos
            exibir_cabecalho("LISTA DE ALUNOS")
            exibir_lista_alunos()

        elif opcao == "3":
            # Média da Turma
            exibir_cabecalho("MÉDIA DA TURMA")
            exibir_media_turma()

        elif opcao == "4":
            # Buscar Aluno
            exibir_cabecalho("BUSCAR ALUNO")
            nome = input("  Digite o nome do aluno: ").strip()
            aluno = buscar_aluno(nome)
            if aluno:
                exibir_aluno(aluno)
            else:
                print(f"  Aluno '{nome}' não encontrado.")

        elif opcao == "5":
            # Remover Aluno
            exibir_cabecalho("REMOVER ALUNO")
            nome = input("  Digite o nome do aluno: ").strip()
            if remover_aluno(nome):
                print(f"  ✓ Aluno '{nome}' removido com sucesso!")
            else:
                print(f"  Aluno '{nome}' não encontrado.")

        elif opcao == "0":
            # Sair
            exibir_cabecalho("ENCERRANDO SISTEMA")
            print("  Obrigado por usar o Sistema de Notas!")
            print("=" * 50)
            break

        else:
            print("  [ERRO] Opção inválida. Tente novamente.")

        input("\n  Pressione Enter para continuar...")



if __name__ == "__main__":
    menu_interativo()