use std::env;
use std::net::Ipv4Addr;
use std::str::FromStr;

trait Ipv4Format {
    fn to_hex(&self) -> String;
}

impl Ipv4Format for Ipv4Addr {
    fn to_hex(&self) -> String {
        //decimal_to_hex(self.to_bits())
        format!("{:02X}", self.to_bits())
    }
}

/*
fn decimal_to_hex(decimal: u32) -> String {
    format!("{:02X}", decimal)
}
*/

fn byte_to_bin(decimal: u8) -> String {
    format!("{:08b}", decimal)
}


fn byte_to_oct(decimal: u8) -> String {
    format!("{:04o}", decimal)
}


fn main() {
    let args: Vec<String> = env::args().collect();
    let ips: Vec<_> = args.into_iter().skip(1).collect();
    //let ips: Vec<Result<Ipv4Addr, _>> = args.into_iter().skip(1).map(|ip_str| Ipv4Addr::from_str(&ip_str)).collect();
    //let ips: Result<Vec<Ipv4Addr>, _> = args.into_iter().skip(1).map(|ip_str| Ipv4Addr::from_str(&ip_str)).collect();
    //let ips: Result<Vec<Ipv4Addr> = args.into_iter().skip(1).map(|ip_str| Ipv4Addr::from_str(&ip_str).expect("IP address parsing failed!")).collect();
    //let ips:Vec<Ipv4Addr> = args.into_iter().skip(1).map(|ip_str| Ipv4Addr::from_str(&ip_str).unwrap()).collect();
    //let ips = ips.unwrap();

    for s in ips.iter() {
        let ip = Ipv4Addr::from_str(&s);
        match ip {
            Ok(ip) => {                
                println!("Original:  {}", ip);
                println!("Decimal:   {}", ip.to_bits());
                //println!("Binary:    {}", ip.octets().map(|x| byte_to_bin(x)).join("."));
                println!("Binary:    {}", ip.octets().map(byte_to_bin).join("."));
                println!("Octals:    {}", ip.octets().map(|x| byte_to_oct(x)).join("."));
                //println!("Hex:       {}", decimal_to_hex(ip.to_bits()));
                println!("Hex:       {}", ip.to_hex());
            },
            Err(e) => { println!("Error: {e} in '{s}'")},
        }
        println!("-----");
    }
}