import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

model = ols('Y ~ C(Treatment)', data=df).fit()
anova_table = sm.stats.anova_lm(model)

print(anova_table)

# Tukey
tukey = pairwise_tukeyhsd(df['Y'], df['Treatment'])
print(tukey)
