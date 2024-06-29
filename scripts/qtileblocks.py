#!/usr/bin/env python
import psutil,subprocess,sys

# /=======/ help getting stuff in common /==========/
def findCommand(module: int) -> str:
    match module:
        case "volume":
            return "pactl list sinks | awk '/Volume:/{print $5; exit}' | tr -d '%'"
        case "brightness":
            return r"brightnessctl | grep -oP '\d+(?=%)'"
        case "ram":
            return r"free -m | awk '/Mem/ {print $3}'"
        case "cpu":
            return r"top -b -n1 | awk '/%Cpu/{print $2 + $4}'"
        case "battery":
            return round(psutil.sensors_battery().percent,2)

def findIcon(iconSet: str, param_percentage: int) -> str:
    match iconSet:
        case "ram": icons = {0: ""}
        case "cpu": icons = {0: "",}
        case "brightness": icons = { 0: "󱣞"}
        case "volume": icons = {0: "󱡏",}
        case "battery":
            icons = {
                90: "󰁹", 80: "󰂂", 70: "󰂁", 60: "󰂀", 50: "󰁿", 
                40: "󰁾", 30: "󰁽", 20: "󰁼", 10: "󰁻",  0: "󰁺", }
        case "network":
            icons = {
                80: "󰣺", 60: "󰣸", 40: "󰣶", 20: "󰣴", 0: "󰣾", }

    for percent, symbol in icons.items():
        if param_percentage >= percent:
            return symbol

# /=======/ modules /==========/

def network(wantback: str) -> str:
    command_ssid = "iw dev | awk '/ssid/{print $2}'"
    command_signal = "nmcli -t -f SIGNAL device wifi | head -n1"

    ssid = subprocess.run(command_ssid, shell=True, 
        stdout=subprocess.PIPE, text=True ).stdout.strip()
    signal = int(float(subprocess.run(command_signal, shell=True, 
        stdout=subprocess.PIPE, text=True ).stdout.strip()))

    #if there is not wifi connection prints as null
    ssid = ssid if ssid else "NULL"
    if signal == "--" or not signal: return "󰣽"
    else: icon = findIcon("network",signal)

    match wantback:
        case "full": return f"{icon} {ssid}"
        case "icon": return f"{icon}"
        case "perc": return f"{ssid}"


#modules: 'battery','volume', 'brightness', 'ram', 'cpu',  
def module(module: str, wantback: str) -> str:
    match module:
        case "battery":
            percentage: float = findCommand(module)
            status: bool = psutil.sensors_battery().power_plugged
            icon = findIcon(module, percentage)
            icon += "  " if status else ""
        case _:
            percentage = findCommand(module)
            percentage = int(float(subprocess.run(percentage, shell=True, 
                stdout=subprocess.PIPE, text=True ).stdout.strip()))
            icon = findIcon(module, percentage)
    
    
    match wantback:
        case "full": return f"{icon} {percentage}%"
        case "icon": return f"{icon}"
        case "perc": return f"{percentage}%"


if __name__ == '__main__':
    match sys.argv[1]:
        case "battery": print(module("battery","full"))
        case "volume": print(module("volume","full"))
        case "brightness": print(module("brightness","full"))
        case "cpu": print(module("cpu","full"))
        case "ram": print(module("ram","full"))
        case "network": print(network("full"))
