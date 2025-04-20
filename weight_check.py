from hx711 import HX711
import time

REFERENCE_UNIT = 105  # You may need to calibrate this

def setup_loadcell():
    hx = HX711(dout_pin=5, pd_sck_pin=6)
    hx.set_reference_unit(REFERENCE_UNIT)
    hx.reset()
    hx.tare()
    return hx

def get_weight(hx):
    return max(0, int(hx.get_weight(5)))

if _name_ == "_main_":
    hx = setup_loadcell()
    print("Initial weight:", get_weight(hx), "grams")

    print("Waiting for pill to be taken...")
    initial_weight = get_weight(hx)

    while True:
        current_weight = get_weight(hx)
        weight_diff = initial_weight - current_weight

        if weight_diff >= 1:  # Assuming 1 pill = 1g
            print("✅ Pill taken. Weight decreased by:", weight_diff, "grams")
            break
        time.sleep(1)
