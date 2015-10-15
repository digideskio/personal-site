Analyzing Shortest Path in Python
=================================

:date: 2015-09-06
:author: Xiaming Chen
:tags: Python, Algorithm

In `mobility analysis </posts/2014/10/23/leveraging-open-data-to-understand-
urban-lives/>`_, one important technique is finding the shortest path people
may walking through given two locations as starting and ending points.

We get started with the target road network from a clean Eris shapefile. If
you do not have such a shapefile containing a connected network topology,
please read my `previous post </posts/2015/08/30/a-tutorial-on-topology-
correction-of- shapefiles-using-grass/>`_ to extract such a clean file. Below
is the main python logic to analyze the shapefile with shortest path algorithm
in `NetworkX <https://networkx.github.io/>`_.

.. code-block:: python

    #!/usr/bin/env python
    # -*- encoding: utf-8 -*-
    # File:
    #    roadnetwork.py
    #
    # Author: Xiaming Chen
    # Email: chen@xiaming.me

    class RoadNetwork(object):
        """Convert an ERIS shapefile to an undirected graph weighted by distance.
        """

        def __init__(self, shapefile, edge_weighted_by_distance=True):
            print("Reading road network ...")
            g = nx.read_shp(shapefile)
            mg = max(nx.connected_component_subgraphs(g.to_undirected()), key=len)
            if edge_weighted_by_distance:
                for n0, n1 in mg.edges_iter():
                    path = np.array(json.loads(mg[n0][n1]['Json'])['coordinates'])
                    distance = np.sum(
                        greate_circle_distance(path[1:,0],path[1:,1], path[:-1,0], path[:-1,1])
                    )
                    mg.edge[n0][n1]['distance'] = distance
            self.G = mg

        def nearest_node_to(self, lonlat):
            """ Find the nearest node of given point with (long, lat).
            """
            nodes = np.array(self.G.nodes())
            nn = np.argmin(np.sum((nodes[:,:] - lonlat)**2, axis=1))
            return nn

        def shortest_path(self, lonlat1, lonlat2, weight='distance'):
            """Find the shortest path for a pair of points.
            Two points are not required to be the vertex of graph.
            """
            nodes = np.array(self.G.nodes())
            p1 = self.nearest_node_to(lonlat1)
            p2 = self.nearest_node_to(lonlat2)
            path = nx.shortest_path(self.G, tuple(nodes[p1]), tuple(nodes[p2]), weight)
            return path

        def shortest_path_distance(self, lonlat1, lonlat2, weight='distance'):
            """Return the distance of two points with the shortest path algorithm.
            """
            sp = self.shortest_path(lonlat1, lonlat2, weight)
            distances = [self.G.edge[sp[i]][sp[i+1]][weight] for i in range(len(sp)-1)]
            distance = np.sum(distances)
            return distance
