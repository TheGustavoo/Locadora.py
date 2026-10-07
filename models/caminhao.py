from models.veiculo import Veiculo


class Caminhao(Veiculo):
    def __init__(self, placa, modelo, ano, valor_diaria, capacidade_carga_kg: float, numero_eixos: int):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.capacidade_carga_kg = capacidade_carga_kg
        self.numero_eixos = numero_eixos

    def calcular_diaria(self) -> float:
        return self.valor_diaria * 1.15 

    def detalhes(self) -> str:
        return f"carga máxima {self.capacidade_carga_kg:.0f} kg, {self.numero_eixos} eixos"
