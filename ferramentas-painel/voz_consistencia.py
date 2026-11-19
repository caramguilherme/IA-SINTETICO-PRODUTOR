"""O campo "Prompt de consistência de voz (opcional)" do gerador de animação da Central (novo em 19/11/2026; a atualização
que o Gustavo prometeu na call de 18/11, 0:49:37 a 0:51:13). O texto entra na seção VOICE CONSISTENCY de cada take, no
lugar da trava padrão. Todo painel novo da Nora leva este campo na seção 5 da Central, logo depois do "Perfil de voz".
Uso nos builders: `import voz_consistencia as VC; VC.adicionar(config)` (config = a lista de seções da Central)."""

NORA = ("VOICE CONSISTENCY (clip {clip} of {total}): This is the SAME woman with the SAME voice as in every other clip and every other "
        "video of her. Her voice never changes: American woman in her mid-30s, natural General American accent, mid register, natural "
        "and slightly textured (never smooth, nasal or thin), light warmth in the chest; warm, confident and straight-talking, like a close "
        "friend across a kitchen table; unhurried diction at about 165 words per minute, short clear phrases with a small natural pause "
        "before the key word. Keep the exact same timbre, pitch, accent, pace, volume and energy from the first word to the last. Never "
        "switch to a different voice, a narrator, a younger or older voice, a whisper or a second speaker. Solo monologue only: no "
        "background voices, no music, no sound effects.")

CAMPO = 'Prompt de consistência de voz (opcional)'


def campo(texto=NORA):
    return {'campo': CAMPO, 'valor': 'colar o texto abaixo, sempre igual em todo vídeo da Nora (o {clip} e o {total} ficam assim: a Central troca pelos números)',
            'copiar': texto}


def adicionar(config, texto=NORA):
    """Põe o campo logo depois do "Perfil de voz do personagem" (ou no fim da seção 5). Não duplica."""
    for s in config:
        nomes = [c['campo'] for c in s['campos']]
        if CAMPO in nomes:
            return config
        for i, n in enumerate(nomes):
            if n.startswith('Perfil de voz'):
                s['campos'].insert(i + 1, campo(texto))
                return config
    for s in config:
        if s['secao'].startswith('5'):
            s['campos'].append(campo(texto)); break
    return config
