# Sistema de Agendamento de Consultas Médicas

Um sistema desenvolvido em **Python** utilizando **Tkinter** para interface gráfica e **SQLite** como banco de dados, para agendar consultas médicas. O sistema permite que administradores cadastrem médicos, agendem consultas, gerenciem horários e consultem históricos de atendimento.

## Funcionalidades

### 1. Cadastro de Pacientes
- Formulário para cadastrar novos pacientes com:
  - Nome completo
  - Data de nascimento
  - CPF
  - Contato (telefone, e-mail)
  - Endereço
- Edição e remoção de pacientes.
- Armazenamento das informações no banco de dados SQLite.

### 2. Cadastro de Médicos
- Formulário para cadastrar médicos com:
  - Nome completo
  - Especialidade (pediatra, cardiologista, etc.)
  - Contato
  - Dias e horários disponíveis para consultas.
- Edição e remoção de médicos.
- Armazenamento dos dados no SQLite.

### 3. Agendamento de Consultas
- Interface para agendar consultas:
  - Seleção do médico e horário disponível.
  - Seleção do paciente.
  - Motivo ou observações sobre a consulta.
- Validação de conflitos de horário.
- Edição ou cancelamento de consultas.
- Armazenamento de consultas no SQLite.

### 4. Consulta de Horários Disponíveis
- Verificação dos horários disponíveis dos médicos.
- Filtros por especialidade e nome do médico.
- Exibição dos dias e horários disponíveis.

### 5. Histórico de Consultas
- Listagem de consultas passadas e futuras.
- Histórico por paciente ou médico.
- Armazenamento no banco de dados.

### 6. Relatórios de Consultas
- Geração de relatórios administrativos:
  - Consultas por médico.
  - Consultas por especialidade.
  - Consultas canceladas e reprogramadas.

### 7. Login e Controle de Acesso
- Sistema de autenticação com diferentes usuários:
  - **Administradores**: podem gerenciar médicos, pacientes e consultas.

## Estrutura do Banco de Dados (SQLite)

- **Tabelas sugeridas**:
   - **Pacientes**: ID, nome, data de nascimento, contato, endereço.
   - **Médicos**: ID, nome, especialidade, contato, disponibilidade.
   - **Consultas**: ID, paciente_id, medico_id, data, horário, observações, status (agendada, concluída, cancelada).
   - **Usuários** (para controle de login): ID, nome, e-mail, senha, nível de acesso (admin/paciente).

## Exemplo de Fluxo:
   - O paciente (ou administrador) acessa o sistema.
   - O paciente escolhe o médico e a especialidade, e vê os horários disponíveis.
   - O paciente escolhe o horário e confirma o agendamento.
   - O paciente pode editar ou cancelar a consulta, se necessário.
   - O administrador pode visualizar todos os agendamentos e gerar relatórios conforme a necessidade.
