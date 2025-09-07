# 🔋 Battery Charge Notifier (Windows)

A simple Python program that monitors your laptop's battery level and
alerts you when it reaches 85% while charging.\
This helps extend battery lifespan by reminding you to unplug the
charger.

------------------------------------------------------------------------

## ✨ Features

-   Monitors battery percentage and charging status.\
-   Plays a repeated beep sound when the battery reaches the threshold.\
-   Shows a Windows toast notification.\
-   Runs continuously in the background.

------------------------------------------------------------------------

## 🛠️ Requirements

Install the required libraries before running:

``` bash
pip install psutil win10toast
```

------------------------------------------------------------------------

## ▶️ Usage

1.  Clone the repository:

    ``` bash
    git clone https://github.com/username/battery-notifier.git
    cd battery-notifier
    ```

2.  Run the program:

    ``` bash
    python battery_notifier.py
    ```

------------------------------------------------------------------------

## ⚙️ Configuration

-   The default alert threshold is **85%**.\

-   To change it, edit this line in the code:

    ``` python
    if percent >= 85 and plugged and not alerted:
    ```

    Replace `85` with your preferred percentage.

-   The script checks the battery every **60 seconds**.\
    You can adjust this interval by editing:

    ``` python
    time.sleep(60)
    ```

------------------------------------------------------------------------

## 📌 Notes

-   Works on **Windows only** (uses `winsound` and `win10toast`).\
-   Can be minimized to run silently in the background.

------------------------------------------------------------------------