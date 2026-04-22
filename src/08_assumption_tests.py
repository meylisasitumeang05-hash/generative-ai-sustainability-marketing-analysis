from scipy.stats import shapiro
import statsmodels.api as sm

# Normality test
stat, p = shapiro(model.resid)
print("Shapiro p-value:", p)

# QQ Plot
sm.qqplot(model.resid, line="45")
