Enable LZO compression on Hadoop, Pig and Spark
###############################################

:date: 2014-05-03 19:20
:author: caesar0301
:category: Programming
:tags: apache, CDH, cloudera, hadoop, LZO, mapreduce, pig, spark

In this tutorial, I will show you how to enable LZO compression on Hadoop, Pig
and Spark. I suppose that you have set up a basic hadoop installation
successfully (if not, please refer to other tutorials for `Hadoop installation
<http://hadoop.apache.org/docs/stable/>`_).

You reach this page possibly because you encounter the same problem
as I encountered, usually starting with Java exception:

.. code-block:: java

    Caused by: java.lang.ClassNotFoundException: Class com.hadoop.compression.lzo.LzoCodec not found.

As the `Apache <http://hadoop.apache.org/>`_ and `Cloudera
<http://www.cloudera.com>`_ distributions are two of the most popular
distributions, configurations for both contexts are shown. Briefly, three
main steps would be walked through towards the final success:

#. Installing ``native-lzo`` libraries
#. Installing ``hadoop-lzo`` library
#. Setting up environment variables correctly (the right part
   consuming my most time)

Step1: Installing ``native-lzo`` libraries
------------------------------------------

The `native-lzo library <http://www.oberhumer.com/opensource/lzo/>`_ is
required for the installation of ``hadoop-lzo``. You can install them manually
or by facilitating the Package Manager (**NOTE:** Make sure all nodes in the
cluster have ``native-lzo`` installed.):

- On Mac OS:

.. code-block:: bash

    sudo port install lzop lzo2

- On RH or CentOS:

.. code-block:: bash

    sudo yum install lzo liblzo-devel

- On Debian or ubuntu:

.. code-block:: bash

    sudo apt-get install liblzo2-dev


Step2: Installing ``hadoop-lzo`` library
----------------------------------------

For Apache Hadoop
~~~~~~~~~~~~~~~~~~~

As the LZO is GPL'ed, it not shipped with official Hadoop distribution which
takes Apache Software License. I recommend the `Twitter version
<https://github.com/twitter/hadoop-lzo>`_ which is a forked version of
`hadoop-gpl-compression
<https://code.google.com/a/apache-extras.org/p/hadoop-gpl-compression>`_ with
remarkable improvements. If you are running the official Hadoop, some
installation structures are provided the `the documentation
<https://github.com/twitter/hadoop-lzo/blob/master/README.md>`_.


For Cloudera Distribution
~~~~~~~~~~~~~~~~~~~~~~~~~

In Cloudera's CDH, ``hadoop-lzo`` is shipped to customers as parcels and you
can download and distribute it conviniently using the Cloudera Manager. By
default, the ``hadoop-lzo`` will be installed in
``/opt/cloudera/parcels/HADOOP_LZO``.

Here we show the configuration on our cluster:

* Cloudera CDH 5
* HADOOP_LZO version 0.4.15

Step3: Setting up env variables
-------------------------------

For Apache Hadoop/Pig
~~~~~~~~~~~~~~~~~~~~~

The basic configuration is for Apache Hadoop, while Pig is piggying upon its
functionality.

- Set compression codecs libraries in ``core-site.xml``:

.. code-block:: xml

   <property>
      <name>io.compression.codecs</name>
      <value>org.apache.hadoop.io.compress.GzipCodec,
              org.apache.hadoop.io.compress.DefaultCodec,
              org.apache.hadoop.io.compress.BZip2Codec,
              com.hadoop.compression.lzo.LzoCodec,
              com.hadoop.compression.lzo.LzopCodec
       </value>
   </property>
   <property>
      <name>io.compression.codec.lzo.class</name>
      <value>com.hadoop.compression.lzo.LzoCodec</value>
   </property>

- Set MapReduce compression configuration in ``mapred-site.xml``:

.. code-block:: xml

   <property>
       <name>mapred.compress.map.output</name>
       <value>true</value>
   </property>
   <property>
       <name>mapred.map.output.compression.codec</name>
       <value>com.hadoop.compression.lzo.LzoCodec</value>
   </property>
   <property>
       <name>mapred.child.env</name>
       <value>JAVA_LIBRARY_PATH=$JAVA_LIBRARY_PATH:/path/to/your/hadoop-lzo/libs/native</value>
   </property>

- Append ``HADOOP_CLASSPATH`` to ``hadoop-env.sh``:

.. code-block:: bash

    HADOOP_CLASSPATH=$HADOOP_CLASSPATH:/opt/cloudera/parcels/CDH/lib/hadoop/lib/*

For Cloudera Distribution
~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the Cloudera Manager to enable the same previous settings via GUI
interface:

* For MapReduce component, change the configuration of corresponding keys as
  above:

   | **io.compression.codecs**
   | **mapred.compress.map.output**
   | **mapred.map.output.compression.codec**
   | **MapReduce Client safety valve for mapred-site.xml**

* Edit **MapReduce Client Environment Snippet for hadoop-env.sh** to append the
  ``HADOOP_CLASSPATH`` variable.

At last, restart dependent services in right order and deploy the
configurations among all nodes. That's it!!. Then you can test the
functionality with command and get successful messages similar to below:

.. code-block:: bash

   $ hadoop jar /path/to/hadoop-lzo.jar com.hadoop.compression.lzo.LzoIndexer lzo_logs
   $ 14/05/04 01:13:13 INFO lzo.GPLNativeCodeLoader: Loaded native gpl library
   $ 14/05/04 01:13:13 INFO lzo.LzoCodec: Successfully loaded & initialized native-lzo library [hadoop-lzo rev 49753b4b5a029410c3bd91278c360c2241328387]
   $ 14/05/04 01:13:14 INFO lzo.LzoIndexer: [INDEX] LZO Indexing file datasets/lzo_logs size 0.00 GB...
   $ 14/05/04 01:13:14 INFO Configuration.deprecation: hadoop.native.lib is deprecated. Instead, use io.native.lib.available
   $ 14/05/04 01:13:14 INFO lzo.LzoIndexer: Completed LZO Indexing in 0.39 seconds (0.02 MB/s).  Index size is 0.01 KB.

For Spark
~~~~~~~~~

This consumes me much time because there are less information in previous
posts. But the solution is strightforward with previous experience.

No matter the Spark is installed via tar or the Cloudera Manager, you need
merely to append two path values to ``spark-env.sh``:

.. code-block:: bash

   SPARK_LIBRARY_PATH=$SPARK_LIBRARY_PATH:/path/to/your/hadoop-lzo/libs/native
   SPARK_CLASSPATH=$SPARK_CLASSPATH:/path/to/your/hadoop-lzo/java/libs

Ralted posts and questions
--------------------------

A comparison of LZO performance is given in `another place
<http://blog.cloudera.com/blog/2009/11/hadoop-at-twitter-part-1-splittable-lzo-compression/>`_. A
related question is also asked on `StackOverflow
<http://stackoverflow.com/q/23441142/1320284>`_ but there are no solutions
about this up to the finish of this tutorial. You maybe also interested in how
to `use the LZO Parcel from Cloudera
<http://www.cloudera.com/content/cloudera-content/cloudera-docs/CM4Ent/latest/Cloudera-Manager-Installation-Guide/cmig_install_LZO_Compression.html>`_.
