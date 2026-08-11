# Requirements

## 1. Functional Requirements

### FR-01 — Galaxy exploration

The system shall allow the user to explore galaxies
stored in the database.

### FR-02 — Galaxy information

The system shall display the relevant properties of
a selected galaxy.

### FR-03 — Planetary system exploration

The system shall allow the user to navigate from a
galaxy to its associated planetary systems.

### FR-04 — Planetary system information

The system shall display information about a selected
planetary system.

### FR-05 — Stellar objects

The system shall allow the user to explore stars
associated with a planetary system.

### FR-06 — Planets

The system shall allow the user to explore planets
associated with a planetary system.

### FR-07 — Natural satellites

The system shall allow the user to explore natural
satellites associated with a planet.

### FR-08 — Object information

The system shall display the physical properties
stored for a selected astronomical object.

### FR-09 — Database communication

The system shall retrieve astronomical information
from the MySQL database through the backend.

### FR-10 — Navigation

The system shall allow the user to navigate between
related astronomical structures.

---

## 2. Non-Functional Requirements

### NFR-01 — Usability

The interface should allow users to understand the
relationship between astronomical structures without
requiring technical knowledge of the database.

### NFR-02 — Scientific consistency

The data presented by the application should maintain
reasonable scientific consistency.

### NFR-03 — Visual approximation

The spatial visualization does not need to represent
the actual universe at physical scale.

### NFR-04 — Maintainability

The application should be divided into separate
frontend, backend and database components.

### NFR-05 — Version control

The source code and documentation shall be managed
using Git.

---

## 3. MVP Acceptance Criteria

The MVP will be considered functional when:

- A user can open the web application.
- The application can communicate with the backend.
- The backend can communicate with MySQL.
- A galaxy can be retrieved from the database.
- A user can select a galaxy.
- Associated planetary systems can be retrieved.
- A planetary system can be selected.
- Associated stars and planets can be retrieved.
- A user can select an astronomical object.
- The object's properties can be displayed.