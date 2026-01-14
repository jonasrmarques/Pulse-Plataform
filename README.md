# Pulse Platform

Pulse Platform é uma **plataforma modular de gestão orientada a dados**, criada para centralizar indicadores estratégicos e apoiar a tomada de decisão em ambientes corporativos.

O projeto foi concebido para crescer de forma incremental, com módulos independentes que podem ser adicionados conforme a necessidade do negócio.

O primeiro módulo desenvolvido é o **People Analytics**, focado em indicadores de RH amplamente utilizados em empresas reais.

---

## 🎯 Visão do Produto

A Pulse Platform tem como objetivo oferecer uma visão clara e confiável da operação da empresa, transformando dados brutos em **insights acionáveis**.

A plataforma foi pensada para:
- Centralizar indicadores estratégicos
- Facilitar análises gerenciais
- Apoiar decisões baseadas em dados
- Evoluir de forma modular e escalável

---

## 🧩 Módulos

### 📌 People Analytics (em desenvolvimento)
Módulo responsável por indicadores de Recursos Humanos, com foco em análise da força de trabalho.

**Principais indicadores:**
- Headcount
- Turnover (%)
- Absenteísmo (%)
- Horas extras
- Custo médio por funcionário

Todos os indicadores podem ser filtrados por:
- Período
- Setor
- Tipo de contrato
- Situação do funcionário (ativo/desligado)

---

## 📊 Visualizações

- Dashboard geral com KPIs (Big Numbers)
- Gráficos interativos com suporte a drill-down
- Tabelas detalhadas para análise aprofundada

Gráficos previstos:
- Evolução do headcount
- Turnover mensal
- Absenteísmo por setor
- Horas extras por mês
- Demissões por motivo

---

## 🧱 Funcionalidades

- Plataforma web modular
- Dashboard corporativo
- Filtros globais aplicáveis a KPIs e gráficos
- Telas de detalhamento (drill-down)
- Listagem e detalhamento de funcionários
- Autenticação de usuários

---

## 🛠️ Stack Tecnológica

- **Backend:** Django
- **Banco de dados:** PostgreSQL
- **ORM:** Django ORM
- **Frontend:** Django Templates + Bootstrap
- **Visualização de dados:** Chart.js
- **Processamento de dados:** Pandas (quando aplicável)

---

## 🧠 Regras de Negócio (People Analytics)

- Funcionários desligados não entram no headcount
- Turnover calculado com base no headcount médio
- Apenas horas extras aprovadas são contabilizadas
- Férias futuras não impactam indicadores atuais
- Absenteísmo considera faltas e afastamentos

---

## 🗂️ Arquitetura

A Pulse Platform segue uma arquitetura modular, separando:
- Domínios de negócio
- Movimentações e eventos
- Cálculo de indicadores
- Camada de apresentação

As regras de negócio e queries complexas são centralizadas, facilitando manutenção e evolução do sistema.

---

## 🧪 Dados de Teste

O projeto conta com **scripts de geração de dados fictícios realistas**, incluindo:
- Funcionários ativos e desligados
- Histórico de movimentações ao longo de múltiplos meses
- Cenários variados para validação dos indicadores

---

## 🚀 Status do Projeto

🚧 **Em desenvolvimento**

O projeto está sendo desenvolvido com foco em:
- boas práticas
- clareza de código
- fidelidade a cenários corporativos reais

---

## 🔮 Roadmap (alto nível)

- Finalização do módulo People Analytics
- Otimização de performance e queries
- Estrutura base para novos módulos

---

## 👨‍💻 Autor

**Jonas Marques**  
Desenvolvedor de Software  

🔗 LinkedIn: *https://www.linkedin.com/in/jonas-rafael-marques/*  
🔗 GitHub: *https://github.com/jonasrmarques*

---

## 📌 Observação

Este projeto foi criado com fins educacionais e profissionais, visando demonstrar habilidades técnicas aplicadas a problemas reais de negócio.
