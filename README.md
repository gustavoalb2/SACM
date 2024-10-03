# SACM

Sistema de Agendamento de Consultas Médicas

Descrição:
    Um sistema que permite aos usuários agendar consultas médicas com base na disponibilidade de médicos. O sistema deve armazenar informações dos pacientes, médicos consultas. Ele oferece uma interface para os administradores (clínicas ou recepcionistas) e/ou os próprios pacientes agendarem, visualizarem, editarem e cancelarem consultas.

Funcionalidades:
    Cadastro de Pacientes
        Formulário para cadastrar novos pacientes com informações como:
            Nome completo
            Data de nascimento
            CPF (opcional, dependendo da necessidade)
            Contato (telefone, e-mail)
            Endereço
        Opção para editar ou remover dados do paciente.
        Listas pacientes.
        Integração com o banco de dados SQLite para armazenar as informações dos pacientes.
    
    Cadastro de Médicos
        Formulário para cadastrar médicos disponíveis, com dados como:
            Nome completo
            Especialidade (pediatra, cardiologista, etc.)
            Contato
            Dias e horários disponíveis para consulta.
        Possibilidade de adicionar e remover médicos.
        Listar médicos.
        Armazenamento das informações no banco de dados.

    Agendamento de Consultas
        Interface onde o administrador pode:
            Selecionar o médico desejado.
            Escolher a data e o horário disponíveis.
            Registrar o motivo ou observações sobre a consulta (sintomas, por exemplo).
        Validação automática de horários para evitar conflitos entre consultas.
        Opção para editar ou cancelar consultas já agendadas.
        Armazenamento de todas as consultas agendadas no banco de dados SQLite.

    Consulta de Horários Disponíveis
        Interface para verificar os horários disponíveis dos médicos.
        Filtragem por especialidade ou nome do médico.
        Listar dias e horários em que cada médico tem disponibilidade para consultas.
    
    Histórico de Consultas
        Listagem de todas as consultas passadas e futuras de cada paciente.
        Possibilidade de visualizar o histórico de um determinado paciente ou médico.
        Armazenar o histórico de consultas no banco de dados SQLite para futuras referências.
    
    Banco de Dados (SQLite)

    Tabelas sugeridas:
        Pacientes: ID, nome, data de nascimento, contato, endereço.
        Médicos: ID, nome, especialidade, contato, disponibilidade.
        Consultas: ID, paciente_id, medico_id, data, horário, observações, status (agendada, concluída, cancelada).
        Usuários (para controle de login(administrativo)): ID, nome, e-mail, senha, nível de acesso (admin).

    Exemplo de Fluxo:

    O administrador acessa o sistema.
    O administrador escolhe o médico e a especialidade, e vê os horários disponíveis.
    O administrador escolhe o horário e confirma o agendamento.
    O administrador pode editar ou cancelar a consulta, se necessário.
    O administrador pode visualizar todos os agendamentos e gerar relatórios conforme a necessidade.