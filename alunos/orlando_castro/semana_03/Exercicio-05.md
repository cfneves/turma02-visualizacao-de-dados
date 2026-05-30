## EXEMPLO 5: USANDO GITHUB DESKTOP (INTERFACE GRÁFICA)


**Nível: Médio-Alto***
O que vamos fazer:
Fazer tudo que fizemos nos exemplos anteriores, mas usando a interface visual do GitHub Desktop (sem comandos).


**Passo a passo:**

Abra o GitHub Desktop
Adicione seu repositório local:

Clique em "File" → "Add local repository"
Clique em "Choose..." e selecione a pasta meu-primeiro-repo
Clique em "Add repository"

**Você vai ver:**

No centro: lista de arquivos modificados
À direita: preview das mudanças (o que adicionou/removeu)
Embaixo: campo para escrever mensagem de commit

**Crie um novo arquivo de teste:**

No explorador de arquivos, abra a pasta meu-primeiro-repo
Crie um arquivo chamado teste.txt
Escreva dentro: Arquivo criado pelo GitHub Desktop
Salve

**Volte para o GitHub Desktop:**

Ele detecta automaticamente que você criou um arquivo novo
O arquivo aparece na lista com uma marcação verde (novo)

**Faça o commit:**

No campo "Summary", escreva: Adicionado arquivo de teste
(Opcional) No campo "Description", você pode dar mais detalhes
Clique no botão azul "Commit to main"
Pronto! Commit feito sem digitar nenhum comando!

**Envie para o GitHub:**

No topo, vai aparecer um botão "Push origin"
Clique nele
Seu código foi enviado para o GitHub!

**Crie uma branch pela interface:**

No topo, onde está escrito "Current branch: main", clique
Clique em "New branch"
Nome: feature/arquivo-teste
Clique em "Create branch"
Automaticamente você já está nessa nova branch

**Edite o arquivo de teste:**

Abra teste.txt
Adicione uma linha: Editado na branch feature
Salve

**Commit na nova branch:**

GitHub Desktop detecta a mudança
Escreva a mensagem: Editado arquivo de teste
Clique em "Commit to feature/arquivo-teste"

**Junte com a main:**

No topo, clique em "Current branch"
Selecione "main" para voltar à branch principal
Clique em "Branch" (menu superior) → "Merge into current branch"
Selecione "feature/arquivo-teste"
Clique em "Create a merge commit"
Pronto! As branches foram mescladas!

**Envie tudo para o GitHub:**

Clique em "Push origin"
