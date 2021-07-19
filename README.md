# Finding the Shortest Path

Your quest requires that you drop off a very important treasure in the city of Nardah but you have to complete this quest as quickly as possible.

Right now you are in Port Sarim. Write a function that implements Djkstra's shortest path algorithm to automatically find the shortest route to Nardah.

Complete the functions `build_shortest_path()` and `get_shortest_path()`, `build_shortest_path()` takes in a graph and implements the algorithm and returns a table containing the vertex, shortest known distance, and previous vertex (similar to the table in [this article](https://medium.com/basecs/finding-the-shortest-path-with-a-little-help-from-dijkstra-613149fbdc8e)).

`get_shortest_path()` takes in the table and a start and end point and returns the shortest path in the form of a list of vertices in order.

An example graph is provided for you in main.py with a visual in locations.draw.

Make sure your code passes the tests, you can see the tests in unit_tests.py. If you need to make changes to the tests please indicate this in a comment.

# Stretch

There are several methods to optimize Djkstra's algorithm using a priority queue or heap. Check out [this article](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-using-priority_queue-stl/) and try to restructure your code to use this method.
