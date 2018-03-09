Liste trajet (a, x, b, y, S, F, t); avec t = (|a-x|+|b-y|)
if (t>(F-S)) => abandonner

Creer une liste de véhicules avec (R, C, tempsAvantDispo)

Pour les trajets commençant à T=0 => attribuer un véhicule sur l'intersection (augmenter tempsAvantDispo de t, remplacer R par x et C par y), sinon abandonner

à chaque incrémentation de T, diminuer tempsAvantDispo de 1 (min 0)

Pour les trajets à T=X => attribuer un véhicule à 0 ou Y (Y étant la distance entre la position du véhicule et le point de départ du trajet : |R-a|+|C-b|) avec tempsAvantDispo < Y) (selon le nombre de véhicules présents aux intersections correspondantes)
