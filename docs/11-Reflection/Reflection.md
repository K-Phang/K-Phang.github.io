---
title: Reflection
---

# Reflection

## Review of Module's Success

My module was the **B1 Propulsion subsystem** for Team 201's project, **The Duck**. The purpose of my module was to control the drive motors for the rover using an ESP32-based PCB, a motor-driver circuit, and separate power rails for logic and motor power.

The module was partially successful. The strongest success was that the board reached the manufactured PCB stage and the **6 V motor rail worked**. This meant the motor-power side of the design was usable and the board could support the motors from the intended motor-voltage rail. The board also physically included the main components needed for the propulsion subsystem, including the ESP32-S3-WROOM-1-N4, the H-bridge motor-driver section, motor connectors, and supporting power circuitry.

The module did not fully succeed as a standalone propulsion controller. The biggest failure was the **3.3 V rail**, which did not work because of a layout/routing issue around the switching regulator and inductor path. Since the ESP32 and logic-side circuitry depend on 3.3 V, this prevented the board from running completely on its own. The second major issue was the missing ESP32 programming-header support. The ESP32 was soldered onto the PCB, but the board did not provide a clean way to program and debug it after assembly. Because of this, testing required an external ESP32 breadboard/devkit setup instead of relying completely on the PCB.

The original plan also considered encoder feedback, but the final motors used were basic TT DC gearbox motors without built-in encoders. Because of that, encoder feedback was not part of the final implementation. The final system should be described as an open-loop motor-control subsystem rather than a closed-loop speed-control subsystem.

Overall, the module succeeded as a manufactured prototype and partially succeeded electrically through the working 6 V rail. It did not fully meet the goal of becoming a complete standalone motor-control PCB because of the failed 3.3 V rail and missing programming access.

## Microcontroller / Module Startup Tips

1. Always design the programming header before finalizing the PCB. A soldered microcontroller is not useful if it cannot be programmed easily after assembly.

2. Bring up the power system before testing anything else. Confirm input voltage, ground, 6 V, and 3.3 V before connecting the microcontroller or motor driver.

3. Add test points for every important rail and signal. At minimum, include VIN, GND, 6 V, 3.3 V, PWM, direction signals, and motor-driver output.

4. Use the regulator datasheet reference layout closely. Switching regulators are layout-sensitive, and small routing mistakes can prevent the entire rail from working.

5. Do not assume a schematic is correct just because the symbols are connected. The PCB layout, footprint, pin mapping, and regulator routing matter just as much.

6. Verify the exact motor before ordering parts around it. If the final motor does not include encoders, the encoder section becomes a future feature rather than a final working requirement.

7. Test the board in stages instead of all at once. First test power rails, then microcontroller programming, then logic outputs, then motor-driver behavior, and only then connect the motors.

8. Label connectors clearly on the silkscreen. During testing, unclear headers waste time and increase the chance of wiring mistakes.

9. Keep motor power and logic power separated. Motors draw large transient currents and should not be treated like normal low-current logic loads.

10. Order extra small components. Small surface-mount parts, connectors, and passives are easy to lose or damage during assembly.

## Lessons Learned

1. I learned that PCB design is not finished when the schematic is finished. The schematic can show the correct architecture while the board still fails because of layout, routing, footprint, or bring-up issues.

2. I learned that power regulation is one of the highest-risk parts of an embedded board. My 6 V rail worked, but the 3.3 V rail failed, and that one failure prevented the ESP32 from operating as a standalone controller.

3. I learned that a switching regulator must be routed carefully. The inductor, capacitors, ground path, and regulator pins need to follow the datasheet layout closely because the circuit is sensitive to physical layout.

4. I learned that programming access must be designed into the board from the beginning. A microcontroller soldered directly onto a PCB needs a reliable way to enter boot mode, reset, and communicate over serial or USB.

5. I learned that test points are not optional on a prototype. If the board does not work immediately, test points are what make it possible to isolate the problem quickly.

6. I learned that motor-control boards need more power margin than basic logic boards. Motors can draw much higher current during startup or stall than they draw during normal no-load operation.

7. I learned that design requirements need to stay synchronized with purchased parts. The original plan considered encoder feedback, but the final TT motors did not include encoders, so the final implementation had to become open-loop.

8. I learned that documentation needs to reflect the final build, not just the original plan. If the final board differs from the initial design, the report needs to explain what changed and why.

9. I learned that naming files clearly matters. Schematic PDFs, ECAD project zips, Gerber files, BOM files, and PCB images need obvious names so graders and future engineers can find them.

10. I learned that a partially working board can still be valuable if the failure is documented honestly. The 6 V rail working, the 3.3 V rail failing, and the programming-header issue all gave clear lessons for Hardware V2.0.

## Recommendations for Future Students

1. Start the PCB earlier than you think you need to, because schematic work, footprint checking, routing, fabrication, soldering, and debugging all take longer than expected.

2. Add a programming header and test points before sending the board out for fabrication, because debugging without them becomes much harder than it needs to be.

3. Treat the power system as its own design problem instead of a small support section, because one failed voltage rail can stop the entire board from working.

4. Verify your purchased parts before finalizing the schematic and BOM, especially motors, connectors, regulators, and microcontrollers.

5. Keep your documentation updated while you work instead of trying to reconstruct everything at the end, because the final report requires accurate files, screenshots, explanations, and links from every stage of the design.

## Final Reflection

This project showed me that embedded systems design is mostly about integration. Selecting an ESP32, motor driver, and regulators was only one part of the work. The harder part was making those components work together on a physical PCB with correct routing, programming access, testability, and power behavior.

My final board was not a complete success, but it was not a useless failure either. It reached fabrication, the 6 V rail worked, and the remaining issues were specific enough to turn into a clear second revision plan. The main thing I would change next time is designing for bring-up from the start. A board should not only be designed to work; it should be designed to be tested when it does not work.
