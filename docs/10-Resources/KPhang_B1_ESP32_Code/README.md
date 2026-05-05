# KPhang_B1_ESP32_Code

Final code artifact for K Phang's B1 Propulsion subsystem for Team 201's EGR 314 project, The Duck.

## Notes

- Receiver/module ID: D
- UART2 baud rate: 9600
- UART TX: GPIO17
- UART RX: GPIO16
- Motor pins: GPIO18 and GPIO19
- Local final test commands:
  - F = forward
  - B = back/reverse
- Legacy throttle handling is included.
- This code was used as a MicroPython/devkit-oriented test artifact because the final PCB 3.3 V rail did not work and the soldered ESP32 did not have proper programming-header support.
