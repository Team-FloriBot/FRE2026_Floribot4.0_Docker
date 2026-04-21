# FRE2026 FloriBot 4.0 Docker

Containerisierte Umgebung für den FloriBot 4.0 auf Basis von ROS 2.

---

## Überblick

Dieses Repository stellt eine modulare Docker-Infrastruktur für den FloriBot 4.0 bereit.

**Features:**

* Trennung in Hardware-nahe Komponenten und Simulation
* Unterstützung für:

  * Base (Kinematik + Robotik-Grundsystem)
  * Sensors (Sensorintegration)
  * Webteleop (Webbasierte Steuerung)
  * Stage (2D-Simulation)
  * Gazebo (3D-Simulation)
* Docker Compose mit Profilen
* Skriptbasierte Steuerung (Build, Start, Stop, Logs)

---

## Repository-Struktur

```
FRE2026_FloriBot4.0_Docker/
├── base/
├── sensors/
├── webteleop/
├── stage/
├── gazebo/
├── compose/
├── scripts/
└── README.md
```

---

## Installation

### 1. Repository klonen

```bash
git clone https://github.com/Team-FloriBot/FRE2026_FloriBot4.0_Docker.git
cd FRE2026_FloriBot4.0_Docker
```

### 2. Konfiguration

```bash
cp compose/.env.example compose/.env
```

### 3. Build

```bash
cd compose
docker compose build
```

Alternativ über Script:

```bash
./scripts/build.sh
```

### 4. Start

```bash
cd compose
docker compose up
```

Oder über Script:

```bash
./scripts/up.sh
```

---

## Services

| Service              | Beschreibung             |
| -------------------- | ------------------------ |
| `floribot-base`      | Robotik-Kern + Kinematik |
| `floribot-sensors`   | Sensorintegration        |
| `floribot-webteleop` | Webbasierte Steuerung    |
| `floribot-stage`     | 2D-Simulation (Stage)    |
| `floribot-gazebo`    | 3D-Simulation (Gazebo)   |

---

## Docker Compose Profile

### Core / Robot

**Profile:**

* `core`
* `robot`

**Startet:**

* floribot-base
* floribot-sensors
* floribot-webteleop

---

### UI

**Profile:**

* `ui`

**Startet:**

* floribot-webteleop

---

### Simulation

**Profile:**

* `sim`

**Startet:**

* floribot-stage
* floribot-gazebo

---

### Stage

**Profile:**

* `stage`

**Startet:**

* floribot-stage

---

### Gazebo

**Profile:**

* `gazebo`

**Startet:**

* floribot-gazebo

---

## Profile starten

### Robotik-System

```bash
docker compose --profile core up
```

### Nur Webteleop

```bash
docker compose --profile ui up
```

### Simulation komplett

```bash
docker compose --profile sim up
```

### Nur Stage

```bash
docker compose --profile stage up
```

### Nur Gazebo

```bash
docker compose --profile gazebo up
```

### Mehrere Profile kombinieren

```bash
docker compose --profile core --profile sim up
```

### Im Hintergrund starten

```bash
docker compose --profile core up -d
```

---

## Skripte

Im Ordner `scripts/` stehen Hilfsskripte zur Verfügung:

```bash
./scripts/build.sh   # Build aller Container
./scripts/up.sh      # Start der Umgebung
./scripts/down.sh    # Stoppen aller Container
./scripts/logs.sh    # Logs anzeigen
```

---

## Stoppen

### Alle Container stoppen

```bash
docker compose down
```

