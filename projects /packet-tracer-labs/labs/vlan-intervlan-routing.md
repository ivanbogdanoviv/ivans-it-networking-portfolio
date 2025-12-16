# VLANs & Inter-VLAN Routing (Router-on-a-Stick)

## 🎯 Objective
Design and configure a small network using VLANs and enable communication between VLANs using a router-on-a-stick approach.

---

## 🧩 Topology
- 1 Router
- 1 Switch
- Multiple end devices in different VLANs

---

## ⚙ Configuration Summary

- Created multiple VLANs on the switch
- Assigned access ports to the appropriate VLANs
- Configured an 802.1Q trunk between the switch and router
- Configured router subinterfaces for inter-VLAN routing
- Enabled DHCP for each VLAN

---

## ✅ Validation & Testing

- Verified VLAN configuration using:
  - `show vlan brief`
- Verified trunking using:
  - `show interfaces trunk`
- Verified routing using:
  - `show ip route`
- Successfully tested connectivity using:
  - Ping between hosts in different VLANs

---

## 🧠 Skills Demonstrated

- VLAN configuration and segmentation
- Inter-VLAN routing concepts
- DHCP configuration
- Network troubleshooting and verification
