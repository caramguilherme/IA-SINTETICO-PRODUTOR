# Pente fino nos painéis do nora48 e do nora49 (05/11/2026 ~13h15, pedido do aluno antes de produzir).
# Uso: python3 ferramentas-painel/r0511/patch_pente_fino_4849.py  (na raiz do repositório)
import re, json, io

def carregar(n):
    s = io.open(f'PAINEL-NORA{n}.html', encoding='utf-8').read()
    m = re.search(r'const PACOTE = (\{.*?\});\n', s, re.S)
    return s, m, json.loads(m.group(1))

def salvar(n, s, m, p):
    novo = 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';\n'
    s = s[:m.start()] + novo + s[m.end():]
    io.open(f'PAINEL-NORA{n}.html', 'w', encoding='utf-8').write(s)

REG = (' 05/11 ~13h15 (pente fino pedido pelo aluno antes de produzir): conferidos falas (21 e 22 palavras), '
       'movimentação sem palavras da fala, colagem igual ao take, links, legenda, comentários, story e edição; '
       'corrigidos os pontos listados no fim deste registro.')

NUM_RULE = ('numbers are spoken as words (11:11 and 11/11 as "eleven eleven", 222 as "two two two"); ')

# ---------------- nora48 ----------------
s, m, p = carregar(48)
p['roteiro']['id'] = 'nora48-CORPO-A-LIMPO-TAKE1-CANCER-ESCORPIAO-PEIXES'
p['figurino'] = ('fortune-teller, subtle mystic; plain black fine ribbed knit top with a round crew neckline and long fitted sleeves, '
                 'smooth matte finish, no print, embroidery, logo or shine. Fixed accessories, always visible: the long gold star-and-moon '
                 'drop earrings, the long thin gold chain with the small gold Venus-symbol pendant, thin gold bracelets on her left wrist, '
                 'a small gold sun-symbol ring on her right index finger and the gold face gems from the reference sheet; no flag pin, '
                 'no other jewelry, turban, cape or costume')
for sec in p['central']['config']:
    for f in sec['campos']:
        if 'copiar' in f and f['campo'].startswith('LIVRE'):
            t = f['copiar']
            alvo = 'no added sentence before, between or after; '
            assert alvo in t and 'eleven eleven' not in t
            f['copiar'] = t.replace(alvo, alvo + NUM_RULE, 1)
p['story']['nota'] = ('REPOSTE O STORY AGORA, ou no máximo antes das 17h (o story-0311 venceu em 04/11 ~22h45 e o link está fora): '
                      'a mesma imagem (story-3110), o mesmo texto e o adesivo com o link certo de cada rede; confira na prévia. '
                      'Repostado hoje, ele vale 24 h e cobre o nora48 (17h) e o nora49 (19h30). '
                      'Insta (STORYIG): https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=instagram&utm_content=STORYIG&aff=dl7zx6ks'
                      ' · Face (FACE): https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks')
p['roteiro']['leitura_registro'] += REG + (' nora48: o código do roteiro dizia CORPO-B (é o corpo A limpo); o figurino guardado era o '
    'do estúdio (o vídeo usa a nora37-IMG, blusa preta canelada); o texto LIVRE ganhou a regra dos números falados ("eleven eleven"), '
    'porque o Take 1 diz 11:11; a nota do story dizia que o repost valia até 01h de 06/11 (vale 24 h a partir do repost).')
salvar(48, s, m, p)

# ---------------- nora49 ----------------
s, m, p = carregar(49)
p['roteiro']['descricao_instagram'] = ('Aries, Leo, Sagittarius: if you know something has to change, but not how, listen before 11/11, '
    'the most powerful portal of the year. 🔮\n3 signs it\'s opening for you. Your private reading is waiting in my story.\n'
    '#manifestation #1111portal #aries #leo #sagittarius')
p['central']['passos'][0] = 'Story: não precisa. Vale o story-0311 repostado hoje antes do nora48 (se ainda não repostou, reposte antes das 19h30).'
p['story']['nota'] = '✅ NÃO FAÇA STORY PARA ESTE VÍDEO: vale o story-0311 repostado hoje antes do nora48 (se ainda não repostou, reposte antes das 19h30).'
mt = p['mapa_tela']
mt['estilos'] = [
    {"nome": "Números fixos espalhados (11:11, 222, 888)", "fonte": "Poppins Bold (poppins-bd)",
     "cor": "uma cor para cada número (abaixo)", "tamanho": "um tamanho para cada número (abaixo)",
     "contorno": "Traço preto + Sombra preta, sem Plano de fundo",
     "obs": "As cores e os tamanhos do nora46, puxados para dentro da margem do Face (P43): 11:11 vermelho #E53935, 15, X 230 · Y 486; "
            "222 roxo #8E24AA, 12, X -230 · Y 294; 888 verde-esmeralda #00A86B, 11, X 230 · Y 77. Do 1º quadro do hook ao fim. Eu ponho (P45)."},
    {"nome": "Caixa do topo: “ARIES, LEO, SAGITTARIUS” / “11:11, the most powerful portal” / “3 signs it's opening for you”",
     "fonte": "Poppins Bold (poppins-bd)", "cor": "texto preto; a 1ª linha (os signos) em vermelho #E53935",
     "tamanho": "10, em 3 linhas (até ~84% da largura)", "contorno": "Plano de fundo branco arredondado",
     "obs": "X 0 · Y 397, do 1º quadro do hook até o fim do Take 1. Eu ponho (P45)."},
    {"nome": "Caixas do corpo B (as mesmas do nora47)", "fonte": "Poppins Bold (poppins-bd)",
     "cor": "texto preto; os números 1., 2., 3. e o 4.7 em vermelho #E53935", "tamanho": "9",
     "contorno": "Plano de fundo branco arredondado",
     "obs": "Os 3 sinais um embaixo do outro, na hora em que ela fala cada um (“11:11 everywhere”, “The wrong people fade out”, "
            "“Something good is coming”); “Rated 4.7 by 2,000+ people” durante as avaliações; “Your private reading is in my story” "
            "(“my story” em vermelho) do CTA até o fim. Eu ponho (P45)."},
    {"nome": "Imagens do desejo e avaliações reais", "fonte": "—", "cor": "—", "tamanho": "tela cheia (desejo) e 630 de largura (avaliações)",
     "contorno": "—",
     "obs": "Dinheiro, casal e casa em tela cheia, na frase do desejo; depois as 3 avaliações reais do Trustpilot (Leukia, Patricia, Darcey) "
            "no alto, com fade. Mesmos tempos do nora47, achados pela transcrição. Eu ponho (P45)."},
    {"nome": "Legenda (eu ponho, P45)", "fonte": "Poppins Bold", "cor": "branco, em MAIÚSCULAS; palavra-chave em amarelo-ouro #FFD21F",
     "tamanho": "uns 38 px (vídeo 720×1280)", "contorno": "preto grosso",
     "obs": "Do Take 1 ao fim (menos durante as imagens do desejo e as avaliações), Y -294, blocos de 2 a 4 palavras. "
            "Destaques: Aries, Leo, Sagittarius, 11:11, portal, sign, money, peace, love e 222. Sem legenda no hook."},
    {"nome": "Seta vermelha (↓)", "fonte": "—", "cor": "vermelho #E53935 com traço preto", "tamanho": "14", "contorno": "—",
     "obs": "Do CTA (depois das avaliações) até o fim, embaixo à esquerda (X -288 · Y -333, P43), apontando para a foto do perfil. Eu ponho (P45)."},
]
mt['regras'] = [
    "Conferido na nora46-IMG: a faixa da legenda (Y -294, 73%) fica nos antebraços, logo acima da borda da mesa, abaixo do microfone e do rosto.",
    "O nora47-montado não tem nenhum texto: eu ponho tudo no vídeo inteiro (P45), igual ao nora47, com os números e a seta já dentro da margem do Face (P43).",
    "Os números ficam na parede, na janela e acima da cabeça: eu confiro no quadro do vídeo e mexo uns 40 se algum cobrir a cabeça, o braço do microfone, a bandeirinha ou o cabelo.",
]
for nmr in mt['numeros']:
    if nmr['t'] == '11:11': nmr['x'] = 82
    if nmr['t'] == '222': nmr['x'] = 18
    if nmr['t'] == '888': nmr['x'] = 82
mt['seta'] = {"x": 10, "y": 76, "onde": "embaixo à esquerda, apontando para baixo, para a foto do perfil (do CTA até o fim)"}
p['roteiro']['leitura_registro'] += REG + (' nora49: a legenda do post dizia "if this describes your life" (agora repete a dor do Take 1); '
    'o mapa da tela ainda falava do Claude das legendas e de pôr números e legenda só no Take 1, mas o nora47-montado não tem texto: '
    'eu ponho tudo no vídeo inteiro (P45); números e seta puxados para dentro da margem do Face (P43); a seta voltou ao mapa.')
salvar(49, s, m, p)
print('ok')
