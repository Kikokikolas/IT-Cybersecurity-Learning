# SSH moderno — Resumo de estudo de SIO

**Disciplina:** Segurança nas Organizações e Informática (SIO)  
**Data de revisão:** 26 de novembro de 2026

Este resumo acompanha uma ligação SSH com **Ed25519 para autenticação**, **X25519 para Key Exchange** e **AES-GCM para proteção do tráfego**. São funções distintas: a chave que prova uma identidade não é a chave que cifra os comandos.

O exemplo não representa todos os algoritmos possíveis. Versões recentes do OpenSSH também negoceiam Key Exchange híbrido pós-quântico, como `mlkem768x25519-sha256`. X25519 isoladamente continua a ser útil para compreender ECDHE, mas não oferece segurança contra um computador quântico suficientemente poderoso. [OpenSSH: Post-Quantum Cryptography](https://www.openssh.com/pq.html).

## 1. SSH — Secure Shell

SSH permite executar comandos, transferir ficheiros e criar túneis através de uma rede não fiável. A porta TCP habitual é a **22**.

| Objetivo | O que protege | Mecanismo no exemplo |
| --- | --- | --- |
| Confidencialidade | Impede a leitura do conteúdo por observadores da rede. | Encryption com AES-GCM. |
| Integridade | Permite detetar alterações não autorizadas. | Authentication Tag do AEAD. |
| Autenticação do servidor | Confirma a posse da Host Key esperada. | Assinatura do Key Exchange e validação da Host Key. |
| Autenticação do utilizador | Prova a posse de uma credencial autorizada para uma conta. | Assinatura com a chave privada do utilizador. |

**SSH possui o seu próprio protocolo de transporte seguro e não depende de TLS.** A arquitetura separa transporte seguro, autenticação do utilizador e canais lógicos, como shell e forwarding. [RFC 4251 — Arquitetura SSH](https://www.rfc-editor.org/rfc/rfc4251.html).

### SSH e TLS

| Aspeto | SSH | TLS |
| --- | --- | --- |
| Utilização habitual | Administração remota, SFTP e túneis. | Proteção de protocolos de aplicação, como HTTP em HTTPS. |
| Transporte seguro | SSH Transport Layer Protocol. | TLS Record Protocol e handshake TLS. |
| Confiança no servidor | Frequentemente Host Key guardada, TOFU ou SSH CA. | Frequentemente certificado X.509 validado por uma CA; existem outras modalidades. |
| Identificação do utilizador | Protocolo SSH de autenticação, normalmente antes de abrir a shell. | Pode usar client certificates; muitas aplicações autenticam depois, ao nível aplicacional. |
| Primitivas | Pode usar curvas elípticas, AES e ChaCha20. | Pode usar as mesmas famílias, com mensagens e derivação diferentes. |

Partilhar algoritmos não torna os protocolos intercambiáveis. TLS 1.3 também suporta Key Exchange efémero; Forward Secrecy não é exclusiva de SSH. [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446.html).

## 2. Ed25519 — Digital Signature

### 2.1. Geração e relação com EdDSA

**Ed25519** é uma instanciação de **EdDSA (Edwards-curve Digital Signature Algorithm)** sobre uma curva elíptica na forma twisted Edwards. Serve para assinar e verificar, não para cifrar o tráfego nem para realizar X25519.

```bash
ssh-keygen -t ed25519
```

Por omissão, o comando propõe `~/.ssh/id_ed25519` para a chave privada e `~/.ssh/id_ed25519.pub` para a pública. Uma passphrase protege o ficheiro privado em repouso; não é a origem matemática da identidade Ed25519. O comando é um exemplo de estudo, não foi executado para criar chaves neste repositório. [Manual de ssh-keygen](https://man.openbsd.org/ssh-keygen).

A geração utiliza um **CSPRNG — Cryptographically Secure Pseudorandom Number Generator**, sustentado por entropia adequada do sistema. Um gerador previsível comprometeria as chaves, mesmo com algoritmos fortes. [RFC 4086 — Randomness](https://www.rfc-editor.org/rfc/rfc4086.html).

### 2.2. Da seed à chave pública

O processo Ed25519 parte de uma **seed aleatória de 32 bytes, ou 256 bits**:

1. Calcula `SHA-512(seed)`, obtendo 64 bytes.
2. Ajusta determinados bits da primeira metade, num processo chamado pruning, para obter o escalar privado `a`.
3. Conserva a segunda metade como material utilizado na geração determinística das assinaturas.
4. Calcula o ponto público `A = aG` e codifica-o em 32 bytes.

`G` é um ponto base público; `aG` significa **scalar multiplication**, não multiplicação das coordenadas como números comuns. A seed, o escalar e o ficheiro privado são representações diferentes de material privado relacionado.

É eficiente obter `A` a partir de `a`. Recuperar `a` a partir de `A` e `G` corresponde ao **Elliptic Curve Discrete Logarithm Problem (ECDLP)**, considerado inviável com parâmetros adequados e métodos clássicos conhecidos. Uma seed de 256 bits não implica 256 bits de segurança contra todos os ataques; Ed25519 oferece aproximadamente 128 bits de segurança clássica. [RFC 8032, secção 5.1](https://www.rfc-editor.org/rfc/rfc8032.html#section-5.1).

### 2.3. Assinar e verificar

```text
Assinatura:  σ = Sign(chave_privada, mensagem)
Verificação: Verify(chave_pública, mensagem, σ) → válida ou inválida
```

A chave privada nunca precisa de ser enviada. A assinatura demonstra posse do material privado e liga essa prova à mensagem; não esconde a mensagem. Ed25519 usa SHA-512 internamente, mas não deve ser reduzido à instrução genérica “cifrar um hash com a chave privada”. O identificador SSH é `ssh-ed25519`. [RFC 8709 — Ed25519 no SSH](https://www.rfc-editor.org/rfc/rfc8709.html).

### 2.4. Chaves do utilizador e Host Keys

| Elemento | Onde fica normalmente | Finalidade |
| --- | --- | --- |
| Chave privada do utilizador | Cliente, por exemplo `~/.ssh/id_ed25519`. | Assinar o pedido de autenticação. |
| Chave pública do utilizador | Servidor, em `~/.ssh/authorized_keys` da conta de destino. | Identificar credenciais autorizadas para essa conta. |
| Host Key privada | Servidor, por exemplo `/etc/ssh/ssh_host_ed25519_key`. | Assinar o Key Exchange. |
| Host Key pública conhecida | Cliente, em `~/.ssh/known_hosts`. | Associar o servidor à chave esperada. |

Estes pares são **independentes**, mesmo quando ambos usam Ed25519. `authorized_keys` responde a “quem pode entrar nesta conta?”; `known_hosts` a “que chave espero deste servidor?”. Existem alternativas, incluindo certificados SSH e configurações de localização diferentes. [Manual de sshd](https://man.openbsd.org/sshd).

São chaves de **longo prazo** porque mantêm a continuidade da identidade e das autorizações entre ligações. Não precisam de ser recriadas a cada login, mas devem poder ser substituídas e revogadas. “Longo prazo” não significa “eterna”.

## 3. Challenge-Response e Replay Attacks

### 3.1. Modelo tradicional com nonce

Um **nonce** é um valor usado uma única vez. Num Challenge-Response simples:

1. O servidor gera um nonce novo e imprevisível e envia-o ao cliente.
2. O cliente assina o nonce com a sua chave privada.
3. O servidor verifica a assinatura com a chave pública autorizada.
4. O servidor associa a resposta ao desafio pendente e invalida-o depois da utilização.

Uma assinatura capturada para `nonce₁` não valida `nonce₂`. Esta frescura, juntamente com a gestão correta do desafio, impede a reutilização da resposta num **Replay Attack**. Num protocolo real, também se deve ligar a assinatura ao contexto para evitar reutilizações entre finalidades diferentes.

### 3.2. O que o SSH efetivamente assina

No método SSH `publickey`, não se trata simplesmente de assinar um nonce separado enviado pelo servidor. A assinatura inclui o **Session ID** e os campos do pedido:

```text
Session ID
SSH_MSG_USERAUTH_REQUEST
username + service name + "publickey" + TRUE
public key algorithm + public key
```

O servidor verifica tanto a autorização da chave como a assinatura. O Session ID liga a prova à ligação: transportar uma assinatura antiga para outra ligação não produz um pedido válido. Uma consulta opcional sobre a aceitação da chave pode preceder o pedido assinado; não é o nonce de um Challenge-Response tradicional. [RFC 4252, secção 7](https://www.rfc-editor.org/rfc/rfc4252.html#section-7).

## 4. ECDH e X25519 — Key Exchange

### 4.1. Ed25519 não é X25519

| Aspeto | Ed25519 | X25519 |
| --- | --- | --- |
| Função | Digital Signature. | Acordo de segredo partilhado. |
| Operação | Assinar e verificar. | Combinar material privado local com chave pública remota. |
| Curva e representação | Edwards; chave pública codifica um ponto. | Montgomery; interface baseada na coordenada `u`. |
| Uso neste exemplo | Identidades de longo prazo. | Pares efémeros de cada Key Exchange. |

As construções são matematicamente relacionadas, mas não são o mesmo algoritmo nem justificam reutilizar as mesmas chaves para os dois fins. X25519 é definido no [RFC 7748](https://www.rfc-editor.org/rfc/rfc7748.html).

### 4.2. Simplificação pedagógica do ECDH

Cada nova ligação do exemplo gera automaticamente pares temporários e independentes:

| Operação | Cliente | Servidor |
| --- | --- | --- |
| Escolher escalar privado | `a`, mantido secreto. | `b`, mantido secreto. |
| Calcular chave pública | `A = aG`. | `B = bG`. |
| Trocar apenas valores públicos | Envia `A`; recebe `B`. | Envia `B`; recebe `A`. |
| Calcular segredo | `K = aB`. | `K = bA`. |

```text
Cliente:  K = aB = a(bG) = abG
Servidor: K = bA = b(aG) = abG
```

**Esta notação é uma simplificação pedagógica.** Aqui `K` representa um ponto partilhado abstrato. X25519 calcula uma saída de 32 bytes a partir de escalares e coordenadas `u`; SSH converte-a segundo as regras do algoritmo negociado. Estes `a` e `b` não são os escalares Ed25519 da secção anterior.

Ambos chegam ao mesmo resultado localmente. **O segredo partilhado não é enviado pela rede.** Observar `A`, `B` e os parâmetros públicos não permite calculá-lo eficientemente sob as hipóteses criptográficas adotadas. No SSH, `curve25519-sha256` usa X25519 e SHA-256. [RFC 8731](https://www.rfc-editor.org/rfc/rfc8731.html).

### 4.3. ECDH, ECDHE e autenticação

**ECDH** designa o mecanismo geral, que pode usar chaves estáticas ou temporárias. **ECDHE** explicita a variante ephemeral: novos pares para cada troca. O ECDH usado no cenário SSH é efémero, mesmo que o nome negociado não contenha a letra “E”.

ECDH sozinho não identifica o interlocutor: um atacante ativo poderia interpor trocas separadas. A assinatura do servidor sobre o Exchange Hash, combinada com a validação da Host Key, autentica a troca. [RFC 5656, secção 4](https://www.rfc-editor.org/rfc/rfc5656.html#section-4).

## 5. Key Derivation Function — KDF

### 5.1. Três entradas distintas

| Valor | Significado |
| --- | --- |
| `K` — Shared Secret | Segredo obtido pelo Key Exchange. |
| `H` — Exchange Hash | Hash que liga identificações, negociação, Host Key, valores públicos efémeros e `K`. |
| `session_id` | Primeiro `H` da ligação; mantém-se nos rekeyings. |

O Shared Secret **não é utilizado diretamente como chave AES**. A KDF de transporte SSH é uma construção baseada no hash do Key Exchange; não se deve assumir que é o HKDF de TLS 1.3.

### 5.2. Separação por finalidade e sentido

A derivação clássica usa `HASH(K || H || etiqueta || session_id)`:

| Etiqueta | Material derivado |
| --- | --- |
| `A` | IV inicial: cliente → servidor. |
| `B` | IV inicial: servidor → cliente. |
| `C` | Chave de Encryption: cliente → servidor. |
| `D` | Chave de Encryption: servidor → cliente. |
| `E` | Chave de integridade: cliente → servidor, quando necessária. |
| `F` | Chave de integridade: servidor → cliente, quando necessária. |

`||` representa concatenação com as codificações SSH exigidas. O resultado é truncado ou expandido até ao comprimento necessário. IVs, nonces e chaves de integridade usados efetivamente dependem do cipher. [RFC 4253, secção 7.2](https://www.rfc-editor.org/rfc/rfc4253.html#section-7.2).

**As chaves AES não são derivadas da chave privada Ed25519.** O material secreto vem do Key Exchange. A Host Key pública participa no contexto autenticado, mas a chave privada de assinatura não se transforma num segredo de Encryption.

Exemplo: o cliente cifra com `key_C→S`; o servidor usa essa mesma chave para decifrar. Na resposta, ambos utilizam outra, `key_S→C`. Nenhuma precisa de ser enviada.

## 6. Encryption e Integrity

### 6.1. Conceitos

| Conceito | Resultado | O que não garante isoladamente |
| --- | --- | --- |
| Encryption | Plaintext transforma-se em ciphertext. | Deteção de todas as alterações. |
| MAC | Tag calculada com uma chave simétrica. | Confidencialidade ou prova pública de autoria. |
| AEAD | Ciphertext e Authentication Tag; pode autenticar Associated Data não cifrados. | Confiança inicial na identidade sem autenticação do Key Exchange. |

Um hash sem chave não substitui um MAC: quem altera dados também pode recalcular esse hash.

### 6.2. Opções de proteção

| Construção | Encryption | Integridade | HMAC separado? |
| --- | --- | --- | --- |
| AES-CTR + HMAC | AES em Counter Mode. | HMAC, por exemplo com SHA-256. | Sim. |
| AES-GCM | AES em Galois/Counter Mode. | Authentication Tag integrada no GCM. | Não. |
| ChaCha20-Poly1305 | Stream cipher ChaCha20. | Poly1305. | Não. |

**AES-CTR** precisa de proteção de integridade adicional: modificar ciphertext pode provocar alterações no plaintext. O MAC é uma escolha separada; implementações OpenSSH também oferecem variantes Encrypt-then-MAC, identificadas por `-etm@openssh.com`. A ordem concreta depende do algoritmo negociado. [RFC 4344 — CTR](https://www.rfc-editor.org/rfc/rfc4344.html), [RFC 6668 — HMAC-SHA-2](https://www.rfc-editor.org/rfc/rfc6668.html).

**AES-GCM** integra autenticação e Encryption. A tag permite rejeitar dados alterados, pelo que acrescentar outro HMAC não faz parte desta construção SSH. Os nonces têm de respeitar as regras de unicidade para cada chave. [RFC 5647 — AES-GCM no SSH](https://www.rfc-editor.org/rfc/rfc5647.html).

**`chacha20-poly1305@openssh.com`** também dispensa HMAC separado. A variante SSH não é byte a byte a construção de TLS: utiliza dois conjuntos de 256 bits por sentido, incluindo proteção do comprimento do pacote, e deriva uma chave Poly1305 por pacote. [Especificação OpenSSH](https://raw.githubusercontent.com/openssh/openssh-portable/V_9_9_P2/PROTOCOL.chacha20poly1305).

```text
AEAD_Encrypt(chave, nonce, plaintext, associated_data)
    → ciphertext + authentication_tag

AEAD_Decrypt(...) → plaintext autenticado OU falha
```

A aplicação não deve aceitar conteúdo cuja autenticação falhou. MAC e AEAD autenticam dados com segredos simétricos; não substituem a assinatura de identidade Ed25519.

### 6.3. Rekeying

Uma ligação longa pode realizar novo Key Exchange sem fechar a shell. No cenário ECDHE, gera novos pares temporários, um novo segredo e novas chaves de tráfego. Os limites dependem de dados transmitidos, tempo, algoritmos e configuração.

O **Session ID original permanece**; o novo Exchange Hash muda. Chaves de tráfego duram até ao rekeying ou ao fim da ligação, não necessariamente durante toda a sessão interativa. [RFC 4253, secção 9](https://www.rfc-editor.org/rfc/rfc4253.html#section-9).

## 7. Perfect Forward Secrecy — PFS

### 7.1. O que significa

PFS protege a confidencialidade das ligações anteriores perante um **comprometimento posterior das chaves de longo prazo**. Depende de segredos efémeros independentes, eliminação do material antigo e segurança dos algoritmos e implementações.

Não significa que os dados guardados nos equipamentos ficam protegidos contra quem obtém acesso a esses equipamentos.

### 7.2. Três ligações em dias diferentes

Suponhamos que Ana usa sempre a mesma chave privada Ed25519 para entrar num servidor e que todas as ligações negoceiam X25519 e AES-GCM:

| Ligação | Autenticação de Ana | Pares X25519 temporários | Shared Secret | Chaves AES por sentido |
| --- | --- | --- | --- | --- |
| Dia 1 | `Ed_Ana` | `(a₁,A₁)` e `(b₁,B₁)` | `K₁` | `AES₁_C→S`, `AES₁_S→C` |
| Dia 2 | `Ed_Ana` | `(a₂,A₂)` e `(b₂,B₂)` | `K₂` | `AES₂_C→S`, `AES₂_S→C` |
| Dia 3 | `Ed_Ana` | `(a₃,A₃)` e `(b₃,B₃)` | `K₃` | `AES₃_C→S`, `AES₃_S→C` |

Os pares são gerados novamente; os segredos e chaves resultantes são diferentes com probabilidade esmagadora. A Host Key do servidor também pode manter-se durante os três dias.

Um atacante grava todo o tráfego, incluindo valores públicos de Key Exchange e ciphertext. No dia 4, rouba uma cópia **utilizável** da chave privada Ed25519 de Ana.

| Ação do atacante | Resultado e condições |
| --- | --- |
| Autenticar-se como Ana | Pode fazê-lo enquanto a chave continuar autorizada, o acesso for permitido e não existirem outros fatores exigidos. |
| Ler ficheiros e históricos no servidor | Pode aceder ao que a conta tiver permissão para ler, incluindo logs ou históricos que realmente existam. |
| Recuperar `a₁`, `b₁` ou `K₁` apenas a partir de `Ed_Ana` | Não: são materiais independentes. |
| Decifrar as gravações dos dias 1–3 | Não apenas com `Ed_Ana`, assumindo eliminação dos segredos temporários e mecanismos seguros. |
| Ler plaintext já guardado num ficheiro | PFS não o impede; isso é acesso a dados em repouso, não decifragem da captura antiga. |

A chave Ed25519 permite criar **novas assinaturas**. Não fornece as antigas chaves X25519 nem as chaves AES derivadas dessas trocas. Uma cópia do ficheiro privado ainda protegida por passphrase não equivale necessariamente a uma chave imediatamente utilizável.

Se o atacante também tiver copiado chaves de sessão da memória, segredos efémeros ou plaintext, a hipótese muda. A revogação da chave de Ana impede autenticações futuras com essa credencial; não apaga ficheiros já lidos.

### 7.3. Contraste: RSA Key Transport sem Forward Secrecy

Considere um sistema em que o cliente gera um segredo `Sᵢ` para cada sessão e envia `Encrypt(RSA_public_permanente, Sᵢ)`. As chaves simétricas são derivadas de `Sᵢ`.

Se o atacante gravar estes valores e depois roubar a **chave RSA privada do destinatário**, consegue recuperar cada `Sᵢ` e reconstruir as chaves antigas. A comparação usa o papel de Key Transport, não uma chave de assinatura. Este modelo existiu no TLS com RSA Key Exchange. [RFC 5246, secção 7.4.7.1](https://www.rfc-editor.org/rfc/rfc5246.html#section-7.4.7.1).

| Propriedade | ECDHE autenticado | Segredo cifrado com RSA permanente |
| --- | --- | --- |
| Novas chaves simétricas por sessão | Sim. | Também pode ter. |
| Compromisso da chave permanente recupera segredos antigos? | Não, sob as hipóteses de PFS. | Sim, se existirem as mensagens gravadas necessárias. |
| Forward Secrecy | Sim, quando corretamente implementado. | Não neste modelo. |

**Chaves diferentes por sessão não bastam: as chaves antigas têm de permanecer irrecuperáveis a partir da chave permanente comprometida.**

Usar **RSA para assinar um Key Exchange efémero** é outra situação: não elimina PFS por si só. O problema do exemplo é cifrar o segredo para uma chave RSA permanente.

## 8. Funcionamento completo de uma ligação SSH

O diagrama mostra uma execução simplificada de SSH com X25519 e autenticação por chave pública. Omite mensagens opcionais e detalhes de codificação.

```mermaid
sequenceDiagram
    autonumber
    participant C as Cliente SSH
    participant S as Servidor SSH
    C->>S: TCP Connection, normalmente porta 22
    C->>S: Identificação de versão SSH
    S->>C: Identificação de versão SSH
    C->>S: SSH_MSG_KEXINIT, algoritmos suportados
    S->>C: SSH_MSG_KEXINIT, algoritmos suportados
    Note over C,S: Algorithm Negotiation, exemplo X25519 + Ed25519 + AES-GCM
    C->>C: Gera par X25519 temporário a, A
    S->>S: Gera par X25519 temporário b, B
    C->>S: SSH_MSG_KEX_ECDH_INIT, valor público A
    S->>S: Calcula Shared Secret K e Exchange Hash H
    S->>S: Assina H com a Host Key privada
    S->>C: SSH_MSG_KEX_ECDH_REPLY, Host Key pública, B e assinatura
    C->>C: Calcula o mesmo K e H
    C->>C: Verifica assinatura e confiança na Host Key
    Note over C: known_hosts ou CA; no primeiro contacto, TOFU com fingerprint verificada
    Note over C,S: Session ID = primeiro H; falhas de validação interrompem a ligação
    C->>C: KDF gera chaves e parâmetros por sentido
    S->>S: KDF gera os mesmos materiais por sentido
    C->>S: SSH_MSG_NEWKEYS
    S->>C: SSH_MSG_NEWKEYS
    Note over C,S: Canal cifrado ativo em ambos os sentidos
    C->>S: Pedido do serviço ssh-userauth, já protegido
    S->>C: Aceitação do serviço, já protegida
    C->>C: Assina Session ID e pedido com Ed25519 do utilizador
    C->>S: SSH_MSG_USERAUTH_REQUEST com assinatura, cifrado
    S->>S: Verifica authorized_keys, assinatura e política de acesso
    S->>C: SSH_MSG_USERAUTH_SUCCESS, se os requisitos estiverem satisfeitos
    C->>S: Abre canal e pede shell ou execução de comando
    S->>C: Confirmação protegida
    Note over C,S: Comandos e respostas protegidos por criptografia simétrica
```

### Duas verificações diferentes do servidor

- **Assinatura válida:** quem respondeu possui a chave privada correspondente à Host Key apresentada.
- **Host Key de confiança:** essa chave pertence ao servidor a que se pretendia aceder.

Uma assinatura válida de uma chave arbitrária não basta. No **TOFU — Trust On First Use**, o cliente guarda a chave aceite no primeiro contacto e deteta mudanças posteriores. Para proteger também esse primeiro contacto, confirma-se a fingerprint por um canal independente ou utiliza-se confiança previamente configurada. Aceitar uma chave desconhecida sem validação deixa esse momento exposto a Man-in-the-Middle.

**O canal já está cifrado antes da autenticação do utilizador.** Cada emissor ativa as novas chaves depois de enviar `NEWKEYS`, e o recetor depois de receber essa mensagem. O servidor já demonstrou a sua identidade; ainda falta decidir se o utilizador pode entrar. A aceitação criptográfica da credencial pode continuar sujeita a MFA e outras políticas.

## 9. Tabela comparativa dos componentes

| Componente | Finalidade | Tipo de criptografia | Origem das chaves | Duração neste exemplo | Propriedades de segurança |
| --- | --- | --- | --- | --- | --- |
| Ed25519 | Assinar a troca ou o pedido de autenticação. | Assimétrica, Digital Signature. | Seed aleatória gerada com CSPRNG; SHA-512 e derivação na curva. | Longo prazo, até rotação ou revogação. | Autenticidade e integridade da mensagem assinada; não cifra dados. |
| X25519 | Obter um Shared Secret. | Assimétrica, Key Agreement. | Material privado aleatório novo em cada extremo. | Um Key Exchange; novos pares no rekeying. | Acordo de segredo; suporta PFS quando efémero e autenticado. Não identifica sozinho o interlocutor. |
| AES-GCM | Proteger pacotes. | Simétrica, AEAD. | KDF a partir do Shared Secret e contexto SSH. | Até rekeying ou fim da ligação, por sentido. | Confidencialidade e integridade; exige nonces corretamente geridos. |
| HMAC | Autenticar pacotes quando usado com um cipher como AES-CTR. | MAC simétrico baseado em hash. | Chaves de integridade derivadas pela KDF. | Até rekeying ou fim da ligação, por sentido. | Integridade e autenticidade entre detentores do segredo; não cifra nem fornece prova pública de autoria. |
| KDF | Produzir material separado para cada utilização. | Derivação criptográfica baseada em hash; não é um cipher. | Recebe `K`, `H`, Session ID e etiquetas. | Executada por Key Exchange; saídas usadas no respetivo período. | Separação de chaves e ligação ao contexto; não cria entropia a partir do nada. |

## 10. Revisão rápida para SIO

1. **Quem autentica?** Ed25519, com pares independentes para servidor e utilizador.
2. **Quem estabelece o segredo?** X25519 no exemplo.
3. **Quem cria as chaves de tráfego?** A KDF, não a chave privada Ed25519.
4. **Quem protege os comandos?** Criptografia simétrica: AES-GCM, ChaCha20-Poly1305 ou cipher com MAC adequado.
5. **O que impede repetir a assinatura de outro login?** A ligação da assinatura ao Session ID e ao pedido.
6. **O que permite PFS?** Segredos efémeros que não são recuperáveis através das chaves permanentes, com eliminação segura do material antigo.
7. **O que PFS não protege?** Ficheiros, históricos e plaintext acessíveis num equipamento comprometido.
8. **Quando é autenticado o utilizador?** Depois de estabelecido o transporte cifrado e autenticado o servidor.

```text
Ed25519 → provar identidade
X25519 → estabelecer segredo
KDF → derivar chaves separadas
AES-GCM / ChaCha20-Poly1305 → proteger tráfego
```
