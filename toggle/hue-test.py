from hue import Hue;

# Initialize the class
h = Hue()

# Your base station IP
h.station_ip = "192.168.1.142"

# Authenticate, bootstrap your lighting system
h.get_state()

# get bulb
l1 = h.lights.get('l1')
l2 = h.lights.get('l2')
l3 = h.lights.get('l3')

# toggle light
l1.toggle()
l2.toggle()
l3.toggle()