# bloop

Bloop will be a machine learning project, to measure and then predict the relative humidity levels in a small caravan, named Edwin.

# Why?

Edwin the caravan has had several leaks whilst in storage, which caused his insides to become quite damp and moldy. Now cleaned, resealed, and smelling quite wonderful, I want to ensure he remains this way. 

Bloop will get data feeds from a DHT11 sensor backed off by a Pi inside Edwin, and the Met Office current observations API, logging this data to a MYSQL database (Soon to be RocksDB, cooler, less evil). This data will then be fed to a machine learning package, or API, in order to predict given the observed conditions, what the %rh should be. Measured values above the prediction could indicate that Edwin has spring a leak.

# Why Bloop?

Computttaaaa. Blip blip clicky click bleep bloop.
