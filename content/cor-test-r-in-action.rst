统计中的样本检验基础和R实践
###########################

:date: 2014-05-07 05:07
:author: caesar0301
:category: Data mining
:tags: data mining, hypothesis testing, R, t-test
:slug: 统计中得样本检验基础和R实践

本文总结了\ `R in Action`_\ 一书中提到的关于样本检验的内容，以概要的形式提供给读
者以及自己参考。

*注: H0表示空假设，即样本检测的假设对象。*


**独立性检验（列联表）**\ ：

#. 卡方检验：\ *H0:假设二维表的行和列变量相互独立。*\ stats包的\
   **chisq.test()**.
#. Fisher精确检验: \ *H0:边界固定的二维列联表行和列独立。*\ stats包的\
   **fisher.test()**
#. Cochran-Mantel-Haenszel检验：\ *H0:两个名义变量在第三个变量的每一层中都是条件
   独立的。*\ stats包的.test().


**相关性检验**\ ：


#. 常用系数：Pearson, Spearman, Kendall, 偏相关系数, 多分格polychoric,多系列
   polyserial.
#. PSK: 相关系数\ **cor()**, 协方差\ **cov()**, psych包的\ **corr.test()**
#. 偏相关：控制一个或多个定量变量，检验另外两个变量之间的相关性。ggm包的\
   **pcor()**,
#. 其他类型：polycor包的\ **hetcor()**\ 有多种其他类型的相关函数


**相关显著性检验**\ ：

#. PSK: **cor.test(), corr.test()**.后者可同时检测多种相关关系。
#. 其他类型：psych包的\ **pcor.test() & r.test()**


**分组检测**\ ：

1) 参数检验

- 独立样本t检验：*H0:被检验的两组样本独立且均值相等，并且从正态总体中抽的。*\
  stats包的\ **t.test()**
- 非独立样本t检验：两组观测相关，一般通过非独立组设计获得，如pre-post design,
  repeated measures design.  *H0：假定组间差异呈正态分布，且均值相等。*\ stats包
  的\ **t.test(.. , paired=TRUE)**\ 。
- 多于两组的非独立样本：如果对比组大于2且满足数据是从正态总体中独立抽样获得的假
  设，可采用ANOVA方差分析。

2) 非参数检验

- 两组独立样本：可以使用Wilcoxon秩和检验(Mann-Whitney U检验), **wilcox.test()**
- 两组非独立样本：可以使用Wilcoxon符号秩检验。它适用于两组成对数据且无法保证正态
  性假设的情景。stats包的\ **wilcox.test(.., paired=TRUE)**.
- 多于两组的样本：如果各组样本独立，则可使用Krushkal-Wallis检验；如果不独立，可
  使用Friedman检验。\ *H0:各组的平均值相同。*\ stats包的\ **kruskal.test() &
  friedman.test()**\ 。npmc包的\ **npmc()**\ 函数可实现非参数的多组比较。

*通常独立样本也被称作单样本(one-sample)检验，非独立样本被称作双样本(two-sample)
检验。单样本检验的自由度是n1+n2-1，双样本检验自由度是n/2-1.*


**样本检验的一般步骤**\ ：

#. 提出研究问题，总结出需要通过数据分析得出的问题。
#. 描述空假设和被选假设。空假设的提出通常需要能够通过数据分析得出“接受”或“拒绝”
   的结论，如均值相等，均值大于X0等。
#. 清楚假设条件。检验过程是在一定的假设条件下进行的，比如通常需要考虑，样本是否
   独立分布，均值和方差的统计分布等。
#. 根据样本数量和假设条件，选择合适的检验方法，如t检验，以及检验统计量T。
#. 在空假设和观测样本的基础上，计算检验的统计分布，如学生分布或正态分布。
#. 选择合适的统计显著水平p-value，常用的5%和1%。
#. 计算检验统计量T的拒绝区间(critical region)，即在该区间内，空假设即被拒绝为真。
#. 根据观测样本，计算检验统计量的观测直t\_obs。
#. 得出结论：如果t\_obs落在拒绝区间里，则拒绝空假设；否则，无法拒绝空假设。


相关链接：

- Statistical hypothesis testing: `wikipedia`_
- Exploratory data analysis: `wikipedia
  <http://en.wikipedia.org/wiki/Exploratory_data_analysis>`__
- `Quick-R: t-test`_


.. _本文: http://www.hsiamin.com/blog/?p=77
.. _R in Action: http://www.amazon.com/R-Action-Robert-Kabacoff/dp/1935182390
.. _wikipedia: http://en.wikipedia.org/wiki/Statistical_hypothesis_testing
.. _`Quick-R: t-test`: http://www.statmethods.net/stats/correlations.html
