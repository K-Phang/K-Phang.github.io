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
| Team Message ID / Receiver ID | D |
| Function | Propulsion throttle and motor direction control |

The final team communication design used single-character IDs and message types. My propulsion module was receiver **D**. The formal team-level command for propulsion was **Message Type B: Set Throttle Percentage**.

During final testing, the propulsion module also used a simplified local test command structure where **F** meant forward and **B** meant back. That local shorthand was useful for direct testing, but it should not replace the team-wide API because the team message table already uses **F** for distance data.

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

## Formal Team Message Format

The formal team UART message structure used sender ID, receiver ID, message type, and optional data. For my subsystem, the important formal command was the throttle command sent to receiver **D**.

| Byte | Variable Name | Type | Meaning |
|---:|---|---|---|
| 1 | Sender_ID | char | Module sending the message |
| 2 | Receiver_ID | char | Module receiving the message |
| 3 | Message_Type | char | Command type |
| 4 | Value | uint8_t | Optional command value, such as throttle percentage |

## Formal Propulsion Command

### Message Type B - Set Throttle Percentage

| Field | Value |
|---|---|
| Sender | A |
| Receiver | D |
| Message Type | B |
| Data | Throttle percentage |

| Byte | Variable Name | Type | Example |
|---:|---|---|---|
| 1 | Sender_ID | char | A |
| 2 | Receiver_ID | char | D |
| 3 | Message_Type | char | B |
| 4 | Throttle | uint8_t | 125 |

Example formal message:

| Sender_ID | Receiver_ID | Message_Type | Throttle |
|---|---|---|---:|
| A | D | B | 125 |

This means the controller subsystem is sending a throttle command to B1 Propulsion.

## Throttle Interpretation

The team documentation described the throttle command as a percentage command that could be used for forward or reverse thrust. In final testing, the actual motor-control behavior was simplified into forward and back commands.

The clean interpretation for this report is:

| Throttle / Command Case | Intended Motor Behavior |
|---|---|
| Positive throttle command | Forward motor direction |
| Zero throttle command | Stop motor output |
| Negative throttle command, if supported by parser | Backward/reverse motor direction |
| Local test command `F` | Forward motor test |
| Local test command `B` | Backward motor test |

Because the formal team message used an unsigned byte in some tables, the safest final documentation is that **Message Type B controls throttle**, while **F/B were local test commands used during final motor testing**.

## Final Local Test Commands

During final bring-up and motor testing, I used simplified command letters to test motion direction directly.

| Local Test Command | Meaning | Notes |
|---|---|---|
| F | Forward | Used in final local test run |
| B | Back / Reverse | Used in final local test run |
| Stop / 0 | Stop motor output | Safe default behavior |

These local commands were useful for quickly proving motor direction behavior, but they should not be treated as the team-wide message types. The team-wide meaning of **F** was already assigned to distance data, so using **F** as a formal propulsion message would create a protocol conflict.

## Team Message Type Reference

| Message Type | Team Meaning | Related Subsystem |
|---|---|---|
| A | Set Steering Angle | B2 Steering |
| B | Set Throttle Percentage | B1 Propulsion |
| C | Set Camera Angle | C2 Camera Arm |
| D | Take Photo | C1 Camera |
| E | Send Speed Data | C3 / sensor path |
| F | Send Distance Data | D2 Distance Sensor |
| G | Send Temperature Data | D1 Temperature Sensor |
| H | Stabilize Arm | C3 to C2 |
| J / L | Rollcall, depending on document version | Team debugging |

The important point for B1 Propulsion is that **B is the formal throttle command** and **D is the receiver ID for my board**.

## Motor-Control Behavior

The ESP32 was intended to translate valid propulsion commands into H-bridge control signals.

| Command Source | Command | H-Bridge Behavior |
|---|---|---|
| Formal team API | A D B with throttle value | Set motor output based on throttle value |
| Local test API | F | Set direction forward and drive motor |
| Local test API | B | Set direction backward and drive motor |
| Local test API | Stop / 0 | Disable motor output |

For safety, invalid messages should not drive the motors. The safest default state is motor output disabled.

## Error Handling

The propulsion API should reject or ignore invalid messages under these conditions:

1. The receiver ID is not `D`.
2. The message type is unsupported.
3. The throttle value is outside the expected range.
4. The message is malformed or incomplete.
5. The motor driver is unavailable.
6. The module has not completed startup.
7. The command conflicts with the team-wide message table.

Invalid messages should not cause motor movement.

## Final Implementation Notes

The final B1 propulsion hardware did not fully validate the complete team API on the standalone PCB. The main reasons were:

1. The onboard 3.3 V rail did not work.
2. The ESP32-S3-WROOM-1-N4 was soldered onto the PCB, but the board was missing proper programming-header support.
3. The final motors were basic TT DC gearbox motors without built-in encoders.
4. Encoder feedback was not implemented in the final system.

The final run used simple local direction commands, with **F for forward** and **B for back**, to test motor behavior. The formal report should still keep the team-wide API aligned with the team protocol: **receiver D, message type B, throttle command**.

## Future API Improvements

A future version of the B1 propulsion API should define throttle direction more cleanly. The team should choose one of these options:

| Option | Description |
|---|---|
| Signed throttle | One value supports forward, stop, and reverse |
| Direction + speed | One byte for direction and one byte for speed |
| Separate message types | Separate formal commands for forward, reverse, and stop |

The cleanest future design would be **direction + speed**, because it avoids confusion between team-wide message letters and local motor-test letters.
