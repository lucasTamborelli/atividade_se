# Banco XYZ (Padrão Command) — CSI-22

Lucas Guedes Tamborelli

Interação entre a aplicação cliente e a aplicação do Banco XYZ, usando o padrão de projeto **Command** e interface tkinter


## ARQUITETURA:
```
atividade_se/
├── main.py       # 
├── gui.py        # interface + histórico
├── commands.py   # padrão Command
├── bank.py       # regras (Bank e Account)
├── db.py         # acesso ao sqlite
└── xyz.db        # banco na root
```


(i) Funcionamento do Command:

```
GUI -> Command -> Bank -> Database
```

Cada botão da GUI cria um comando e chama `execute()`. Quem fala com o `Bank` é o comando (não GUI).
Todo comando realizado entra no histórico.


**Como Executar**
```bash
cd atividade_se
python main.py
```


## Banco de dados
SQLite: `xyz.db`, que é criado na primeira execução já com 3 contas para testarmos o funcionamento:

| Conta | Titular | Saldo inicial |
|-------|---------|---------------|
| 1     | pessoa1 | 100.00        |
| 2     | pessoa2 | 200.00        |
| 3     | pessoa3 | 300.00        |

Para voltar aos iniciais, é só apagar o `xyz.db`.
