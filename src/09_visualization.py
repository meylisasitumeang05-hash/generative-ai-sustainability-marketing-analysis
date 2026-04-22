import seaborn as sns
import matplotlib.pyplot as plt

# Boxplot treatment
sns.boxplot(x="Treatment", y="Y_PI_mean", data=df)
plt.title("Purchase Intention by Treatment")
plt.show()
