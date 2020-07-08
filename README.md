# pytools

some tool writed in python

## iprange2network.py

convert ip range to network representation

Dependences:
```
python 3.7
```

Usage:

1. Place your ip ranges in `range.txt` file placed in same directory with the script
, `range.txt` look like:

    ```
    2409:8c14:f1a:8702:0:0:0:0-2409:8c14:f1a:8702:0:0:0:ff
    192.168.1.1-192.168.1.128
    61.160.224.0-61.160.224.255
    ``` 

1. Convert
    ```bash
    python iprange2network.py 
    # or
    python iprange2network.py > output.txt
    ``` 

1. Done, look `network.txt` or your output file
    ```
    2409:8c14:f1a:8702::/120
    192.168.1.1/32
    192.168.1.2/31
    192.168.1.4/30
    192.168.1.8/29
    192.168.1.16/28
    192.168.1.32/27
    192.168.1.64/26
    192.168.1.128/32
    61.160.224.0/24
    ```