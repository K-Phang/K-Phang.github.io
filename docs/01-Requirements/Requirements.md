---
title: Module Requirements
---

## Module Requirements

The following table outlines the functional and design constraints for the propulsion module.  
This subsystem is responsible for controlling a DC motor-driven propeller capable of forward and reverse motion with variable speed control. The module integrates power regulation, communication, motor driving, and feedback from an incremental encoder to support closed-loop motor operation within the overall team system.

The table includes minimum threshold values for basic operation, target performance levels for optimal system behavior, and identifies stretch requirements that extend beyond baseline functionality.

| **Requirement Description** | **Measure of<br>Threshold** | **Target<br>Measure** | **Stretch<br>Requirement<br>(Y-N)** |
|----------------------------|----------------------------|----------------------|:---:|
| Surface mounted 3.3V switching power regulator | 3.2 V output | 3.3 V regulated output | No |
| Surface mounted microcontroller |  ESP32  | ESP32 handling control, UART, and encoder processing | No |
| UART bus communication | Able to receive motor commands from A1 | Reliable bidirectional UART communication with A1 | No |
| Power sharing | Able to receive power from terminal or pin header | Powered through shared system bus | Yes |
| Motor type | DC motor without feedback | DC gearmotor with incremental encoder | No |
| Motor driver interface | Basic motor on/off control | H-bridge motor driver enabling bidirectional PWM control | No |
| Forward motor control | Motor rotates forward | Smooth forward propulsion under load | No |
| Reverse motor control | Motor rotates backward | Smooth reverse propulsion under load | No |
| Motor speed control | Limited discrete speed levels | Continuous PWM-based speed control | Yes |
| Encoder feedback | Encoder signal readable | Accurate speed and direction feedback for control | No |
| Central control interface | Relay commands received from A1 | Translated A1 commands into motor speed and direction control | No |
| Debugging support | Basic LED indicators | LEDs and test pads for signal and voltage probing | No |
