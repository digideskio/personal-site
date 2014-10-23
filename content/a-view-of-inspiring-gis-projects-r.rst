A view of inspiring GIS projects in R
=====================================

:date: 2014-10-16
:author: Xiaming Chen
:category: Visualization
:tags: spatial, GIS, R

`R`_ is a free software for statistical computing and graphics (as declaimed in
its project vision). But in my view, its horizon is beyond that thanking to its
flexible extension infrastructure. As a PhD student leveraging data mining
techniques in computer network measurement and analysis, I am even shocked by
the community passion and creativity after an experienced (more or less)
journey in `R`_ world.

`R`_ has facilitated my daily mining tasks as a tiny *Swiss-army-knife* in
pocket, from data collection, wangling, and transforming, to modeling,
visualization, and more importantly, communication with others. In this blog, I
collect and make a list about some inspiring GIS (`Geographic Information
System <http://bit.ly/1zepNZi>`_) projects (mostly using `R`_) that inspire me
in my studies and provide me another vantage point to see this world *dataly*.

Preliminaries
-------------

Through this journey, I do not require any programming experience from you in
`R`_, or even other computer languages. What you need to know is this is just a
computer tool and you can also produce the following artistic works when you
know how to use it. I bet more, you will fall in love with it.

(You are safe to skip to next section if you have no plan to learn this tool
for now.)

For readers who want to practice `R`_, I also prepare a table of "quick-start"
meal for you. These are actually the material from which I learn this
language. Do not be frightened by the "steep learning curve" statement
elsewhere. It is there only if you are trying to learn `R`_ from previous
experience of other programming languages. **Leaning from scratch, that's my
advice**.

- `R Official Site <http://www.r-project.org/>`_: First you need to install R
  environment on your computer. Because R is cross-platform, you can `download
  <http://cran.rstudio.com/>`_ and install corresponding binaries for your
  system.

- `RStudio <http://www.rstudio.com/>`_: This may be the best option to edit,
  debug, or even publish your own packages and applications within an
  integrated IDE.

- `Quick-R <http://www.statmethods.net/>`_: This may be your first arrival in
  real R's world. This site is created to help the user quickly access the
  power of R in their own work. More details in each part of this site can be
  read in the book `R in Action (2nd Edition)
  <http://www.manning.com/kabacoff2/>`_.

- `CRAN Task View <http://cran.r-project.org/web/views/>`_: You will like these
  repositories if you are an expert in specific domain and want to leverage R's
  packages in your researches. For example, the task view "Spatial" and
  "SpatioTemporal" would be preferred by GIS users or others interested in
  sptial and temporal series.

- `Advanced R <http://adv-r.had.co.nz/>`_: A book (still in-progress when I
  write this blog) is written by Hadley Wickham for advanced users to learn or
  comprehend the core concepts in R and become a professional R developers.

- `R Bloggers <http://www.r-bloggers.com/>`_: One of my heavily accessed
  website to keep up with the development of community. I have learned many
  modeling and visualization techniques since my first discovery of this site.

- `R Documentation <http://www.rdocumentation.org/>`_: A documentation hub to
  search R packages from CRAN repositories, `bioconductor
  <http://www.bioconductor.org/>`_, and `GitHub <http://www.github.com>`_.

.. _R: http://www.r-project.org/


Projects
--------

I have make up serveral creteria to filter out other projects in face of what I
want. The most important rule is that **the work is mainly generated with R
language**. Due to the data scale, sometimes, the author requires other tools
to manipulate the raw data and this does not affect our selection. The second
rule is that the work must be inspiring for others (feel free to propose your
ideas in comments), either impressive or useful in uncovering the data
information. Okey, finally, it is about GIS, for this list.


Using R as a GIS
~~~~~~~~~~~~~~~~

This is a `tutorial <http://pakillo.github.io/R-GIS-tutorial/>`_ contributed by
`Francisco Rodriguez-Sanchez <http://sites.google.com/site/rodriguezsanchezf>`_
to perform basic operations with spatial data in R, such as importing and
exporting data (both vectorial and raster), plotting, analyzing and making
maps. Also `github site <https://github.com/Pakillo/R-GIS-tutorial>`_. Here is
an example to plot Europe countries using the package **rworldmap**:

.. image:: http://bit.ly/1vCOtZb
   :height: 400
   :width: 400


Mapping the World’s Biggest Airlines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: http://bit.ly/1vCQwwo
   :height: 300
   :width: 600

This colored map `visualizes the top 7 airlines in the world
<http://bit.ly/1vCRloK>`_. It is totally generated with open data and R (i.e.,
a graphical package `ggplot2 <http://ggplot2.org/>`_). The author combines the
urban area of `dense human habitation <http://bit.ly/1vCScGd>`_ and the airline
`route data <http://bit.ly/1vCSw7R>`_ from `OpenFlights
<http://bit.ly/1vCSA7v>`_. The beautiful style inherits the spirit of "`Earth
at Night <http://apod.nasa.gov/apod/ap001127.html>`_" which is a composite of
hundreds of pictures made by the orbiting DMSP satellites.

Visualising Topography
~~~~~~~~~~~~~~~~~~~~~~

.. image:: http://topography.geotheory.co.uk/slides/world.png
   :height: 300
   :width: 600

`Robin Edwards <http://geotheory.co.uk/>`_, a researcher at UCL CASA, has
created these `stunning topographic
<http://geotheory.co.uk/blog/2014/02/07/visualising-topography/>`_ maps using
the high resolution elevation data provided by the British Oceanographic Data
Centre. The transitions from black (high areas) to blue (low areas) give the
maps a slightly ethereal appearance to dramatic effect.

Facebook Friends
~~~~~~~~~~~~~~~~

.. image:: http://bit.ly/1odI8A4
   :height: 300
   :width: 600

You have possibly seen this figure in other media to illustrate the impacts of
social networks on our lives. This figure is created by `Paul Butler
<http://paulbutler.org/>`_ when he was an intern in Facebook, 2010. The details
are given `here <http://on.fb.me/1CucrEA>`_ and `here, too
<http://bit.ly/1CucKzq>`_. The main challenge is to adjust the plotting order
and colors of lines regarding the line weight (number of friends).


[TO BE CONTINUED]
