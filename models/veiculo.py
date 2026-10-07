from abc import ABC, abstractmethod
from datetime import date

from models.manutencao import Manutencao


class Veiculo(ABC):

    def __init__(self, placa: str, modelo: str, ano: int, valor_diaria: float):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria
        self._alugado = False
        self._manutencoes: list[Manutencao] = []  

    @abstractmethod
    def calcular_diaria(self) -> float:
        """Valor da diária considerando a regra de cada tipo de veículo."""

    @abstractmethod
    def detalhes(self) -> str:
        """"""
    # --- disponibilidade (usada pelo Contrato) ---
    @property
    def disponivel(self) -> bool:
        return not self._alugado

    def _reservar(self) -> None:
        if self._alugado:
            raise ValueError(f"Veículo {self.placa} já possui contrato ativo")
        self._alugado = True

    def _liberar(self) -> None:
        self._alugado = False

    # --- Composição: o veículo CRIA suas manutenções ---
    def registrar_manutencao(self, data: date, tipo_servico: str, custo: float) -> Manutencao:
        manutencao = Manutencao(data, tipo_servico, custo)
        self._manutencoes.append(manutencao)
        return manutencao

    def historico_manutencoes(self) -> list[Manutencao]:
        return list(self._manutencoes)

    def custo_total_manutencao(self) -> float:
        return sum(m.custo for m in self._manutencoes)

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.modelo} ({self.placa}, {self.ano})"
