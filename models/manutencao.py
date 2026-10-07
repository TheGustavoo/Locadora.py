from datetime import date


class Manutencao:
    def __init__(self, data: date, tipo_servico: str, custo: float):
        if custo < 0:
            raise ValueError("O custo da manutenção não pode ser negativo")
        self.data = data
        self.tipo_servico = tipo_servico
        self.custo = custo

    def descricao(self) -> str:
        return f"{self.data:%d/%m/%Y} - {self.tipo_servico} - R$ {self.custo:.2f}"

    def eh_custosa(self, limite: float = 1000.0) -> bool:
        return self.custo >= limite
