# Datasets Compartilhados

Datasets utilizados nas aulas e exercícios da turma. Todos os arquivos aqui são de uso livre para fins educacionais.

---

## Regras para contribuição

| Critério | Regra |
|----------|-------|
| **Tamanho** | Até **50 MB** direto no repositório; arquivos maiores via link externo |
| **Formatos aceitos** | `.csv`, `.json`, `.xlsx` |
| **Formatos ignorados** | `.zip`, `.gz`, `.parquet` (listados no `.gitignore`) |
| **Fonte** | Sempre documentar a origem do dado na tabela abaixo |
| **Privacidade** | Nunca adicionar dados pessoais ou sensíveis sem anonimização |

---

## Datasets Disponíveis

| Arquivo | Descrição | Fonte | Adicionado por |
|---------|-----------|-------|----------------|
| `base_rh.csv` | Dataset de RH fictício com funcionários, departamentos, salários, cargos e datas de admissão — utilizado nas aulas de manipulação de dados | Criado para o curso | Professor |

---

## Como adicionar um dataset

```bash
# 1. Copie o arquivo para esta pasta
cp meu_dataset.csv datasets/

# 2. Atualize a tabela acima com nome, descrição e fonte

# 3. Commit com o prefixo "data"
git add datasets/meu_dataset.csv datasets/README.md
git commit -m "data: adiciona dataset nome_do_dado"
git push origin master
```

Depois, abra um **Pull Request** para que o professor revise antes de mesclar.

---

## Fontes recomendadas de dados públicos

| Portal | URL | Tipo de dados |
|--------|-----|---------------|
| IBGE | [ibge.gov.br](https://www.ibge.gov.br) | Demográficos, econômicos, sociais |
| Portal Brasileiro de Dados Abertos | [dados.gov.br](https://dados.gov.br) | Governamentais diversos |
| Kaggle | [kaggle.com/datasets](https://www.kaggle.com/datasets) | ML, negócios, esportes, ciências |
| INEP | [inep.gov.br](https://www.inep.gov.br) | Educação |
| ANS | [ans.gov.br](https://www.ans.gov.br) | Saúde suplementar |

> Sempre verifique a licença do dataset antes de usá-lo ou redistribuí-lo.
