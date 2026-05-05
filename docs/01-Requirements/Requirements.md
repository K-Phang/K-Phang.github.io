---
title: Module Requirements
---

# Module Requirements

This page defines the requirements for my individual module: **K Phang, B1 Propulsion, message ID D**, for Team 201's rover project, **The Duck**.

The B1 propulsion module was responsible for controlling the drive motors used to move The Duck. The original goal was to create an ESP32-based motor-control board that could receive team communication commands, drive the propulsion motors through an H-bridge, and eventually support encoder feedback for closed-loop speed control. During final implementation, the module was reduced to basic open-loop motor control because encoder feedback remained a stretch goal and the PCB had bring-up issues.

## Final Module Scope

The final B1 propulsion implementation focused on these core functions:

1. Receive or support propulsion-control commands as part of the team communication structure.
2. Use an ESP32-based controller for motor-control logic.
3. Drive the propulsion motors using an H-bridge motor driver.
4. Provide a working 6 V motor rail for the motors.
5. Support forward and reverse motor control through the H-bridge design.
6. Document PCB bring-up issues and identify hardware changes for a future revision.

The final board included the soldered **ESP32-S3-WROOM-1-N4** module, but the ESP32 was tested using a breadboard/devkit setup because the PCB was missing the correct programming-header support and the onboard 3.3 V rail did not function correctly. The 6 V rail did work and was used for the motor side of the circuit.

## Requirement Table

| Requirement Description | Threshold Measure | Target Measure | Final Status | Stretch Requirement |
|---|---|---|---|:---:|
| Surface-mounted 3.3 V regulator | Produce a usable 3.3 V logic rail | Stable 3.3 V rail for ESP32 and H-bridge logic | **Not met.** The 3.3 V rail did not work because of a routing/layout issue involving the regulator inductor path. | No |
| Surface-mounted microcontroller | ESP32 included in the schematic and PCB | ESP32-S3-WROOM-1-N4 soldered to final PCB and able to run motor-control code | **Partially met.** The ESP32-S3-WROOM-1-N4 was soldered to the PCB, but programming and power issues prevented full onboard use. | No |
| External ESP32/devkit fallback | Use a breadboard/devkit if onboard MCU bring-up fails | Validate motor-control behavior with an external ESP32 setup | **Met.** The ESP32 was tested through a breadboard/devkit setup. | No |
| UART communication support | Define module ID and expected command behavior | Match Team 201 communication structure with B1 mapped to message ID D | **Partially met.** The module identity was defined, but final integrated communication testing was limited by hardware bring-up issues. | No |
| Motor power rail | Provide a working motor-voltage rail | Use a stable 6 V rail to power the propulsion motors | **Met.** The 6 V rail worked and was used for the motors. | No |
| Motor driver interface | Connect ESP32 control signals to an H-bridge | Use an H-bridge motor driver for bidirectional motor control | **Partially met.** The H-bridge was included, but final full-system testing was limited. | No |
| Motor channel count | Control at least one motor channel | Use one H-bridge channel to drive the propulsion motor pair | **Met.** The final board used one H-bridge channel to power two motors. | No |
| Forward motor control | Motor can rotate forward | Smooth forward propulsion under command | **Partially met.** The circuit supported forward control, but complete integrated validation was limited. | No |
| Reverse motor control | Motor can rotate backward | Smooth reverse propulsion under command | **Partially met.** The H-bridge design supported reverse control, but complete integrated validation was limited. | No |
| PWM speed control | Basic speed control using PWM | Adjustable open-loop speed control from ESP32 PWM output | **Partially met.** PWM control was part of the design and breadboard testing path, but not fully validated on the final PCB. | Yes |
| Encoder feedback | Include possible encoder input path | Read motor encoder feedback for speed and direction measurement | **Not met.** Encoder feedback was treated as a stretch goal and was not used in the final implementation. | Yes |
| Debugging support | Allow basic voltage and signal probing | Include clear programming access, test points, and debugging indicators | **Not met.** The missing programming header made bring-up harder, and future revisions need better debug access. | No |
| PCB implementation | Create a manufactured PCB for the subsystem | Solder and test the final propulsion board | **Partially met.** The PCB was manufactured and soldered, but the 3.3 V rail and programming-header issues prevented full standalone operation. | No |

## Final Requirement Review

The most successful part of the module was the **motor-power side**. The 6 V rail worked and could be used to power the motors. The final board also included the correct general architecture for a propulsion module: ESP32 controller, motor-driver circuit, motor rail, and support for team communication.

The weakest part of the module was **board bring-up and debugging**. The missing programming header made the soldered ESP32 difficult to program directly, and the failed 3.3 V regulator rail prevented the board from operating as a fully standalone controller. Because of this, the final test setup required an external ESP32 breadboard/devkit instead of relying only on the PCB.

The encoder requirement was not completed. It should be treated as a future improvement rather than a final working feature. For the final version of this report, the propulsion subsystem should be described as an **open-loop motor-control module**, not a closed-loop encoder-controlled module.
