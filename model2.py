import pandas as pd
import matplotlib.pyplot as plt #导入图像库
import statsmodels.api as sm
from sklearn.metrics import roc_curve, auc
from pylab import mpl
from sklearn.linear_model import LogisticRegression

if __name__ == '__main__':
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

    data = pd.read_csv('WoeData.csv')
    Y = data['SeriousDlqin2yrs']
    X = data.drop(['SeriousDlqin2yrs', 'DebtRatio', 'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans', 'NumberRealEstateLoansOrLines', 'NumberOfDependents'], axis=1)
    X1 = sm.add_constant(X)
    #
    logit = sm.Logit(Y, X1)
    result = logit.fit()
    print(result.params)
    # print(result.summary())

    classifier = LogisticRegression()
    result = classifier.fit(X1, Y)
    print(result.intercept_ )
    print(result.coef_ )

    # test = pd.read_csv('TestWoeData.csv')
    # Y_test = test['SeriousDlqin2yrs']
    # X_test = test.drop(['SeriousDlqin2yrs', 'DebtRatio', 'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans','NumberRealEstateLoansOrLines', 'NumberOfDependents'], axis=1)
    # X3 = sm.add_constant(X_test)
    # resu = result.predict(X3)
    # fpr, tpr, threshold = roc_curve(Y_test, resu)
    # rocauc = auc(fpr, tpr)
    # plt.plot(fpr, tpr, 'b', label='AUC = %0.2f' % rocauc)
    # plt.legend(loc='lower right')
    # plt.plot([0, 1], [0, 1], 'r--')
    # plt.xlim([0, 1])
    # plt.ylim([0, 1])
    # plt.ylabel('真正率')
    # plt.xlabel('假正率')
    # plt.show()