import pingouin as pg
from factor_analyzer import calculate_kmo, calculate_bartlett_sphericity

# Cronbach Alpha
alpha = pg.cronbach_alpha(df[items])[0]
print("Cronbach Alpha:", alpha)

# Validitas item
r = item.corr(total_score - item)

# KMO & Bartlett
kmo, kmo_model = calculate_kmo(data)
chi, p = calculate_bartlett_sphericity(data)
