
from datetime import date

from models.caminhao import Caminhao
from models.carro import Carro
from models.cliente import PessoaFisica, PessoaJuridica
from models.contrato import Contrato
from models.moto import Moto

print("=== 1. Herança e polimorfismo (Veiculo) ===")
carro = Carro("ABC-1D23", "Onix", 2023, 150.0, 4, "manual")
moto = Moto("MOT-4E56", "CG 160", 2024, 80.0, 160)
caminhao = Caminhao("CAM-7F89", "Volvo FH", 2022, 400.0, 18000, 3)
for v in (carro, moto, caminhao):
    print(f"{v} | {v.detalhes()} | diária: R$ {v.calcular_diaria():.2f}")

print("\n=== 2. Herança (Cliente) ===")
maria = PessoaFisica("Maria Silva", "123.456.789-09", "(86) 99999-0000")
empresa = PessoaJuridica("Transportes Delta LTDA", "12.345.678/0001-90", "(86) 3322-1100")
print(maria)
print(empresa)

print("\n=== 3. Associação: Contrato liga Cliente e Veiculo ===")
contrato = Contrato(maria, carro, date(2026, 10, 10), date(2026, 10, 15),
                    "João Souza", "12345678901")
print(contrato.resumo())

print("\n=== 4. Regra: veículo não pode ter 2 contratos ativos ===")
try:
    Contrato(empresa, carro, date(2026, 10, 11), date(2026, 10, 12), "Pedro Lima", "98765432100")
except ValueError as erro:
    print("Bloqueado:", erro)

print("\n=== 5. Composição Veiculo -> Manutencao ===")
carro.registrar_manutencao(date(2026, 8, 1), "Troca de óleo", 250.0)
carro.registrar_manutencao(date(2026, 9, 5), "Troca de pastilhas de freio", 480.0)
for m in carro.historico_manutencoes():
    print(" -", m.descricao())
print(f"Custo total de manutenção: R$ {carro.custo_total_manutencao():.2f}")

print("\n=== 6. Composição Contrato -> Condutor ===")
print("Condutor:", contrato.condutor.descricao())
contrato.finalizar()
print("Status após finalizar:", contrato.status.value, "| carro disponível:", carro.disponivel)
contrato.excluir()
print("Contrato excluído -> condutor:", contrato.condutor)

input("\nPressione Enter para sair...")
