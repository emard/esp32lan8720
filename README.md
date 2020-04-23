# ESP32 + LAN8720 ethernet

Connect unmodified LAN8720 module.
ESP32 will be unreliable to start but after
few attempts of power OFF/ON or reset
it will boot and respond to ping and allow
REPL etc over wired ethernet.

Start it just as this (can be put in main.py)

    import lan8720

It will request IP address by DHCP or editign
file "lan8720.py" you can place fixed IP.