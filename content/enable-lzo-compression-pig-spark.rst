Enable LZO compression on Hadoop, Pig and Spark
###############################################
:date: 2014-05-03 19:20
:author: caesar0301
:category: Programming
:tags: apache, CDH, cloudera, hadoop, LZO, mapreduce, pig, spark

I will show you in this tutorial how to enable LZO compression on hadoop, pig
and spark. You reach this page possibly because you encounter the same problem
as I encountered, usually a frustrating Java exception:

.. code-block:: java exception

    Caused by: java.lang.ClassNotFoundException: Class com.hadoop.compression.lzo.LzoCodec not found.

I suppose that you have set up a basic hadoop installation successfully
following other tutorials for example `official hadoop doc`_. As the apache and
`cloudera`_ are two of the most popular distributions, I will show different
configurations for both textual and cloudera manager settings. You will walk
through three steps towards enabling LZO for your hadoop/pig/spark development
environment, i.e.,

#. Installing native-lzo libraries
#. Installing hadoop-lzo library
#. Setting up necessary environment variables correctly (right part
   consuming my most time)

Step1: Installing native-lzo libraries
----------------------------------------------

Before installing hadoop-lzo, the `native lzo`_\ is required. You can install
them manually or facilitating package manager according to your system:

- On Mac OS:

.. code-block:: install-on-mac

    sudo port install lzop lzo2

- On RH or Centos:

.. code-block:: centos

    sudo yum install lzo liblzo-devel

- On Debian or ubuntu:

.. code-block:: ubuntu

    sudo apt-get install liblzo2-dev

*Make sure all nodes have native-lzo installed*.

Step2: Installing hadoop-lzo library
---------------------------------------

As the LZO is GPL'ed, it not shipped with official hadoop package under Apache
Software License. I recommend `github repo`_ which is a splitable version as
well as many improvements based on the `google repo`_. You can follow
`directions on github repo to compile and install it`_. I have not tested it
because we are running CDH as follows.

In CDH 5, HADOOP_LZO is shipped as recommended parcels and you can
DOWNLOAD/DISTRIBUTE/ACTIVATE it via the Cloudera Manager. Here we are running
CDH-5 + HADOOP_LZO-0.4.15. By default, the HADOOP_LZO will be installed in
``/opt/cloudera/parcels/HADOOP_LZO``.

Step3: Setting up env variables
---------------------------------

The basic configuration is for hadoop, while Pig is piggying upon this
functionality.

**For Hadoop with LZO**, we have to add several fields to ``core-site.xml``,
``mapred-site.xml`` and ``hadoop-env.sh`` under hadoop ``conf`` folder,
usually ``$HADOOP_HOME/conf``.

- Add following lines to the ``core-site.xml``:

.. code-block:: config.hadoop

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

- Add following properties to ``mapred-site.xml``:

.. code-block:: config.hadoop2

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

Replace the bold part with your local path.

- Append ``HADOOP_CLASSPATH`` to ``hadoop-env.sh``:

.. code-block:: config.hadoop.env

   HADOOP_CLASSPATH=$HADOOP_CLASSPATH:/opt/cloudera/parcels/CDH/lib/hadoop/lib/*

If you are using cloudera manager, you can change previous settings with GUI
interface; otherwise, skip this paragraph.

- Browse to "mapreduce1-->Configuration,view & edit-->search \`compression\`
  keyword".
- Edit **mapred.compress.map.output**, **mapred.map.output.compression.codec**,
  **MapReduce Client safety valve for mapred-site.xml**, and
  **io.compression.codecs** with values addressed above.
- Search \`valve\` to edit **MapReduce Client Environment Snippet for
  hadoop-env.sh**.

At last, restart dependent services in right order and deploy the
configurations among all nodes. That's it!!. Then you can test the
functionality with command and get successful messages similar to below:

.. code-block:: success message

   $ hadoop jar /path/to/hadoop-lzo.jar com.hadoop.compression.lzo.LzoIndexer lzo_logs
   $ 14/05/04 01:13:13 INFO lzo.GPLNativeCodeLoader: Loaded native gpl library
   $ 14/05/04 01:13:13 INFO lzo.LzoCodec: Successfully loaded & initialized native-lzo library [hadoop-lzo rev 49753b4b5a029410c3bd91278c360c2241328387]
   $ 14/05/04 01:13:14 INFO lzo.LzoIndexer: [INDEX] LZO Indexing file datasets/lzo_logs size 0.00 GB...
   $ 14/05/04 01:13:14 INFO Configuration.deprecation: hadoop.native.lib is deprecated. Instead, use io.native.lib.available
   $ 14/05/04 01:13:14 INFO lzo.LzoIndexer: Completed LZO Indexing in 0.39 seconds (0.02 MB/s).  Index size is 0.01 KB.

**For Spark with LZO**, this consumes me much time because there are less
information in searched posts. But the solution is simple based on previous
knowledge. After installing spark via tar or cloudera manager, you need merely
to append ``spark-env.sh`` with

.. code-block:: config.spark

   SPARK_LIBRARY_PATH=$SPARK_LIBRARY_PATH:/path/to/your/hadoop-lzo/libs/native
   SPARK_CLASSPATH=$SPARK_CLASSPATH:/path/to/your/hadoop-lzo/java/libs

Now you can use the LZO compression for both map output and final results. A
comparison of LZO performance is briefly given in `another place`_. This post
was born from a two-day searching and testing work on the cluster. A related
question is also asked on `stackoverlfow.com`_ but there are no solutions about
this up to the finish of this tutorial.


Useful links
------------------

- `Using the LZO Parcel from Cloudera`_

.. _official hadoop doc: http://hadoop.apache.org/docs/stable/
.. _cloudera: http://www.cloudera.com
.. _native lzo: http://www.oberhumer.com/opensource/lzo/
.. _github repo: https://github.com/twitter/hadoop-lzo
.. _google repo: https://code.google.com/a/apache-extras.org/p/hadoop-gpl-compression
.. _directions on github repo to compile and install it: https://github.com/twitter/hadoop-lzo/blob/master/README.md
.. _another place: http://blog.cloudera.com/blog/2009/11/hadoop-at-twitter-part-1-splittable-lzo-compression/
.. _stackoverlfow.com: http://stackoverflow.com/q/23441142/1320284
.. _Using the LZO Parcel from Cloudera: http://www.cloudera.com/content/cloudera-content/cloudera-docs/CM4Ent/latest/Cloudera-Manager-Installation-Guide/cmig_install_LZO_Compression.html
