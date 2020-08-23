from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY

from btlewrap import GatttoolBackend

poller = MiFloraPoller(mac='MAC ADDRESS', backend=GatttoolBackend)

print('Temperature: ', poller.parameter_value(MI_TEMPERATURE))
print('Moisture: ', poller.parameter_value(MI_MOISTURE))
print('Light: ', poller.parameter_value(MI_LIGHT))
print('Conductivity: ', poller.parameter_value(MI_CONDUCTIVITY))
print('Battery: ', poller.parameter_value(MI_BATTERY))
