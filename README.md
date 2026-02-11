# dual-rotary-encoder-breakout
This is an open-source breakout PCB for the Bourns Inc. PEC11D-4120F-S0015 dual rotary encoder with switch.

This was made in KiCad 9.0.

All hardware and associated files are under the CERN Open Hardware Licence Version 2 - Permissive license.

All software and associated files are under the MIT license.

## Bill of Materials
Everything you'll need to make one yourself!

Alternative interactive BOM in `./ibom.html`

0603 resistors and 0603 capacitors may be swapped out for 

|   | References                         | Value              | Footprint                         | Quantity |
|---|------------------------------------|--------------------|-----------------------------------|----------|
| 1 | R1, R2, R3, R4, R5, R6, R7, R8, R9 | 10K                | 0603 (1608 Metric)                | 9        |
| 2 | C1, C2, C3, C4                     | 0.01u              | 0603 (1608 Metric)                | 4        |
| 3 | S1                                 | PEC11D-4120F-S0015 | PEC11D-4120F-S0015 Rotary Encoder | 1        |
| 4 | J3                                 | PINHD_1x7_Male     | 2.54mm pitch header               | 1        |

## Software Example

I used [Mike Teachman's micropython-rotary library](https://github.com/miketeachman/micropython-rotary) for some micropython code to run on a Raspberry Pi Pico.

You can find example code in `./software`. Be sure to use the latest version of Mike's library.

## 3D Render

![preview-3d](https://github.com/user-attachments/assets/9e8ff5df-3afc-4efa-b591-1b52379d8451)
