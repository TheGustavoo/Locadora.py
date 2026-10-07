from datetime import date
from enum import Enum

from models.cliente import Cliente
from models.condutor import Condutor
from models.veiculo import Veiculo


class StatusContrato(Enum):
    ATIVO = "ativo"
    FINALIZADO = "finalizado"
    CANCELADO = "cancelado"


class Contrato:

    def __init__(self, cliente: Cliente, veiculo: Veiculo, data_inicio: date,
                 data_termino_prevista: date, nome_condutor: str, cnh_condutor: str):
        if data_termino_prevista < data_inicio:
            raise ValueError("A data de término não pode ser anterior à data de início")

        self.cliente = cliente      
        self.veiculo = veiculo      
        self.data_inicio = data_inicio
        self.data_termino_prevista = data_termino_prevista
        self.status = StatusContrato.ATIVO

        self._condutor: Condutor | None = Condutor(nome_condutor, cnh_condutor)

        veiculo._reservar()  
        self.valor_total = self.calcular_valor_total()

    @property
    def condutor(self) -> Condutor | None:
        return self._condutor

    def calcular_valor_total(self) -> float:
        dias = max((self.data_termino_prevista - self.data_inicio).days, 1)
        return round(dias * self.veiculo.calcular_diaria(), 2)

    def finalizar(self) -> None:
        self._encerrar(StatusContrato.FINALIZADO)

    def cancelar(self) -> None:
        self._encerrar(StatusContrato.CANCELADO)

    def _encerrar(self, novo_status: StatusContrato) -> None:
        if self.status != StatusContrato.ATIVO:
            raise ValueError(f"Contrato já está {self.status.value}")
        self.status = novo_status
        self.veiculo._liberar()

    def excluir(self) -> None:
        if self.status == StatusContrato.ATIVO:
            self.veiculo._liberar()
        self._condutor = None
        self.cliente = None
        self.veiculo = None

    def resumo(self) -> str:
        condutor = self._condutor.descricao() if self._condutor else "removido"
        return (f"Contrato [{self.status.value}] {self.data_inicio:%d/%m/%Y} a "
                f"{self.data_termino_prevista:%d/%m/%Y} | cliente: {self.cliente} | "
                f"veículo: {self.veiculo} | condutor: {condutor} | total: R$ {self.valor_total:.2f}")
