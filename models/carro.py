from models.veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, placa, modelo, ano, valor_diaria, numero_portas: int, cambio: str):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.numero_portas = numero_portas
        self.cambio = cambio

    def calcular_diaria(self) -> float:
        return self.valor_diaria

    def detalhes(self) -> str:
        return f"{self.numero_portas} portas, câmbio {self.cambio}"
