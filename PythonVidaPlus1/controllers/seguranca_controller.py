


from PythonVidaPlus1.models.usuario import Usuario
from PythonVidaPlus1.models.auditoria import Auditoria

class SegurancaController:
    def __init__(self):
        self.auditoria = Auditoria()

    def criar_usuario(self, id_: str, nome: str, perfil: str) -> Usuario:
        usuario = Usuario(id_, nome, perfil)
        self.auditoria.registrar(nome, f"Usuário criado com perfil {perfil}")
        return usuario

    def validar_usuario(self, usuario: Usuario) -> bool:
        return usuario.validar()

    def registrar_acao(self, usuario: Usuario, acao: str):
        self.auditoria.registrar(usuario.nome, acao)

    def listar_logs(self):
        return self.auditoria.listar_logs()
