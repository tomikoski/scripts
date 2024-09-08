# Rust experiments
Proof of Concepts in Rust <3

## ipconverter
Will convert IP's, hostnames into different forms such as octal, hex, binary and decimal.

## usage

```
# build
cargo build --release

# run
./target/release/ipconverter 1.1.1.1 tk0.fi thisdoesnotexists.tk0.fi google.fi
```

```
cargo run 1.1.1.1 tk0.fi thisdoesnotexists.tk0.fi google.fi
```

Outputs:
```
Hostname:   1.1.1.1
IP-address: 1.1.1.1
Decimal:    16843009
Binary:     00000001.00000001.00000001.00000001
Octals:     0001.0001.0001.0001
Hex:        1010101
-----
Hostname:   tk0.fi
IP-address: 37.139.22.205
Decimal:    629872333
Binary:     00100101.10001011.00010110.11001101
Octals:     0045.0213.0026.0315
Hex:        258B16CD
-----
Error: Resolving hostname: 'thisdoesnotexists.tk0.fi'
Error: invalid IPv4 address syntax for 'thisdoesnotexists.tk0.fi'
-----
Hostname:   google.fi
IP-address: 216.58.211.227
Decimal:    3627733987
Binary:     11011000.00111010.11010011.11100011
Octals:     0330.0072.0323.0343
Hex:        D83AD3E3
-----
```
