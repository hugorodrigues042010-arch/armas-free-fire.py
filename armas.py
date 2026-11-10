# Tabela de armas do Free Fire com os preços do modo Contra Squad (CS)
armas = {
    "1": {"nome": "Desert Eagle", "tipo": "Pistola", "preco": 800},
    "2": {"nome": "FAMAS", "tipo": "Fuzil de Assalto", "preco": 1200},
    "3": {"nome": "UMP", "tipo": "Submetralhadora", "preco": 1200},
    "4": {"nome": "SPAS12", "tipo": "Espingarda", "preco": 1200},
    "5": {"nome": "P90", "tipo": "Submetralhadora", "preco": 1300},
    "6": {"nome": "M4A1", "tipo": "Fuzil de Assalto", "preco": 1400},
    "7": {"nome": "SCAR", "tipo": "Fuzil de Assalto", "preco": 1400},
    "8": {"nome": "Thompson", "tipo": "Submetralhadora", "preco": 1400},
    "9": {"nome": "XM8", "tipo": "Fuzil de Assalto", "preco": 1500},
    "10": {"nome": "AUG", "tipo": "Fuzil de Assalto", "preco": 1500},
    "11": {"nome": "Vector", "tipo": "Submetralhadora", "preco": 1500},
    "12": {"nome": "AK-47", "tipo": "Fuzil de Assalto", "preco": 1600},
    "13": {"nome": "M1014", "tipo": "Espingarda", "preco": 1600},
    "14": {"nome": "Carapina", "tipo": "Atiradeira", "preco": 1700},
    "15": {"nome": "Kar98k", "tipo": "Sniper", "preco": 1800},
    "16": {"nome": "M1887", "tipo": "Espingarda", "preco": 1800},
    "17": {"nome": "Groza", "tipo": "Fuzil de Assalto", "preco": 1900},
    "18": {"nome": "MP40", "tipo": "Submetralhadora", "preco": 2000},
    "19": {"nome": "M82B", "tipo": "Sniper", "preco": 2000},
    "20": {"nome": "AWM", "tipo": "Sniper", "preco": 2200}
}

def loja_free_fire():
    saldo = 3000  # Saldo inicial de ouro para a rodada
    
    print("=" * 45)
    print("      LOJA DE ARMASS - FREE FIRE (CS)      ")
    print("=" * 45)
    print(f"Seu saldo disponível: ${saldo} Ouro\n")

    # Exibe o menu com as opções
    for num, item in armas.items():
        print(f"[{num}] {item['nome']:<15} | {item['tipo']:<18} | ${item['preco']} Ouro")

    print("=" * 45)
    
    # Seleção do usuário
    escolha = input("Digite o número da arma que deseja comprar: ").strip()

    if escolha in armas:
        arma = armas[escolha]
        if saldo >= arma["preco"]:
            saldo -= arma["preco"]
            print(f"\n✅ Compra realizada com sucesso!")
            print(f"Arma adquirida: {arma['nome']} ({arma['tipo']})")
            print(f"Ouro restante: ${saldo}")
        else:
            print(f"\n❌ Ouro insuficiente! A arma {arma['nome']} custa ${arma['preco']}.")
    else:
        print("\n❌ Opção inválida! Escolha um número de 1 a 20.")

# Executa o programa
loja_free_fire()