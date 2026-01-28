# 🔥 VULCAN - Super Ferramenta Brute Force 

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Version](https://img.shields.io/badge/version-3.0-green.svg)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

**A ferramenta mais avançada de brute force para testes de segurança autorizados**

</div>

## 🚨 **AVISO LEGAL CRÍTICO**

> ⚠️ **ATENÇÃO**: Esta ferramenta é desenvolvida **EXCLUSIVAMENTE** para:
> - Testes de segurança autorizados
> - Pentests com permissão escrita
> - Ambientes de laboratório controlados
> - Pesquisa acadêmica em segurança
>
> **USO NÃO AUTORIZADO É CRIME** sujeito a ações legais conforme:
> - Artigo 154-A do Código Penal Brasileiro
> - Computer Fraud and Abuse Act (EUA)
> - GDPR/LGPD para proteção de dados

## 🎯 **Características Principais**

### 🔐 **Módulos de Quebra de Hash**
- ✅ **Multi-algoritmo**: MD5, SHA1, SHA256, SHA512, NTLM
- ✅ **Ataque por dicionário** com wordlists personalizadas
- ✅ **Brute force inteligente** com padrões reconhecidos
- ✅ **Rainbow tables** otimizadas
- ✅ **Ataque híbrido** (dicionário + brute force)
- ✅ **Ataque distribuído** (multi-core/multi-nó)

### 🌐 **Módulos de Rede**
- ✅ **SSH Brute Force** com suporte a chaves
- ✅ **FTP Authentication cracking**
- ✅ **HTTP Basic/Digest Auth**
- ✅ **Multi-threading** para performance máxima
- ✅ **Timeout configurável** e reconexão inteligente

### 🛠️ **Ferramentas Avançadas**
- ✅ **Gerador de wordlists** com regras personalizadas
- ✅ **Criador de rainbow tables** local
- ✅ **Análise de padrões** de senhas
- ✅ **Exportação** em JSON, CSV, HTML
- ✅ **Relatórios profissionais** detalhados
- ✅ **Sistema de logging** completo

## 📦 **Instalação Rápida**

### Pré-requisitos
```bash
# Python 3.8 ou superior
python --version

# Gerenciador de pacotes pip atualizado
pip install --upgrade pip
```

### Instalação via Git
```bash
git clone https://github.com/seuusuario/vulcan-brute-force.git
cd vulcan-brute-force

# Instalar dependências
pip install -r requirements.txt

# Ou instalação direta
pip install colorama paramiko requests
```

### Instalação via Docker (Recomendado)
```bash
# Construir imagem
docker build -t vulcan-brute-force .

# Executar container
docker run -it --rm vulcan-brute-force --help
```

## 🚀 **Começando a Usar**

### Verificação Legal Obrigatóri
```bash
python vulcan.py
# O sistema fará 5 verificações legais antes de permitir o uso
```

### Exemplo 1: Quebra de Hash MD5
```bash
python vulcan.py \
  --hash 5f4dcc3b5aa765d61d8327deb882cf99 \
  --mode hybrid \
  --wordlist rockyou.txt \
  --algorithm md5 \
  --export json
```

### Exemplo 2: Ataque SSH
```bash
python vulcan.py \
  --target 192.168.1.100 \
  --service ssh \
  --username admin \
  --port 22 \
  --wordlist passwords.txt \
  --no-report
```

### Exemplo 3: Gerar Rainbow Table
```bash
python vulcan.py \
  --create-rainbow \
  --algorithm sha256 \
  --output my_rainbow.db
```

### Exemplo 4: Ataque Distribuído
```bash
python vulcan.py \
  --hash e10adc3949ba59abbe56e057f20f883e \
  --mode distributed \
  --nodes 8 \
  --algorithm md5
```

## 📊 **Modos de Ataque Disponíveis**

| Modo | Descrição | Uso Recomendado |
|------|-----------|-----------------|
| `simple` | Brute force básico | Senhas curtas (até 6 chars) |
| `dictionary` | Ataque por dicionário | Senhas comuns/wordlists |
| `hybrid` | Dicionário + padrões | Senhas com variações |
| `rainbow` | Rainbow table pré-computada | Hashes conhecidos |
| `distributed` | Multi-processos/cores | Performance máxima |
| `intelligent` | IA + padrões reconhecidos | Senhas complexas |

## 🎨 **Interface e Recursos Visuais**

```
╔══════════════════════════════════════════════════════════════════════════════╗
║ ██╗   ██╗██╗   ██╗██╗      █████╗  ██████╗███╗   ██╗ ████████╗ ██████╗ ██████╗  ██████╗║
║ ██╗   ██║██╗   ██║██║     ██╔══██╗██╔════╝████╗  ██║ ╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗║
║ ██╗   ██║██║   ██║██║     ███████║██║     ██╔██╗ ██║    ██║   ██║   ██║██████╔╝██║   ██║║
║ ██╗   ██║██║   ██║██║     ██╔══██║██║     ██║╚██╗██║    ██║   ██║   ██║██╔══██╗██║   ██║║
║ ╚██████╔╝╚██████╔╝███████╗██║  ██║╚██████╗██║ ╚████║    ██║   ╚██████╔╝██║  ██║╚██████╔╝║
║  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═══╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                         BRUTE FORCE PROFESSIONAL SUITE                      ║
║                    Versão: 3.0 | Codinome: VULCAN                           ║
║                   Desenvolvido por: Leonardo Pereira                         ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## 📈 **Performance e Estatísticas**

### Benchmarks (Intel i7-10700K, 8 cores)
| Técnica | Velocidade | Senhas Testadas |
|---------|------------|-----------------|
| Brute Force (6 chars) | ~500K/s | 2.176.782.336 |
| Dictionary Attack | ~50K/s | Dependente da wordlist |
| Hybrid Attack | ~100K/s | Combinações inteligentes |
| Distributed (8 cores) | ~2M/s | Escalável linearmente |

### Relatório de Saída
```json
{
  "tool": "VULCAN Brute Force Professional",
  "version": "3.0",
  "author": "Leonardo Pereira",
  "timestamp": "2024-01-15T14:30:00",
  "results": [
    {
      "hash": "5f4dcc3b5aa765d61d8327deb882cf99",
      "password": "password",
      "algorithm": "md5",
      "attempts": 1,
      "time": 0.002
    }
  ],
  "statistics": {
    "total_attempts": 1000000,
    "successful_cracks": 1,
    "average_speed": 500000,
    "max_speed": 750000
  }
}
```

## 🔧 **Configuração Avançada**

### Arquivo de Configuração (config.yaml)
```yaml
# config.yaml
general:
  max_threads: 50
  timeout: 30
  retry_attempts: 3
  
hash_cracking:
  default_algorithm: sha256
  rainbow_table_path: ./rainbow/
  wordlist_directory: ./wordlists/
  
network:
  ssh_timeout: 10
  ftp_timeout: 15
  http_timeout: 20
  
reporting:
  auto_export: true
  export_format: json
  save_logs: true
  
security:
  legal_warning: true
  audit_logging: true
  max_attempts_per_target: 10000
```

### Uso com Configuração
```bash
python vulcan.py --config config.yaml --hash TARGET_HASH
```

## 🗂️ **Estrutura do Projeto**
```
vulcan-brute-force/
│
├── vulcan.py              # Script principal
├── requirements.txt       # Dependências
├── README.md             # Este arquivo
├── LICENSE               # Licença MIT
│
├── core/                 # Núcleo do sistema
│   ├── hash_cracker.py   # Módulo de hash
│   ├── network_attacker.py # Ataques de rede
│   └── password_generator.py # Gerador de senhas
│
├── utils/                # Utilitários
│   ├── logger.py         # Sistema de logging
│   ├── reporter.py       # Gerador de relatórios
│   └── validator.py      # Validação de entrada
│
├── wordlists/            # Wordlists padrão
│   ├── common_passwords.txt
│   ├── rockyou.txt.gz
│   └── custom/
│
├── rainbow_tables/       # Rainbow tables
│   └── README.md
│
├── docs/                 # Documentação
│   ├── api.md
│   ├── examples.md
│   └── legal.md
│
└── tests/                # Testes unitários
    ├── test_hash_cracker.py
    ├── test_network.py
    └── test_integration.py
```


<div align="center">

### ⚠️ **USO RESPONSÁVEL É FUNDAMENTAL** ⚠️

**Conhecimento é poder, e com grande poder vem grande responsabilidade**

</div>
