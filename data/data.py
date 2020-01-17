import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('./weibo.xls',encoding="unicode_escape")
print(df.head())
sns.lmplot('attitudes' ,'comments', df, hue = 'id', fit_reg=False)
# hue用于分类
plt.show()
