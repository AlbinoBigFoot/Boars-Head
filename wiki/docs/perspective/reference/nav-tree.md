---
title: "Nav Tree Items"
sidebar_label: "Nav Tree Items"
description: "The full navigation tree (00_Docked/Navigation view.custom.items) with pages, views, faceplates and flags."
generated: true
sidebar_position: 4
---

:::note

:::


Source: `custom.items` on the view [00\_Pages/00\_Docked/Navigation](./views/00-pages/00-docked/navigation.md) (mirrored in the tag `[default]_Config/Navigation`). Flags: hidden (kept, not shown), demo (shown in enterprise mode), flattenLocal (lifted into its parent in local mode), permission (Roles & Permissions row), adminOnly. Faceplate items open a device popup instead of a page.

310 nav items in total.

<details>
<summary>Full nav tree (310 items)</summary>

```text
Boars Head  (material/public)  -> page /; demoPage=/enterprise; localPage=/plants/groveport/utility-overview; localIcon=material/home
  Groveport  (material/location_on)  -> demoPage=/plants/groveport; localPage=/plants/groveport/utility-overview; parkedPage=/plants/groveport
    Utility Overview  (material/ac_unit)  -> page /plants/groveport/utility-overview
    Production Overview  (equipment/conveyor)  -> page /plants/groveport/production-overview; hidden; demo
      Prep  (material/device_hub)  -> page /plants/groveport/production/level-2/prep; hidden; demo
        Vat Dumper  (equipment/devices)  -> page /plants/groveport/production/vat-dumper; hidden; demo
        Hopper  (equipment/devices)  -> page /plants/groveport/production/hopper; hidden; demo
      Forming  (material/device_hub)  -> page /plants/groveport/production/level-2/forming; hidden; demo
        Handtman  (equipment/devices)  -> page /plants/groveport/production/handtman; hidden; demo
        Loaders  (equipment/devices)  -> page /plants/groveport/production/loaders; hidden; demo
      Packaging  (material/device_hub)  -> page /plants/groveport/production/level-2/packaging; hidden; demo
        Roll Stock  (equipment/devices)  -> page /plants/groveport/production/roll-stock; hidden; demo
        Shrink Tunnel  (equipment/devices)  -> page /plants/groveport/production/shrink-tunnel; hidden; demo
        Lazy Susan  (equipment/devices)  -> page /plants/groveport/production/lazy-susan; hidden; demo
    Freezer  (material/domain)  -> page /freezer
      EPMS  (material/offline_bolt)  -> page /plants/groveport/freezer/epms; hidden; demo
      Utility  (material/miscellaneous_services)  -> flattenLocal
        CG-A1  (material/ac_unit)  -> page /cg-a1
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/Freezer/Utility/CG-A1
            Valves  (equipment/valve)
              Bleed SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Freezer/Utility/CG-A1/Valves/Bleed SV
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Freezer/Utility/CG-A1/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Freezer/Utility/CG-A1/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Freezer/Utility/CG-A1/Valves/Liquid SV
        CG-A2  (material/ac_unit)  -> page /cg-a2
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/Freezer/Utility/CG-A2
            Valves  (equipment/valve)
              Bleed SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Freezer/Utility/CG-A2/Valves/Bleed SV
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Freezer/Utility/CG-A2/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Freezer/Utility/CG-A2/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Freezer/Utility/CG-A2/Valves/Liquid SV
      Production  (equipment/conveyor)  -> page /plants/groveport/freezer/production; hidden; demo
    SuperChill  (material/domain)  -> page /superchill
      EPMS  (material/offline_bolt)  -> page /plants/groveport/superchill/epms; hidden; demo
      Utility  (material/miscellaneous_services)  -> flattenLocal
        CG-B1  (material/ac_unit)  -> page /cg-b1
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/SuperChill/Utility/CG-B1
            Valves  (equipment/valve)
              Bleed SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/SuperChill/Utility/CG-B1/Valves/Bleed SV
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/SuperChill/Utility/CG-B1/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/SuperChill/Utility/CG-B1/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/SuperChill/Utility/CG-B1/Valves/Liquid SV
        CG-B2  (material/ac_unit)  -> page /cg-b2
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/SuperChill/Utility/CG-B2
            Valves  (equipment/valve)
              Bleed SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/SuperChill/Utility/CG-B2/Valves/Bleed SV
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/SuperChill/Utility/CG-B2/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/SuperChill/Utility/CG-B2/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/SuperChill/Utility/CG-B2/Valves/Liquid SV
      Production  (equipment/conveyor)  -> page /plants/groveport/superchill/production; hidden; demo
    Club  (material/domain)  -> page /club
      EPMS  (material/offline_bolt)  -> page /plants/groveport/club/epms; hidden; demo
      Utility  (material/miscellaneous_services)  -> flattenLocal
        CG-C1  (material/ac_unit)  -> page /cg-c1
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/Club/Utility/CG-C1
            Valves  (equipment/valve)
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Club/Utility/CG-C1/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Club/Utility/CG-C1/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Club/Utility/CG-C1/Valves/Liquid SV
      Production  (equipment/conveyor)  -> page /plants/groveport/club/production; hidden; demo
    Palletizing  (material/domain)  -> page /palletizing
      EPMS  (material/offline_bolt)  -> page /plants/groveport/palletizing/epms; hidden; demo
      Utility  (material/miscellaneous_services)  -> flattenLocal
        CG-D1  (material/ac_unit)  -> page /cg-d1
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/Palletizing/Utility/CG-D1
            Valves  (equipment/valve)
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Palletizing/Utility/CG-D1/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Palletizing/Utility/CG-D1/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Palletizing/Utility/CG-D1/Valves/Liquid SV
      Production  (equipment/conveyor)  -> page /plants/groveport/palletizing/production; hidden; demo
    East PH  (material/domain)  -> page /east-ph
      EPMS  (material/offline_bolt)  -> page /plants/groveport/east-ph/epms; hidden; demo
      Utility  (material/miscellaneous_services)  -> flattenLocal
        CG-E1  (material/ac_unit)  -> page /cg-e1
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/East PH/Utility/CG-E1
            Valves  (equipment/valve)
              Bleed SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/East PH/Utility/CG-E1/Valves/Bleed SV
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/East PH/Utility/CG-E1/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/East PH/Utility/CG-E1/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/East PH/Utility/CG-E1/Valves/Liquid SV
        CG-E2  (material/ac_unit)  -> page /cg-e2
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/East PH/Utility/CG-E2
            Valves  (equipment/valve)
              Bleed SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/East PH/Utility/CG-E2/Valves/Bleed SV
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/East PH/Utility/CG-E2/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/East PH/Utility/CG-E2/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/East PH/Utility/CG-E2/Valves/Liquid SV
        CG-E3  (material/ac_unit)  -> page /cg-e3
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/East PH/Utility/CG-E3
            Valves  (equipment/valve)
              Bleed SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/East PH/Utility/CG-E3/Valves/Bleed SV
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/East PH/Utility/CG-E3/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/East PH/Utility/CG-E3/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/East PH/Utility/CG-E3/Valves/Liquid SV
        CG-E4  (material/ac_unit)  -> page /cg-e4
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/East PH/Utility/CG-E4
            Valves  (equipment/valve)
              Bleed SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/East PH/Utility/CG-E4/Valves/Bleed SV
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/East PH/Utility/CG-E4/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/East PH/Utility/CG-E4/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/East PH/Utility/CG-E4/Valves/Liquid SV
      Production  (equipment/conveyor)  -> page /plants/groveport/east-ph/production; hidden; demo
    West PH  (material/domain)  -> page /west-ph
      EPMS  (material/offline_bolt)  -> page /plants/groveport/west-ph/epms; hidden; demo
      Utility  (material/miscellaneous_services)  -> flattenLocal
        CG-F1  (material/ac_unit)  -> page /cg-f1
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/West PH/Utility/CG-F1
            Valves  (equipment/valve)
              Bleed SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/West PH/Utility/CG-F1/Valves/Bleed SV
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/West PH/Utility/CG-F1/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/West PH/Utility/CG-F1/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/West PH/Utility/CG-F1/Valves/Liquid SV
        CG-F2  (material/ac_unit)  -> page /cg-f2
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/West PH/Utility/CG-F2
            Valves  (equipment/valve)
              Bleed SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/West PH/Utility/CG-F2/Valves/Bleed SV
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/West PH/Utility/CG-F2/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/West PH/Utility/CG-F2/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/West PH/Utility/CG-F2/Valves/Liquid SV
        CG-F3  (material/ac_unit)  -> page /cg-f3
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/West PH/Utility/CG-F3
            Valves  (equipment/valve)
              Bleed SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/West PH/Utility/CG-F3/Valves/Bleed SV
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/West PH/Utility/CG-F3/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/West PH/Utility/CG-F3/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/West PH/Utility/CG-F3/Valves/Liquid SV
        CG-F4  (material/ac_unit)  -> page /cg-f4
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/West PH/Utility/CG-F4
            Valves  (equipment/valve)
              Bleed SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/West PH/Utility/CG-F4/Valves/Bleed SV
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/West PH/Utility/CG-F4/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/West PH/Utility/CG-F4/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/West PH/Utility/CG-F4/Valves/Liquid SV
      Production  (equipment/conveyor)  -> page /plants/groveport/west-ph/production; hidden; demo
    Dock  (material/domain)  -> page /dock
      EPMS  (material/offline_bolt)  -> page /plants/groveport/dock/epms; hidden; demo
      Utility  (material/miscellaneous_services)  -> flattenLocal
        CG-G1  (material/ac_unit)  -> page /cg-g1
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/Dock/Utility/CG-G1
            Valves  (equipment/valve)
              Bleed SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Dock/Utility/CG-G1/Valves/Bleed SV
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Dock/Utility/CG-G1/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Dock/Utility/CG-G1/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Dock/Utility/CG-G1/Valves/Liquid SV
        CG-G2  (material/ac_unit)  -> page /cg-g2
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/Dock/Utility/CG-G2
            Valves  (equipment/valve)
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Dock/Utility/CG-G2/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Dock/Utility/CG-G2/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Dock/Utility/CG-G2/Valves/Liquid SV
        CG-G3  (material/ac_unit)  -> page /cg-g3
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/Dock/Utility/CG-G3
            Valves  (equipment/valve)
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Dock/Utility/CG-G3/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Dock/Utility/CG-G3/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Dock/Utility/CG-G3/Valves/Liquid SV
        CG-G4  (material/ac_unit)  -> page /cg-g4
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/Dock/Utility/CG-G4
            Valves  (equipment/valve)
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Dock/Utility/CG-G4/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Dock/Utility/CG-G4/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Dock/Utility/CG-G4/Valves/Liquid SV
        CG-G5  (material/ac_unit)  -> page /cg-g5
          Devices  (equipment/devices)
            Evaporator  (material/ac_unit)  -> faceplate Evaporator on [default]Boars_Head/GrovePort/Dock/Utility/CG-G5
            Valves  (equipment/valve)
              Suction SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Dock/Utility/CG-G5/Valves/Suction SV
              Hot Gas SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Dock/Utility/CG-G5/Valves/Hot Gas SV
              Liquid SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Dock/Utility/CG-G5/Valves/Liquid SV
      Production  (equipment/conveyor)  -> page /plants/groveport/dock/production; hidden; demo
    Machine Room  (material/domain)  -> page /machine-room
      EPMS  (material/offline_bolt)  -> page /plants/groveport/machine-room/epms; hidden; demo
      Utility  (material/miscellaneous_services)  -> flattenLocal
        Devices  (equipment/devices)
          Tanks  (material/opacity)  -> page /tanks
            HTR  (material/opacity)
            HPR  (material/opacity)
            LTR  (material/opacity)
          Comps  (equipment/compressor)  -> page /compressors
            COMP 1  (equipment/compressor)
            COMP 4  (equipment/compressor)
            COMP 5  (equipment/compressor)
            COMP 6  (equipment/compressor)
            COMP 7  (equipment/compressor)
          Valves  (equipment/valve)  -> page /valves
            MAIN LIQ SV  (equipment/valve)  -> faceplate SolenoidValve on [default]Boars_Head/GrovePort/Machine Room/Valves/Main Liq SV
          Pumps  (equipment/pump)  -> page /pumps
            HTLR-Pump 1  (equipment/pump)  -> faceplate Pump on [default]Boars_Head/GrovePort/Machine Room/Pumps/HTLR-Pump 1
            HTLR-Pump 2  (equipment/pump)  -> faceplate Pump on [default]Boars_Head/GrovePort/Machine Room/Pumps/HTLR-Pump 2
            LTLR-Pump 1  (equipment/pump)  -> faceplate Pump on [default]Boars_Head/GrovePort/Machine Room/Pumps/LTLR-Pump 1
            LTLR-Pump 2  (equipment/pump)  -> faceplate Pump on [default]Boars_Head/GrovePort/Machine Room/Pumps/LTLR-Pump 2
          Exhaust Fans  (equipment/exhaust_fan)  -> page /exhaust-fans
          Sensors  (material/device_hub)  -> page /sensors
            HSS-PT2  (material/device_hub)
            HSL-PSIG  (material/device_hub)
            LSL-PSIG  (material/device_hub)
            LSS-PT1  (material/device_hub)
            HSD-PT3  (material/device_hub)
            COND SUMP  (material/device_hub)
          Rupture Disks  (equipment/rupture-disk)  -> page /rupture-disks
            PS01 EC1A-1  (equipment/rupture-disk)
            PS02 EC1A-2  (equipment/rupture-disk)
            PS03 EC1B-1  (equipment/rupture-disk)
            PS04 EC1B-2  (equipment/rupture-disk)
            PS05 COMP-1-SEPR-1  (equipment/rupture-disk)
            PS06 COMP-1-SEPR-2  (equipment/rupture-disk)
            PS07 COMP-1-TSYPHON  (equipment/rupture-disk)
            PS08 COMP-2-SEPR-1  (equipment/rupture-disk)
            PS09 COMP-2-SEPR-2  (equipment/rupture-disk)
            PS10 COMP-2-TSYPHON  (equipment/rupture-disk)
            PS14 COMP-4-SEPR-1  (equipment/rupture-disk)
            PS15 COMP-4-SEPR-2  (equipment/rupture-disk)
            PS16 COMP-4-TSYPHON  (equipment/rupture-disk)
            PS17 COMP-5-SEPR-1  (equipment/rupture-disk)
            PS18 COMP-5-SEPR-2  (equipment/rupture-disk)
            PS19 COMP-5-TSYPHON  (equipment/rupture-disk)
            PS20 COMP-6-SEPR-1  (equipment/rupture-disk)
            PS21 COMP-6-SEPR-2  (equipment/rupture-disk)
            PS22 COMP-6-TSYPHON  (equipment/rupture-disk)
            PS23 COMP-7-SEPR-1  (equipment/rupture-disk)
            PS24 COMP-7-SEPR-2  (equipment/rupture-disk)
            PS25 COMP-7-TSYPHON  (equipment/rupture-disk)
            PS26 TSYPON-VESSEL-1  (equipment/rupture-disk)
            PS27 TSYPON-VESSEL-2  (equipment/rupture-disk)
            PS28 LTR-VESSEL-1  (equipment/rupture-disk)
            PS29 LTR-VESSEL-2  (equipment/rupture-disk)
            PS30 LTR-OIL POT  (equipment/rupture-disk)
            PS31 HTR-VESSEL-1  (equipment/rupture-disk)
            PS32 HTR-VESSEL-2  (equipment/rupture-disk)
            PS33 HTR-VESSEL-2  (equipment/rupture-disk)
            PS34 HTR-OIL POT  (equipment/rupture-disk)
            PS35 PURGER  (equipment/rupture-disk)
            PS36 HPR-1  (equipment/rupture-disk)
            PS37 HPR-2  (equipment/rupture-disk)
          Safety Relays  (material/verified_user)  -> page /safety-relay
      Production  (equipment/conveyor)  -> page /plants/groveport/machine-room/production; hidden; demo
    Condensers  (material/domain)  -> page /condensers
      Utility  (material/miscellaneous_services)  -> flattenLocal
        Devices  (equipment/devices)
          Condensers  (equipment/exhaust_fan)  -> page /condensers/condenser-fans
            EC-1A Fan 1  (equipment/exhaust_fan)
            EC-1A Fan 2  (equipment/exhaust_fan)
            EC-1B Fan 1  (equipment/exhaust_fan)
            EC-1B Fan 2  (equipment/exhaust_fan)
          Pumps  (equipment/pump)  -> page /condensers/pumps
            Sump Pump 1  (equipment/pump)
            Sump Pump 2  (equipment/pump)
            Sump Pump 3  (equipment/pump)
          Valves  (equipment/valve)  -> page /condensers/valves
            MAIN HG SV  (equipment/valve)
            CSV MAKEUP SV  (equipment/valve)
            CSV MAKEUP BACKUP SV  (equipment/valve)
          Sensors  (material/device_hub)  -> page /condensers/sensors
            HSD-PT3  (material/device_hub)
            OAT  (material/device_hub)
            CSV-LEVEL  (material/device_hub)
          Tanks  (material/opacity)  -> page /condensers/tanks
            CSV  (material/opacity)
          Level Switches  (material/toggle_on)
            RS-LVL-OL2  (material/toggle_on)
            RS-LVL-OL3  (material/toggle_on)
            RS-LLCO2  (material/toggle_on)
          Sequences  (material/format_list_numbered)
            High Stage Discharge  (material/format_list_numbered)
    Operations  (material/build)
      Alarm Status  (material/notifications)  -> page /alarms
      Alarm Journal  (equipment/alarm_journal)  -> page /alarms/journal
      Trending  (equipment/trending)  -> page /trending
      Saved Trends  (material/bookmarks)  -> page /trending/saved
      Out Of Service Log  (material/sticky_note_2)  -> page /operations/out-of-service; permission=OutOfService/View
      Forms  (material/format_list_numbered)
        Daily Rounds Log  (material/ac_unit)  -> page /operations/forms/daily-rounds; permission=Forms/Use
        NH3 Shift Log  (material/opacity)  -> page /operations/forms/shift-log; permission=Forms/Use
        Annual P&ID Verification  (material/verified_user)  -> page /operations/forms/pid-verification; permission=Forms/Use
        Form History  (material/history)  -> page /operations/forms/history; permission=Forms/Use
      Reports  (material/show_chart)  -> permission=Reports/Page
        Report Builder  (material/show_chart)  -> page /operations/reports; permission=Reports/Page
        Saved Reports  (material/bookmarks)  -> page /operations/reports/saved; permission=Reports/Page
      PLCs  (material/memory)  -> page /operations/plcs
        RCP1  (material/developer_board)  -> page /operations/plcs/RCP1
    Admin  (material/admin_panel_settings)
      Audit Log  (material/history)  -> page /operations/audit; permission=AuditLog/View
      User Management  (material/supervisor_account)  -> page /operations/users; permission=UserManagement/Edit
      Roles & Permissions  (material/admin_panel_settings)  -> page /operations/roles-permissions; permission=RolesPermissions/Edit
  New Castle  (material/location_on)  -> page /plants/new-castle; hidden; demo
  Forrest City  (material/location_on)  -> page /plants/forrest-city; hidden; demo
  Petersburg  (material/location_on)  -> page /plants/petersburg; hidden; demo
  Holland  (material/location_on)  -> page /plants/holland; hidden; demo
  Enterprise Operations  (material/build)  -> hidden; demo
    Alarm Status  (material/notifications_active)  -> page /alarms
    Alarm Journal  (material/notifications_active)  -> page /alarms/journal
    AdHoc Trend  (material/show_chart)  -> page /trending
```

</details>
