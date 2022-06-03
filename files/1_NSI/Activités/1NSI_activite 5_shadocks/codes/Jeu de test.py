# Jeu de test du convertisseur Shadocks

assert chiffreShadDec('GA') == 0, 'chiffreShadDec error'
assert chiffreShadDec('BU') == 1, 'chiffreShadDec error'
assert chiffreShadDec('ZO') ==2, 'chiffreShadDec error'
assert chiffreShadDec('MEU') == 3, 'chiffreShadDec error'
assert decoupeNbreShad('GA BU ZO MEU')== ['GA', 'BU', 'ZO', 'MEU'], 'decoupe error'
assert convShadDec('ZO MEU') == 11, 'conversion error'
assert convShadDec('BU GA ZO') == 18, 'conversion error'
assert convShadDec('BU ZO GA MEU') == 99, 'conversion error'
print('Test finished without error')