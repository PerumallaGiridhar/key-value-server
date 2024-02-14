# key value server
to start the server, you have to follow the below steps:
1. build a docker image
    ```bash build.sh```

2. run the docker image
    ```bash run.sh```

3. to test the server (using pytest)
    ```bash test.sh```


# How to query key value server
you can make an http get request on /items/<yourid>
if your are running this server locally on port 8123 then use the below curl command
```curl http://localhost:8123/items/your-uuid```
for more details on documentation use the following url
```http://localhost:8123/docs```
```http://localhost:8123/redoc```


# How much data can your server handle? 
We are using Python dictionaries to store the key value data. Python dictionaries are optimised enough to perform lookups on very large data. Hence the key-value-server does not have limitations on data size that it can handle. It depends on the underlying hardware capacity of the host. We are good to go if the host has enough memory (RAM) to store the data. If we go in a scale of GBs of data, still the server would respond to users' queries but latency would increase


## little about Python Dictionaries
Python uses open addressing with double hashing to implement hash tables for dictionaries. In open addressing, if a collision occurs (i.e., two keys hash to the same location), the algorithm searches for the next available slot in a systematic way. Double hashing involves using a second hash function to determine the step size for each probe.
The actual details can be complex, but in essence, Python's dictionary uses a combination of hash codes, table resizing, and open addressing to handle key-value pairs efficiently. The goal is to provide a good trade-off between memory usage and quick access times for dictionary operations.


# How could you improve it so it can handle even larger datasets?
If the data size is very large, and the high latency of Python dictionaries is a problem,  we can use a read-through cache, where we store frequently used data in a separate dictionary object. The type of cache we implement depends on the usage pattern of the client.


# How many milliseconds it takes for the client to get a response on average?
it depends on the data size. For 10k data items, it took 0.012103 seconds whereas upon testing with 1 million items, it took 0.062446 seconds.


# How could you improve the latency?
As I mentioned earlier, we can improve latency by implementing caching. The implementation of a cache would require more details on the usage of the client. Alternatively, we can divide the data into multiple zones (think of it like a shard) based on users' locality. Eg we can create multiple zone files based on users' locality and route requests from a zone to a specific server handling that zone data. This along with caching would further improve the latency.
