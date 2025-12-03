


// Lista de pacientes
let pacientes = [];

// Captura o formulário
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("formPaciente");
    const tabela = document.getElementById("tabelaPacientes").querySelector("tbody");

    form.addEventListener("submit", (event) => {
        event.preventDefault();

        // Pega os valores
        const nome = document.getElementById("nome").value;
        const idade = document.getElementById("idade").value;
        const genero = document.getElementById("genero").value;
        const contato = document.getElementById("contato").value;

        // Cria objeto paciente
        const paciente = { nome, idade, genero, contato };
        pacientes.push(paciente);

        // Atualiza tabela
        const row = tabela.insertRow();
        row.insertCell(0).textContent = paciente.nome;
        row.insertCell(1).textContent = paciente.idade;
        row.insertCell(2).textContent = paciente.genero;
        row.insertCell(3).textContent = paciente.contato;

        // Limpa formulário
        form.reset();
    });
});


// Lista de profissionais
let profissionais = [];

document.addEventListener("DOMContentLoaded", () => {
    const formProf = document.getElementById("formProfissional");
    const tabelaProf = document.getElementById("tabelaProfissionais")?.querySelector("tbody");

    if (formProf) {
        formProf.addEventListener("submit", (event) => {
            event.preventDefault();

            // Pega os valores
            const nome = document.getElementById("nomeProf").value;
            const especialidade = document.getElementById("especialidade").value;
            const registro = document.getElementById("registro").value;

            // Cria objeto profissional
            const profissional = { nome, especialidade, registro };
            profissionais.push(profissional);

            // Atualiza tabela
            const row = tabelaProf.insertRow();
            row.insertCell(0).textContent = profissional.nome;
            row.insertCell(1).textContent = profissional.especialidade;
            row.insertCell(2).textContent = profissional.registro;

            // Limpa formulário
            formProf.reset();
        });
    }
});

// Lista de Consultas & Exames
let consultasExames = [];

document.addEventListener("DOMContentLoaded", () => {
    const formCE = document.getElementById("formConsultaExame");
    const tabelaCE = document.getElementById("tabelaCE")?.querySelector("tbody");

    if (formCE) {
        formCE.addEventListener("submit", (event) => {
            event.preventDefault();

            // Pega os valores
            const paciente = document.getElementById("pacienteCE").value;
            const profissional = document.getElementById("profissionalCE").value;
            const tipo = document.getElementById("tipoCE").value;
            const data = document.getElementById("dataCE").value;

            // Cria objeto
            const registro = { paciente, profissional, tipo, data };
            consultasExames.push(registro);

            // Atualiza tabela
            const row = tabelaCE.insertRow();
            row.insertCell(0).textContent = registro.paciente;
            row.insertCell(1).textContent = registro.profissional;
            row.insertCell(2).textContent = registro.tipo;
            row.insertCell(3).textContent = registro.data;

            // Limpa formulário
            formCE.reset();
        });
    }
});

// Lista de Agendamentos
let agendamentos = [];

document.addEventListener("DOMContentLoaded", () => {
    const formAg = document.getElementById("formAgendamento");
    const tabelaAg = document.getElementById("tabelaAgendamentos")?.querySelector("tbody");

    if (formAg) {
        formAg.addEventListener("submit", (event) => {
            event.preventDefault();

            // Pega os valores
            const paciente = document.getElementById("pacienteAg").value;
            const profissional = document.getElementById("profissionalAg").value;
            const tipo = document.getElementById("tipoAg").value;
            const data = document.getElementById("dataAg").value;

            // Cria objeto
            const agendamento = { paciente, profissional, tipo, data };
            agendamentos.push(agendamento);

            // Atualiza tabela
            const row = tabelaAg.insertRow();
            row.insertCell(0).textContent = agendamento.paciente;
            row.insertCell(1).textContent = agendamento.profissional;
            row.insertCell(2).textContent = agendamento.tipo;
            row.insertCell(3).textContent = agendamento.data;

            // Limpa formulário
            formAg.reset();
        });
    }
});

// Lista de Prontuários
let prontuarios = [];

document.addEventListener("DOMContentLoaded", () => {
    const formPr = document.getElementById("formProntuario");
    const tabelaPr = document.getElementById("tabelaProntuario")?.querySelector("tbody");

    if (formPr) {
        formPr.addEventListener("submit", (event) => {
            event.preventDefault();

            // Pega os valores
            const paciente = document.getElementById("pacientePr").value;
            const descricao = document.getElementById("descricaoPr").value;
            const prescricao = document.getElementById("prescricaoPr").value;
            const data = document.getElementById("dataPr").value;

            // Cria objeto
            const registro = { paciente, descricao, prescricao, data };
            prontuarios.push(registro);

            // Atualiza tabela
            const row = tabelaPr.insertRow();
            row.insertCell(0).textContent = registro.paciente;
            row.insertCell(1).textContent = registro.descricao;
            row.insertCell(2).textContent = registro.prescricao;
            row.insertCell(3).textContent = registro.data;

            // Limpa formulário
            formPr.reset();
        });
    }
});
