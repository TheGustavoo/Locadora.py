from abc import ABC, abstractmethod


def _somente_digitos(texto: str) -> str:
    return "".join(c for c in texto if c.isdigit())


class Cliente(ABC):

    def __init__(self, nome: str, documento: str, telefone: str):
        self.nome = nome
        self.documento = documento
        self.telefone = telefone
        if not self.validar_documento():
            raise ValueError(f"Documento inválido para {self.__class__.__name__}: {documento}")

    @abstractmethod
    def validar_documento(self) -> bool:
        """Valida o formato do documento (CPF ou CNPJ)."""

    @abstractmethod
    def tipo(self) -> str:
        ...

    def atualizar_telefone(self, novo_telefone: str) -> None:
        self.telefone = novo_telefone

    def __str__(self) -> str:
        return f"{self.nome} ({self.tipo()} - {self.documento})"


class PessoaFisica(Cliente):
    def __init__(self, nome: str, cpf: str, telefone: str):
        super().__init__(nome, cpf, telefone)

    def validar_documento(self) -> bool:
        return len(_somente_digitos(self.documento)) == 11  

    def tipo(self) -> str:
        return "Pessoa Física"


class PessoaJuridica(Cliente):
    def __init__(self, razao_social: str, cnpj: str, telefone: str):
        super().__init__(razao_social, cnpj, telefone)

    def validar_documento(self) -> bool:
        return len(_somente_digitos(self.documento)) == 14  

    def tipo(self) -> str:
        return "Pessoa Jurídica"
