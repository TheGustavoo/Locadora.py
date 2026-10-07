class Condutor:

    def __init__(self, nome: str, cnh: str):
        self.nome = nome
        self.cnh = cnh
        if not self.cnh_valida():
            raise ValueError("CNH inválida (esperadas 11 dígitos)")

    def cnh_valida(self) -> bool:
        digitos = "".join(c for c in self.cnh if c.isdigit())
        return len(digitos) == 11

    def descricao(self) -> str:
        return f"{self.nome} (CNH {self.cnh})"
