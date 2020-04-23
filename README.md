# ESP32 + LAN8720 ethernet

Connect unmodified LAN8720 module.

    #GPIO00 - EMAC_TX_CLK : nINT/REFCLK (50MHz)
    #GPIO16 - SMI_MDC     : MDC (relocateable)
    #GPIO17 - SMI_MDIO    : MDIO (relocateable)
    #GPIO19 - EMAC_TXD0   : TX0
    #GPIO21 - EMAC_TX_EN  : TX_EN
    #GPIO22 - EMAC_TXD1   : TX1
    #GPIO25 - EMAC_RXD0   : RX0
    #GPIO26 - EMAC_RXD1   : RX1
    #GPIO27 - EMAC_RX_DV  : CRS
    #GND                  : GND
    #3V3                  : VCC

ESP32 will be unreliable to start but after
few attempts of power OFF/ON or reset
it will boot and respond to ping and allow
REPL etc over wired ethernet.

Start it just as this (can be put in main.py)

    import lan8720

It will request IP address by DHCP.
Edit file "lan8720.py" to set fixed IP.

    import network
    from machine import Pin
    lan = network.LAN(mdc=Pin(16), mdio=Pin(17), power=None, id=None, phy_addr=1, phy_type=network.PHY_LAN8720)
    lan.active(True)
    # by default (no parameters), ifconfig() will request IP from DHCP
    lan.ifconfig()
    # set fixed IP
    #lan.ifconfig(('192.168.0.190', '255.255.255.0', '192.168.0.1', '192.168.0.1'))
