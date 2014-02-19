from django.shortcuts import render, redirect
from toggle.hue import Hue;
from toggle.forms import HueeeForm

# Create your views here.
def index(request):

    if request.method == "GET":
        # Convert
        form = HueeeForm(request.GET)

        # Check
        if form.is_valid():
            hue_ip = form.cleaned_data["hue_ip"]

            # Initialize the class
            h = Hue()

            # Your base station IP
            h.station_ip = hue_ip

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
        return redirect('/toggle/')