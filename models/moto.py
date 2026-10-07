from models.veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, placa, modelo, ano, valor_diaria, cilindradas: int, exige_capacete: bool = True):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.cilindradas = cilindradas
        self.exige_capacete = exige_capacete

    def calcular_diaria(self) -> float:
        return self.valor_diaria * 0.90  

    def detalhes(self) -> str:
        return f"{self.cilindradas}cc, capacete incluso: {'sim' if self.exige_capacete else 'não'}"
