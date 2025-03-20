# Qualidade de Software

### 1. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 2. Acessar o ambiente virtual
 - #### para ambientes ruindows

```bash
.venv\Scripts\activate
```

- #### para ambientes unix

```bash
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar os testes

```bash
pytest
```

### Para rodar os testes completos

- #### para testes completos use a flag `-v`

```bash
pytest -v
```
