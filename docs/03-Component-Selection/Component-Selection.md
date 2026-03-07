---
title: Component Selection - Team 201 B1 Motor Control Subsystem
---

## K Phang - Motor Control Subsystem

### Role and Responsibilities
I am responsible for the motor control subsystem which receives UART serial commands from the control system and translates them into motor direction and speed control. My subsystem includes:
- **Communication**: UART serial interface (RX/TX) for receiving motor commands
- **Actuation**: Dual DC motors with H-bridge drivers for bidirectional control
- **Power Management**: 3.3V regulation for microcontroller and 6V regulation for motors
- **Sensing (Stretch Goal)**: Optical encoders for position/speed feedback

# Component Selection

## **Controller Subsystem — ESP32 Module**

The controller subsystem requires a surface-mount microcontroller module with Wi-Fi support, adequate GPIO availability, and strong documentation support for firmware development and team integration.

<img src="https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/5910/MFG_ESP32-S3-WROOM-1-N4R2.jpg" alt="ESP32-S3-WROOM-1-N4 module" width="260">

| Option | Product | Unit Cost | Pros | Cons |
|---|---|---:|---|---|
| **Option 1 — Selected** | [ESP32-S3-WROOM-1-N4](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1-N4/16162639) | **$5.06** | Surface-mount module already aligned with the current design; integrated PCB antenna simplifies layout; strong ESP32 ecosystem and documentation; avoids external RF hardware. | More expensive than simple MCUs without wireless; integrated PCB antenna gives less flexibility than an external antenna version. |
| Option 2 | [ESP32-S3-WROOM-1U-N4](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1U-N4/16162640) | **$5.28** | Same family and feature set as the selected part; external antenna can improve placement flexibility; useful in an enclosure that attenuates RF. | Requires external antenna hardware; adds BOM and mechanical integration complexity; less convenient for an initial board revision. |
| Option 3 | [ESP32-S3-WROOM-1-N8](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1-N8/15200089) | **$5.49** | Same family as the selected part; larger flash gives more firmware margin; still uses integrated PCB antenna. | Extra flash is not currently required by the project; slightly higher cost for limited immediate benefit. |

### Final Choice
**Selected Option:** ESP32-S3-WROOM-1-N4

### Rationale
The ESP32-S3-WROOM-1-N4 is the best fit for the current design because it preserves the exact module family already planned, keeps RF integration simple through the onboard PCB antenna, and provides enough capability without introducing unnecessary cost or integration risk. The external-antenna version would only be better if enclosure constraints or RF placement became a major problem, and the N8 variant adds memory that is not currently required by the design.

---

## **Logic Power Subsystem — 12V to 3.3V Converter**

The logic power subsystem requires a compact surface-mount buck regulator that can efficiently convert the 12V rail to 3.3V for logic and control circuitry.

<img src="https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/5293/MFG_AP63203WU-7.jpg" alt="AP63203WU-7 buck regulator" width="220">

| Option | Product | Unit Cost | Pros | Cons |
|---|---|---:|---|---|
| **Option 1 — Selected** | [AP63203WU-7](https://www.digikey.com/en/products/detail/diodes-incorporated/AP63203WU-7/9858426) | **$0.71** | Fixed 3.3V output simplifies design; compact surface-mount package; low cost; appropriate for a dedicated logic rail from 12V input. | Less configurable than an adjustable regulator; current margin must still be checked against total 3.3V rail demand. |
| Option 2 | [AP63203QWU-7](https://www.digikey.com/en/products/detail/diodes-incorporated/AP63203QWU-7/16548045) | **$0.96** | Same basic function as the selected part; automotive-qualified variant; still compact and surface mount. | Higher cost; qualification level is not currently necessary for this project. |
| Option 3 | [LMR51420XDDCR](https://www.digikey.com/en/products/detail/texas-instruments/LMR51420XDDCR/16705125) | **$1.81** | Good vendor support; surface-mount buck regulator; flexible adjustable output. | Requires external feedback design to set 3.3V; less direct than a fixed 3.3V part; higher cost than the selected option. |

### Final Choice
**Selected Option:** AP63203WU-7

### Rationale
The AP63203WU-7 is the strongest choice because it directly provides a fixed 3.3V output from the 12V source without needing extra feedback-divider work. It is also the least expensive of the compared options while still meeting the design intent for a compact surface-mount logic regulator. The automotive-qualified version does not provide enough project benefit to justify its added cost, and the adjustable TI part introduces extra design effort without solving a current problem.

---

## **Intermediate Power Subsystem — 12V to 6V Converter**

The 6V subsystem requires a regulator capable of stepping the 12V source down to 6V while maintaining substantial current capacity for downstream loads.

<img src="https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/1966/MFG_LMZ23610TZ_NOPB.jpg" alt="LMZ23610TZ/NOPB power module" width="260">

| Option | Product | Unit Cost | Pros | Cons |
|---|---|---:|---|---|
| **Option 1 — Selected** | [LMZ23610TZ/NOPB](https://www.digikey.com/en/products/detail/texas-instruments/LMZ23610TZ-NOPB/2673196) | **$31.11** | High current capability up to 10A; wide 6V to 36V input range; integrated power module reduces external design burden; strong fit for a robust 6V rail. | Highest cost among the compared options; physically larger than simpler regulators. |
| Option 2 | [LMZ22010TZ/NOPB](https://www.digikey.com/en/products/detail/texas-instruments/LMZ22010TZ-NOPB/2626436) | **$23.90** | Also supports up to 10A; lower price than the selected option; surface-mount module reduces implementation difficulty. | Lower maximum input range at 20V; gives less headroom if the upstream rail or future revisions change. |
| Option 3 | [LMZ22008TZ/NOPB](https://www.digikey.com/en/products/detail/texas-instruments/LMZ22008TZ-NOPB/2626435) | **$23.43** | Lower cost than the selected part; same general module family; still surface mount and adjustable. | Reduced output current at 8A; lower input-voltage range; gives less operating margin for future expansion. |

### Final Choice
**Selected Option:** LMZ23610TZ/NOPB

### Rationale
The LMZ23610TZ/NOPB remains the best choice because it preserves the greatest electrical margin on both input range and output current. That margin matters for a power rail that may feed multiple downstream loads or experience design changes later in the semester. The lower-cost alternatives are valid, but both reduce flexibility. Since power-system robustness is a high-value area of the design, the selected module is justified despite its higher price.

---

## **Motor Actuation Subsystem — Motor Driver**

The motor actuation subsystem requires a surface-mount brushed motor driver that can handle the planned supply voltage and current while remaining manufacturable.

<img src="https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/4751/MFG_TB67H450FNG,EL.jpg" alt="TB67H450FNG motor driver" width="220">

| Option | Product | Unit Cost | Pros | Cons |
|---|---|---:|---|---|
| **Option 1 — Selected** | [TB67H450FNG,EL](https://www.digikey.com/en/products/detail/toshiba-semiconductor-and-storage/TB67H450FNG-EL/10130904) | **$1.29** | Matches the current design direction; suitable voltage and current range for a brushed motor channel; compact surface-mount package; low cost. | Marked by DigiKey as not recommended for new designs; future availability risk should be monitored. |
| Option 2 | [TB67H451FNG,EL](https://www.digikey.com/en/products/detail/toshiba-semiconductor-and-storage/TB67H451FNG-EL/11568781) | **$1.29** | Very close same-family alternative; similar electrical class and package style; easy fallback option. | Requires confirming pin-level and behavior compatibility before substitution; not the currently integrated part. |
| Option 3 | [DRV8251ADDAR](https://www.digikey.com/en/products/detail/texas-instruments/DRV8251ADDAR/16182453) | **$2.25** | Strong alternative from TI; higher current rating; good documentation ecosystem. | Higher cost; different package family and integration path; not the part currently shown in the design. |

### Final Choice
**Selected Option:** TB67H450FNG,EL

### Rationale
The TB67H450FNG,EL remains the best current choice because it is already aligned with the existing design and meets the voltage and current requirements at a low cost. The main drawback is lifecycle risk because DigiKey flags it as not recommended for new designs. For that reason, the TB67H451FNG,EL should be treated as the immediate backup option if sourcing or lifecycle issues appear. At the current design stage, however, keeping the originally selected part is still the most practical choice.

---

# Minor Component Selection

| Component | Selected Part | Unit Cost | Product Link |
|---|---|---:|---|
| 12V Power Connector x10 | JST `SVH-21T-1.1` | **$0.10** | [JST SVH-21T-1.1 contact](https://www.digikey.com/en/products/detail/jst-sales-america-inc/SVH-21T-1-1/527366) |
| 12V Power Connector Header x10 | JST `VHR-2N` | **$0.10** | [JST VHR-2N housing](https://www.digikey.com/en/products/detail/jst-sales-america-inc/VHR-2N/608624) |
| Fuse | Littelfuse `0213005.M` | **$2.06** | [Littelfuse 0213005.M](https://www.digikey.com/en/products/detail/littelfuse-inc/0213005-M/552068) |
| Motor Power Header and 12V Power Header x3 | JST `B2PS-VH` | **$0.16** | [JST B2PS-VH](https://www.digikey.com/en/products/detail/jst-sales-america-inc/B2PS-VH/926555) |
| Green LED | Lite-On `LTST-C150GKT` | **$0.15** | [Lite-On LTST-C150GKT](https://www.digikey.com/en/products/detail/lite-on-inc/LTST-C150GKT/269216) |
| Red LED | Lite-On `LTST-C150EKT` | **$0.14** | [Lite-On LTST-C150EKT](https://www.digikey.com/en/products/detail/liteon/LTST-C150EKT/269215) |
| 8-Pin UART Header | Amphenol / FCI `75869-332LF` | **$0.68** | [Amphenol 75869-332LF](https://www.digikey.com/en/products/detail/amphenol-cs-fci/75869-332LF/1523267) |
| Fuse Holder | Schurter `3-143-050` | **$2.31** | [Schurter 3-143-050](https://www.digikey.com/en/products/detail/schurter-inc/3-143-050/25659195) |
| Capacitor 10uF | Murata `GRM31CR71E106MA12K` | **$0.30** | [Murata GRM31CR71E106MA12K](https://www.digikey.com/en/products/detail/murata-electronics/GRM31CR71E106MA12K/13904832) |
| Capacitor 100uF | Murata `GRM31CD80J107MEA8L` | **$0.42** | [Murata GRM31CD80J107MEA8L](https://www.digikey.com/en/products/detail/murata-electronics/GRM31CD80J107MEA8L/13904781) |
| Capacitor 22uF | Würth `885012208019` | **$0.71** | [Würth 885012208019](https://www.digikey.com/en/products/detail/w%C3%BCrth-elektronik/885012208019/5453421) |
| Capacitor 0.1uF | Yageo `CC1206JRX7R9BB104` | **$0.20** | [Yageo CC1206JRX7R9BB104](https://www.digikey.com/en/products/detail/yageo/CC1206JRX7R9BB104/2833600) |
| Motor Encoder Header | TE Connectivity `281695-4` | **$1.01** | [TE Connectivity 281695-4](https://www.digikey.com/en/products/detail/te-connectivity-amp-connectors/281695-4/1150102) |
| Button | E-Switch `TL9320AF400QG` | **$0.90** | [E-Switch TL9320AF400QG](https://www.digikey.com/en/products/detail/e-switch/TL9320AF400QG/11698099) |
| 100 Ohm Resistor | Yageo `RC1206FR-07100RL` | **$0.10** | [Yageo RC1206FR-07100RL](https://www.digikey.com/en/products/detail/yageo/RC1206FR-07100RL/728491) |
| 10K Ohm Resistor | Yageo `RC1206FR-0710KL` | **$0.10** | [Yageo RC1206FR-0710KL](https://www.digikey.com/en/products/detail/yageo/RC1206FR-0710KL/728483) |
| Resistor for 6V Module Setpoint | Yageo `RC1206FR-076K49L` | **$0.10** | [Yageo RC1206FR-076K49L](https://www.digikey.com/en/products/detail/yageo/RC1206FR-076K49L/729022) |
| 1K Resistor for 6V Module Setpoint | Yageo `RC1206JR-071KP` | **$0.10** | [Yageo RC1206JR-071KP](https://www.digikey.com/en/products/detail/yageo/RC1206JR-071KP/4935356) |

## Summary

The selected components form a cohesive embedded motor-control subsystem built around a wireless controller, regulated power rails, and dedicated motor-drive hardware:

- **ESP32-S3-WROOM-1-N4**: Serves as the main controller and provides the processing capability, wireless connectivity, and peripheral support needed for system control and communication.
- **TB67H450FNG,EL Motor Driver**: Provides the motor actuation stage for the design and was selected because it matches the current electrical and packaging requirements at low cost.
- **AP63203WU-7**: Generates the 3.3V logic rail from the 12V input and was selected because its fixed 3.3V output simplifies implementation.
- **LMZ23610TZ/NOPB**: Generates the 6V rail from the 12V source and provides strong current and input-range margin for downstream loads.
- **Supporting connectors, headers, LEDs, fuse components, capacitors, buttons, and resistors**: Complete the interface, protection, filtering, and setpoint functions required for the subsystem to operate reliably.

All selected parts align with the current surface-mount design approach except where connector-style components inherently require header or terminal hardware. The major components were chosen by comparing three realistic options and selecting the part that best balanced integration effort, cost, electrical margin, and fit with the existing design. The minor components were kept as single selections based on the stated project exceptions.
