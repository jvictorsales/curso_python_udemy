"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
....<- Contagem de complexidade (ruim)
"""

velocidade = 60  # velocidade atual do carro
local_carro = 99  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # a distância onde o radar pega

alcance_minimo_do_radar_1 = LOCAL_1 - RADAR_RANGE
alcance_maximo_do_radar_1 = LOCAL_1 + RADAR_RANGE
velocidade_do_carro_acima_do_limite_do_radar_1 = velocidade > RADAR_1
carro_dentro_do_range_do_radar_1 = (local_carro >= alcance_minimo_do_radar_1) and (local_carro <= alcance_maximo_do_radar_1)
carro_multado_no_radar_1 = carro_dentro_do_range_do_radar_1 and velocidade_do_carro_acima_do_limite_do_radar_1

if carro_dentro_do_range_do_radar_1:
    print('Você está no range de atuação do radar.')
    if carro_multado_no_radar_1:
        print('Você está acima do limite de velocidade. Carro multado.')
    else:
        print('Você não atingiu o limite de velocidade.')
else:
    print('Você não está no range de atuação do radar.')
