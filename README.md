## J

* Running on Linux or Windows: `jconsole j/1.ijs`

## Python

* Running on Linux: `python3 python/1.py < data/1.txt`
* Running on Windows: `Get-Content data/1.txt | python python/1.py`

## Profiling

* Linux: `time python data/1.py < data/1.txt`
* Windows: `Measure-Command { Get-Content data/1.txt | python python/1.py }`