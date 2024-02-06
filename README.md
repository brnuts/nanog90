# NANOG90 code examples
# for performace testing between Python, Pypy, Go and Rust

## Language versions

### Python version
```
root@telco:~/code/nanog90% python3.12 --version
Python 3.12.0
```


### Pypy version
```
claus@telco:~/code/nanog90% pypy3 --version
Python 3.6.9 (7.3.1+dfsg-4ubuntu0.1, Nov 15 2022, 06:22:42)
[PyPy 7.3.1 with GCC 9.4.0]
```

### Go version
```
claus@telco:~/code/nanog90% go version
go version go1.21.6 linux/amd64
```

### Rust version
```
claus@telco:~/code/nanog90% rustc --version
rustc 1.75.0 (82e1608df 2023-12-21)
```
	
## Examples for testing  flipsum with multi-thread or goroutines

### Python
```
% /usr/bin/time -f "%MKB %P %es" python3.12 flipsum-threads.py
```

### Pypy
```
% /usr/bin/time -f "%MKB %P %es" pypy3 flipsum-threads.py
```

### Go
```
% go build flipsum-goroutines.go
% /usr/bin/time -f "%MKB %P %es" ./flipsum-goroutines
```

### Rust
```
% rustc -C opt-level=3 flipsum-threads.rs
% /usr/bin/time -f "%MKB %P %es" ./flipsum-threads
```



## Examples for testing prime with multi-processing, threads and goroutines

### Python
```
% /usr/bin/time -f "%MKB %P %es" python3.12 prime-multiproc.py
```


### Pypy
```
% /usr/bin/time -f "%MKB %P %es" pypy3 prime-multiproc.py
```


### Go
```
% go build prime-goroutines.go
% /usr/bin/time -f "%MKB %P %es" ./prime-goroutines
```

### Rust
```
% rustc -C opt-level=3 prime-threads.rs
% /usr/bin/time -f "%MKB %P %es" ./prime-threads
```

