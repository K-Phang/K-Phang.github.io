---
title: Module Schematic
---

# Module Schematic

## Overview

This schematic documents the **B1 Propulsion subsystem** for Team 201's project, **The Duck**. The schematic was designed around an **ESP32-S3-WROOM-1-N4** microcontroller, a **TB67H450FNG,EL H-bridge motor driver**, a **6 V motor rail**, and a **3.3 V logic rail**.

The intended function of the schematic was to allow the ESP32 to receive propulsion commands, generate PWM and direction-control signals, and drive the motors through the H-bridge. The 6 V rail was used for the motor-power side of the system, while the 3.3 V rail was intended to power the ESP32 and logic-side circuitry.

In the final board bring-up, the **6 V rail worked**, but the **3.3 V rail did not work** because of a routing/layout issue around the switching regulator and inductor path. The ESP32-S3-WROOM-1-N4 was soldered onto the PCB, but because of the missing programming-header support and the failed 3.3 V rail, final testing used a breadboard/devkit ESP32 setup where needed.

## Final Schematic Image

![B1 Propulsion Subsystem Schematic](SchematicPropulsion.webp){ width="900" }

**Figure 1:** B1 Propulsion subsystem schematic for The Duck.

## Schematic Design Description

The schematic is divided into the following major sections:

1. **Power input and protection:** brings external power into the board and routes it to the regulator sections.
2. **6 V motor rail:** supplies the motor-power side of the H-bridge and was confirmed to work during final testing.
3. **3.3 V logic rail:** intended to power the ESP32 and logic-side motor-driver circuitry, but did not function correctly on the final PCB.
4. **ESP32-S3-WROOM-1-N4:** intended to act as the main propulsion controller.
5. **TB67H450FNG,EL H-bridge:** provides bidirectional motor-control capability.
6. **UART/team communication interface:** supports the team communication structure for B1 Propulsion, message ID D.
7. **Motor output connector:** routes the H-bridge output to the propulsion motors.

## Final Schematic Review

The schematic captured the correct high-level architecture for the B1 propulsion module. The separation between the logic rail and motor rail was the correct design decision because the motors draw significantly more current than the ESP32 and logic circuitry. The H-bridge was also the correct type of driver for bidirectional DC motor control.

The main issue was not the overall schematic architecture, but the final implementation and board bring-up. The failed 3.3 V rail prevented the PCB from operating as a complete standalone propulsion controller. The missing programming-header support also made the soldered ESP32 difficult to program and debug directly.

For a future revision, the schematic should be updated to include a clearly defined ESP32 programming header, more test points, clearer power-rail indicators, and a corrected 3.3 V regulator implementation based directly on the regulator datasheet reference layout.

## Resources

The final schematic files are linked below:

- [Final Schematic PDF](KPhang_B1_Final_Schematic.pdf)
- [Final Schematic / ECAD Project ZIP](KPhang_B1_ECAD_Project.zip)

