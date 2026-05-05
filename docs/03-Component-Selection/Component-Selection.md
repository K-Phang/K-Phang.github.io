---
title: Component Selection - Team 201 B1 Propulsion Subsystem
---

# Component Selection

## K Phang - B1 Propulsion Subsystem

I was responsible for the **B1 Propulsion subsystem** for Team 201's rover project, **The Duck**. My subsystem was assigned to **K Phang, B1 Propulsion, message ID D**.

The propulsion subsystem was intended to receive commands from the team communication system and translate those commands into motor direction and speed control. The final design used an ESP32-based controller, a motor-driver stage, a 6 V motor rail, and a planned 3.3 V logic rail.

The original design also included encoder feedback as a stretch goal. Encoder feedback was not used in the final implementation, so the final propulsion module should be treated as an **open-loop motor-control subsystem**.

## Final Major Component Summary

| Subsystem | Selected Component | Purpose in Final Design | Final Implementation Status |
|---|---|---|---|
| Microcontroller | ESP32-S3-WROOM-1-N4 | Main controller for receiving commands and generating motor-control signals | Soldered to PCB, but tested through breadboard/devkit because onboard programming and 3.3 V power were not fully functional |
| 3.3 V Logic Regulator | AP63203WU-7 | Intended to generate the 3.3 V rail for ESP32 and logic-side motor-driver power | Included in design, but final 3.3 V rail did not work because of a layout/routing issue |
| 6 V Motor Regulator | LMZ23610TZ/NOPB | Intended to generate the 6 V rail for motor power | Worked and was used for the motor side of the system |
| Motor Driver | TB67H450FNG,EL | H-bridge motor driver for bidirectional motor control | Included in final design; one H-bridge channel was used to power two motors |
| Motors | DC drive motors | Provide propulsion for The Duck | Powered from the working 6 V rail |
| Team Communication Header | UART header/interface | Provides interface path for team command communication | Included as part of the subsystem design and API documentation |

---

## Controller Subsystem - ESP32 Module

The controller subsystem required a surface-mount microcontroller module with enough GPIO pins for motor-control signals, UART communication, and possible future encoder feedback. The team also needed a controller family with strong documentation and easy firmware development support.

<img src="https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/300/773/504/MFG_Attachment-2-ESP32-S3-WROOM-1_sml.jpg" alt="ESP32-S3-WROOM-1-N4 module" width="260">

| Option | Product | Unit Cost | Pros | Cons |
|---|---|---:|---|---|
| **Option 1 - Selected** | [ESP32-S3-WROOM-1-N4](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1-N4/16162639) | **$5.06** | Surface-mount module aligned with the PCB design; integrated PCB antenna simplifies layout; strong ESP32 ecosystem and documentation; enough GPIO for UART, PWM, direction signals, and future encoder work. | More complex than a simpler microcontroller; direct PCB programming requires proper programming-header support; RF keepout and module placement still need to be respected. |
| Option 2 | [ESP32-S3-WROOM-1U-N4](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1U-N4/16162640) | **$5.28** | Same general ESP32-S3 family; external antenna can improve RF placement flexibility. | Requires external antenna hardware; adds BOM and mechanical complexity; unnecessary for this first propulsion board. |
| Option 3 | [ESP32-S3-WROOM-1-N8](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1-N8/15200089) | **$5.49** | Same family as the selected part; larger flash gives more firmware margin. | Extra flash was not required for the propulsion module; slightly higher cost without enough benefit for this design. |

### Final Choice

**Selected Option:** ESP32-S3-WROOM-1-N4

### Rationale

The ESP32-S3-WROOM-1-N4 was selected because it matched the surface-mount requirement, had enough GPIO capability for the propulsion subsystem, and fit the team's ESP32-based development direction. It also avoided the extra hardware required by the external-antenna version.

In the final build, the ESP32-S3-WROOM-1-N4 was soldered to the PCB. However, the board was missing proper programming-header support and the onboard 3.3 V rail did not work. Because of this, the final testing process used a breadboard/devkit ESP32 setup while the PCB was used where possible for the motor-power and driver portions.

---

## Logic Power Subsystem - 12 V to 3.3 V Converter

The logic power subsystem required a compact surface-mount buck regulator to convert the main input rail to 3.3 V for the ESP32 and logic-side circuitry.

<img src="https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/010/103/MFG_AP6320x_sml.jpg" alt="AP63203WU-7 buck regulator" width="220">

| Option | Product | Unit Cost | Pros | Cons |
|---|---|---:|---|---|
| **Option 1 - Selected** | [AP63203WU-7](https://www.digikey.com/en/products/detail/diodes-incorporated/AP63203WU-7/9858426) | **$0.71** | Fixed 3.3 V output simplifies design; compact surface-mount package; low cost; appropriate for a dedicated logic rail from the main input. | Layout-sensitive because the regulator, inductor, and grounding path must be routed correctly; current margin must still be checked against the logic load. |
| Option 2 | [AP63203QWU-7](https://www.digikey.com/en/products/detail/diodes-incorporated/AP63203QWU-7/16548045) | **$0.96** | Same general function as the selected part; automotive-qualified variant; compact and surface mount. | Higher cost; automotive qualification was not necessary for this class project. |
| Option 3 | [LMR51420XDDCR](https://www.digikey.com/en/products/detail/texas-instruments/LMR51420XDDCR/16705125) | **$1.81** | Good vendor support; surface-mount buck regulator; adjustable output gives flexibility. | Requires feedback-resistor design; higher cost; less direct than a fixed 3.3 V part. |

### Final Choice

**Selected Option:** AP63203WU-7

### Rationale

The AP63203WU-7 was selected because it directly provides a fixed 3.3 V output without requiring an external feedback divider. It was also low-cost and compact, making it a strong fit for the propulsion board.

The final board did not successfully produce the 3.3 V rail. The failure appears to be related to the regulator layout, specifically the inductor path and grounding/routing around the regulator. This made the 3.3 V subsystem one of the main items that would need to be corrected in a hardware Version 2.0.

---

## Intermediate Power Subsystem - 12 V to 6 V Converter

The 6 V subsystem required a regulator capable of stepping the main input rail down to a motor-supply voltage. This rail was important because the propulsion motors needed a separate supply from the ESP32 logic rail.

<img src="https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/003/210/375/296%7ETZA11A%7ENDY%7E11_sml%28200x200%29.jpg" alt="LMZ23610TZ/NOPB power module" width="260">

| Option | Product | Unit Cost | Pros | Cons |
|---|---|---:|---|---|
| **Option 1 - Selected** | [LMZ23610TZ/NOPB](https://www.digikey.com/en/products/detail/texas-instruments/LMZ23610TZ-NOPB/2673196) | **$31.11** | High current capability up to 10 A; wide input range; integrated power module reduces external power-design burden; strong margin for motor loads. | Highest cost among compared options; physically larger than simpler regulators; more expensive than necessary if final current demand is low. |
| Option 2 | [LMZ22010TZ/NOPB](https://www.digikey.com/en/products/detail/texas-instruments/LMZ22010TZ-NOPB/2626436) | **$23.90** | Also supports up to 10 A; lower cost than the selected option; surface-mount module reduces implementation difficulty. | Lower maximum input range; less future margin if upstream power changes. |
| Option 3 | [LMZ22008TZ/NOPB](https://www.digikey.com/en/products/detail/texas-instruments/LMZ22008TZ-NOPB/2626435) | **$23.43** | Lower cost than the selected part; same general module family; still surface mount and adjustable. | Reduced output current at 8 A; lower input-voltage range; less margin for expansion. |

### Final Choice

**Selected Option:** LMZ23610TZ/NOPB

### Rationale

The LMZ23610TZ/NOPB was selected because it provided strong current margin for the motor rail and reduced the amount of power-regulator design work required. The high current capacity was useful because motor startup and stall conditions can demand significantly more current than normal unloaded operation.

The 6 V rail was one of the successful parts of the final board. It worked and was used to power the propulsion motors. In the final test setup, the motor side of the H-bridge drew from the 6 V rail while the ESP32 logic side required external support because the onboard 3.3 V rail did not function.

---

## Motor Actuation Subsystem - H-Bridge Motor Driver

The motor actuation subsystem required a surface-mount brushed DC motor driver capable of bidirectional control. The final design used one H-bridge channel to power two motors.

<img src="https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/010/328/264%3B-P-HSOP8-0405-1%2C27-001%3B-FN%3B-8_sml.jpg" alt="TB67H450FNG motor driver" width="220">

| Option | Product | Unit Cost | Pros | Cons |
|---|---|---:|---|---|
| **Option 1 - Selected** | [TB67H450FNG,EL](https://www.digikey.com/en/products/detail/toshiba-semiconductor-and-storage/TB67H450FNG-EL/10130904) | **$1.29** | Matches the current design direction; suitable for a brushed DC motor channel; compact surface-mount package; low cost; supports bidirectional H-bridge control. | DigiKey flags it as not recommended for new designs; current and thermal limits must be checked carefully when driving more than one motor from one channel. |
| Option 2 | [TB67H451FNG,EL](https://www.digikey.com/en/products/detail/toshiba-semiconductor-and-storage/TB67H451FNG-EL/11568781) | **$1.29** | Close same-family alternative; similar electrical class and package style; useful fallback option. | Requires checking pin-level and behavior compatibility before substitution; not the currently integrated part. |
| Option 3 | [DRV8251ADDAR](https://www.digikey.com/en/products/detail/texas-instruments/DRV8251ADDAR/16182453) | **$2.25** | Strong alternative from TI; good documentation ecosystem; good candidate for a future redesign. | Higher cost; different package and integration path; would require schematic and PCB redesign. |

### Final Choice

**Selected Option:** TB67H450FNG,EL

### Rationale

The TB67H450FNG,EL was selected because it fit the surface-mount board design, supported bidirectional brushed DC motor control, and had a low unit cost. It was also already aligned with the schematic direction when the design was finalized.

The main weakness of this selection is that the part was marked as not recommended for new designs. A future revision should consider replacing it with a more current motor-driver option, especially because the final implementation used one H-bridge channel to power two motors. That makes current margin and thermal behavior more important.

---

## ESP32 Pinout and Subsystem Mapping

The table below summarizes the intended subsystem use for the ESP32 pins in the B1 propulsion design. Exact GPIO assignments should match the final schematic and firmware. If a pin changed during testing, the schematic and code should be treated as the final source.

| Function | Signal Type | Intended Use | Final Notes |
|---|---|---|---|
| UART RX | Digital input | Receive commands from team communication bus | Used for team API design and subsystem communication planning |
| UART TX | Digital output | Send response/status messages to team communication bus | Used for team API design and subsystem communication planning |
| Motor PWM | PWM output | Control motor speed through H-bridge input | Intended for open-loop speed control |
| Motor Direction 1 | Digital output | H-bridge direction input | Used to define motor direction |
| Motor Direction 2 | Digital output | H-bridge direction input | Used to define motor direction |
| Enable / Sleep | Digital output | Enable or disable motor-driver operation | Useful for safe startup and shutdown |
| Encoder A | Digital input | Planned encoder feedback | Stretch goal, not used in final implementation |
| Encoder B | Digital input | Planned encoder feedback | Stretch goal, not used in final implementation |
| Debug LED | Digital output | Basic status indication | Useful for future debugging |
| Debug Button | Digital input | Manual debug or test input | Useful for future board bring-up |

---

## Minor Component Selection

| Component | Selected Part | Unit Cost | Product Link |
|---|---|---:|---|
| 12 V Power Connector Contact | JST `SVH-21T-1.1` | **$0.10** | [JST SVH-21T-1.1 contact](https://www.digikey.com/en/products/detail/jst-sales-america-inc/SVH-21T-1-1/527366) |
| 12 V Power Connector Housing | JST `VHR-2N` | **$0.10** | [JST VHR-2N housing](https://www.digikey.com/en/products/detail/jst-sales-america-inc/VHR-2N/608624) |
| Fuse | Littelfuse `0213005.M` | **$2.06** | [Littelfuse 0213005.M](https://www.digikey.com/en/products/detail/littelfuse-inc/0213005-M/552068) |
| Motor Power Header and 12 V Power Header | JST `B2PS-VH` | **$0.16** | [JST B2PS-VH](https://www.digikey.com/en/products/detail/jst-sales-america-inc/B2PS-VH/926555) |
| Green LED | Lite-On `LTST-C150GKT` | **$0.15** | [Lite-On LTST-C150GKT](https://www.digikey.com/en/products/detail/lite-on-inc/LTST-C150GKT/269216) |
| Red LED | Lite-On `LTST-C150EKT` | **$0.14** | [Lite-On LTST-C150EKT](https://www.digikey.com/en/products/detail/liteon/LTST-C150EKT/269215) |
| 8-Pin UART Header | Amphenol / FCI `75869-332LF` | **$0.68** | [Amphenol 75869-332LF](https://www.digikey.com/en/products/detail/amphenol-cs-fci/75869-332LF/1523267) |
| Fuse Holder | Schurter `3-143-050` | **$2.31** | [Schurter 3-143-050](https://www.digikey.com/en/products/detail/schurter-inc/3-143-050/25659195) |
| Capacitor 10 uF | Murata `GRM31CR71E106MA12K` | **$0.30** | [Murata GRM31CR71E106MA12K](https://www.digikey.com/en/products/detail/murata-electronics/GRM31CR71E106MA12K/13904832) |
| Capacitor 100 uF | Murata `GRM31CD80J107MEA8L` | **$0.42** | [Murata GRM31CD80J107MEA8L](https://www.digikey.com/en/products/detail/murata-electronics/GRM31CD80J107MEA8L/13904781) |
| Capacitor 22 uF | Würth `885012208019` | **$0.71** | [Würth 885012208019](https://www.digikey.com/en/products/detail/w%C3%BCrth-elektronik/885012208019/5453421) |
| Capacitor 0.1 uF | Yageo `CC1206JRX7R9BB104` | **$0.20** | [Yageo CC1206JRX7R9BB104](https://www.digikey.com/en/products/detail/yageo/CC1206JRX7R9BB104/2833600) |
| Motor Encoder Header | TE Connectivity `281695-4` | **$1.01** | [TE Connectivity 281695-4](https://www.digikey.com/en/products/detail/te-connectivity-amp-connectors/281695-4/1150102) |
| Button | E-Switch `TL9320AF400QG` | **$0.90** | [E-Switch TL9320AF400QG](https://www.digikey.com/en/products/detail/e-switch/TL9320AF400QG/11698099) |
| 100 Ohm Resistor | Yageo `RC1206FR-07100RL` | **$0.10** | [Yageo RC1206FR-07100RL](https://www.digikey.com/en/products/detail/yageo/RC1206FR-07100RL/728491) |
| 10 kOhm Resistor | Yageo `RC1206FR-0710KL` | **$0.10** | [Yageo RC1206FR-0710KL](https://www.digikey.com/en/products/detail/yageo/RC1206FR-0710KL/728483) |
| Resistor for 6 V Module Setpoint | Yageo `RC1206FR-076K49L` | **$0.10** | [Yageo RC1206FR-076K49L](https://www.digikey.com/en/products/detail/yageo/RC1206FR-076K49L/729022) |
| 1 kOhm Resistor for 6 V Module Setpoint | Yageo `RC1206JR-071KP` | **$0.10** | [Yageo RC1206JR-071KP](https://www.digikey.com/en/products/detail/yageo/RC1206JR-071KP/4935356) |

## Final Component Selection Summary

The selected components formed a propulsion subsystem built around an ESP32 controller, regulated power rails, and H-bridge motor-driver hardware.

The **ESP32-S3-WROOM-1-N4** was selected as the main controller because it provided enough GPIO, strong documentation, and compatibility with the team's ESP32 development workflow. The **AP63203WU-7** was selected for the 3.3 V logic rail because it simplified the design with a fixed output, although this part of the final board did not work due to layout/routing issues. The **LMZ23610TZ/NOPB** was selected for the 6 V motor rail because it provided strong current margin, and this rail successfully worked in the final board. The **TB67H450FNG,EL** was selected for bidirectional motor control, though a future design should consider a newer motor-driver option with better lifecycle support and clearer current margin.

Overall, the component choices were reasonable for the intended design, but the final project showed that correct layout, programming access, and testability were just as important as selecting capable parts.
