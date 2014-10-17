Researches
############################

:date: 2014-06-25 18:00
:author: Xiaming Chen
:slug: researches


Distributed PCAP Analysis Platform
-----------------------------------

Network traffic processing may becomes the next big-data-nut to be smashed by
both network managers and researchers. A tremendous amount of real-time bits
flows over the network devices and pipes everyday. Network managers face the
challenges of analyzing the data with some time limit to find abnormal
behaviors (e.g., attacks) and network failures with some complicated
processing. For example, Deep Packet Inspection (DPI), as a signature-based
application classification method, requires to search the flow payload, at
times covering the whole bits when the signature insertion point is unknown or
changeable.

Another example comes from the network traffic miners who analyze traffic
characteristics and network protocols, optimize the network performance etc.
The common tools for these goals are usually running on one machine based on
pcap (e.g. libpcap) or other packet formats. It may be a time-wasted progress
to analyze the packets one after another and repeat again and again.

This project aims to face these challenges with the distributed processing
platform like Hadoop and parallel programming framework like MapReduce.
Recently, a simple pcap processing library based on hadoop, i.e., hadoop-pcap-
lib, is introduced by the engineers of RIPE NCC to meed their requirements of
processing DNS traffic. Differently and further, the DPCAP is designed as a
distributed platform by modularization of functions based on hadoop-pcap-lib
(or other library developed). Some general application modules will be
developed like packet processing module (hadoop-pcap-lib or other library
developed) and flow processing module; and the general interfaces will be
designed to meet users' specific module development without considering the
basic processing details. Two specific modules of application identification
module based on nDPI and flow feature generation module are both in the plan.



Optimization of User-perceived Mobile Performance
--------------------------------------------------

Due to the rapid development of mobile technologies (wireless networks and
devices, mobile OS and applications), traditional problems such as networking
optimization and human social analysis can be tackled in new ways. From a high
view, users with mobile devices are sophisticated sensors to this world. Thus
we can make analyses on our world indirectly with the sensor information.

Recently, people becomes more concerned about the mobile performance as well as
convenience of mobility. Compared to the traditional fixed Internet
communication devices, mobile clients like smart phones and tablets are limited
by the battery, processing ability, hand-off between signal sources, and varied
connection states and so on to gain fast and stable user experience. Meanwhile,
some popular mobile applications like voice search, HTTP live streaming require
instant or fluent (stable) data transmission between client and server, which
is not fully satisfied by current TCP implementation, cache optimization or
middle box architectures (e.g., CDN).

This project attempts to address this problem via two aspects. First, the
characteristics of mobile ans fixed Web traffic will be measured to obtain the
knowledge of differences between these two Internet usage scenarios. Several
aspects of client diversity, delivery requirements (e.g., protocols, network
stability) and content difference will be compared to comprehend the
limitations for mobile experience improvement. Second and further, we will
search for the forward-looking optimizations for the user mobile performance
via reorganization of the content to be delivered, improvement of network
infrastructures, and development of protocols etc.
