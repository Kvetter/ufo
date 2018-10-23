# Benchmark

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

The way we measured the time was with the "ping" command. That command is a simple way of testing the reachability of a host. The ping command meassures the "round-trip" time for a simple request. "Round-trip" time is the time it takes for the request to be send, and the response to be recieved. By doing that we only focus on the request istelf and dont spend time to meassure other features like the time it would take to execute a command or having to wait for our program to be compiled.

There are several things that could influence the results when working on measuring time over the internet. Peter Sestoft talk about this [benchmarking.pdf](https://www.itu.dk/people/sestoft/papers/benchmarking.pdf). He talks about when measuring the time it takes for a program to execute, you should be aware that the measurements are easily affected by other processes running at the same time. We avoid this since we dont measure our whole program, but just use the ping command, which simply calculates the time it took to reach the host and get a response. Things that may influence our trip time would be things like: distance, server response time, traffic/internet connection, number of network hops (meaning the specific route the signal is travelling). 
 
