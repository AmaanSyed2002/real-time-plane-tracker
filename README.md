# Closest Plane Finder

A Python tool that tracks live airplane data and identifies the two closest planes in the sky in real-time. Built using the [OpenSky Network API](https://opensky-network.org/), this script filters out irrelevant or stale data and performs 3D distance calculations using the Haversine formula with altitude.

---

## Features

 Real-time flight data using OpenSky Network  
 Filters stale, grounded, or airport-near flights  
 Calculates 3D distance using lat/lon + altitude  
 Finds the closest pair of aircraft  
 Clean terminal logging for live feedback  
 Direct link to view planes on a live radar map

---

## Demo Output

Plane 1: PQU (-34.8108, 138.6261, 83.82, 1745460986)
Plane 2: MBE (-34.8105, 138.629, 167.64, 1745460986)
Distance: 917.67 FT
https://globe.adsb.fi/?icao=7c4e44,7c3ce8

---

## File Description

📁 plane/
├── 📄 data.py        → Fetches and filters plane data
├── 📄 distance.py    → Calculates Haversine + altitude distance
├── 📄 logoff.py      → Logging configuration
├── ✈️ plane.py       → Class definition for a plane with details like ICAO, position, and altitude
├── 🚀 main.py        → Main execution file
└── 📘 README.md      → You're here!

