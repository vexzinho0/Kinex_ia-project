# Kinex IA

Base inicial da Kinex IA, construída em Python.

## Objetivo

Criar uma IA própria com um núcleo de modelo independente e uma arquitetura modular para pesquisa, memória, aprendizado validado e ferramentas externas.

## Módulos planejados

- Modelo próprio
- Memória persistente
- Pesquisa e coleta de conhecimento
- Validação de conhecimento
- Blender para geração/manipulação 3D
- Codex para tarefas de programação
- Geração de imagens
- Geração de vídeos
- Conexões com serviços externos
- Aprendizado sobre ferramentas conectadas

## Executar localmente

```bash
pip install -r requirements.txt
python app.py
```

A API ficará disponível em `http://localhost:5000`.

### Endpoints iniciais

- `GET /` status da aplicação
- `GET /health` health check
- `POST /api/chat` conversa com o núcleo

Exemplo de requisição:

```json
{"message":"Olá, Kinex IA"}
```
