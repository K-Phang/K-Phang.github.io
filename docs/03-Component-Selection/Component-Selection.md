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

## Major Component Selections

### 1. Microcontroller

#### Option 1: ESP32-S3-WROOM-1-N4 (Surface Mount)
![ESP32-S3](https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/300/767/688/MFG_Attachment-3-ESP32-S3-WROOM-1U_sml.jpg)
* **Price**: $2.69/each
* [Digikey Link](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1-N4/16162635)

| Pros | Cons |
|------|------|
| Dual-core 240MHz processor provides plenty of processing power for motor control | More expensive than simpler microcontrollers |
| Built-in WiFi/Bluetooth (not needed now but allows future expansion) | Higher power consumption than PIC alternatives |
| Multiple UART, SPI, I2C, PWM channels available | Larger footprint than minimal solutions |
| Strong community support and extensive documentation | 3.3V logic requires level shifting for some 5V peripherals |
| Native USB support for programming and debugging | |
| Surface mount QFN package is solderable in lab | |

#### Option 2: PIC18F47Q10 (Surface Mount)
![PIC18F47Q10](https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/010/961/607/150%7EC04-076%7EPT%7E44_sml%28200x200%29.jpg)
* **Price**: $2.12/each  
* [Digikey Link](https://www.digikey.com/en/products/detail/microchip-technology/PIC18F47Q10-I-PT/10187786)

| Pros | Cons |
|------|------|
| Lower cost than ESP32 | Less processing power (64MHz vs 240MHz) |
| Lower power consumption | Smaller community support compared to ESP32 |
| Multiple PWM channels for motor control | No built-in wireless capabilities |
| Good MPLabX tool support | More complex toolchain setup |
| Surface mount TQFP-44 package | Requires external programmer/debugger |
| 5V tolerant I/O pins | |

#### Option 3: ATmega328P-AU (Surface Mount)
![ATmega328P](https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/001/198/094/150%7E32A%7EA%2CAU%7E32-Top_sml%28200x200%29.jpg)
* **Price**: $2.45/each
* [Digikey Link](https://www.digikey.com/en/products/detail/microchip-technology/ATMEGA328P-AU/1832260)

| Pros | Cons |
|------|------|
| Extremely well-documented (Arduino compatible) | Limited to single UART (problematic for multi-device communication) |
| Simple architecture good for learning | Only 20MHz clock speed |
| Low power consumption | Limited memory (32KB flash, 2KB RAM) |
| TQFP-32 surface mount package | Fewer PWM channels |
| Extensive Arduino library support | Less powerful than other options |

**Choice: ESP32-S3-WROOM-1-N4**

**Rationale**: The ESP32-S3 provides the best balance of features for this motor control application. While more expensive, its dual UART channels allow clear separation of team communication and motor control commands. The multiple PWM channels support independent speed control of both motors, and the processor headroom ensures responsive real-time motor control. The surface-mount QFN-56 module is solderable in Peralta Labs and includes integrated flash memory, reducing external component count. Most importantly, extensive MicroPython and Arduino support means proven motor control libraries are readily available, reducing development risk.

---

### 2. Motor with Encoder

#### Option 1: DFRobot FIT0450 Micro Metal Gearmotor with Encoder
![FIT0450](https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/300/279/621/MFG_FIT0450_sml.jpg)
* **Price**: $9.90/each
* [Digikey Link](https://www.digikey.com/en/products/detail/dfrobot/FIT0450/7597205)

| Pros | Cons |
|------|------|
| Integrated optical encoder provides position feedback without additional components | Higher cost than motor-only solutions |
| 6V nominal operation matches our power rail | Requires two motors for differential drive |
| Compact form factor suitable for mobile robots | Encoder requires 4 additional GPIO pins per motor |
| 120:1 gear ratio provides good torque for load | Limited documentation on encoder resolution |
| Documented current draw aids power budget | May need custom mounting brackets |

#### Option 2: Pololu 2215 Micro Metal Gearmotor with Encoder
![Pololu 2215](https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/001/197/307/MFG_2183_2200_sml%28200x200%29.jpg)
* **Price**: $24.95/each
* [Digikey Link](https://www.digikey.com/en/products/detail/pololu/2215/10450001?s=N4IgTCBcDaIAoHsA2yCuACMYCMBWdAsgJYDGATgoQKYAuAhkugOJV1kC2CNCZ6A7kRoALdAFEAdiQQATKmRABdAL5A)

| Pros | Cons |
|------|------|
| Well-documented encoder specifications (12 CPR) | Significantly more expensive at $24.95 |
| High-quality Japanese brand motor | Higher cost may strain project budget |
| Extended motor shaft allows additional accessories | Price is 2.5x the FIT0450 option |
| Wide voltage range (3-6V) provides flexibility | |
| Proven reliability in robotics applications | |
| Now available on Digikey for consistent ordering | |

#### Option 3: Standard DC Motor + Separate Optical Encoder
![Generic Motor](https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/008/141/485/FIT0016_sml%28200x200%29.jpg) + ![Encoder](https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/002/467/381/AEDR-8710-102_sml.jpg)
* **Price**: 3.50 motor + 34.50 encoder = $38 total
* [Motor Link](https://www.digikey.com/en/products/detail/dfrobot/FIT0016/6579313) | [Encoder Link](https://www.digikey.com/en/products/detail/broadcom-limited/AEDR-8710-102/4966730)

| Pros | Cons |
|------|------|
| More flexible - can use motor without encoder initially | Extremely expensive at $38 total ($76 for two motors) |
| Can test motor functionality before encoder integration | Highest cost option by far - nearly 4x the FIT0450 |
| Can select motor specs independently from encoder | Requires custom mechanical coupling between motor and encoder |
| | Additional assembly time and potential alignment issues |
| | Two separate components increase PCB space requirements |
| | More complex mounting and wiring |

**Choice: DFRobot FIT0450 Micro Metal Gearmotor with Encoder**

**Rationale**: The integrated motor-encoder solution eliminates mechanical alignment issues and simplifies both electrical and mechanical design. While the encoder functionality is a stretch goal, having it integrated from the start means no design changes if we implement it later. The 6V operation aligns perfectly with our power budget, and the compact form factor is ideal for our mobile platform. At $9.90 per motor ($19.80 for two), it's by far the most cost-effective solution—the Pololu option costs $49.90 for two motors, and the separate motor+encoder approach costs a staggering $76 total. The FIT0450 offers the best value while maintaining quality. DFRobot availability on Digikey ensures fast shipping to meet project deadlines.

---

### 3. H-Bridge Motor Driver

#### Option 1: DRV8833CPWPR (Dual H-Bridge, Surface Mount)
![DRV8833](https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/001/202/812/296%7E4073225-3%7EPWP%7E16_sml%28200x200%29.jpg)
* **Price**: $1.47/each
* [Digikey Link](https://www.digikey.com/en/products/detail/texas-instruments/DRV8833CPWPR/4972147?s=N4IgTCBcDaICICUBqAOFBmdBhACgdRwQAIQBdAXyA)

| Pros | Cons |
|------|------|
| Dual H-bridge controls both motors from single IC | Requires external Schottky diodes for protection |
| 1.5A per channel exceeds our motor requirements | PWM frequency limited to 250kHz |
| Low Rdson (0.35Ω) minimizes power loss | Small HTSSOP-16 package requires careful soldering |
| Built-in current limiting and thermal shutdown | 3.3V logic compatible but needs careful PWM setup |
| Surface mount package meets project requirements | |
| Extensive TI documentation and reference designs | |

#### Option 2: A3909GLNTR-T (Dual Full-Bridge PWM Motor Driver, Surface Mount)
![L298N](https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/300/338/565/620%3B%2010SSOP-3.9%3B%20LN%3B%2010_sml.jpg)
* **Price**: $1.24/each
* [Digikey Link](https://www.digikey.com/en/products/detail/allegro-microsystems/A3909GLNTR-T/3979655)

| Pros | Cons |
|------|------|
| Dual full-bridge driver controls both motors | Requires external sense resistors for current sensing |
| 500mA per channel rated output | Lower current rating than DRV8833 (500mA vs 1.5A) |
| 3.3V logic compatible | Limited headroom for motor surges |
| Surface mount SOIC-10 package solderable in lab | May not handle simultaneous motor startup well |
| Built-in thermal shutdown protection | Less commonly used, fewer application examples |
| Lower cost than some alternatives | Requires more careful current management |

#### Option 3: TB6612FNG (Dual H-Bridge, Surface Mount)  
![TB6612FNG](https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/002/357/24-SSOP_sml.jpg)
* **Price**: $2.15/each
* [Digikey Link](https://www.digikey.com/en/products/detail/toshiba-semiconductor-and-storage/TB6612FNG-C-8-EL/1730070?s=N4IgTCBcDaICoCEBsSCMYBiA5A4iAugL5A)

| Pros | Cons |
|------|------|
| Dual H-bridge in single IC | Slightly more expensive than DRV8833 |
| 1.2A per channel sufficient for our motors | SSOP-24 package larger than DRV8833 |
| Low saturation voltage (0.9V) efficient design | Less commonly used than TI parts |
| Built-in protection features | Requires more external components |
| Separate standby pins for power saving | Documentation not as extensive as TI |

**Choice: DRV8833CPWPR Dual H-Bridge Motor Driver**

**Rationale**: The DRV8833 provides the optimal combination of performance, integration, and cost for this application. At $1.47, it's the most economical surface-mount solution while providing 1.5A per channel—sufficient headroom above our motor's requirements. The dual H-bridge architecture allows both motors to be controlled from a single IC, minimizing PCB space and component count. Texas Instruments provides extensive application notes and reference designs specifically for DC motor control, reducing development risk. The built-in thermal shutdown and current limiting protect against fault conditions. While the HTSSOP-16 package is small, it's within the capabilities of Peralta Labs soldering equipment and much easier than BGA packages. The 3.3V logic compatibility with the ESP32 eliminates the need for level shifters.

---

### 4. Power Management

#### 3.3V Regulator Options

**Option 1: LM1117-3.3 (Linear Regulator, Surface Mount)**
![LM1117](https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/001/202/815/296%7E4202506%7EDCY%7E4_sml%28200x200%29.jpg)
* **Price**: $0.58/each
* [Digikey Link](https://www.digikey.com/en/products/detail/texas-instruments/LM1117MPX-3-3-NOPB/366733)

| Pros | Cons |
|------|------|
| Very inexpensive solution | Linear regulator wastes power as heat |
| Simple circuit requires only two capacitors | Requires heatsinking for higher currents |
| Low dropout voltage (1.2V typical) | Inefficient when input voltage is much higher than 3.3V |
| 800mA output sufficient for ESP32 | SOT-223 package requires adequate copper for heat dissipation |
| Widely used with extensive application notes | |

**Option 2: TCR2EF33,LM(CT)**
![TPS63031](https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/003/226/442/264%7ESOT25%28SMV%29%7EEF%7E5_sml%28200x200%29.jpg)
* **Price**: $0.12/each
* [Digikey Link](https://www.digikey.com/en/products/detail/toshiba-semiconductor-and-storage/TCR2EF33-LM-CT/4503183)

| Pros | Cons |
|------|------|
| Extremely low cost at only $0.12 | Only 200mA output current (may be insufficient for ESP32 peak loads) |
| Very small SOT-25 package saves PCB space | Limited current capacity doesn't provide safety margin |
| Low dropout voltage (160mV at 200mA) | No short-circuit or thermal protection features |
| Simple implementation with minimal external components | Less commonly used than industry-standard regulators |
| Ultra-low quiescent current (35µA) good for battery life | May struggle with ESP32's WiFi current bursts |

**Option 3: AP2112K-3.3 (Linear Regulator, Surface Mount)**
![AP2112K](https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/1766/MFG_AP2112K-3.3TRG1.jpg)
* **Price**: $0.42/each
* [Digikey Link](https://www.digikey.com/en/products/detail/diodes-incorporated/AP2112K-3-3TRG1/4505257)

| Pros | Cons |
|------|------|
| Lowest cost option | Only 600mA output (marginal for ESP32 under load) |
| Ultra-low quiescent current (55µA) extends battery life | Linear topology still wastes power |
| Very small SOT-23-5 package | May require additional bulk capacitance for ESP32 WiFi bursts |
| Excellent line and load regulation | Lower current rating provides less safety margin |

**3.3V Choice: LM1117-3.3**

**Rationale**: The LM1117 provides the best balance for this application. Its 800mA output current provides adequate margin for the ESP32-S3 (typical 240mA, peak 500mA with WiFi). While a switching regulator would be more efficient, the assignment requires a linear voltage regulator, and the LM1117 is proven technology with extensive documentation. The simple two-capacitor circuit reduces PCB complexity and component count. The SOT-223 package is easier to solder than QFN alternatives. At $0.58, it's cost-effective while providing better current capability than the AP2112K.

#### 6V Regulator Options

**Option 1: LM20BIM7X-NOPB (Temperature Sensor)**
![LM1084](https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/300/732/756/296%7E4093553-3%7EDCK%7E5_sml.jpg)
* **Price**: $0.82/each
* [Digikey Link](https://www.digikey.com/en/products/detail/texas-instruments/LM20BIM7X-NOPB/3440103)

| Pros | Cons |
|------|------|
| Extremely low cost solution | This is a temperature sensor, NOT a voltage regulator |
| Tiny SC-70-5 package saves PCB space | Cannot provide 6V power output |
| Low power consumption (11µA) | Wrong component type for motor power delivery |
| Analog output proportional to temperature | No current drive capability |
| | Completely unsuitable for this application |

**Option 2: MC78M06CDTRKG**
![XL4015](https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/001/197/963/488%7E369C-01%7ED%2CDT%7E2_sml%28200x200%29.jpg)
* **Price**: $0.42/each
* [Digikey Link](https://www.digikey.com/en/products/detail/onsemi/MC78M06CDTRKG/921046)

| Pros | Cons |
|------|------|
| Fixed 6V output matches our requirement exactly | Only 500mA output current (marginal for motor surges) |
| Very low cost at $0.42 | DPAK package requires significant PCB copper for heat dissipation |
| No external resistors needed for voltage setting | Limited current may not handle dual motor startup |
| Built-in thermal shutdown and current limiting | Linear regulator wastes power as heat |
| Surface mount DPAK package | Higher dropout voltage (2V typical) requires higher input voltage |

**Option 3: L78M06CDT-TR**
![TPS54302](https://mm.digikey.com/Volume0/opasdata/d220001/derivates/1/003/209/488/497%7EDPAK%28TO252-3%29%7E%7E2_sml%28200x200%29.jpg)
* **Price**: $0.45/each
* [Digikey Link](https://www.digikey.com/en/products/detail/stmicroelectronics/L78M06CDT-TR/1165898)

| Pros | Cons |
|------|------|
| Fixed 6V output requires no external voltage-setting components | 500mA maximum output current limits motor surge capability |
| Low cost solution | DPAK (TO-252) package requires heatsinking |
| Widely available from STMicroelectronics | Linear regulator design inefficient for motor loads |
| Built-in overcurrent and thermal protection | 2V dropout voltage requires 8V+ input |
| Surface mount package meets requirements | May struggle with simultaneous motor startup current |

**6V Choice: MC78M06CDTRKG**

**Rationale**: Among the available options, the MC78M06CDTRKG provides the best practical solution for this motor control application. While Option 1 (LM20BIM7X) is actually a temperature sensor and completely unsuitable, both Options 2 and 3 are legitimate 6V linear regulators with 500mA output. The MC78M06CDTRKG at $0.42 offers slightly better value than the L78M06CDT-TR at $0.45, though both would work. The fixed 6V output eliminates the need for external voltage-divider resistors, simplifying the circuit. While the 500mA current rating is lower than ideal for motors that can draw up to 1A, the assignment requires linear regulators (not switching types), and this represents the best available compromise. In practice, we may need to add additional current-limiting circuitry or carefully manage motor startup to stay within the 500mA limit. The DPAK package is solderable in Peralta Labs and provides good thermal performance with adequate copper pour on the PCB.

---

## Summary

The selected components form a cohesive motor control subsystem:
- **ESP32-S3-WROOM-1**: Provides processing power, multiple PWM channels, and dual UART
- **DFRobot FIT0450 Motors**: Integrated encoders enable future position feedback
- **DRV8833 H-Bridge**: Dual-channel driver controls both motors efficiently  
- **LM1117-3.3**: Powers ESP32 with adequate current margin
- **MC78M06CDTRKG**: Provides 6V power for motors (may require current management)

All components meet the surface-mount requirement, are available on Digikey for fast shipping, and have been selected based on proven performance in similar applications.
