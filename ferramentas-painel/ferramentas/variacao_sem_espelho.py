# Roda o editar_simples_2311.py com a variação do Face SEM o espelho (a bandeira dos EUA no quadro não pode ficar invertida).
import sys, runpy
sys.path.insert(0, '/workspace/IA-SINTETICO-PRODUTOR/ferramentas-painel/ferramentas')
import variacao_face as VF
VF.BRILHO = VF.BRILHO.replace('hflip,', '')
assert 'hflip' not in VF.BRILHO
sys.argv = ['editar_simples_2311.py'] + sys.argv[1:]
runpy.run_path('/workspace/IA-SINTETICO-PRODUTOR/ferramentas-painel/dia-2311/editar_simples_2311.py', run_name='__main__')
