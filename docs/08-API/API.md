---
title: API
---

# API

## Overview

This page documents the communication API for my **B1 Propulsion subsystem** for Team 201's project, **The Duck**. My subsystem was assigned to:

| Field | Value |
|---|---|
| Team Member | K Phang |
| Subsystem | B1 Propulsion |
| Team Message ID | D |
| Function | Motor control for propulsion |

The purpose of the B1 propulsion API was to allow the team communication system to send motor-control commands to the propulsion module. The propulsion module would interpret those commands and use the ESP32 to control the H-bridge motor driver.

The final hardware did not become a fully standalone integrated communication module because of the failed 3.3 V rail and missing ESP32 programming-header support. However, the API below documents the intended command structure and the role of the B1 propulsion module within the team system.

## Team Module ID Map

| Team Member | Subsystem | Message ID |
|---|---|---|
| Isaac | A1 | A |
| MK | A2 | B |
| Neel | A3 | C |
| K Phang | B1 | D |
| Jacob | B2 | E |
| Levi | C1 | F |
| Austin | C2 | G |
| Hafsa | C3 | H |
| Kelton | D1 | I |
| Seth | D2 | J |

## B1 Propulsion Message Role

The B1 propulsion module was responsible for receiving commands addressed to message ID **D**. These commands controlled propulsion motor behavior.

The main command types for B1 Propulsion were:

1. Stop motor output.
2. Drive forward.
3. Drive reverse.
4. Set motor speed using PWM.
5. Report basic status if requested.

The final implementation should be treated as **open-loop motor control** because the final motors did not include built-in encoders and encoder feedback was not completed.

## Intended Message Format

`<START><TARGET_ID><COMMAND><VALUE><END>`

| Field | Description | Example |
|---|---|---|
| START | Start character indicating the beginning of a message | `<` |
| TARGET_ID | Target subsystem ID | `D` |
| COMMAND | Command character or command code | `F`, `R`, `S`, `P`, `Q` |
| VALUE | Optional command value, usually speed percentage or PWM level | `000` to `100` |
| END | End character indicating the end of a message | `>` |

Example message:

`<D:F:075>`

This means:

| Message Part | Meaning |
|---|---|
| `D` | Message is for B1 Propulsion |
| `F` | Forward command |
| `075` | Run at 75 percent speed |

## Command Table

| Command | Example Message | Intended Behavior |
|---|---|---|
| Stop | `<D:S:000>` | Disable motor output and stop propulsion |
| Forward | `<D:F:050>` | Drive the motor output forward at 50 percent speed |
| Reverse | `<D:R:050>` | Drive the motor output reverse at 50 percent speed |
| PWM / Speed Set | `<D:P:075>` | Set motor PWM duty cycle to 75 percent |
| Query Status | `<D:Q:000>` | Request basic propulsion-module status |

## Response Format

`<START><SOURCE_ID><STATUS><VALUE><END>`

Example response:

`<D:OK:075>`

This response means that B1 Propulsion accepted the command and is operating at the requested output value.

## Response Table

| Response | Example Message | Meaning |
|---|---|---|
| OK | `<D:OK:075>` | Command accepted |
| ERR | `<D:ERR:000>` | Command rejected or invalid |
| STOP | `<D:STOP:000>` | Motor output stopped |
| BUSY | `<D:BUSY:000>` | Module is active or unavailable |
| FAIL | `<D:FAIL:000>` | Hardware or command failure detected |

## Motor-Control Behavior

The ESP32 was intended to translate valid API messages into H-bridge control signals.

| API Command | H-Bridge Direction Behavior | PWM Behavior |
|---|---|---|
| Stop | Both motor-control outputs disabled or set to safe stop state | 0 percent duty cycle |
| Forward | Direction pins set for forward polarity | PWM set by command value |
| Reverse | Direction pins set for reverse polarity | PWM set by command value |
| PWM / Speed Set | Direction remains from previous valid direction command | PWM updated to command value |

For safety, any invalid command should default to a stopped or disabled motor-output state. Motor-control messages should not cause movement unless the target ID is **D** and the command is valid.

## Error Handling

The propulsion API should reject invalid messages under these conditions:

1. The target ID is not `D`.
2. The command field is missing or unsupported.
3. The value field is outside the valid range.
4. The message does not include the required start/end structure.
5. The motor driver is disabled or unavailable.
6. The module has not completed startup.

Invalid messages should not drive the motors. The safest default state is motor output disabled.

## Final Implementation Notes

The final B1 propulsion hardware did not fully validate the complete API on the standalone PCB. The main reasons were:

1. The onboard 3.3 V rail did not work.
2. The ESP32-S3-WROOM-1-N4 was soldered onto the PCB, but the board was missing proper programming-header support.
3. The final motors were basic TT DC gearbox motors without built-in encoders.
4. Encoder feedback was not implemented in the final system.

Because of those limitations, this API should be understood as the final intended interface for the B1 propulsion module rather than a fully validated standalone communication implementation.

## Future API Improvements

A future version of the B1 propulsion API should include:

1. A startup self-test message.
2. A rail-status message showing whether 3.3 V and 6 V are present.
3. A motor-driver fault message if the H-bridge enters a fault state.
4. A clear stop or emergency-stop command.
5. Optional encoder fields if future motors include feedback.
6. Better integration between the team message structure and firmware-level parsing.

## Example Message Sequence

| Step | Message | Description |
|---:|---|---|
| 1 | `<D:Q:000>` | Control system asks B1 Propulsion for status |
| 2 | `<D:OK:000>` | B1 Propulsion responds that it is ready |
| 3 | `<D:F:050>` | Control system commands forward motion at 50 percent speed |
| 4 | `<D:OK:050>` | B1 Propulsion confirms the command |
| 5 | `<D:S:000>` | Control system commands propulsion stop |
| 6 | `<D:STOP:000>` | B1 Propulsion confirms motor output stopped |
