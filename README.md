# CSCN_project
Final project Communication System in Corporate Networks' subject, erasmus 2023-2024

![image](https://github.com/user-attachments/assets/271adc48-5682-43fe-80a7-355360ab32ca)

# Asterisk PBX Information System

This project involves the creation of a small information system using Asterisk PBX within Docker containers. Below is an outline of the system architecture and components.

## System Schema
The system consists of the following components:

- **3 Docker Containers**:
  1. Asterisk
  2. Backend (FastAPI)
  3. HTTPS Proxy

### Components
- **Asterisk Server** (`asterisk.vsb.cz`):
  - Phones with numbers `10` and `11` connected to Asterisk via port `5060` using the `PJSIP` protocol.
  - Phones communicate with Asterisk using RTP protocol over ports `10000-10100`.

- **Backend**:
  - Bidirectional communication with Asterisk through the Asterisk Manager Interface (AMI).
  
- **HTTPS Proxy**:
  - Communicates bidirectionally with the Backend via HTTP.
  - HTTPS Proxy listens on port `443`.

## Asterisk Configuration
Using Asterisk version `alpine-20.5.2`, you will configure the following:

1. **PJSIP Accounts**:
   - Phone 10 (`number 10`)
   - Phone 11 (`number 11`)

2. **Conference**:
   - Conference reachable on number `18`.

3. **Simple IVR (Autoattendant)**:
   - Multi-level IVR system with at least two levels.

4. **Trunk Connection**:
   - Establish a trunk connection to `asterisk.vsb.cz`, which is the university's Asterisk server.

## Backend
The backend will be built using [FastAPI](https://fastapi.tiangolo.com/). The main functionality of the backend will include a simple interface, allowing users to perform operations like making calls (from one number to another).

## Docker Containers Setup
The system will run within Docker Desktop, with three containers configured as follows:

1. **Asterisk Container**:
   - Handles phone communication, IVR, and conference calls.

2. **Backend Container** (FastAPI):
   - Provides an API interface for interaction with the Asterisk PBX.

3. **Proxy Container** (HTTPS Proxy):
   - Manages HTTPS communication between the Backend and external systems, using port `443`.

## Summary
The system integrates Asterisk PBX with a FastAPI backend and an HTTPS proxy, facilitating communication between phones, handling IVR and conference calls, and providing a simple API for managing calls.
