---
title: Welcome
tags:
- EGR314
- Team201
- Propulsion
- ESP32
- PCB
---

<center>
<font size="6">K Phang Datasheet</font><br>
as part of<br>
<font size="8">Rover Project</font><br>
for<br>
<font size="5">Team 201</font><br>

**Final Report Submission: May 2026**
</center>

## Introduction

This individual datasheet documents my work on the **B1 Propulsion module** for Team 201's EGR 314 rover project. The overall team project was a modular exploration rover designed to operate in environments that may be unsafe or inconvenient for direct human access. My subsystem focused on driving the rover's propulsion motors through an ESP32-based motor-control board.

The purpose of this datasheet is to record the design process, hardware decisions, schematic design, PCB design, final implementation state, testing results, and design changes that occurred throughout the project. This report also documents what worked, what did not work, and what should be improved in a future hardware revision.

## Project Summary

Team 201's rover was divided into multiple subsystem modules, with each module assigned to a team member and mapped to a team communication ID. My module was **K Phang, B1 Propulsion, message ID D**. The intended function of this subsystem was to receive commands from the team communication system and control the rover's drive motors using an ESP32 microcontroller and an H-bridge motor driver.

The final B1 propulsion board included an **ESP32-S3-WROOM-1-N4**, a motor-driver circuit, a 6 V motor rail, and supporting power circuitry. The final implementation changed from the original stretch-goal design because encoder feedback was not completed, and the PCB had a missing programming-header issue. The 6 V rail functioned and was usable for the motors, but the 3.3 V rail did not function correctly because of a power-routing issue involving the inductor and regulator layout. As a result, the ESP32 was tested through a breadboard/devkit setup while the PCB was used where possible for motor-power and driver testing.

The team report website can be found here: [Team 201 Final Report](https://egr314-s-2026-201.github.io/).

## My Contribution

My role was to design and document the **B1 Propulsion subsystem**. This included selecting the main propulsion-control components, designing the schematic, creating the PCB layout, preparing the bill of materials, documenting the power budget, and evaluating what changes would be required for a more reliable second revision.

The final propulsion subsystem used one H-bridge motor-driver channel to power two motors from the 6 V rail. The original concept included encoder feedback as a stretch goal, but the final tested implementation focused on basic motor control because the encoder system was not completed. The board was also affected by two important bring-up issues: the missing ESP32 programming header and the failed 3.3 V rail. These issues are documented in the PCB, Hardware V2.0, Resources, and Reflection sections.

## Datasheet Navigation

The sections of this datasheet are organized in the same order as the final individual report rubric.

- [Requirements](01-Requirements/Requirements.md): summarizes the module requirements and what the B1 propulsion board needed to accomplish.
- [Block Diagram](02-Block-Diagram/Block-Diagram.md): shows the subsystem layout and explains how the propulsion module connects to the rest of the rover.
- [Component Selection](03-Component-Selection/Component-Selection.md): documents the major components selected for the final propulsion design.
- [Power Budget](04-Power-Budget/Power-Budget.md): estimates the electrical load of the subsystem and explains the power-rail decisions.
- [Schematic](05-Schematic/Schematic.md): provides the final schematic image, PDF, and ECAD source files.
- [BOM](06-BOM/BOM.md): lists the final bill of materials used for the board.
- [PCB](07-PCB/PCB.md): documents the final PCB design, board images, and bring-up results.
- [API](08-API/API.md): describes the communication interface and message behavior for the B1 propulsion module.
- [Hardware V2.0](09-Hardware-V2.0/Hardware-V2.0.md): explains the main hardware improvements needed for a second revision.
- [Resources](10-Resources/Resources.md): contains final source files, code files, project files, and supporting media.
- [Reflection](11-Reflection/Reflection.md): reviews what succeeded, what failed, lessons learned, and recommendations for future students.
