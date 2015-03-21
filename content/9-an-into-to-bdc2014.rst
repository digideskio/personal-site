第二届中国大数据技术创新大赛及Spark基本使用
############################################

:date: 2014-10-30
:author: Xiaming Chen
:tags: Spark, Python
:slug: an-into-to-bdc2014


中国计算机协会近期举办的“`第二届中国大数据技术创新大赛
<http://bigdatacontest.ccf.org.cn/index.html>`_”，的确调动了小伙伴们的热情，
甚至对Hadoop或者编程仅停留在听说阶段的童鞋们也积极参与。我们Omnilab小组最近也关注到这个比赛，
看到大家玩得这么热闹，而且又有丰富的数据集，手一抖报了个名。**数据挖掘， 小伙伴一起玩才有意思嘛！**

我首先关注到的题目是思明公司提供的“电商消费行为预测”，也是我在第一时间看到数据内容的题目。
宣传的话不多讲，我在QQ交流群里看到大家对基本的Hadoop和Spark都有疑问，也有人私聊解决。
但是我个人更喜欢看到大家在数据上玩出心意，这里就对思明提供的3节点集群上的Spark（Pyspark）
使用方法写个小教程，大家也不要私聊了，这里可以放开讨论。

首先，如果报名成功，你将收到管理员发送的ssh私钥和teamxxxx (xxxx是编号)，同时有使用说明。 这里有疑问，直接咨询群里的答疑君。

登陆集群需要ssh工具。mac和linux用户已经有ssh客户端。windows用户可以使用putty或其他类似工具。

登陆到集群后，我们可以通过``hadoop fs``命令查看HDFS上比赛用的数据。默认数据是放在'/data/'目录下。
接下来，我们只需要两步，即可成功运行spark例子程序（见下文）。

Get Started
===========

**第一步：配置Spark运行环境参数**：比赛的集群上的Spark环境安装在非标准路径，因此用户如果
直接使用，需要每次手动加入完整命令路径。这里方便起见，先配置路径参数。步骤很简单：

编辑'～/.bash_profile'或者'~/.bashrc'文件

.. code-block:: editbash

	$ nano ~/.bash_profile

并追加以下内容，按CTRL+X，回车，保存。

.. code-block:: envvars

	SPARK_VERSION=spark-1.1.0
	export SPARK_HOME=/home/workspace/$SPARK_VERSION
	export PATH=$SPARK_HOME/bin:$PATH

为了使变量当即生效，可运行

.. code-block:: validbash

	$ . ~/.bash_profile

检验变量是否生效的方法是，在终端直接运行pyspark命令，启动pyspark交互模式。

.. code-block:: testenv

	$ pyspark
	$ quit()


**第二步：编写Spark代码并提交任务**：我们这里基于Python API来编写“统计每个用户的记录总数”这一任务。
（Python是一种脚本语言，对于新手上手快。但是并不意味着可以轻松成为Python大拿。）这里我提供了一份Pyspark
样例代码，各位可以试着跑一跑，找找感觉。

.. code-block:: sourcecode

	#!/usr/bin/env python
	#_*_ encoding: utf-8 _*_
	# Spark script
	import sys
	import os
	import shutil
	from pyspark import SparkContext, StorageLevel

	def split_line(line):
	        parts = line.strip('\r\n ').split('^')
	        return parts

	def main():
		if len(sys.argv) < 3:
	                print("Usage: heatmap <input> <output>")
	                exit(-1)

	        sc = SparkContext(appName="testbdc2014")
	        input = sys.argv[1]
	        output = sys.argv[2]

	        # Read data
	        data = sc.textFile(input) \
	                .map(split_line) \
	                .groupBy(lambda x: x[0]) \
	                .mapValues(lambda x: len(x)) \
	                .saveAsTextFile(output)

	if __name__ == "__main__":
	        main()

将这段代码复制保存到集群上，命名为``testspark.py``。**注：由于Python是基于缩进的语法风格，因此
请保留文件的原有缩进格式，否则Python会报错。**

接下来提交任务，这里我们用小数据集来测试，即比赛提供的用户购买记录，数据路径：``/data/train/transformData/``.
完整的提交命令是：

.. code-block:: submitjob

	$ spark-submit --master yarn testspark.py /data/train/transformData/ testspark.out

等待运行完毕，可查看HDFS上的运行结果。结果保存在‘testspark.out’目录底下：

.. code-block:: checkresult

	$ hadoop fs -tail testspark.out/part-00000

这里是部分输出结果：

.. code-block:: resultsample

	(u'mzid3042783', 1)
	(u'mzid2916313', 1)
	(u'mzid1588072', 1)
	(u'mzid2276343', 1)
	(u'mzid3164735', 1)
	(u'mzid1796842', 1)
	(u'mzid2062379', 1)
	(u'mzid2582701', 1)

祝比赛愉快。Enjoy!


By Xiaming
http://hsiamin.com

