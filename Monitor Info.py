import platform

def get_monitor_info():
  """Tries to get monitor information using different methods based on OS.

  Returns:
      A list of dictionaries. Each dictionary contains 'Manufacturer' and 'Model' keys with corresponding values if available, 
      otherwise None.
  """
  if platform.system() == "Windows":
    return get_monitor_info_windows()
  elif platform.system() == "Linux":
    return get_monitor_info_linux()
  else:
    # Add logic for other operating systems if needed
    return []

def get_monitor_info_windows():
  """Uses wmi (Windows Management Instrumentation) to get monitor info on Windows.

  Requires subprocess module to be installed (`pip install subprocess`).

  Returns:
      A list of dictionaries containing monitor information or an empty list if unsuccessful.
  """
  try:
    import subprocess
    output = subprocess.check_output(['powershell', 'Get-WmiObject -Class Win32_DesktopMonitor']).decode("utf-8")
    monitors = []
    for line in output.splitlines():
      if line.startswith("Manufacturer"):
        manufacturer = line.split(":")[1].strip()
      elif line.startswith("ModelName"):
        model = line.split(":")[1].strip()
        monitors.append({"Manufacturer": manufacturer, "Model": model})
    return monitors
  except subprocess.CalledProcessError:
    return []
  except ModuleNotFoundError:
    print("WARNING: 'subprocess' module not found. Monitor information might not be available on Windows.")
    return []

def get_monitor_info_linux():
  """Uses dmidecode (needs to be installed) to get monitor info on Linux.

  Returns:
      A list of dictionaries containing monitor information or an empty list if unsuccessful.
  """
  try:
    import subprocess
    output = subprocess.check_output(['dmidecode', '-t display']).decode("utf-8")
    monitors = []
    current_monitor = {}
    for line in output.splitlines():
      if line.startswith("Display Type"):
        current_monitor["Type"] = line.split(":")[1].strip()
      elif line.startswith("Manufacturer"):
        current_monitor["Manufacturer"] = line.split(":")[1].strip()
      elif line.startswith("Monitor Serial Number"):
        current_monitor["Model"] = line.split(":")[1].strip()
      elif line and not line.startswith(" "):
        if current_monitor:
          monitors.append(current_monitor)
          current_monitor = {}
    if current_monitor:
      monitors.append(current_monitor)
    return monitors
  except subprocess.CalledProcessError:
    return []
  except FileNotFoundError:
    print("WARNING: 'dmidecode' command not found. Monitor information might not be available on Linux.")
    return []

# Get monitor information
monitor_info = get_monitor_info()

if monitor_info:
  for monitor in monitor_info:
    manufacturer = monitor.get("Manufacturer")
    model = monitor.get("Model")
    print(f"Monitor: Manufacturer - {manufacturer}, Model - {model}")
else:
  print("Unable to get monitor information.")