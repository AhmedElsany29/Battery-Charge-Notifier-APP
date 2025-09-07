import psutil
import time
import winsound
from win10toast import ToastNotifier

toaster = ToastNotifier()
alerted = False

while True:
    try:
        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = battery.power_plugged

        if percent >= 85 and plugged and not alerted:

            for i in range(5):  
                winsound.Beep(1000, 3000)  
                time.sleep(0.5)  

            
            toaster.show_toast(
                "⚡ Enough Charging",
                f"Battery is {percent}%. Unplug the charger.",
                duration=10,
                threaded=True
            )
            alerted = True

        if percent < 85:
            alerted = False

    except Exception as e:
        print("Error:", e)

    time.sleep(60)  
