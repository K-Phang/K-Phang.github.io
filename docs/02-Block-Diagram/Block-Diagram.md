---
title: Module Block Diagram
tags:
  - egr314
  - propulsion
  - TheDuck
  - ESP32
---

# Module Block Diagram

## Overview

This block diagram illustrates the architecture of the **B1 Propulsion subsystem** for Team 201's rover project, **The Duck**. My subsystem was responsible for motor control and was assigned to **K Phang, B1 Propulsion, message ID D**.

The original block diagram showed the intended final architecture: an ESP32 microcontroller receiving team communication commands, generating motor-control outputs, and driving the propulsion motors through an H-bridge motor driver. The design also included separate power regulation for the logic and motor sections of the board. The target hardware architecture included a **3.3 V logic rail** for the ESP32 and H-bridge logic, plus a **6 V motor rail** for the drive motors.

In the final implementation, the system did not fully match the ideal block diagram. The **6 V motor rail worked**, so it was usable for motor power. The **3.3 V regulator rail did not work** because of a layout/routing issue involving the inductor path. Because of this, the ESP32 had to be powered and tested through a breadboard/devkit setup rather than relying only on the PCB. The encoder feedback path was also not completed and should be treated as a stretch goal rather than a final working feature.

## Propulsion Subsystem Block Diagram

![K Phang EGR314 B1 Propulsion Subsystem Block Diagram](314_KPhang_BlockDiagram.png)

## Block Diagram Decision-Making Process

The block diagram was developed by separating the propulsion module into four major functions:

1. **Power input and regulation**
2. **Microcontroller logic**
3. **Motor-driver output**
4. **Team communication interface**

This structure was chosen because the propulsion board needed to handle both low-voltage logic signals and higher-current motor power. Keeping these functions visually separate made it easier to design and debug the system. The ESP32 section represents the control logic, the H-bridge section represents the motor-power switching stage, and the voltage-regulator section shows how the board was supposed to generate the required power rails.

The original design also included encoder feedback because closed-loop motor control was considered useful for future speed regulation. However, the final purchased and used motors were basic TT DC gearbox motors without built-in encoders. For the final report, the encoder path should be interpreted as an earlier design goal and future improvement rather than a validated final function.

## How the Block Diagram Meets Product Requirements

The block diagram supports the core propulsion requirements for The Duck by showing how commands would move from the team communication system into the B1 propulsion controller and then into the motor driver. The ESP32 receives or interprets motion commands, outputs direction and PWM signals, and uses the H-bridge to control motor direction and speed.

The diagram also supports the power requirements by separating the board into a **3.3 V logic rail** and a **6 V motor rail**. This separation was important because the ESP32 and logic-side motor-driver inputs require low-voltage logic power, while the motors require a separate supply capable of handling larger current draw.

The final hardware partially met this diagram. The motor rail and basic motor-driver architecture were present, but the failed 3.3 V rail prevented full standalone PCB operation. The final working setup therefore used the PCB for the motor-power side where possible and used an external ESP32 breadboard/devkit setup for controller testing.

## Final Implementation Notes

The final B1 propulsion system differed from the original diagram in these ways:

- The onboard **6 V rail worked** and was used for motor power.
- The onboard **3.3 V rail did not work**, so the ESP32 logic had to be powered externally during testing.
- The **ESP32-S3-WROOM-1-N4** was soldered onto the PCB, but the board was missing proper programming-header support.
- The final motor design used **one H-bridge motor-driver channel** to power two motors.
- Encoder feedback was not used in the final implementation.

## Source Files

The block diagram image used on this page is included directly in this repository:

- [Block Diagram PNG](314_KPhang_BlockDiagram.png)

A future cleanup item is to include the editable source file for this diagram, such as a Draw.io, PowerPoint, or other source file, as a zipped archive in this folder.

