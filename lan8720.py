# LAN8720 MODULE

#GPIO00 - EMAC_TX_CLK : nINT/REFCLK (50MHz) - 4k7 Pullup
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

#GPIO23 JTAG_TDI
#GPIO34 JTAG_TDO (was 19)
#GPIO18 JTAG_TCK
#GPIO5  JTAG_TMS (was 21)

import network
from machine import Pin
lan = network.LAN(mdc=Pin(16), mdio=Pin(17), power=None, id=None, phy_addr=1, phy_type=network.PHY_LAN8720)
lan.active(True)
lan.ifconfig(('192.168.18.190', '255.255.255.0', '192.168.18.254', '192.168.18.254'))

# press RESET or power ON/OFF ESP32 several times until it boots
# download speed with ftp from ESP32 flash is 300KB/s (3Mbps)
