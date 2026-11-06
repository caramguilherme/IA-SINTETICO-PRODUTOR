---
name: "leitura-discord-mvm"
description: "Use quando o Guilherme pedir pra ler os canais chat-appyon e vitórias-dólar do Discord do MVM Legacy no navegador ao lado: gera os 2 .md com a conversa completa, um .zip com todas as imagens dos canais e um resumo pro Claude Code."
---

# Leitura do Discord MVM Legacy (versão 2, 06/11/2026)

Objetivo: ler chat-appyon e vitórias-dólar desde o ponto que o Guilherme disser, sem perder mensagem nem imagem, e entregar 4 arquivos: os 2 .md com a conversa completa, o .zip com as imagens e o resumo. **Não mexer no doc "Plano MVM Legacy – Appyon" do claude.ai**: desde 06/11 a cópia principal do doc fica no repositório do projeto e quem atualiza é o Claude Code, a partir destes arquivos.

## Regras
- Ele mesmo faz o login. Se cair na tela de login, pedir pra logar e esperar "loguei". Nunca digitar senha.
- Nunca digitar nada na caixa de mensagem do Discord, nunca reagir, nunca clicar em botão de mensagem.
- Não usar WebFetch em link do Loom.
- **Ponto de partida:** o que ele disser na mensagem (o Claude Code manda pronto, ex.: "chat-appyon depois de 06/11 02h36; vitórias-dólar depois de 05/11 18h45"). Horários de Brasília (UTC-3). A última mensagem já lida fica de fora.
- **Nada de resumo nos .md:** cada mensagem inteira, na ordem, com quem respondeu a quem, prévias de link e anexos. O resumo vai em arquivo separado.

## IDs
- Servidor 1295051181344952427
- chat-appyon 1501333667371290745
- vitórias-dólar 1297313696955240538

## Passo a passo
1. Carregar numa chamada só: tabs_context, preview_start, javascript_tool, resize_window, tabs_close, computer (mcp__remote-devices__Claude_Browser__*) e SendUserMessage.
2. preview_start em https://discord.com/channels/1295051181344952427/1501333667371290745. Se a URL virar /login, pedir login.
3. resize_window 1600x2400.
4. Colar o bloco JS abaixo (uma vez por carregamento de página).
5. Rodar `__read('chat','<início em ISO UTC>')` sem await e fazer polling com `for(let i=0;i<38&&!__st.done;i++)await new Promise(r=>setTimeout(r,1000));__st` (o tool corta em 45s; nunca esperar mais de 40s numa chamada).
6. Repetir pra 'vit'.
7. Exportar o texto: `const f=(ch,min)=>Object.values(__D[ch]).filter(x=>x.ts>=min).sort((a,b)=>a.ts<b.ts?-1:1); JSON.stringify({chat:f('chat','<ISO>'),vit:f('vit','<ISO>')})+' '.repeat(70000)` (o espaço força o resultado a ir pra arquivo).
8. **Imagens (sem pular nenhuma):**
   1. Listar todos os anexos de imagem do export (png, jpg, jpeg, webp, gif) dos dois canais, **com a URL assinada inteira** (`?ex=...&is=...&hm=...`; sem a assinatura o link do Discord não abre depois). Dar a cada uma o nome `<canal>_<AAAA-MM-DD>_<HHhMM>_<autor>_<n>.<ext>` (canal = chat ou vit; horário de Brasília; autor sem espaço nem acento).
   2. Baixar, nesta ordem, parando no primeiro que funcionar: (a) Python na sandbox (`urllib.request.urlretrieve(url, caminho)`); (b) pelo navegador, em lotes de até 6: `window.__IMG={}; for(const [nome,url] of lote){const b=await (await fetch(url)).blob(); __IMG[nome]=await new Promise(r=>{const fr=new FileReader();fr.onload=()=>r(fr.result);fr.readAsDataURL(b)});} JSON.stringify(__IMG)+' '.repeat(70000)` e decodificar o base64 em Python; (c) abrir a URL numa aba nova com preview_start, screenshot e fechar a aba (só se (a) e (b) falharem).
   3. **Olhar cada imagem** e escrever em `imagens.json` (`{"<url sem a assinatura>": {"arquivo": "<nome>", "descricao": "<o que mostra>"}}`) uma descrição curta e **a transcrição de todo número e texto que aparece** (painel de vendas, Tracker, prints de configuração, copy, conversa). No vitórias-dólar é obrigatório para todas.
   4. Juntar tudo em `imagens-discord_<sufixo>.zip` (pasta `imagens/` dentro). Vídeo, áudio e PDF do cdn não entram: listar no resumo o que ficou de fora, com a mensagem de origem.
9. Rodar mk.py no arquivo salvo do export, com o corte exato e o `imagens.json`.
10. **Conferência de buraco:** no fim de cada .md, a 1ª mensagem tem de vir logo depois do ponto de partida e a última tem de ser a mais recente do canal. Se houver mais de 2 horas sem mensagem durante o dia (8h a 2h), voltar àquele horário e conferir; anotar no resumo "conferido: sem mensagens de X a Y".
11. resize_window preset desktop. Fechar abas extras.
12. Mandar com SendUserFile: os 2 .md, o .zip e o `resumo-leitura_<sufixo>.md`. Responder curto: período de cada canal, quantas mensagens e imagens, e o que importa.

## Bloco JS

```js
window.__D=window.__D||{chat:{},vit:{}};
const G='1295051181344952427';
window.__C={chat:'1501333667371290745',vit:'1297313696955240538'};
window.__sf=ms=>(BigInt(Math.round(ms)-1420070400000)<<22n).toString();
window.__go=async(ch,ms)=>{history.pushState(null,'','/channels/'+G+'/'+__C[ch]+'/'+__sf(ms));dispatchEvent(new PopStateEvent('popstate'));await new Promise(r=>setTimeout(r,2800));};
window.__scr=function(ch){
  let author=null,n=0;
  for(const li of document.querySelectorAll('li[id^="chat-messages-"]')){
    const id=li.id.split('-').pop();
    const u=li.querySelector('h3 span[id^="message-username-"]');
    if(u) author=u.innerText.trim(); else {let p=li.previousElementSibling;while(p){const uu=p.querySelector&&p.querySelector('h3 span[id^="message-username-"]');if(uu){author=uu.innerText.trim();break;}p=p.previousElementSibling;}}
    const t=li.querySelector('time[id^="message-timestamp-"]');
    const c=li.querySelector('#message-content-'+id);
    const rc=li.querySelector('[id^="message-reply-context-"]');
    let reply=null;
    if(rc){const ru=rc.querySelector('[class*="username"]');const rt=rc.querySelector('[id^="message-content-"]')||rc.querySelector('[class*="repliedTextContent"]');reply=((ru?'@'+ru.innerText.trim()+' ':'')+(rt?rt.innerText:rc.innerText)).replace(/\s+/g,' ').trim();}
    const acc=li.querySelector('[id^="message-accessories-"]');let att=[],emb=[];
    // URL INTEIRA, com a assinatura (?ex=...): sem ela a imagem não baixa depois
    if(acc){acc.querySelectorAll('a[href*="cdn.discordapp.com"],a[href*="media.discordapp.net"],img[src*="discordapp"],video').forEach(e=>{const h=e.href||e.src;if(h&&!h.includes('/emojis/')&&!h.includes('/avatars/'))att.push(h);});acc.querySelectorAll('article').forEach(a=>emb.push(a.innerText.replace(/\s+/g,' ').trim().slice(0,400)));}
    const rec={id,author,ts:t?t.getAttribute('datetime'):null,text:c?c.innerText:'',reply,att:[...new Set(att)],emb};
    if(!__D[ch][id]) n++; __D[ch][id]=rec;
  }
  return n;
};
// Anda pra frente por saltos (não por rolagem, que pula mensagem) e depois confere buracos.
window.__read=async function(ch,startIso,thr=15){
  window.__st={ch,done:false,jumps:0,found:0};
  const mn=Date.parse(startIso);
  const after=()=>Object.values(__D[ch]).filter(x=>x.ts&&Date.parse(x.ts)>=mn).sort((a,b)=>a.ts<b.ts?-1:1);
  try{
    let t=mn;
    for(let i=0;i<80;i++){await __go(ch,t);__st.jumps++;__scr(ch);const k=after();const last=k.length?Date.parse(k[k.length-1].ts):t;if(last<=t)break;t=last+1;}
    await __go(ch,Date.now());__scr(ch);
    for(let pass=0;pass<4;pass++){
      const k=after();const gs=[];
      for(let i=1;i<k.length;i++){const a=Date.parse(k[i-1].ts),b=Date.parse(k[i].ts);if((b-a)/60000>thr)gs.push((a+b)/2);}
      let nf=0;for(const m of gs){await __go(ch,m);__st.jumps++;nf+=__scr(ch);}
      __st.found+=nf;if(nf===0)break;
    }
    const k=after();__st.count=k.length;__st.first=k[0]&&k[0].ts;__st.last=k.length&&k[k.length-1].ts;
  }catch(e){__st.err=String(e);}
  __st.done=true;
};
'ok'
```

Pra parar um job no meio: `const g=__go;window.__go=async()=>0;await new Promise(r=>setTimeout(r,4000));window.__go=g;`

## mk.py

Uso: `python3 mk.py <arquivo salvo do export> <corte chat ISO UTC> <corte vit ISO UTC> <sufixo> "<leitura feita em dd/mm às HHhMM>" [imagens.json]`. O corte é estritamente maior que (ex.: última lida em 01:04:21.776Z → corte 2026-11-04T01:04:22). O sufixo segue o padrão dos arquivos antigos: `06-11_02h36_a_06-11_18h10`.

```python
import json,re,datetime as dt,sys,os
d=json.load(open(sys.argv[1]))
s=json.JSONDecoder().raw_decode(d[0]['text'])[0]
data=json.loads(s.rstrip()) if isinstance(s,str) else s
cut_chat,cut_vit,suf,lida=sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]
IMG=json.load(open(sys.argv[6])) if len(sys.argv)>6 and os.path.exists(sys.argv[6]) else {}
def loc(t): return dt.datetime.fromisoformat(t.replace('Z','+00:00'))-dt.timedelta(hours=3)
def cleanA(a): return re.split(r',|\n',a or '?')[0].strip()
DATA=r' ?(segunda|terça|quarta|quinta|sexta|sábado|domingo)(-feira)?, [0-9]+ de \w+ de 20[0-9]{2} às [0-9]{2}:[0-9]{2}'
def build(msgs,title,canal,after,fname):
    v=sorted([m for m in msgs if m['ts'] and m['ts']>after],key=lambda m:int(m['id']))
    if not v: open(fname,'w').write(f"# {title}\n\nNenhuma mensagem nova ({lida}).\n"); print(fname,0); return
    a=loc(v[0]['ts']); b=loc(v[-1]['ts'])
    nimg=0
    L=[f"# {title} — conversa completa","",f"Canal: {canal} · servidor MVM Legacy",
       f"Período: {a:%d/%m/%Y %Hh%M} até {b:%d/%m/%Y %Hh%M} ({lida})",
       f"Total: {len(v)} mensagens, na ordem do canal. Horário de Brasília. Imagens no zip imagens-discord_{suf}.zip.",""]
    day=None
    for m in v:
        t=loc(m['ts'])
        if t.date()!=day: day=t.date(); L+=["",f"## {t:%d/%m/%Y}",""]
        L.append(f"**{t:%Hh%M} · {cleanA(m['author'])}**")
        if m['reply']:
            r=re.sub(r'\s+',' ',m['reply']).strip().replace('@@','@',1)
            r=re.sub(r' ?\(editado\).*$','',r)
            L.append("> respondendo a: "+r[:220])
        body=re.sub(r' ?\(editado\)','',m['text'] or '')
        body=re.sub(DATA,'',body).strip()
        if body: L.append(body)
        for e in m['emb']: L.append("Prévia de link: "+re.sub(r'\s+',' ',e).strip()[:400])
        vistos=set()
        for u in m['att']:
            base=u.split('?')[0]
            if base in vistos: continue
            vistos.add(base)
            if base in IMG:
                nimg+=1
                i=IMG[base]; L.append(f"Imagem: imagens/{i['arquivo']}"+(f" — {i['descricao']}" if i.get('descricao') else ""))
            else:
                L.append("Anexo: "+base)
        if not body and not m['att'] and not m['emb']: L.append("_(só figurinha ou reação)_")
        L.append("")
    open(fname,'w').write("\n".join(L)); print(fname,len(v),'mensagens',nimg,'imagens',a,b)
build(data['chat'],"Chat-appyon","#💬︱chat-appyon",cut_chat,f"chat-appyon_{suf}.md")
build(data['vit'],"Vitórias-dólar","#🏆︱vitórias-dólar",cut_vit,f"vitorias-dolar_{suf}.md")
```

## O resumo (`resumo-leitura_<sufixo>.md`, pro Claude Code)
1. **Conferência:** período de cada canal (1ª e última mensagem), número de mensagens e de imagens, buracos conferidos, o que não baixou.
2. **Resultados com número:** quem, data, funil (Manifestation, Love Reading, Love Chart/Soulmate, ou "funil não dito") e os números do print (vendas, comissão, cliques, checkouts, conversão), com o nome do arquivo da imagem. Separados por funil.
3. **Estratégias, dicas e avisos oficiais** (Appyon, Gustavo, Iorhan, Ju, staff), com quem disse e o horário. Problema com solução junto.
4. **Perguntas sem resposta** no chat (quem perguntou, horário, a pergunta), para o Claude Code ver o que a Nora já sabe responder.
5. **Menções ao Guilherme** e respostas às mensagens dele.
Nada de parabéns solto nem papo sem informação. Português coloquial, frases curtas.
