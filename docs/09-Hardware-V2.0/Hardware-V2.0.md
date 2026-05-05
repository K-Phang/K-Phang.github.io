---
title: Hardware V2.0
---

# Hardware V2.0

## Overview

This page describes the changes I would make if I created a second hardware revision of my **B1 Propulsion subsystem** for Team 201's project, **The Duck**.

The first revision of the propulsion board successfully reached the manufactured PCB stage and partially worked during bring-up. The **6 V motor rail worked**, and the board physically included the ESP32-S3-WROOM-1-N4, H-bridge motor-driver stage, motor connectors, and supporting power hardware. However, the board did not become a fully standalone working controller because the **3.3 V rail did not work** and the PCB did not include proper programming-header support for the ESP32.

The main goal of Hardware V2.0 would be to turn the board from a partially testable prototype into a reliable, programmable, and easier-to-debug propulsion controller.

## Version 1.0 Issues

The most important issues from the first version were:

| Issue | Effect on Final Build |
|---|---|
| Missing ESP32 programming header | Made it difficult to program and debug the soldered ESP32 directly on the PCB |
| Failed 3.3 V rail | Prevented the ESP32 and logic circuitry from being powered onboard |
| Weak bring-up visibility | Made it harder to quickly identify whether power, logic, or motor-driver sections were working |
| Encoder design not finalized | Encoder feedback was not used in the final implementation |
| Motor choice changed | Final TT motors did not include built-in encoders |
| Limited test points | Required more manual probing and made debugging slower |
| One H-bridge channel powering two motors | Worked as a simplified final approach, but current and thermal margins should be reviewed |

## Fix 1: Add a Dedicated ESP32 Programming Header

The most important Hardware V2.0 change would be adding a proper ESP32 programming and debug header. In the first board, the ESP32-S3-WROOM-1-N4 was soldered onto the PCB, but the board did not provide convenient programming access. This made the microcontroller difficult to flash after assembly.

A second revision should include clearly labeled access to:

| Signal | Purpose |
|---|---|
| 3.3 V | Programming/debug reference power |
| GND | Common ground |
| TX | Serial transmit |
| RX | Serial receive |
| EN / Reset | Reset control |
| BOOT / GPIO0 equivalent | Bootloader entry |
| USB D+ / D-, if used | Direct USB programming option |

This would allow the ESP32 to be programmed and debugged without soldering temporary wires or relying on an external breadboard setup.

## Fix 2: Redesign the 3.3 V Regulator Layout

The 3.3 V rail was the most important electrical failure on the first board. The selected regulator was reasonable, but the implementation failed because of the routing/layout around the regulator, inductor, and grounding path.

For Hardware V2.0, the 3.3 V regulator section should be rebuilt directly from the regulator datasheet reference layout. The regulator, inductor, input capacitor, output capacitor, and ground return should be placed tightly together. The switching loop should be short, and the ground path should be clean.

The new layout should include:

1. Short routing between regulator switch node and inductor.
2. Input capacitor placed close to the regulator input and ground pins.
3. Output capacitor placed close to the inductor/output node.
4. Clean ground return path.
5. Wider power traces or pours where appropriate.
6. A clearly labeled 3.3 V test point.
7. A 3.3 V status LED.

This would directly address the failure that prevented the ESP32 from running from onboard power.

## Fix 3: Add Power-Rail Test Points and Status LEDs

The first board was harder to debug than it needed to be. Hardware V2.0 should include labeled test points for every important rail and signal group.

Recommended test points:

| Test Point | Purpose |
|---|---|
| VIN | Confirms input power reaches the board |
| 6 V | Confirms motor rail output |
| 3.3 V | Confirms logic rail output |
| GND | Common probe reference |
| H-bridge VM | Confirms motor-driver power |
| H-bridge VCC / logic | Confirms motor-driver logic power |
| PWM | Confirms ESP32 speed-control signal |
| DIR1 | Confirms direction-control signal |
| DIR2 | Confirms direction-control signal |
| Motor output A/B | Confirms switched motor output |

Status LEDs should be added for VIN, 6 V, and 3.3 V. This would make initial board bring-up much faster because power problems could be seen immediately.

## Fix 4: Separate Motor Power and Logic Routing More Clearly

The propulsion board handles both motor power and low-voltage logic. These should be separated as much as practical in the layout because motors create electrical noise and can draw large transient currents.

Hardware V2.0 should improve this by:

1. Keeping motor-current paths short and wide.
2. Keeping ESP32 logic traces away from high-current motor traces.
3. Routing motor outputs away from sensitive logic inputs.
4. Adding bulk capacitance near the motor-driver power input.
5. Using a more deliberate ground strategy.
6. Making the motor rail visually and electrically distinct from the logic rail.

This would improve reliability and make the design easier to inspect.

## Fix 5: Update the Motor-Driver Strategy

The first design used the TB67H450FNG,EL H-bridge motor driver. This part was acceptable for the prototype, but it was marked as not recommended for new designs. Hardware V2.0 should consider a newer motor-driver part with better lifecycle status, stronger documentation, and clearer current margin.

The final implementation used one H-bridge channel to power two TT motors. In Hardware V2.0, I would avoid treating this as the default design unless the current and thermal behavior were verified. A cleaner design would either:

1. Use one motor-driver channel per motor, or
2. Use a single motor driver with enough current margin for both motors, clearly documented in the schematic and BOM.

The motor-driver section should also include better fault handling if the selected driver supports it.

## Fix 6: Decide Whether Encoder Feedback Is Actually Needed

The original design considered encoder feedback, but the final motors were basic TT DC gearbox motors without built-in encoders. Because of that, the final system became open-loop motor control.

For Hardware V2.0, there should be a firm decision before schematic design:

| Option | Design Direction |
|---|---|
| Open-loop control | Remove encoder headers and simplify the board |
| Closed-loop control | Select motors with encoders before the purchase order and include proper encoder input circuitry |
| External encoder add-on | Keep encoder headers, but document them as future expansion |

The main mistake to avoid is designing around encoder feedback while purchasing motors that do not provide encoder outputs.

## Fix 7: Improve Connector Labels and Silkscreen

The first PCB included useful labeling, including the project name and team information. Hardware V2.0 should go further by making every connector understandable during lab testing.

Recommended silkscreen labels:

| Connector / Area | Label Needed |
|---|---|
| Power input | VIN and GND |
| Motor output | Motor + and Motor - |
| UART header | TX, RX, GND, 3.3 V |
| Programming header | TX, RX, EN, BOOT, 3.3 V, GND |
| Regulator outputs | 6 V and 3.3 V |
| H-bridge pins | PWM, DIR, VM, VCC |
| Test points | Exact voltage or signal name |

This would reduce wiring mistakes and make the board easier for another student to understand.

## Fix 8: Improve Bring-Up Procedure

Hardware V2.0 should be designed around a staged bring-up process instead of assuming the whole board works at once.

Recommended bring-up order:

1. Inspect the unpowered PCB for solder bridges and orientation errors.
2. Apply input power with current limiting.
3. Verify VIN and ground.
4. Verify 6 V rail.
5. Verify 3.3 V rail.
6. Confirm power LEDs.
7. Program ESP32 through onboard header.
8. Blink a debug LED.
9. Send UART test message.
10. Test PWM and direction outputs without motors.
11. Connect motor driver.
12. Test motor output with one motor.
13. Test full motor load.

Designing the PCB to support this process would make debugging more controlled and less chaotic.

## Hardware V2.0 Summary

The second hardware revision should keep the same basic architecture: ESP32 controller, separate logic and motor rails, H-bridge motor drive, and team communication support. The core idea was correct.

The main changes should focus on execution:

1. Add a real ESP32 programming header.
2. Correct the 3.3 V regulator layout.
3. Add test points and power LEDs.
4. Improve motor-power routing.
5. Reconsider the motor-driver selection.
6. Decide early whether encoder feedback is required.
7. Improve silkscreen labels.
8. Make the board easier to bring up in stages.

The most important lesson is that a PCB is not finished when the schematic is finished or when the board is manufactured. A good board must also be programmable, measurable, debuggable, and recoverable when something goes wrong.
