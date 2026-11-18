# Configuração do Muse para a Nora (18/11/2026 ~11h40)

Montada a partir do painel do nora70 (`PAINEL-NORA70.html`): a voz é o perfil de voz LIVRE da Central (o mesmo desde outubro), a continuidade é o LIVRE do nora70, a fala e a movimentação do T01 são as do painel, e a imagem C é o prompt do hook. Formato dos blocos: o do Prompt Mestre do Vinicius (`netlify/PROMPT-MESTRE-CHATGPT.txt`, seção 11). Regras de isolamento: `LEIA.md` e a seção 2 do `CLAUDE.md`.

## Passo 0: responder ao Muse
O Muse pergunta "qual é o seu nome?": responder só **Gui**.

## Passo 1: configurar (colar uma vez)
```
Hi Muse. My name is Gui. In this account you have one job: to generate images and short vertical video clips for one fictional AI character, Nora Kensley, an AI tarot and manifestation creator. Follow these permanent rules in this whole account.

ACCOUNT AND SAFETY RULES
1. Never connect, link or ask me to connect any account or app (Instagram, Facebook, WhatsApp, email, calendar or any other). Never post, publish, upload, send messages or make purchases anywhere. You only create files that I download myself.
2. Do not create scheduled tasks, heartbeats or proactive check-ins. Only act when I send a request.
3. Ask me before any action that is not generating an image or a video.

VIDEO RULES (every clip)
- Vertical 9:16, maximum 10 seconds per clip, one clip per block, generated in order and named with the block name I give.
- The image I attach is the first frame of every clip. Never use a frame from a generated clip as the next first frame.
- Spoken words: exactly the words in the DIALOGUE line, in American English, each word once and in order. Never add, remove, repeat, translate, rephrase or reorder words. Numbers and dates are spoken as written.
- If a line is refused or blocked, do not rewrite it yourself: tell me which block and wait. I will send the approved replacement.
- Speech starts within the first 0.15 seconds, with no opening breath. When the last word ends she closes her lips and stays silent until the clip ends.
- No on-screen text, no captions, no music and no sound effects: only her voice and quiet room sound.
- Keep the face, hair, jewelry, clothes, hands (exactly five fingers each), objects and background exactly as in the first frame. No zoom, no cuts and no camera moves unless I ask.

NORA_VOICE_LOCK (use this exact text, unchanged, in every clip where Nora speaks):
[Voice and Audio Instructions]

Voice Profile: Woman, mid-30s, American, warm, magnetic and confident voice — sounds like a straight-talking friend who knows astrology and says things plainly, with a bright, high-vibe warmth. Natural General American accent, unhurried diction.

Vocal Characteristics: Mid register, natural and slightly textured (not smooth or polished), light warmth in the chest, never nasal or thin.

Tone: Warm, confident and firm, with an upbeat, high-vibe energy. Not theatrical, not "spooky", no performance — she says things the way a close friend would across a kitchen table. Honest and direct, with occasional soft warmth. Never sugarcoats, never scolds.

Delivery style: Short, clear phrases with a natural pause before the key word. Sounds like she's speaking directly to one person, not performing for a crowd.

Naturalness: The voice must sound as natural and human as possible — real breathing, natural micro-pauses, subtle imperfections, organic intonation shifts. It must NEVER sound robotic, synthetic, flat, or AI-generated. No text-to-speech cadence of any kind.

Technical Settings: STRICTLY a solo monologue. The speaker is completely ALONE. Absolutely NO background voices, ZERO interviewer noises, and STRICTLY NO agreement sounds (like 'mhm', 'yeah', 'aha', 'uh-huh'). NO background music, NO sound effects, NO automatic subtitles. Output must be a 100% clean, raw voice track. STRICTLY DO NOT imitate or impersonate any famous public figure or celebrity — the voice must be entirely original.

Save these rules and NORA_VOICE_LOCK as permanent instructions for this account. Reply in Portuguese with a 5-line summary of how you will work. Do not generate anything yet.
```

## Passo 2: apagar as 2 tarefas programadas
No painel da direita do Muse, "Ver todas as tarefas programadas": apagar o **Heartbeat** (roda o agente sozinho a cada 30 min; provavelmente gasta tokens) e o **Tour de recursos para agente** (19/11 9:39).

## Passo 2b: o teste de qualidade (pedido do aluno, 18/11 ~11h42: "quero testar o muse antes, pra ver como sai o video, quanto gasta, voz, tudo")
A mesma imagem, a mesma fala e o mesmo prompt do T01 do nora69 (postado em 17/11, gerado no Flow), para comparar o Muse com o Flow no mesmo take. Anexar `ferramentas-painel/dia-1711/d1711-PRE-carro-IMG-C-escolhida-opcao1.jpg`. Antes, o print da tela "Utilização" (0% no grátis, 1 bi nos adicionais); depois, outro print. Colar:
```
Generate ONE video clip now. This is a quality test. Use the attached image as the first frame.

BLOCK 01 / 01 — 19 WORDS — name: teste-muse-carro-T01
SOURCE FRAME: the attached image (Nora in the driver's seat of a dark gray pickup truck, seatbelt on, one hand on the steering wheel, the other pointing at the lens)
MAX CLIP DURATION: 10 seconds
TARGET SPEECH RATE: 165 WPM
ESTIMATED SPOKEN TIME: 6.9 seconds

CANONICAL VOICE LOCK (VERBATIM):
[Voice and Audio Instructions]

Voice Profile: Woman, mid-30s, American, warm, magnetic and confident voice — sounds like a straight-talking friend who knows astrology and says things plainly, with a bright, high-vibe warmth. Natural General American accent, unhurried diction.

Vocal Characteristics: Mid register, natural and slightly textured (not smooth or polished), light warmth in the chest, never nasal or thin.

Tone: Warm, confident and firm, with an upbeat, high-vibe energy. Not theatrical, not "spooky", no performance — she says things the way a close friend would across a kitchen table. Honest and direct, with occasional soft warmth. Never sugarcoats, never scolds.

Delivery style: Short, clear phrases with a natural pause before the key word. Sounds like she's speaking directly to one person, not performing for a crowd.

Naturalness: The voice must sound as natural and human as possible — real breathing, natural micro-pauses, subtle imperfections, organic intonation shifts. It must NEVER sound robotic, synthetic, flat, or AI-generated. No text-to-speech cadence of any kind.

Technical Settings: STRICTLY a solo monologue. The speaker is completely ALONE. Absolutely NO background voices, ZERO interviewer noises, and STRICTLY NO agreement sounds (like 'mhm', 'yeah', 'aha', 'uh-huh'). NO background music, NO sound effects, NO automatic subtitles. Output must be a 100% clean, raw voice track. STRICTLY DO NOT imitate or impersonate any famous public figure or celebrity — the voice must be entirely original.

DIALOGUE — EXACT WORDS ONLY:
"Keep your mouth shut if this video showed up for you on Tuesday, November seventeenth or Wednesday, November eighteenth."

ACTION / PERFORMANCE:
Throughout the whole 10 seconds the phone stays mounted on the dashboard in front of her with an unchanged framing while the truck keeps rolling slowly forward and the houses and trees glide past the windows behind her; the hand that holds the steering wheel stays on the wheel the whole time and only makes tiny natural steering corrections; the seatbelt stays across her chest; with her other hand she points her index finger straight at the lens and keeps it there, with a serious, knowing look; her eyes stay on the lens; from the end of the final sentence of the take until the clip ends she keeps her lips closed and silent; no zoom and no cuts, the braid stays in place and each hand has exactly five fingers.

TIMING:
Begin the first word at 0.00 to 0.15 seconds. Speak each word exactly once. Complete every word before the clip ends. No opening breath, no unnecessary silence, no repeated phrase and no clipped final word.

CONTINUITY:
Casual real video in the afternoon inside a dark gray pickup truck that is driving slowly along a quiet American suburban street, filmed by a phone mounted on the dashboard about 60 centimeters in front of her at face height, looking exactly like a real phone video, lit by soft natural daylight through the windows. She sits in the driver's seat. The truck keeps moving slowly forward during every take: through the side and rear windows the houses, lawns and trees glide past smoothly and the daylight shifts gently across her face; the camera moves only with the very slight vibration of the road. CONTINUITY LOCKS for every take: the woman, her face, her long black wavy hair, the thin braid wrapped with small gold rings, the small flat gold crescent moon on her cheek on the left side of the frame with three tiny separate gold five-pointed stars next to it (three stars with visible points, never dots or circles), her star-and-moon drop earrings, her thin gold Venus necklace, the thin gold bracelets and the gold sun ring, her light heather-gray fitted ribbed top under a long open black knit cardigan, and the steering wheel, the seatbelt across her chest and the truck's interior stay exactly as in the reference image; the framing is exactly the one of the reference image, her face in the upper middle of the frame; the hand that holds the steering wheel stays on the wheel the whole time and only makes tiny natural steering corrections; the seatbelt stays across her chest; natural skin texture with visible pores, slight phone grain, everything in focus, no bokeh, no filter, no glow and no sparkles; no zoom, no cuts and no reframing; no phone, phone stand, tripod, object, person, animal or text appears or disappears; each hand always has exactly five fingers; no on-screen text, no captions; quiet car interior sound and a soft road hum only, no music. SPEECH RULE for every take: she says only the exact words of that take's script, each word exactly once and in order, with no repeated word, no extra word and no added sentence before, between or after; numbers and dates are spoken as words exactly as written; she speaks in a direct, serious, intimate tone, like telling a secret to one person; when she finishes the last word she closes her lips, stays silent and keeps a calm still expression until the clip ends.
```

## Passo 3: a imagem C do nora70 (só se o Flow grátis não gerar imagem)
Anexar, nesta ordem: 1º `ferramentas-painel/dia-1511/d1511-PRE-sal-IMG-C-escolhida-opcao2.jpg` (a Nora aprovada), 2º a folha da Nora (1K). Colar:
```
Generate 4 different options of one vertical 9:16 photo, following this description exactly. Name them d1711-PRE-alcapao-IMG-C (options 1 to 4).

the first image is the approved photo of the woman (keep exactly her face, her long black wavy hair, the thin braid with small gold rings, the small flat gold crescent moon with three tiny gold five-pointed stars on her cheek, her star-and-moon earrings, her gold Venus necklace, the thin gold bracelets and the gold sun ring); the second image is her character sheet (same woman, same face). Same woman and same face: change her clothes to her cream silky long-sleeve wrap blouse tied at the waist and her beige knee-length wrap skirt; change the place and the light: an upstairs hallway of an American home with white walls, white doors and a white ceiling, soft warm indoor evening light; an aluminum stepladder stands in the hallway right under a white square attic hatch in the ceiling. RAW photo taken from about one meter in front of her at chest height: she stands on the stepladder framed from the waist up, her face in the upper middle of the image, looking straight into the camera with a serious, knowing look and her lips closed; an old painted resin statue of Saint Michael the Archangel, about 35 centimeters tall, with large beige-brown painted wings, silver-gray armor, a faded pinkish-red cape, one arm raising a sword high, standing on a rocky painted base, covered with a thin layer of grey dust stands on the flat top cap of the ladder right beside her, on the side of the image, fully visible and never covering her face; one hand rests on the top rail of the ladder; her other hand is raised in front of her chest, pointing her index finger straight at the lens; the open dark attic hatch is in the ceiling above her; the upper 15 percent of the image is the plain white ceiling; looks exactly like a real casual iPhone photo, slight phone grain, natural colors, everything in focus, no bokeh; no glow, no sparkle, no light effect; no phone, phone stand or tripod anywhere in the image; no text and no logo anywhere; each hand has exactly five fingers; photorealistic, unretouched, vertical 9:16
```

## Passo 4: o teste do T01 (depois de escolher a imagem C)
Anexar a imagem C escolhida. Colar:
```
Generate ONE video clip now. This is a test of one block. Use the attached image as the first frame.

BLOCK 01 / 17 — 22 WORDS — name: d1711-alcapao-T01-abertura-data
SOURCE FRAME: the attached image (Nora standing on an aluminum stepladder under the open attic hatch, with the dusty angel statue on the top cap of the ladder beside her)
MAX CLIP DURATION: 10 seconds
TARGET SPEECH RATE: 165 WPM
ESTIMATED SPOKEN TIME: 8.0 seconds

CANONICAL VOICE LOCK (VERBATIM):
[Voice and Audio Instructions]

Voice Profile: Woman, mid-30s, American, warm, magnetic and confident voice — sounds like a straight-talking friend who knows astrology and says things plainly, with a bright, high-vibe warmth. Natural General American accent, unhurried diction.

Vocal Characteristics: Mid register, natural and slightly textured (not smooth or polished), light warmth in the chest, never nasal or thin.

Tone: Warm, confident and firm, with an upbeat, high-vibe energy. Not theatrical, not "spooky", no performance — she says things the way a close friend would across a kitchen table. Honest and direct, with occasional soft warmth. Never sugarcoats, never scolds.

Delivery style: Short, clear phrases with a natural pause before the key word. Sounds like she's speaking directly to one person, not performing for a crowd.

Naturalness: The voice must sound as natural and human as possible — real breathing, natural micro-pauses, subtle imperfections, organic intonation shifts. It must NEVER sound robotic, synthetic, flat, or AI-generated. No text-to-speech cadence of any kind.

Technical Settings: STRICTLY a solo monologue. The speaker is completely ALONE. Absolutely NO background voices, ZERO interviewer noises, and STRICTLY NO agreement sounds (like 'mhm', 'yeah', 'aha', 'uh-huh'). NO background music, NO sound effects, NO automatic subtitles. Output must be a 100% clean, raw voice track. STRICTLY DO NOT imitate or impersonate any famous public figure or celebrity — the voice must be entirely original.

DIALOGUE — EXACT WORDS ONLY:
"Keep your mouth shut. If this video showed up for you on November eighteenth, do not tell anyone what's about to happen."

ACTION / PERFORMANCE:
Throughout the whole 10 seconds the camera stays static at her chest height in front of her with an unchanged framing; the hand that rests on the top rail of the ladder stays there the whole time; the dusty angel statue with golden wings stands still on the top cap of the ladder beside her and never moves; with her other hand she points her index finger straight at the lens and keeps it there, with a serious, knowing look; her eyes stay on the lens; from the end of the final sentence of the take until the clip ends she keeps her lips closed and silent; no zoom and no cuts, the braid stays in place and each hand has exactly five fingers.

TIMING:
Begin the first word at 0.00 to 0.15 seconds. Speak each word exactly once. Complete every word before the clip ends. No opening breath, no unnecessary silence, no repeated phrase and no clipped final word.

CONTINUITY:
Casual real video in the evening in a bright upstairs hallway of an American home with white walls and a white ceiling, filmed from a static camera at her chest height about one meter in front of her, looking exactly like a real phone video, lit by soft warm indoor light. She stands on an aluminum stepladder right under the open attic hatch. CONTINUITY LOCKS for every take: the woman, her face, her long black wavy hair, the thin braid wrapped with small gold rings, the small flat gold crescent moon on her cheek on the left side of the frame with three tiny separate gold five-pointed stars next to it (three stars with visible points, never dots or circles), her star-and-moon drop earrings, her thin gold Venus necklace, the thin gold bracelets and the gold sun ring, her cream silky long-sleeve wrap blouse tied at the waist and her beige knee-length wrap skirt, and the dusty angel statue with golden wings on the top of the ladder, the aluminum stepladder and the open attic hatch above stay exactly as in the reference image; the framing is exactly the one of the reference image, her face in the upper middle of the frame; the hand that rests on the top rail of the ladder stays there the whole time; the dusty angel statue with golden wings stands still on the top cap of the ladder beside her and never moves; natural skin texture with visible pores, slight phone grain, everything in focus, no bokeh, no filter, no glow and no sparkles; no zoom, no cuts and no reframing; no phone, phone stand, tripod, object, person, animal or text appears or disappears; each hand always has exactly five fingers; no on-screen text, no captions; quiet indoor room sound only, no music. SPEECH RULE for every take: she says only the exact words of that take's script, each word exactly once and in order, with no repeated word, no extra word and no added sentence before, between or after; numbers and dates are spoken as words exactly as written; she speaks in a direct, serious, intimate tone, like telling a secret to one person; when she finishes the last word she closes her lips, stays silent and keeps a calm still expression until the clip ends.
```
Depois: baixar o clipe e mandar para o Claude, junto com o print da tela "Utilização" (para medir quantos tokens custa 1 take de 10 s).
