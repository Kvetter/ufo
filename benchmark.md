# Code Analysis

By Kasper Vetter and Phillip Brink

## Hypothesis

When pinging servers that are placed in different parts of the world, we would expect that the ping would
be higher, the longer we are from the server

## Experiment

The code used for the experiment can be found in the connect.py file. The python file uses the commandline to "ping" the servers with the ping command. We ping each server 20 times, and get the average time it takes to ping.

To run the experiment simply execute the "connect.py"

## Execute the experiment

![Analysis Report](https://github.com/Kvetter/ufo-linq/blob/master/img/benchmark.png)

This is our result. It shows what the average ping time is (in milliseconds) to the given servers

The average ping time to 128.199.144.199 is 211 ms

The average ping time to 167.99.51.33 is 92.76 ms

The average ping time to 46.101.253.149 is 16.52 ms


### Evaluate

Looking at our results we expect that the server: 128.199.144.199 is the furthest away from where we are
while we expect the server: 46.101.253.149 to be the one that is closest to us

### Discuss the results

The results are heavily influenced by the network connection. A slower connection would give a different result, but the order of which is slowest and which is faster should still be the same.

We also don't see how our packages is being routed through to the server.  
