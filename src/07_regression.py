import statsmodels.formula.api as smf

model = smf.ols("Y_PI_mean ~ M2_TR_mean", data=df).fit()

print(model.summary())
