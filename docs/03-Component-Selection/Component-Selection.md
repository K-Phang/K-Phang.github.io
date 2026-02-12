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
![ESP32-S3](https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/4776/MFG_ESP32-S3-WROOM-1-N4.jpg)
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
![PIC18F47Q10](https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/1477/MFG_PIC18F47Q10-I~PT.jpg)
* **Price**: $2.12/each  
* [Digikey Link](https://www.digikey.com/en/products/detail/microchip-technology/PIC18F47Q10-I-PT/9947430)

| Pros | Cons |
|------|------|
| Lower cost than ESP32 | Less processing power (64MHz vs 240MHz) |
| Lower power consumption | Smaller community support compared to ESP32 |
| Multiple PWM channels for motor control | No built-in wireless capabilities |
| Good MPLabX tool support | More complex toolchain setup |
| Surface mount TQFP-44 package | Requires external programmer/debugger |
| 5V tolerant I/O pins | |

#### Option 3: ATmega328P-AU (Surface Mount)
![ATmega328P](https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/262/MFG_ATMEGA328P-AU.jpg)
* **Price**: $2.45/each
* [Digikey Link](https://www.digikey.com/en/products/detail/microchip-technology/ATMEGA328P-AU/2357085)

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
![FIT0450](https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/4831/MFG_FIT0450.jpg)
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
![Pololu 2215](https://a.pololu-files.com/picture/0J10360.600.jpg)
* **Price**: $14.95/each
* [Pololu Link](https://www.pololu.com/product/2215)

| Pros | Cons |
|------|------|
| Well-documented encoder specifications (12 CPR) | More expensive option |
| High-quality Japanese brand motor | Not available on Digikey (shipping delays) |
| Extended motor shaft allows additional accessories | Requires separate purchase from different vendor |
| Wide voltage range (3-6V) provides flexibility | |
| Proven reliability in robotics applications | |

#### Option 3: Standard DC Motor + Separate Optical Encoder
![Generic Motor](https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/1233/1528-1431-ND~2.jpg) + ![Encoder](https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/5047/296-41060-ND~2.jpg)
* **Price**: $3.50 motor + $8.00 encoder = $11.50 total
* [Motor Link](https://www.digikey.com/en/products/detail/dfrobot/FIT0186/6588464) | [Encoder Link](https://www.digikey.com/en/products/detail/dfrobot/SEN0230/9559020)

| Pros | Cons |
|------|------|
| More flexible - can use motor without encoder initially | Requires custom mechanical coupling between motor and encoder |
| Lower cost if encoder is skipped for initial testing | Higher total cost if both components needed |
| Can select motor specs independently from encoder | Additional assembly time and potential alignment issues |
| | Two separate components increase PCB space requirements |
| | More complex mounting and wiring |

**Choice: DFRobot FIT0450 Micro Metal Gearmotor with Encoder**

**Rationale**: The integrated motor-encoder solution eliminates mechanical alignment issues and simplifies both electrical and mechanical design. While the encoder functionality is a stretch goal, having it integrated from the start means no design changes if we implement it later. The 6V operation aligns perfectly with our power budget, and the compact form factor is ideal for our mobile platform. The slightly higher cost ($9.90 vs separate components at $11.50) is justified by reduced assembly complexity and higher reliability. DFRobot availability on Digikey ensures fast shipping to meet project deadlines.

---

### 3. H-Bridge Motor Driver

#### Option 1: DRV8833CPWPR (Dual H-Bridge, Surface Mount)
![DRV8833](https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/1030/MFG_DRV8833CPWP.jpg)
* **Price**: $1.47/each
* [Digikey Link](https://www.digikey.com/en/products/detail/texas-instruments/DRV8833CPWPR/2299844)

| Pros | Cons |
|------|------|
| Dual H-bridge controls both motors from single IC | Requires external Schottky diodes for protection |
| 1.5A per channel exceeds our motor requirements | PWM frequency limited to 250kHz |
| Low Rdson (0.35Ω) minimizes power loss | Small HTSSOP-16 package requires careful soldering |
| Built-in current limiting and thermal shutdown | 3.3V logic compatible but needs careful PWM setup |
| Surface mount package meets project requirements | |
| Extensive TI documentation and reference designs | |

#### Option 2: L298N Module (Through-Hole Module)
![L298N](https://m.media-amazon.com/images/I/61kiXU3FVEL._AC_SL1001_.jpg)
* **Price**: $3.50/each
* [Amazon Link](https://www.amazon.com/HiLetgo-Controller-Stepper-H-Bridge-Mega2560/dp/B07BK1QL5T)

| Pros | Cons |
|------|------|
| Simple to use, well-documented breakout board | Through-hole module violates surface mount requirement |
| Dual H-bridge on pre-assembled board | Larger footprint than IC solution |
| Built-in voltage regulator | Higher voltage drop (2V) wastes power |
| Screw terminals for easy motor connection | Much more expensive per channel |
| | Poor efficiency due to bipolar transistor design |
| | Not suitable for final PCB design |

#### Option 3: TB6612FNG (Dual H-Bridge, Surface Mount)  
![TB6612FNG](https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/6047/2073-TB6612FNG%2CCT.jpg)
* **Price**: $2.15/each
* [Digikey Link](https://www.digikey.com/en/products/detail/toshiba-semiconductor-and-storage/TB6612FNG-C-8-EL/5409464)

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
![LM1117](https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/1040/MFG_LM1117IMPX-3.3.jpg)
* **Price**: $0.58/each
* [Digikey Link](https://www.digikey.com/en/products/detail/texas-instruments/LM1117IMPX-3-3-NOPB/363584)

| Pros | Cons |
|------|------|
| Very inexpensive solution | Linear regulator wastes power as heat |
| Simple circuit requires only two capacitors | Requires heatsinking for higher currents |
| Low dropout voltage (1.2V typical) | Inefficient when input voltage is much higher than 3.3V |
| 800mA output sufficient for ESP32 | SOT-223 package requires adequate copper for heat dissipation |
| Widely used with extensive application notes | |

**Option 2: TPS63031 (Buck-Boost Switching Regulator, Surface Mount)**
![TPS63031](https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/1030/MFG_TPS63031DSKR.jpg)
* **Price**: $2.95/each
* [Digikey Link](https://www.digikey.com/en/products/detail/texas-instruments/TPS63031DSKR/2551906)

| Pros | Cons |
|------|------|
| High efficiency (>90%) reduces battery drain | More expensive than linear regulators |
| Buck-boost topology works with wide input range (2.5-12V) | Requires external inductor and multiple capacitors |
| Up to 1200mA output current | More complex PCB layout to minimize EMI |
| Small 3x3mm QFN package | QFN package more difficult to solder |
| | Switching noise may require additional filtering |

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

**Option 1: LM1084-ADJ (Adjustable Linear Regulator, Surface Mount)**
![LM1084](https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/1040/MFG_LM1084IS-ADJ.jpg)
* **Price**: $1.85/each
* [Digikey Link](https://www.digikey.com/en/products/detail/texas-instruments/LM1084IS-ADJ-NOPB/363611)

| Pros | Cons |
|------|------|
| 5A output current provides plenty of headroom for motor surges | More expensive than fixed-voltage regulators |
| Adjustable output allows fine-tuning voltage | Requires two external resistors to set voltage |
| Low dropout (1.3V) works with 9V battery | TO-263 package requires significant heatsinking |
| Built-in thermal shutdown and current limiting | Linear design wastes power during motor operation |
| | Larger PCB footprint than alternatives |

**Option 2: XL4015 (Buck Switching Regulator Module)**
![XL4015](https://m.media-amazon.com/images/I/61V07cVbCFL._AC_SL1000_.jpg)
* **Price**: $2.50/each
* [Amazon Link](https://www.amazon.com/Valefod-Converter-Adjustable-Electronic-Regulator/dp/B0BXPRLRJM)

| Pros | Cons |
|------|------|
| High efficiency (>90%) reduces heat generation | Module-based solution violates surface mount requirement |
| 5A output handles motor surge currents easily | Large footprint not suitable for compact PCB |
| Adjustable output voltage | Poor documentation for module version |
| Heat dissipation through module PCB | Cannot integrate into custom PCB design |
| | Not appropriate for final submission |

**Option 3: TPS54302 (Buck Switching Regulator IC, Surface Mount)**
![TPS54302](https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/1030/MFG_TPS54302DDCR.jpg)
* **Price**: $1.42/each
* [Digikey Link](https://www.digikey.com/en/products/detail/texas-instruments/TPS54302DDCR/2094660)

| Pros | Cons |
|------|------|
| Efficient buck converter (>90%) minimizes heat | Requires external inductor, diode, and multiple capacitors |
| 3A continuous output sufficient for our motors | More complex PCB layout than linear regulator |
| Wide input voltage range (4.5-28V) | Switching regulator generates EMI (may affect encoders) |
| Small SOT-23-6 package saves space | Requires careful component selection and layout |
| Adjustable output via resistor divider | Violates assignment requirement for linear regulator |

**6V Choice: LM1084-ADJ**

**Rationale**: Despite its higher cost and power inefficiency, the LM1084 adjustable linear regulator best meets the assignment requirements while providing robust motor power delivery. The 5A current capability handles motor startup surges and provides significant safety margin above the motors' 1A rating. The adjustable output allows precise setting of 6V using standard resistor values. While the linear design wastes power, it eliminates switching noise that could interfere with encoder signals—critical for the stretch goal. The assignment specifically requires linear voltage regulators, ruling out switching alternatives. The TO-263 package, while requiring heatsinking, is solderable in Peralta Labs and provides excellent thermal performance.

---

## Summary

The selected components form a cohesive motor control subsystem:
- **ESP32-S3-WROOM-1**: Provides processing power, multiple PWM channels, and dual UART
- **DFRobot FIT0450 Motors**: Integrated encoders enable future position feedback
- **DRV8833 H-Bridge**: Dual-channel driver controls both motors efficiently  
- **LM1117-3.3**: Powers ESP32 with adequate current margin
- **LM1084-ADJ**: Provides clean 6V power for motors with surge capability

All components meet the surface-mount requirement, are available on Digikey for fast shipping, and have been selected based on proven performance in similar applications.
