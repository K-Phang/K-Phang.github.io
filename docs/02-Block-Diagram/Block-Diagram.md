---
title: Module Block Diagram
tags:
  - egr314
  - propulsion
---

## Overview

This block diagram illustrates the architecture of the Team 201 B1 propulsion subsystem and its interface with the overall system. The subsystem is responsible for controlling two DC motors that drive propellers, enabling forward and reverse motion as well as variable speed operation.

Power is supplied by a 9V battery through a main power switch. The battery voltage is regulated into two separate rails: a 3.3V logic rail used to power the ESP32 microcontroller and communication circuitry, and a 6V motor rail used to supply the H-bridge motor drivers and DC motors.

The propulsion subsystem receives motion commands from the Control Subsystem through a shared UART serial communication link (RX/TX). The ESP32 decodes these commands and generates direction and PWM control signals to the H-bridge drivers, which provide bidirectional motor control.

Motor encoders are connected directly to the ESP32 to provide speed feedback, enabling monitoring and potential closed-loop speed regulation. Debugging features, including a debug button and status LEDs, are included to support system testing and troubleshooting.

## Propulsion Subsystem Block Diagram

![K Phang EGR314 Propulsion Subsystem Block Diagram](314_KPhang_BlockDiagram.png)
