Researches
##########

:date: 2014-06-25 18:00
:author: Xiaming Chen
:slug: researches


Large-scale Human Mobility Analysis
-----------------------------------

Mobility networks are essential in the history of human society, from
population and commodity exchange to culture and civilization expansion.  Since
the seminal migration model of Ravenstein a hard century ago, generations of
social and physical scientists have made great efforts towards universal laws
that naturally govern human movement.  Technology of man-carried equipment and
wearable sensors, as well as boosting our communication and monitoring, brings
about huge amounts of data about human daily activities. Inspecting such
activity patterns makes promising suggestions and conclusions on urban
transport plan, epidemic prediction, and the estimation of economic exchange
and population migration.


Optimization of User-perceived Mobile Performance
--------------------------------------------------

Due to the rapid development of mobile technologies (wireless networks and
devices, mobile OS and applications), traditional problems such as networking
optimization and human social analysis can be tackled in a few new ways. From a
high perspective, users with mobile devices are sophisticated sensors of our
realistic world. Thus we can make analyses on our world indirectly with these
`sensor` information.

Recently, people become more concerned about the mobile performance as well as
convenience of mobility. Compared to the traditional fixed Internet
communication devices, mobile clients like smart phones and tablets are limited
by the battery, processing ability, hand-off between signal sources, and varied
connection states and so on to gain fast and stable user experience
(UX). Meanwhile, some popular mobile applications like voice search, HTTP live
streaming require instant and stable data transmission between clients and
servers, which is not fully satisfied by current TCP implementation, cache
optimization or middle box architectures (say content distributed networks).

This study attempts to address this problem via two aspects. First, the
characteristics of mobile and fixed Web traffic will be measured to obtain the
knowledge of differences between these two use scenarios. Several aspects of
client diversity, delivery requirements (e.g., protocols, network stability)
and content difference will be measured to comprehend the limitations for
mobile experience improvement. Second, we will search for the forward-looking
optimization for the user perceived mobile performance via reorganization of
the content to be delivered, improvement of network infrastructures, and
development of protocols etc.


Distributed PCAP Analysis Platform (DPCAP)
------------------------------------------

Network traffic processing may become the next big-data-nut to be smashed by
both network managers and researchers. A tremendous amount of real-time bits
flow over our network devices and pipes everyday. Network managers face the
challenges of analyzing the data with some time limit to find abnormal
behaviours (e.g., attacks) and network failures with some complicated
processing. For example, the Deep Packet Inspection (DPI), a signature-based
protocol classification method, needs to inspect flow bytes covering the whole
stream where the signature insertion point is unknown and unstable over
time. Another example comes from network traffic miners who analyze traffic and
protocol characteristics. The existing methods for these tasks are usually
running on one machine (using tools like `libpcap <http://www.tcpdump.org/>`_),
which is a really time-consuming process, especially when the offline PCAP
files are huge that can not be handled by a single or several machines.

This project aims to face these challenges with the distributed processing
platform like Hadoop or, generally, parallel programming frameworks like
MapReduce. Recently, a simple PCAP processing library based on Hadoop, i.e.,
`hadoop-pcap-lib <https://github.com/RIPE-NCC/hadoop-pcap>`_, is introduced by
the engineers of RIPE NCC to meed their requirements of processing DNS
traffic. Differently and to go further, our DPCAP is designed as a distributed
platform by modularization of functions based on hadoop-pcap-lib (and related
libraries developed). Some general application modules will be developed like
packet processing module (PPM) and flow processing module (FPM). The general
interfaces will be designed to meet users' specific module development without
considering the basic processing details. Two specific modules of application
identification module (AIM) based on nDPI and flow feature generation module
(FFM) are both on the development roadmap.
