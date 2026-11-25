# (19/05) Blueprint de personagem e avatars no Heijin (AULA 11 - IA DAY - BLUEPRINT + HEYGEN) — transcrição do Loom

Fonte: Loom https://www.loom.com/share/2e91fb220b9848a892c482760a5e7c2b (1:27:03; mandado pelo aluno em 25/11/2026 ~01h00, a pedido meu: as aulas que o Clone cita e não tínhamos). Texto: a legenda automática do próprio Loom (português), baixada pela API pública do Loom e juntada em blocos de ~12 s com o tempo do começo de cada bloco; a transcrição do Loom vai até 1:24:42. Erros de reconhecimento de voz ficam como vieram.

0:00:00
<v 0>bem? Tranquilinhos? Happy?</v> Trabalhando? O que é a vida? A vida é uma coisa boa, né? Ah, sim, dá certo, mano, não dá tão certo assim quanto uma copia falada, mas dá certo. É uma maneira mais preguiçosa, né, de fazer, mas dá pra fazer. Onde está a aula 3.1?
0:00:18
No mapa mental, embaixo da aula 3. 100 a 200 de aposto a 10, mete marcha mano, mete marcha, tá suave, vamos esperar mais um pouquinho a rapaziada entrar, a rapaziada tá tímida pra aparecer né, terça-feira todo mundo querendo ver a copa, ninguém quer ver o Gugu, estão indo no mercado comprar cerveja deixa eu fechar meu mapa mental aqui pra não aparecer spoilers que hoje eu tô misterioso também hoje nóis tá misterioso já tá liberado?
0:00:59
o que? vai alterar o setup que a gente, vou alterar, posso alterar, só que temos um B agora que eu não tenho acesso direto para alterar, tá ligado? aí eu tenho que mandar para a galera e a galera altera eu faço alterações aqui, mando o negócio para eles e eles alteram lá, então pode ser que demore um pouquinho para ficar pronto lá, mas deixa eu anotar aqui, acabou a partida, roupa, então podemos Vamos começar Tô pensando até em botar, sei lá, 5 mil copies lá Pode?
0:01:33
Não, não é muita coisa Eu quero botar mais umas copies lá também Tem mais umas que tão escalando legal Mas vocês não podem se acostumar mal, mano, e usar só o copy de lá, tá ligado? Vocês tem que fazer as copies de vocês também, coloca os vídeos editados também. Vou botar, mano. Pra cada aluno que tá online hoje, vou botar 100 vídeos lá. Deixa eu coisar o fio aqui, né? Senão eu vou ficar me mutando.
0:02:03
Esperar mais um pouquinho a galera chegar. Galera não tá querendo vir, hein? Deixa eu avisar no Instagram. Eu avisei já ou não? Não. Mas só não foca mano Aí foca em cima, tu foca embaixo Aí, W não, não precisa de W não Consegue postar pra mim?
0:02:35
Então é claro mano Passa as contas aí, passa teu bagulho da App Aí eu boto lá no Minha conta bancária no Checkout Esse aqui é o iPhone do TikTok Shop Não é nem da Shoppee, mas, Marcar MVM, Reposta lá MVM! Alô, Luca! Coloca meu link aí nas suas páginas, é uma ideia melhor, né? É uma ideia melhor. Mano, estou percebendo aqui que vocês estão com bem menos dúvidas, né? Da parte estrutural. Isso é um bom sinal, isso é um bom sinal. O GPT está meio fraco, o João, para esse estilo de copies.
0:03:25
Notebook LM está desatualizado? Marco Luiz. Marco Luiz que ele vai ver e atualiza. 275. Cláudio? O cloudzinho tá muito bom pra copy, tá?
0:03:43
Eu tô pensando em trazer uns materiais pra vocês alimentarem um cloud. Mano, cloud free, não sei, nunca usei, mas acho que não muda muita coisa não. Mano, tá de boa entrega o Matheus, pode seguir.
0:04:04
Qual o tamanho de vídeo? Mano, cerca de 1 minuto, 50 e poucos segundos Tem alguns vídeos de 40 segundos que tão indo muito bem também, nesse pique aí Mano, o Cloud tá muito totoso, véi, muito totoso Pra tudo E o pratica-se?
0:04:50
Que isso? Como? Alguém vai animar aí, mano? Imagem proibida em 37 países, apaguei. Que frente é esse, cara?
0:05:19
Eu queria saber como você conseguiu matar o Soneu. Eu que te passei? Vou te bloquear, mano. Mano, no Cloud eu uso o último ópio sempre. Ele é mais caro, mas ele é muito bom. O Soneu eu usei algumas vezes, mas era bom também, velho. Não era ruim, não. Quais os critérios que você usa pra escolher uma conta? Mano, tá entregue, sei lá, 50 views ali, 10 vídeos, 50 views, eu jogo fora.
0:05:51
Bora começar? Bora começar o conteúdo? Sim ou não? Sim ou não? Sim? Vamos. Mano, hoje é coisinha bem, bem de boa, mas são, Mas são coisas que vai agregar muito bastante.
0:06:09
Bora, deixa eu botar minha telinha aqui, deixa eu trancar minha porta porque eu já tirei essa feira e daqui a pouco vem minha irmã aqui. Gu, quer comprar uma pizza pra mim? Eu vou falar não, ai vão falar nossa, que peste meu irmão Ai com a porta trancada ninguém vê eu sendo um mau irmão Pronto Deixa ela aparecer, vai tomar no teu cu moleque Se eu te vejo em São Paulo eu te mato filho Para ai cara, não, ninguém vai cuidar dela não Bora, rapaziada, eu fiz aqui um negocinho novo para vocês, deixa eu só pegar aqui no cloud porque ainda não foi upado, vou mostrar para vocês aqui.
0:07:01
Não era pra mim não, tinha gente com pedra no rinho aí que eu queria ajudar, pô. Aqui ó, nosso geradorzinho de Prompt, fiz algumas alterações nele, que foram sugestões de vocês, inclusive muito obrigado, ótimas sugestões. Quem tiver sugestões de alterações, vai mandando aí pra gente sempre, porque conforme dá tempo eu vou fazendo, tá ligado? Aqui, eu vou ensinar vocês a fazer o blueprintzinho do personagem, que é nesse pique aqui ó, nesse pique da titia que falaram ontem no Macau, aí eu falei pô, verdade né, vamos fazer isso aqui e vai ficar mais fácil de manter a consistência.
0:07:41
Aí, fazendo esse Blueprint aqui, a gente vem aqui, marca que já tem, e a gente altera só, tipo, o que o personagem vai estar fazendo, a expressão facial, as características aqui de fenótipo fica locada, tá ligado? E muda aí os acessórios, locais, tudo mais. Amaram ou não?
0:08:03
E também, pra quando a gente tá com muita preguiça ou com pouca criatividade, tem aqui ó, moleque, eu tava imersivo, tá? Tava muito imersivo, falei, caralho, vou falar que é o Taro que decide o nosso personagem. Aí cê vem aqui, ele vai literalmente aleatorizar tudo.
0:08:19
ó rola rola rola foda-se tá vendo aqui que tá mudando olha aí hum trolei aqui ó cometi um erro tá alterando o tipo de personagem tem que alterar tem que mexer tem que mexer calma como fazer esse blueprint será falado hoje na cal deixa eu até avisar os moleques que vão mexer não muda ainda, esqueci de alterar no negócio pai ta burro, pai ta burro porque que é bom esse blueprint? você vai entender, você vai entender Hum, boa, boa, Amanda. Nice. Gerador de hooks?
0:09:03
Ainda não. Hum, peraí. Só deixa eu anotar isso aqui pra não esquecer, guys. Aí fica muito bom depois. Fica uma hora pra decidir, isso mesmo. Hum, liberar, tipo de personagem, e gênero. Nice. Eu nem me liguei disso aqui na hora que eu tava fazendo. O que é Blueprint é como se fosse tipo um, um projeto ali, o bagulho dos arquitetos, sabe? A planta, essa porra aí, que basicamente é o nosso, essa porra aqui, ó. Vista frontal, vista lateral, vista com vista lateral esquerda, lateral direita, tá ligado?
0:09:44
Isso, isso é um Blueprint, um projetinho. Aí a gente vai criar o Blueprint do personagem, já marca aqui, aí ele vai manter alocado isso, vai falar no Prompt que é pra seguir esse padrão aqui, e aí lá na IA que a gente vai usar pra gerar imagem, a gente anexa essa imagem, entendeu? Pra isso serve um Blueprint.
0:10:12
Então, vamos lá. Primeira coisa que a gente vai fazer, vamos na central MVM aqui, não está conectado Abre ticket, aliado. Vem aqui no negócio da Appium. Aí a galera te ajuda.
0:10:31
Mano, é foda ficar olhando o perfil, viado. Não tem como ficar olhando o perfil um por um, não. Senão eu ficaria, 35 horas do dia só olhando conta da galera. Mas eu faço call de análise de vídeo. Aí nas call de análise de vídeo, você vai mandando os vídeos. Pode pá? Beleza. Vamos aqui no painel da Appium, gerador de prompts.
0:10:48
a gente vai primeiro gerar o nosso bonequinho né, aqui ele ainda não tá não tá mexido eu vou já gerar no novo, vou já gerar no novo aqui, vamos deixar o Taro desse jeito aqui, só vou até, eu não mexer aqui, vou até ele local ele cartomante, aí beleza. A gente vem, gera o Prompt, pegamos aqui, NanoBanana.
0:11:12
Primeira coisa tá, NanoBanana, Grok, GPT, o que vocês quiserem para criar esse Blueprint. Vou criar nos três aqui se vocês quiserem, vamos lá. Aí já fica mais uma aula mostrando como usa todos.
0:11:28
NanoBanana, copiei o print, o prompt, jogo aqui posso jogar aqui no grok também posso jogar aqui no gpt também Aí, isso aqui é só para eu ver o personagem inicial né, mas eu quero gerar o Blueprint dele.
0:11:48
Como que eu vou fazer para gerar esse Blueprint? Nosso grande amigo Claude nos ajuda. Conhecem o Claude? Esse fofucho? Se não conhecem o Claude, podem conhecer, está aqui no mapa mental, linkzinho dele.
0:12:04
Claude, vem aqui, faz o registro. Para gerar essa imagem aqui mano, não usou a minha pedra no que não é minha, eu tomo 6 litros d'água por dia. A gente vem, conversa com o Cloud, eu tenho ele instalado no PC, mas vocês podem usar no navegador de boa. E aí, eu já deixei os promptzinhos aqui que você vai mandar pra ele. Mano, é coisa simples, ó. Vem aqui, copia isso, manda aqui pra ele. Vou te mandar um prompt.
0:12:29
Quero manter a consistência do personagem. Me dê um prompt para criar um full view do personagem, nesse estilo aqui. Que estilo? Que estilo, Gustavo? Eu deixei aqui, ó, o estilo da imagem. É só vocês abrirem o link aqui e baixar o blueprint da senhorinha. Baixei aqui. Eu vou anexar no meu cloud aqui a senhora, espero fazer o upload.
0:13:01
Aí ele vai entender o que eu quero. Ele vai mandar um prompt aqui de maluco, mas eu não quero esse, mano. Calma, Claude, calma. Calma, seu psicopata.
0:13:16
Ele é afobado mesmo. Espera ele fazer aqui, aí o que a gente vai fazer? Eu vou mandar um calma aqui, porque ele foi afobado. Calma, filho. vou te mandar o prompt ainda não é é só pra você se basear no estilo Ele é meio lentinho as vezes, na porra do Opus.
0:13:46
Então o Benji Tokens, Ah filhote, não tá liso. Precisa, Bota mais aqui! Não precisa do Opus 47 pra fazer isso não, tá? Ih! Caí? Não. E aí, Caldinho? Vamos de novo.
0:14:12
Eu não uso tanto tanto ele não, o Pablo, então é suave. Vou até colocar aqui. Se ele mandar o prompt direto, fala para esperar, pede calma e envia o prompt gerado no nosso gerador.
0:14:36
Calma, vou te mandar o prompt correto. Cadê o nosso promptzinho aqui? Copia, joga para ele, aí ele vai fazer jeitoso. Vai se fuder, ô Claudio, porra, nem tá sensual. Toma de boa mulher, oh, ih, tá pelada Aparentemente o nosso gerador deu ele ultra hot, me fude também né, vamos fazer outro aqui Eu não vi que tava ultra hot Beleza cartomante, não me fala ela pelada não Beleza, tá de boa esse eu acho, vamos ver se esse aqui vai fazer, faz esse então.
0:15:37
Vamos ver esse aqui como é que sai. Acabou o limite? Acabou nada. Eu achei sensual. Mandei o mesmo? Não é possível.
0:16:01
Pô, irmão. Esqueci de clicar para gerar prompt, velho. Faz esse. Sou burro. Se eu já tiver uma influencer, aí você manda uma fotinho dela e pede para, Você manda uma fotinho do Claudio, tá ligado? Manda uma fotinho para o Claudio e pede para ele te dar um prompt para gerar o blueprint. e depois você pode jogar.
0:16:20
a tua personagem aqui no Flow ou na IA que você vai usar de criação de imagem, tá ligado? Geradora de imagem e manda o Prompt do Blueprint que o Cláudio gerou. Meu Deus, olha o cartomante que ele fez com uma taça de vinho na mão, meu amigo! O que? Que porra é essa? Isso aqui saiu feminino ou é feminino? Isso aqui saiu o que? Masculino!
0:16:56
Masculino é baita homem, mano! Caralho, bizarro. Enfim, vamos pegar aqui agora, copia, e agora mano, a gente vai jogar esse prompt que o Claudio nos deu, do nosso blueprint, na IA de gerar imagem.
0:17:23
Olha aí que beleza. o negócio não me ajuda olha que fácil velho olha que coisa mais simples de fazer velho é muito fácil fazer o blueprintzinho tá ligado Olha aí, tá lindo, né? Portanto, ele ficou absurdamente bom, cara.
0:17:58
Qual é, cara? Será que é aparente do covata? Como assim, velho? Foi esse cartomante que o Taro escolheu, isso mesmo, mano. É esse aqui, velho, que vai deixar a gente muito rico. Olha que beleza. Aí é só pegar uma imagenzinha do Blueprint aqui.
0:18:20
Vamos ver qual que ele ficou mais totoso. Essa aqui do Grock tá boa, mas tá meio massinha, não tá tão qualidade quanto eu gostaria. Vou pegar essa aqui em 4K. Os Iron Man. Mano, isso aqui vende, pô. Isso aqui vai vender, carai.
0:18:50
Mas olha, conteúdo da cal, saiu um bagulho engraçado, não era a intenção, tá ligado? Mas de conteúdo da cal, entenderam como fazer o Blueprint ou ficou óbvio? muito escaralhado, muito zoado, a forma de mostrar.
0:19:11
Não entenderam? Tá, vamos mostrar de novo. Vamos fazer algo sem ser escaralhado. O Taro não pode mais decidir, mano. O Taro não pode mais decidir. O Taro não pode mais decidir. Vamos mudar aqui, ó. Vamos escolher uma pessoa de 61 anos, pode ser homem, cartomante, ele é um mediterrâneo, bronzeado. com um sorriso provocante.
0:19:41
Ai, que delícia! O cabelo dele é de dread, prateado, não, castanho claro. Ele não está usando um corset de seda preta com decote velho, ele está usando um, Meu Deus, não tem roupa de homem aqui? É essa aqui, eu não sei o que é uma camiseta band vintage, mas parece coisa de homem.
0:19:58
Ele está usando uma, um cinto de couro. Tá de pé, junta a janela, com uma carta de tarô na mão, em um apartamento moderno minimalista, numa tarde chuvosa com reflexos.
0:20:20
Alô! luz foda-se meu deus, que que é isso, tão uns mel quentes eu gosto da primeira câmera, gosto do primeiro bagulho, primeiro, primeiro primeiro também, primeiro também gerar o prompt geramos o prompt, o que faremos agora? vamos para o nano banana clean, sem essa aberração aqui que vocês chamaram de aberração Então, não sou eu que estou chamando o novo projeto. Joga o prompt aqui, só pra ver o que vai sair, tá ligado? Vamos ver o que vai sair aqui.
0:21:06
Vai acabar meus créditos, mano. Eu cheguei falando que eu não tava liso. Mas suave. Puta que pariu. Ô, mano.
0:21:29
Ô, bagulho de próprio. Hoje tá muito gay, cara. Caralho, moleque. Não dá velho, caralho moleque, que barulho absurdo, pelo menos vocês se divertem nessa calva. Mano, vamos fazer isso aqui, homem, homem, homem, eu quero que ele esteja com um olhar Olha, calma e sábio, olha, calma e sábio, hum, um cabelo longo, não, mano, buzz cut é cor de homem, buzz cut, cabelo preto é cabelo de homem, ele não tá com uma camisa band vintage?
0:22:20
jaqueta de couro não roupa de homem místico relógio de homem místico pé junto a janela com a cara de estar perto do rosto o resto beleza geral prompt copia o prompt vamos ver o que vai sair agora Vamos ver o que vai sair. Bora meu mentor, tenho que jantar? Ué! Pode ir, Mano, eu ia fazer uma piada muito, Feia. Ah, esse aqui tá mais homem, olha que cara, Textual, tá? Esse aqui não tá tanto. Para mano, olha esse cara aqui ó, monge chinês tá ligado?
0:23:32
Beleza! Ah, mas esse aqui tá mais, tá mais, tá mais, mais, mais de boa né? Enfim, bora! Temos aqui o nosso prompt, o que que a gente O a gente vai fazer agora? Eu deixei aqui, mas eu vou até trocar esse prompt aqui, mas espere, ainda vou te mandar o prompt. Apenas faça no estilo que pedir.
0:23:54
Beleza, vamos copiar isso aqui, mandar para o Claudio, vou criar um chat novo aqui, espero que ele não me de barra, senão vou ter que botar dinheiro, pode mandar, nossa eu esqueci do estilo, calma, vou mandar o prompt aqui, vou baixar esta imagem aqui que é o estilo do blueprint que a gente vai usar, baixei a imagem.
0:24:20
Está aqui o estilo do Blueprint, vamos jogar aqui no Claudinho, beleza, ele vai falar ok e vai aguardar. Olha aí, agora a gente vai lá, vai pegar o nosso Prompt que a gente tirou no gerador de Prompts, mandei, e ele vai me dar o Prompt para gerar o Blueprint. Olha aí que beleza!
0:25:03
copia, vamos aqui na nossa IA geracional de imagens e vamos gerar aqui, vou gerar um monte aqui para vocês verem e aí a gente escolhe o melhor só esperar a imagem base, rapaziada, está aqui no mapa mental, só pegar aqui vou disponibilizar o mapa mental para vocês, aqui está o prompt, aqui está a imagem base para usar fechou?
0:25:32
Olha aí que beleza, nosso baita homem aí. Bom, não é? Entenderam? Tem que fazer isso no Cloud?
0:25:49
Ah, eu acho o Cloud o melhor para essa função. Mas faça onde vocês quiserem. Ah, eu vou baixar ela aqui, vou baixar em 4K essa. E aí depois, mano, o que a gente vai fazer? No nosso gerador novo, né, que o papai fez. O nosso girador novo, a gente vai vir aqui ó, se a gente quiser girar ele em outra roupa, outro ambiente, vem aqui. já tem o blueprint, aí ele vai colocar aqui as características de fenótipo dele, tudo mais mantém aqui como quiser, escolhe a roupa que ele tá de avental, agora nós vamos escaralhar ele agora nós vamos escaralhar ele, tá com uma cartinha de tarô beleza, gera o prompt, aí eu vou copiar esse prompt aqui, e o que eu vou fazer? Com meu Blueprint em mãos, eu faço upload deste Blueprint que a gente acabou de gerar.
0:27:04
Espera fazer o upload aqui Tututu E ai?
0:27:27
Vamos? Achei que tinha caído na internet Vamos afim Vou mandar de novo Opa, foi! Pego aqui o Blueprintzinho, inclui no comando, jogo o Prompt Olha a mágica acontecendo Toma, filhote! E aí? Easy, né? Easy ou não easy?
0:28:20
Tudo muito fácil Tudo muito fácil, tudo muito mastigadinho. Deixem o cara, o cara é tarólogo. Vocês querem que ele tenha mil de textos lendo tarô, porra? O importante é que funciona e que vai vender para a galera que quer encontrar uma gêmea. tá ligado?
0:28:47
Repita essa última parte, upload do blueprint, não, basicamente ó, vou repetir do princípio. Estou aqui no nosso gerador de prompts, zerado, eu clico em, já tenho o blueprint aqui, o blueprint, bota as características que eu quero, aqui como eu quiser tá ligado, quando eu botar que eu já tenho o blueprint, ele vai alocar aqui os fenótipos do cara, e aí beleza, gera o prompt, copio, faça o upload do blueprint, esse blueprint o ideal é vocês guardarem ele né, sempre guarda ele, faça o upload do blueprint, joga o prompt que o gerador me deu, e pronto mano, easy, tá ligado?
0:29:32
Duvidas? Dúvidas sobre o conteúdo de agora, dúvidas gerais para o final, aguardem, não vou responder dúvidas gerais agora mano, vou responder no final da call, beleza? Quando já tem um avatar?
0:29:53
Boa! Mano, quando já tem um avatar, é bem de boa, quer ver? Só as 9h, rapaziada. Credo, Claudio, calma, calma, calma, 20, 20, 20. Vocês não precisam ficar pagando o código e tá usando o Opus 4.7, eu tô usando porque eu sou imbecil.
0:30:20
Eu acho que o Cláudio Grátis já dá conta disso, eu nem precisaria estar pagando isso aqui mais, mas eu vou usar ele depois, talvez. Deixa eu ver se ele vai aqui, Oi? Oi, Claudinho? Oi?
0:30:38
Aí ele vai falar, pague? Pague? Aí, ó, pague? Oi? Pague, porra! Não, não quero recargar o telefone, NÃO! Que isso, não? Dois mil reais? Tá louco, porra?
0:30:55
Calma! Mano, agora, outra coisa, você pode simplesmente falar pra ele. Cláudio. já tenho um personagem, quero um Prompt para gerar esse mesmo Blueprint, porém vou anexar a imagem do personagem na hora de gerar. Me dê esse Prompt, por favor. Muito fácil, pra personagem já existente, tá ligado?
0:31:26
Vocês não precisam pagar, lembrando, é muito suave, eu tô pagando porque eu sou idiota. copio o prompt, deixa eu vir no nano banana zerado Aí, eu vou jogar aqui, vamos ver, um personagem que eu já tenho já existente Esse aqui ó Eu vou pegar esse cara aqui ó, esse cara aqui é bom Eu faço com a Ava?
0:31:58
Nossa, eu não sei se eu tenho a Ava aqui ainda Por que que tem a Eucareca aqui? Eu tava testando no GPT se eu ficava legal careca, aí eu vi no GPT que não, aí eu falei vou carecar igual. Cadê que essa véia aqui também é? Mas nesse próximo tifonais, possivelmente, mas é muito fácil, é só você ir no cloud e fazer isso aí mano, eu prefiro o cloud, ô Thiago vamos jogar aqui a nossa senhora opa, incluí ela no comando já vamos fazer com o nosso homem vitíligo aqui também vamos fazer os blueprints dos dois Ronaldinho gaúcho, não, só pensei num cara, vou fazer um com vitiligo pra ver, fazer umas cartomantes sem braço, olha aí, suave né, entenderam como usar personagem resistente?
0:33:13
Muito de boa, e olha o blueprint sai, maravilhoso, até o vitiligo sai corretinho tá ligado, nas partes que estava te ligado, a mãozinha, os olhos, na boca a senhorinha aqui, saiu toda fofa também sacaram gays? O personagem assistente tem como mudar o vestimento? Sim! Você muda pelo nosso gerador de prompts, tá ligado? Não o que está lá atual, ele vai ser atualizado, já tem o Blueprint.
0:33:55
Coloque mais o prompt que você mandou? Isso! Qualquer imagem que você tiver, mais esse prompt aqui. Mano, eu vou até deixar esse prompt aqui. Para avatares já existentes, anexe a imagem existente. e envie o seguinte prompt, vou deixar aqui também, vai ficar bom pra vocês, easy né, aí não precisa fazer muita coisa não, só pode fazer uma vez, acabou a aula?
0:34:35
que isso cara? que isso cara? Acabou de começar rapá, acabou de começar rapá, manda o mapa mental, calma meu princeso lindo do meu coração, após a cal eu já atualizo, já boto a aula ali, calma meu anjo. Que W o que, caralho, vai acabar a aula não, pô. Sim, é o mais novo mapa mental da aba de materiais, eu vou banir todo mundo que tá mandando W. Vou embora, vou embora, então me segue. Expulsando, rapaziada.
0:35:05
Eu vou botar modo lento. Depois que gerou o Blueprint, você pega essa imagem do Blueprint e depois segue o que? Mano, só cria o, Ó, vou mostrar de novo. Vem aqui, já tem o Blueprint do personagem, altera as coisas que você quer alterar e só joga o Blueprint junto do Prompt gerado aqui, entendeu? Muito simples, mano. Bora de, não acabou a cal, não, porra. Estão falando aí que acabou a cal?
0:35:34
Agora vai para o reijin, que vocês pediram há mil anos. Ou vocês não querem ver reijin hoje? Vocês querem mimir? Não quer, não quer, não quer? Ah, canalhas, canalhas. Mano, minha opinião sincera, Rei Jhin de graça não, infelizmente não.
0:35:53
Minha opinião sincera sobre o Rei Jhin pra mim não compensa, tá ligado? Eu acho ele um pouquinho, um pouquinho mercenário, por quê? Porque o Avatar 3 não tem mais, tá ligado? Não tem mais ilimitado. E ele fica com a mesma qualidade do Dreamface. Vamos fazer um teste com vocês primeiro?
0:36:12
É, minha câmera ainda me zoina, não faz isso comigo. Vamos fazer um teste com vocês? É, o Avatar 3 ele é barato, tá ligado? Você consegue gerar 200 vídeos dele. Vamos fazer um teste? Ó, Eu, antes da Kal, separei aqui 3 vídeos gerados pelo Avatar 3, Avatar 4 e Avatar 5. Mas primeiro eu vou explicar pra vocês o que cada um faz. Vamos para o Hei'jin.
0:36:43
Não sei, Alessandro, deve ser. Como que a gente vai criar o nosso bonequinho no Hei'jin? Bom, ele era ilimitado, mas parou de ser dia 15 de maio, infelizmente. A gente vem aqui em avatar, aqui em cima a gente tem a opção de, Aqui em cima a gente tem a opção de criar avatar, clicando nela a gente vem em criar um personagem virtual, carregar fotografia, e aí o que a gente faz? Vamos pegar aqui o blueprint, ah, eu não baixei o boneco né, deixa eu voltar lá para o flow, eu vou baixar ele também, alguma imagem que a gente fez, vamos pegar o nosso tarólogo Então, cheio de texto, vou baixar ainda Skype só para ser mais rápido, tendo aqui as imagens dele, a gente vai vir no regen, vai fazer o upload. Vou fazer um upload do Blueprint dele, e dele aqui todo fofinho.
0:38:09
Carrego, Alô? Alô? Alô? Não está fácil morar em Estação, Não está fácil morar em Estação Grande do Sul. Carreguei, Aqui as imagens do meu avatar, ele vai revisar os apelidos aqui, continua, vou dar um nomezinho pra ele, qual que é o nome do nosso avatar, Testosterono, aqui ele vai identificar as características, vai morrer o Mario, etnia tanto faz, dá pra deixar não especificado, continua, você pode escolher uma voz pra ele, mas a gente não vai usar a voz aqui, Se você quiser usar, pode usar, mas eu não gosto que não. Eu prefiro gerar a voz no Eleven Labs ou em outro lugar. Só para ter uma voz aqui, tá ligado? Oi, estou animado que você esteja aqui. É que combina a Vada e James com o Testosterono, tá? Ele vai aqui validar as fotinhas, pá, beleza. Aí, o que a gente vai fazer agora? Cadê nossa mapinha mental?
0:39:11
Aqui. A gente pode vir aqui, ó. Carrega alguma imagem que a gente quer. Deixa eu baixar outra foto dele. Do Testosterono. Só pra mostrar pra vocês. sem render e usar os 11labs essa aqui ele tá, o caralho essa aqui ele parece um, Pai de família, pô!
0:40:02
Qual é, Julia? Fez tudo ao contrário, pô! É só copiar os prompts que eu mandei. A gente pega aqui ele. Vamos jogar ele aqui.
0:40:17
Aí, carrega. Joga ele aqui. Crivisório do Testosterono nessa cena é mais que beleza vem aqui ó pode clicar nele e usar em vídeo adicionar um script porque que eu prefiro usar a áudio do 11 Labs? porque eu vou fazer vários tá ligado eu vou fazer 99999999999999 áudios em escala porque eu gosto de separar os processos primeiro a ver Eu gero o copy, depois eu faço o audios, e aí depois eu vou criando avatares, entendeu? É a minha forma de escalar.
0:41:07
Se quiserem jogar aqui a copy de vocês, fica à vontade, mano. Cada um faz como quer. Eu vou usar o áudio da Eleven Labs aqui, eu venho encarregar, escolho o áudio. Já tenho o áudio gerado aqui. Eu estou marcando o espeidamento de voz sempre. E aí, tem aqui ó, Avatar 3, Avatar 4 e Avatar 5. O avatar 5, nos testes que eu fiz, com um áudio de 55 segundos, ele gastou 19 créditos, o avatar 4 também gastou 19 créditos e o avatar 3 gastou 3 créditos.
0:41:41
com áudios de 55 segundos. Não sei se com áudios maiores ele vai aumentar ou não. Descubram aí para nós também, porque eu não tô usando áudios muito longos, tá ligado? Se alguém usa áudios mais longos, dá o feedback para nós. Aumenta muito? Aí, já sabemos.
0:42:01
Então, com áudios mais longos, aumenta. Experimento de voz. Escolhe uma voz e combinaremos estilo, emoção e tom da sua gravação. Quanto é o regen? 29 dólares, 600 créditos. Então você consegue gerar 200 vídeos no Avatar 3, tá ligado? E aí, você escolhe.
0:42:21
O Avatar 5, estilo de movimento consistente do personagem, que se adapta ao roteiro. Avatar 4, movimento genérico, que se adapta ao roteiro. E o Avatar 3, ele vai dar uma movimentadinha ali, vai loopar depois de um tempo, e vai fazer o lip-sync, tá ligado? Fica uma qualidade bem legal. A diferença é que ele faz tipo o trabalho do Dreamface, Isa.
0:42:42
Ele já anima e já faz esse trabalho do Dreamface, entendeu? Beleza, aí eu escolho aqui o avatar que eu quero, vamos fazer o avatar 3 primeiro. Ué, por que o teu tá ilimitado, Ana? Qual plano você tá usando?
0:43:04
O meu tá cobrando, quer ver ó? De prova Caralho, esse cara odeia eu Ah, conta antiga ainda ilimitado, caralho Compro conta antiga de regen, pago mil dólares Eu acho que mês que vem não vai mais ficar ilimitado não, hein Pior que eu tenho conta antiga, só preciso achar o e-mail que tá Aí eu faço um Mateio, mano. Vou gerar um Avatar 4 aqui também, pra vocês verem. E depois a gente vai fazer o teste. Experimento de voz, Avatar 4. Vou gerar dos três. E aí eu vou botar, Eu vou botar lado a lado pra vocês, Pra vocês adivinharem qual é qual. O que o 5 faz mesmo? Estilo de movimento consistente do personagem que se adapta ao roteiro. O 4 é um movimento mais genérico, entendeu? E também, se você quiser, Cadê o bagulho?
0:44:21
Aqui ó, se você quiser, você tem a opção de botar movimento personalizado, que vai custar o dobro. No avatar 3 eu acho que não tem, né, essa opção. Vamos botar aqui um avatar 5 também. O meu tá, tá descontando, já olhei. Eu peguei esse aqui só pra cá hoje.
0:44:52
É aqui, Plane Cobrança, não, é uso histórico. 6 cache de avatar 3 e o 4 está entrando no 5 também Vem com quantos créditos? 600. Vamos esperar fazer aqui, ó. Ele fica aqui do lado do progresso.
0:45:17
Se você clicar em ver tudo, ele vem pra todos. Tá desligueido, é só esperar. Ah, dá pra gerar cena por cena. Pô, mó trampo. ser de graça me conquista. Na versão free vem com essa marca d'água gigante, né? Dá pra usar, dá pra usar. E o problema é que na escala você vai ter que ficar criando contas. Dá pra usar?
0:45:46
Enquanto ficar blueprint da Hilda ficou muito bom, bizarro mano, ta quase, ta quase, esse aqui Avatar 4 já gerou, gerou dentro do 3, essa bomba aqui demora pra baixar também, ah não, foi rapidinho agora.
0:46:32
Na foto do Discord eu estava mandando uma rima Se eu pudesse rimar ao vivo aqui, eu rimava, mano Algum dia eu vou fazer uma batalha de rima na calda do Elite, tá? Não dá, mano Não posso rimar numa calda Eu sou expulso da MVM e ainda processado Tá quase, tá quase, tá quase Sim, Vitor. Exatamente.
0:47:20
Vamos aí, Jane. Agiliza. Paguei três mil pra ver um cara rimando no palco? Confere. Gustavo só responde os amigos dele.
0:47:35
Se você não é amigo dele, nem adianta ficar mandando mensagem aqui, pelo amor de Deus, né, gente? É verdade. Por isso que eu sou amigo de todo mundo. depois para fazer outro vídeo. Consegue gerar direto também, ô Bronx. Mas eu gosto de fazer vários diferentes. Eu prefiro, né?
0:48:11
Acho que semana que vem, Matheus. Talvez na sexta dê para fazer também. Tá quase, tá quase, Redjen. Mano, não testei bem.
0:48:48
Você era bom para alguém que não te merecia. Você deu tudo, ficou loyal. Ok, é o avatar qual, pelo nome da imagem? Algumas mulheres amam as pessoas erradas tão profundamente, não porque são naíves, mas porque sua energia ainda não estava alinhada com a pessoa que realmente era destinada a receber esse amor. E quando essa energia muda, as pessoas que entram na sua vida também mudam. O homem que aparece não desaparece. Ele não dá frutas de Ele não faz você se perguntar como ele se sente. Ele simplesmente fica. Porque ele foi feito para você. Sim, há um teste que revela exatamente onde esse desalinhamento está acontecendo E mostra quem a pessoa chamada por você realmente é Incluindo seu corpo, tirado da sua leitura astral Comente, parceiro Abaixo, e eu o envio agora Agora, ou clique no meu profilo e acesse o link da minha bio, ou cheque o primeiro comentário abaixo. O teste é gratuito, porque esta mensagem foi feita para você.
0:50:16
O vaso do véu é muito artificial, não gosto não. Não, não falei que não compensa? Falei que não muda? Uau! 1.000.000 de coisas, 1.000.000 de 1.000.000 por cento, tá ligado? Pra quem tá no início ali se tornar algo caro, mas se você já tá escalado fazendo 1.000 dólares por dia, pô, aí compensa pra caralho, né?
0:50:39
Vamos ver o Avatar 5? Você era bom para alguém que não te merecia. Você deu o seu tudo, ficou loyal, e no fim você foi puxado para o lado. O Universo viu tudo isso. Bate o coração. Se isso tivesse acontecido com você.
0:50:58
Algumas mulheres amam as pessoas erradas tão profundamente. Não porque são naíves. Mas o movimento dele para as expressões. Mas é porque sua energia ainda não estava alinhada com a pessoa que realmente era destinada a receber esse amor. E quando essa energia muda, as pessoas que entram em sua vida também mudam. O homem que aparece não desaparece. Ele não dá frutas de Ele não faz você perguntar como ele se sente. Ele simplesmente permanece. Porque ele foi feito para sua frequência.
0:51:26
Há um teste que revela exatamente onde esse desalinhamento está acontecendo. E mostra quem a pessoa destinada a você realmente é. É bom, é bom para um caralho, tá ligado? O 4 ambientação atrás é melhor, só que a movimentação do personagem em si, o 5 é foda.
0:52:00
E o 3 aqui, daqui a 8 horas, está convertendo-se em Dreamface, o traficante do Vader Calçal. É que trouxeram a manca? Você gosta de uma coisinha fácil né Matheus, caralho, vou mano, vou sim.
0:52:58
Você era bom para alguém que não deserava. Você deu seu todo, ficou loyal, e no final você foi puxado para o lado. O universo viu tudo disso. Bate o coração se isso já aconteceu com você. Algumas mulheres gostam muito de enxergar as pessoas erradas tão profundamente. Não porque elas são naíves, mas porque a energia delas ainda não estava alinhada com a pessoa que era realmente destinada a receber esse amor. E quando essa energia muda, as pessoas que entram na sua vida mudam também.
0:53:22
O homem que aparece não desaparece. Ele não dá frutas. Ele não faz você perguntar como ele se sente. Ele simplesmente permanece. Porque ele foi feito para sua frequência. Existe um teste que revela exatamente onde esse desalinhamento está acontecendo e mostra quem a pessoa querida por você realmente é, incluindo seu rosto, tirado da sua leitura astral.
0:53:43
Comente Soulmate. Aqui em baixo e eu vou enviá-lo a você agora mesmo. Ou clique no meu profilo e acesse o link da minha bio. Ou cheque o primeiro comentário abaixo. O teste é gratuito, porque este mensagem foi feita para você. Você era bom para alguém que não te merecia. Você deu tudo, ficou loyal. E no final você foi expulsado.
0:54:12
Você pode decidir. O universo está em sua mão. Ataque o coração se isso já aconteceu com você. Algumas mulheres amam as pessoas erradas muito profundamente. Não porque elas são naivas, mas porque a energia delas ainda não estava alinhada com a pessoa que era verdadeiramente naiva. O simplesmente feito para receber esse amor, e quando essa energia muda, as pessoas que entram em sua vida mudam também. O homem que aparece não desaparece, ele não dá frango, ele não faz você perguntar como ele se sente.
0:54:37
Ele simplesmente permanece, porque ele foi feito para sua frequência. Há um teste que mostra exatamente o que está acontecendo e mostra quem a pessoa que foi feita para você realmente é, Mano, não trai de Ele foi feito para você.
0:55:13
Ele foi feito para você. O que é isso? Cara, bem dificilmente o Lidia vai perceber esse loop.
0:55:42
O gerador de copies é mais, É um negócio mais complexo, a Amanda tem como fazer, mas é um negocinho um pouco mais complexo, vai demandar um pouquinho mais de tempo e um pouco mais de copies. Isso, Daniel, três créditos para o vídeo de 55 segundos com o Avatar 3.
0:56:05
Não, tá longo não. Eu quero que esse aqui fique pronto para a gente fazer uma comparativa. Há um homem escondendo duas coisas de você, e a segunda, você sempre suspeitou.
0:56:24
Toce seu coração antes de Mas você continua assistindo. As cartas revelaram que alguém que está com você não pode te tirar do seu cérebro. Ele estava em outra relação, mas ele Há uma bondade muito forte entre vocês dois, porque ele compartilha as mesmas frequências.
0:56:41
Isso é o que chamamos de um soulmate. No mês passado, uma das escolhidas foi a Marilyn. Ela descobriu que seu soulmate, Depois some. Headline é bom.
0:57:01
Aqui deu uma leve bugada, mas nada mal. Esse é o nome dele e seu rosto, desenhado especificamente para você. Envie esse vídeo para alguém agora mesmo. Não escolha. Envie para a primeira pessoa que venha à sua mente. Se aquela pessoa é você, é ele.
0:57:18
O Universo acabou de te responder. muito vendível, muito fácil de vender, mas se tu conhece um copy muito foda, sempre compensa, né? Quanto mais, quanto melhor a coisa.
0:57:50
Se você quer um copy foda, que vai pensar em uma copia altamente vendível, a conversão que você vai ter de resultado é brincadeira, né? Só gerou 8D? Totalizo ele. Vai te fazer vender pouquinho.
0:58:09
compensa não então não não muito ruim muito ruim tudo que vem pra somar viado sempre compensa tá ligado será que bugou essa porra mano é que porque é rapidão né essa boa é chato Eu não, é o maior caro, faz você com o movimento Não quero fazer por aqui não Ah, foi, foda-se Nossa, duvidei em quando Não foi não?
0:58:54
Foi sim, aqui, baixei errado, sou burro Ah, não foi não, caralho, que merda 0 Muito caro, diminui aí, que nóis tá duro Preços, muito caro Assinei e agora tô jantando pipoca e almoçando miojo Melhor Já!
0:59:45
tá jantando saliva, tá jantando água mano, vamos ver se vai agora Beleza, vou ver a Antônia depois da calma é só criar a conta, fazer o teste grátis e cancelar e eles vão te ofertar isso, Meraíza Não, o bagulho é almoçar 4 horas da tarde, aí dorme às 9, acorda no outro dia, come um ovo, rouba um ovo na noite. no celeiro do vizinho né, quem mora no mato tem essa vantagem e aí depois eu mostro de novo, 4 horas da tarde, loop, repeto, mastiga a língua é foda 600 créditos dá pra fazer quanto em média?
1:00:41
600 dividido por 3, 200 vídeos isso Marisa, aí você cancela o plano e eles vão te oferecer 3 meses por 30 dólares mas agora que tá bem chato, agora tá limitando bastante a geração Tchau.
1:01:07
Vamos ver se ele vai fazer agora. Eu quero mostrar para vocês para fazer o comparativo. Se bem que eu tenho esses aqui prontos. Enquanto ele gera, vamos fazer com um para a gente não ficar parado. Calma aí. Eu vou embaralhar, tá? Vocês são safados, vocês vão olhar o nome em cima. Ai, cadrai, não consigo.
1:01:38
Agora eu jogo isso aqui para cima. Você já não sabe mais qual é qual. Porém, ninguém sabe qual que eu joguei pra cá e qual que ficou lá.
1:02:04
Tá difícil? Óbvio que tá difícil. Quero embaralhar, mano. Ninguém sabe qual é qual. Ó, aí eu faço isso. Meu Deus, eu joguei pra cima tudo errado. Aí eu jogo pra cá.
1:02:22
Vocês sabem qual é qual? Nem eu sei mais. Mas é que se eu mudar o nome do arquivo, eu não vou saber. Ninguém sabe qual é qual agora. Não faço ideia. 4, 5, 3, os caras chutando.
1:02:47
Vamos lá, deixa eu só mudar dois aqui e vou dar play. Você era bom para alguém que não te merecia. Você deu seu tudo, ficou fiel, e no fim você foi expulsado. O universo viu tudo disso. Bate o coração se isso já aconteceu com você. Algumas mulheres amam as pessoas erradas tão profundamente. Não porque são naíves.
1:03:05
mas porque sua energia ainda não estava alinhada com a pessoa que realmente era destinada a receber esse amor. E quando essa energia muda, as pessoas que entram em sua vida mudam também. O homem que aparece não desaparece. Ele não dá frutas. Ele não faz você se perguntar como ele se sente. Ele simplesmente permanece, porque ele foi feito para sua frequência. Há um teste que revela exatamente onde este desalinhamento está ocorrendo, e mostra quem a pessoa destinada a você realmente é, incluindo seu rosto, de sua leitura astral?
1:03:35
Comente Soulmate abaixo e eu o envio a você agora mesmo, ou clique no meu profilo e acesse o link da minha biografia, ou cheque o primeiro comentário abaixo. O teste é grátis, porque você Porque essa mensagem foi feita para você. Você fez um bom pra alguém que não fez.
1:04:15
Caralho velho Trolei até mesmo Vamos de novo Eu mereço você. Você deu seu tudo, ficou fiel, e no fim você foi expulsado.
1:04:34
O universo viu tudo disso. Bate o coração se isso já aconteceu. Algumas mulheres amam as pessoas erradas muito profundamente. Não porque são naíves, mas porque sua energia ainda não estava alinhada com a pessoa que era realmente destinada a receber esse amor. E quando essa energia muda, as pessoas que entram em sua vida também mudam. O homem que aparece não desaparece. Ele não dá frango de pão. Ele não faz você se perguntar como ele se sente. Ele simplesmente permanece, porque ele foi feito para sua frequência. Há um teste que revela exatamente onde esse desalinhamento está acontecendo. E mostra quem a pessoa que você realmente é Incluindo seu rosto, desenhado da sua leitura astral Comente Soulmate Aqui em baixo e eu vou enviá-lo agora Ou clique no meu profilo e acesse o link da minha bio Ou cheque o primeiro comentário abaixo O teste é gratuito, porque essa mensagem foi feita para você dois. Sim, o 13 dá pra perceber, mas é muito bom igual, né mano?
1:05:41
Tudo muito bom, velho. deixa eu baixar de novo aqui para não confundir vamos ver do nosso cartão do testosterona não a gente não percebe isso que eu queria passar para vocês se a gente não percebe imagina o público tá ligado Calma que é difícil, to pinando o negócio ó Meu Deus do céu, eu vou fazer na mão mesmo, aí fica mais difícil de vocês coisa ao coisa Para de rir mano, sem risadinha Eu não posso bater a bunda da aba ali embaixo, meu Deus Vamo? Vamo? Pau da play?
1:07:15
Tão preparado? Quem tem sharingan? Não tem sharingan? 3, 2, 1, E quando essa energia muda, as pessoas que entram na sua vida mudam também.
1:07:45
O homem que aparece não desaparece, ele não dá frutas de ele não faz você perguntar como ele se sente, ele simplesmente permanece, porque ele foi feito para sua frequência. Há um teste que revela exatamente onde este desalinhamento está ocorrendo e mostra quem a pessoa querida para você realmente é, incluindo o rosto deles, tirado de sua leitura astral. Comente Soulmate abaixo e eu o envio a você agora mesmo, ou clique no meu profilo e acesse o link na minha biografia, ou veja o primeiro comentário abaixo.
1:08:16
O teste é gratuito porque essa mensagem foi feita para você. O número 4 do 4. Por quê? Por causa das expressões faciais dele, tá ligado? O 3 é mais, mais, mais, mais são gamonga, ali e tal. Mas, mano, todos muito bons. Estou errado?
1:08:35
Ou estou correto? Todos muito bons? Olha a capa de Facebook que o pai fez. Ah, moleque! Pô, como que isso aqui não vai vender, papai? Errado? Ah, então desculpa.
1:08:57
Obrigado pela capa free, usa aí! Bom mesmo só se fosse de graça? Nada que é bom vem de graça! E essa capa aqui ó, cadê, essa capa aqui tá boa É o teste né papai Vocês se perdem né mano, vocês se perdem velho Conteúdo Premium né Silvares? Conteúdo Premium mano Mano, dúvidas sobre o conteúdo passado aqui?
1:09:58
Caralho, o cara já salvou a capa Não deu pra ver Cê é casado rapaz Cê é casado Rogério De ontem? O que é de ontem? O Archangel não está disponível.
1:10:22
Mapa mental? Tá, tá lá, totalizado lá. Cal? Tenho certeza. Xinga o suporte. Gravações. Tá lá, tá lá, tá lá. Talvez eu não botei aqui ainda.
1:10:41
Botei, botei também. Tá ali. Tudo lá. Onde seleciona qual avatar eu uso? Lá embaixo. Igual eu fiz na Cal mesmo. Deixa eu tirar a telinha. Dúvidas, rapaziada, sobre o conteúdo passado aqui, depois a gente abre para conteúdo mais geral.
1:11:04
Mostra a capa de novo, não. tem um print ai em cima, bem de boa né, conteúdo tranquilo, coisinha fácil de se fazer calma ai, calma ai Phelps, vou apagar, vou apagar, da pra fazer audio direto no Heijin? mano, tem como sim, mas eu gosto de fazer no Eleven Labs, porque é a forma que eu escalo melhor, ta ligado? mas pode fazer no Heijin se quiser, o próprio Heijin usa o Eleven Labs, mas eu Quando vai ser a próxima caua de análise de vídeos? Cara, eu preciso ver com o Luigi quando que a gente vai fazer essa Que tem mais uns conteúdos pra passar antes disso Mas talvez eu jogue uma cauda de análise de vídeos antes Vamos, questão de organização mesmo Só pensar como vai ser, tá ligado?
1:12:12
Fiz no chatpt, ô Rodrigo, essa capa Vai ter aulas criando cópia ao vivo? Sim, senhor, senhor Sim também, João, de reaproveitando cópias É um vídeo consistente de personagem de novela? Pode sim, Paloma. Pode sim. Luigi tá na Cal?
1:12:35
Luigi tá no Peru, mano. Não levem por trás, mano. Tá literalmente no Peru, no país Peru. Ai, mano. Eu esqueço onde eu tô, velho. Esquei.
1:12:59
Putz Adonias, vai de próxima conta, viado. Eu sei falar muito rápido, mano. Mano, eu uso um pouquinho de cada, mas eu uso mais Dreamface sim, por questão de escala.
1:13:21
Nuvel é igual mostrar nas outras caos, opa lama, tipo, cria nuvel ali, faz o loop. Igual mostrar nas outras caos mesmo. Cria nuvel, faz o loop e joga no Dreamface. Tenho, mas, a única coisa que eu posso falar é logo vem, ô Léo. Só isso. Agora que pago tá chato, mano. O pessoal não tá vendo as mensagens?
1:13:52
Ué, Provavelmente vai pra caixa de solicitações, então. Você é brabo, Bruno. Nice! Vel'Grok ou Heijin? Cara, Heijin é melhor.
1:14:17
Mas você escolhe o que prefere usar. Todos vão performar bem, sabe? Tipo, mesmo os mais simples com Dreamface vão performar bem. O que vai mandar mais na entrega, viralização, venda, é a copy e o avatar ali. Ah, tem o Copywriter lá, que trabalha com o Cobata também, que ele vai colar, fazer uma call sobre copy e avatar aqui. Só não sabemos quando ainda, mas é só marcar. O bichinho é bom, tá? Já escalou alguns milhões aí em vendas. O bicho é GOAT.
1:14:53
Qual o nome do rapaz? É Johan. Cara, pra ser sincero, cidência eu nunca nem usei, mano. Não vi necessidade. Tiago Finch, ele mesmo, ele mesmo. Tchau ela de lado e testarei em outra conta.
1:15:40
Clóvis, estou animando tudo fácil para te apetecer as copias. Júlia, copie de, de news eu to fazendo tudo no gpt sim mas tipo de cartomante não tem necessidade de usar outra coisa não aqui o cloud ta bem, bem chatinho todo vídeo que faço no facebook sempre bate 10, 20 e alguns batendo mais de 60k mano não spama tanto não felps vai mais de boa mas é 10, 20 mil? se o vídeo começar a estourar tipo todo, todo, todo vídeo joga sei lá 6 vídeos por dia nessa conta ai pra ver o que que vai acontecer Aí se todos estourar assim, vai postando 6, mas mais que 6 eu não acho inteligente não.
1:16:21
Tem gente que posta mais, mas eu não gosto de passar desse limite não. O mesmo vídeo colocamos todas as CTAs? Sim, Marília, porque a gente vai aproveitar o vídeo para várias redes, entendeu? Estouraram o Phelps, né? Você está postando e não está indo para frente, Lorena? Tipo, validou uma copy em outra conta e esse avatar aqui, Na conta 1 validei uma copy e aí na conta 2, com um avatar diferente, postei vários vídeos com copy parecida e não, E não deu bom? Aí eu trocaria de avatar.
1:17:02
Pode colocar o link na descrição do Instagram? Deve! 200 views tá suave ainda, Gabriel. Não tem porque jogar fora, não. Sim, de duas em duas horas o ideal fica, né?
1:17:20
Pode jogar tudo lá nos rascunhos, tá ligado? Tipo, porra, fiz mil vídeos hoje. Deixa tudo lá nos rascunhos e vai postando. Nem sei se no Instagram tem rascunho, eu sei que no TikTok pode. Sim, mas não vai perder entrega e venda nisso não. Insta tem também?
1:17:41
Nice! Um minichat da Pozai em todas as contas? Um abraço. Um abraço. Um abraço. A conta do minichat sim, mas você tem que pagar separado por cada conta. O Roberto fez um GPT aí também, que você testar, Eu não tô postando assim não, Mari. Tem gente postando aí.
1:18:22
Lá no chatzinho de apps, a rapaziada tava falando sobre isso. Dá pra, Dá pra Vou trocar uma ideia lá com a galera que tá postando assim, mas eu tô postando direto no Instagram com o Proxy ainda. Bugou meu cérebro aqui, em qual aula o Gustavo ensinou a fazer esses banners mesmo? Mano, ensinei em alguma aula, mas posso fazer de novo, é simples, muito simples. Posso mostrar pra vocês aqui a parte da capinha de Facebook. Cadê, cadê, cadê, cadê, cadê? Capa de Facebook.
1:18:48
e olha aqui como eu fiz umas que eu comecei ontem e acho que o pedrão e não Aqui ó, olha como é que eu fiz a capinha Quero criar uma capa de Facebook na maior qualidade possível para este homem Ele encontrará um logo especializado e encontrará uma gêmea A capa deve ser minimalista, porém muito bonita, toda em inglês Olha aí que beleza? Easy Mano, muito fácil de fazer uma capa Ficou muito boa, aí depois vim e mandei outro Blueprint aqui Olha aí Cara, é a coisa mais fácil do mundo fazer uma capa de Facebook Chat GPT faz ela muito bem Sim, GPT 2 tá muito foda pra imagem Manda aquela capa aqui. Que capa, filho? Sim velho, pra que pagar designer hoje em dia, né? F-Designers Tracamento da API não tá bugado? Não. Manda o prompt?
1:19:57
Pô, deixa eu pegar. A call de amanhã vai ser do que? Mentalidade com cobata. Cadê, cadê, cadê, cadê, cadê, cadê, me pediu o prompt, mandei aqui. F-Barão Vai ter também, Icaro, fica suave. Teremos bagulho de de copy. Tchau, tchau!
1:20:29
Instagram é o link fixado nos primeiros comentários, Não, no Instagram não fica clicável, só no Facebook tem como deixar clicado. Caralho, agora que eu entendi. Onde colocar o link de venda na página do Face? Posso sim, deixa eu abrir aqui o Facebook. o facebook aqui para botar o link na é bem fácil também você vem entrar na página aqui editar aí vai descer aqui ó vai ter links só colocar o link já era O link está na descrição do vídeo.
1:21:35
O que você tá errando, então, velho? É pra deixar. Oxi, eu boto o link curto lá direto Meu TikTok tava metendo o link da Twitch antigamente Aê carai, ao vivo filhote, vai tomando Nice Igor, porra. Carai, comissão tá alta hein papai Orra, a pia não tá pagando bem hein fi Reage nessa foto do Igor aí carai Reage, reage, reage, reage, reage, vai carai fogo porra, fogo, foguete, tudo, reage nessa porra ai, isso caralho Ficar bonito na foto, vou postar uma fotinha aqui, nice porra, parabéns mulekote E a primeira de muitas tá, Caralho, cês é bom mano, cês é foda Sim mano, stripe é nada de taxa né, praticamente Caralho, mas da hora meus números de subida, que coisa linda fi Devia ter gravado eu falando, meu monitor tá todo sujo Ah, já já sai hein leão até olha o meu, olha lá fi hum, dá pra copiar e colar os anos de cada funil?
1:23:16
não entendi nada, Daniel sempre escolhe a opção site ah tá, entendi cara, eu gosto de escolher a opção site, né? já que tem nativo vamos lá que isso, tão me expulsando, porra? tão me expulsando? que isso, cara? então tá, falou, tchau! Ih, pode estar trancada. Não, não foda-se mano, é W nessa porra. vai, espama, espama essa caralha, vai ae porra, espama isso ai caralho, não da nem tempo de carregar a foto mano tava brincando, agora vamos voltar pra cal, bora quem foi embora se fudeu agora é o ouro, agora é segredo suporte não grava mais conteúdo de copy brincadeira rapaziada, por hoje vou liberar vocês vou deixar vocês trampar Valeu rapaziada, tamo junto, amanhã Mentalidade de Cobata 19, espero vocês quinta-feira 20h no TikTalk hein, o bagulho vai pocar mas vai trazer uma rapaziada que tá escalando já.
1:24:25
Esteja presente. É 20 horas? Acho que é. Mas já? Estão me expulsando, estão sabendo tudo. Usei o chat de apps lá pra se ajudar, rapaziada, tô sempre por lá também, tamo junto, bom trampo aí. É nóis. Valeu pela presença, tá? Mas já? É que você chegou, né, Edu? Tem que ir embora.
