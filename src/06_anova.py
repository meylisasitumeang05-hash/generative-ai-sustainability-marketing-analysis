import scipy.stats as stats

# contoh ANOVA
f_stat, p_val = stats.f_oneway(group1, group2, group3)

print("F-statistic:", f_stat)
print("p-value:", p_val)
