# Discord Bot 🤖

Um bot personalizável para Discord, desenvolvido para automatizar tarefas, gerenciar comunidades e adicionar comandos interativos.

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Uma aplicação Discord criada no [Discord Developer Portal](https://discord.com/developers/applications)

## 🚀 Configuração

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd Discord_bot
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente
1. Copie o arquivo de exemplo:
   ```bash
   cp .env.example .env
   ```

2. Edite o arquivo `.env` e adicione seu token do bot:
   ```
   BOT_TOKEN=seu_token_aqui
   ```

### 4. Como obter o token do bot
1. Acesse o [Discord Developer Portal](https://discord.com/developers/applications)
2. Clique em "New Application" e dê um nome ao seu bot
3. Vá para a aba "Bot" no menu lateral
4. Clique em "Add Bot"
5. Na seção "Token", clique em "Copy" para copiar o token
6. Cole o token no arquivo `.env`

### 5. Execute o bot
```bash
python main.py
```

## 🔧 Configurações Opcionais

No arquivo `.env`, você pode configurar:
- `BOT_TOKEN`: Token do seu bot Discord (obrigatório)
- `COMMAND_PREFIX`: Prefixo dos comandos (padrão: '.')

## 📝 Comandos

O bot usa o prefixo `.` por padrão. Exemplo:
- `.help` - Mostra os comandos disponíveis

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
