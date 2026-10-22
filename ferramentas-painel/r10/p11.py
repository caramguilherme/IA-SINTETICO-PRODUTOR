# -*- coding: utf-8 -*-
# Imagem A (nora30 e nora31): cozinha à noite + geodo de ametista grande.  Imagem B (nora32 e nora33): varanda + cristal de quartzo rosa grande.
import sys
SPD='/tmp/claude-0/-home-user-IA-SINTETICO-PRODUTOR/44224f14-0984-54fb-bdf2-ce721dd3e853/scratchpad/'
for d in ('r10','r9','r8','r7','r6'): sys.path.insert(0,SPD+d)
import p9, mov10
p8=p9.p8; P=p8.P
# --- Imagem A
OBJ_A=("LIVRE: Half of an open amethyst geode about 18 cm wide and 14 cm tall: a rough dark grey stone shell on the outside and a hollow cavity packed with deep purple amethyst crystals of different sizes, facing the lens. It is held by her right hand with the fingers curled around the lower edge of the shell and the thumb on its outer rim, tilted about 20 degrees toward the lens so the whole cavity is visible, about 30 cm from the lens and 15 cm from her cheek, filling about a third of the frame width on the left side of the image without covering her face or her chin. It is in sharp focus, the crystals glittering in the warm lamp light. No glow, no magic light, no particles, no ring or other object inside, no letters, no numbers")
vA=dict(p9.VAR['nora31']); vA['obj']=OBJ_A
vA['pose']=vA['pose'].replace('holding the heart stone','holding the geode')
vA['roupa']=vA['roupa']
P.VAR['nora30']=vA
P.FIG['nora30']=p8.FIGX("deep forest-emerald (dark green with a slight blue tone) waffle-knit top with a smooth matte finish and a round neckline, no print, embroidery or shine; plain dark straight trousers.","the amethyst geode")
# --- Imagem B
OBJ_B=("LIVRE: One large raw rose quartz crystal cluster about 15 cm tall and 10 cm wide: translucent pale pink crystal points of different sizes growing from a rough milky-white base, catching a soft highlight. It is held upright by her right hand, the thumb and fingers wrapped around the base, tilted slightly toward the lens, about 30 cm from the lens and 15 cm from her cheek, on the left side of the image, so the whole cluster is visible without covering her face. It is in sharp focus. No glow, no magic light, no particles, no letters, no numbers, no cord, no second crystal")
vB=dict(p9.VAR['nora32']); vB['obj']=OBJ_B
vB['pose']=vB['pose'].replace('holding the key','holding the crystal')
P.VAR['nora32']=vB
P.FIG['nora32']=p8.FIGX("deep navy-blue (almost black) fine ribbed knit top with a round neckline, no print, embroidery or shine; plain dark straight trousers.","the rose quartz crystal")
# --- movimentação: mão livre fora do quadro (abaixo da borda), objeto na mão direita (lado esquerdo da imagem)
def fix(c):
    return (c.replace("resting on her right knee","out of frame below the bottom edge").replace("onto her right knee","out of frame below the bottom edge").replace("from her lap","from below the bottom edge"))
def lines(objdesc):
    out=[p9.LL(objdesc,fix(c)) for c in mov10.CORES]
    out[2]=out[2].replace("her right hand keeps holding","the hand on the left side of the frame keeps holding").replace("from the end of the final sentence of the take until the clip ends","from the final word of the take to the last frame of the clip")
    return out
p8.MOVL['nora30']=lines("half amethyst geode with its purple crystals facing the lens")
p8.MOVL['nora32']=lines("large rose quartz crystal cluster held upright")
# --- travas de continuidade
p8.GLOBAL['nora30']=p9.GL("in a home kitchen at night with warm yellow lamp light",
 ("deep forest-emerald waffle-knit top",
  "she sits upright on a wooden kitchen chair leaning slightly toward the camera, framed from the top of her head to the middle of her chest, her right hand holds the half amethyst geode with its deep purple crystals facing the lens beside her face on the left side of the frame for the whole clip, and the geode never changes hands, never turns away, never tilts further and never drops; her left hand rests out of frame below the bottom edge on her left thigh unless a gesture is described;",
  "the white wall, the white cabinet door, the stone countertop, the small flag in the ceramic jar, the dark window and the warm pendant lamp light stay exactly where they are and never move;",
  "real quiet kitchen room sound only, no music."))
p8.GLOBAL['nora32']=p9.GL("on a home front porch in soft overcast daylight",
 ("deep navy-blue ribbed knit top",
  "she sits on the top wooden step of the porch leaning slightly toward the camera, framed from the top of her head to the middle of her chest, her right hand holds the large rose quartz crystal cluster upright beside her face on the left side of the frame for the whole clip, and the crystal never changes hands, never turns away, never tilts further and never drops; her left hand rests out of frame below the bottom edge on her left thigh unless a gesture is described;",
  "the white front door with its brass doorknob, the small American flag on the siding, the white porch column and the gray floorboards stay exactly where they are and never move;",
  "real outdoor porch ambient sound only, no music."))

# ===== IMAGEM A aprovada em 21/10/2026: o geodo está na mão ESQUERDA dela (lado DIREITO da imagem); a mão direita fica livre =====
def mirror(c):
    return c.replace('left','@@').replace('right','left').replace('@@','right')
CORES_A=[mirror(fix(c)) for c in mov10.CORES]
# T3: sem "right hand" (a fala diz "Close your right hand") nem "until the end"
CORES_A[2]=("she gives one slow nod during the first sentence of the take, then during the second sentence she raises the free hand, the one on the left side of the frame, from below the bottom edge to shoulder height and opens it palm toward the camera, holds it for about two seconds and lowers it out of frame below the bottom edge")
def LLm(obj,core):
    return ("Throughout the whole 10 seconds her left hand keeps holding the "+obj+" steady beside her face on the right side of the frame and it never changes hands, never turns away, never drops and never covers her face, her right hand rests out of frame below the bottom edge on her right thigh except when a gesture is described, her eyes stay on the lens, and "+core+", and from the end of the final sentence of the take until the clip ends she keeps her lips closed and silent; everything else in the scene stays completely still and each hand has exactly five fingers.")
OBJ_A_DESC="slab of amethyst crystals with its deep purple crystals facing the lens"
LA=[LLm(OBJ_A_DESC,c) for c in CORES_A]
LA[2]=LA[2].replace("her right hand rests out of frame below the bottom edge on her right thigh","the free hand rests out of frame below the bottom edge").replace("from the end of the final sentence of the take until the clip ends","from the final word of the take to the last frame of the clip")
p8.MOVL['nora30']=LA
p8.GLOBAL['nora30']=p9.GL("in a home kitchen at night with warm yellow lamp light",
 ("deep forest-green waffle-knit top",
  "she sits upright facing the camera, leaning slightly toward it, framed from the top of the kitchen window down to her waist, her left hand holds the slab of amethyst crystals with its deep purple crystals facing the lens beside her face on the right side of the frame for the whole clip, and the amethyst never changes hands, never turns away, never tilts further and never drops; her right hand rests out of frame below the bottom edge on her right thigh unless a gesture is described;",
  "the white cabinet at the upper left, the black coffee machine at the left edge, the window with the dark night and the hanging pendant lamp at the upper right, the granite counter with the soap dispenser at the right stay exactly where they are and never move;",
  "real quiet kitchen room sound only, no music."))
