# Number-Format-System-
This desktop utility, built in Python using CustomTkinter, allows users to define, apply, and manage custom number formatting presets at the system level on Window
**Number Format System Utility – Documentation**

---

## Table of Contents

1. Project Overview
2. Key Features
3. Technology Stack & Dependencies
4. Environment Setup & Installation
5. Directory Structure
6. User Interface Overview
7. Database Schema
8. Class & Method Breakdown

   * 8.1 `App` Class
   * 8.2 Timer Methods
   * 8.3 Registry Modification Method (`change`)
   * 8.4 Preset Management (Add / Edit / Delete)
   * 8.5 UI Navigation Methods
9. Workflow & Data Flow
10. Security & Permissions
11. Customization & Extensibility
12. Troubleshooting & FAQs
13. SEO Keywords
14. Author & License

---

## 1. Project Overview

This desktop utility, built in Python using CustomTkinter, allows users to define, apply, and manage custom number formatting presets at the system level on Windows. You can:

* Change decimal and grouping symbols via Windows registry.
* Save multiple presets (named configurations) in a local SQLite database.
* Edit or delete saved presets.
* Schedule automatic reversion to a default preset with a timer.

Ideal for finance professionals or international users needing quick locale adjustments.

---

## 2. Key Features

* **System-Wide Format Change**: Updates Windows registry keys—`sDecimal` and `sThousand` under `Control Panel\International`.
* **Preset Management**: Create, read, update, delete named formatting presets stored in a SQLite database.
* **Realtime UI**: Interactive dashboard with sidebar navigation to access all functions.
* **Timer Mode**: Schedule automatic reversion to default formatting after a set duration (HH\:MM).
* **Appearance Themes**: Light/Dark/System modes via CustomTkinter.

---

## 3. Technology Stack & Dependencies

* **Python 3.8+**
* **CustomTkinter**: Modern theming for Tkinter widgets (`pip install customtkinter`).
* **SQLite3**: Built-in database for storing presets.
* **winreg**: Standard Windows registry manipulation.
* **tkinter**: Base GUI toolkit.

---

## 4. Environment Setup & Installation

1. **Clone Repository**:

   ```bash
   git clone <repo_url>
   cd NumberFormatApp
   ```
2. **Install Python**: Ensure Python 3.8+ installed.
3. **Install Dependencies**:

   ```bash
   pip install customtkinter
   ```
4. **Run Application**:

   ```bash
   python number_format_app.py
   ```

> **Note:** Must be run with user account having permission to modify registry.

---

## 5. Directory Structure

```
/NumberFormatApp/
├── number_format_app.py    # Main application
├── customer.db             # SQLite database (auto-created)
└── README.md               # Documentation
```

---

## 6. User Interface Overview

* **Sidebar**:

  * Clear All
  * New Preset
  * Edit Preset
  * Delete Preset
  * Default (apply default comma/dot)
  * Select Preset
  * Timer
  * Appearance Mode switch

* **Main Panel**: Dynamic content area displaying forms for creating/editing presets, listing saved presets, and displaying timers or confirmation messages.

---

## 7. Database Schema

**SQLite Table: `customer`**

| Column    | Type | Description                      |
| --------- | ---- | -------------------------------- |
| firstname | TEXT | Preset name                      |
| lastname  | TEXT | Decimal symbol (e.g. `.`)        |
| email     | TEXT | Grouping symbol (e.g. `,`)       |
| time      | TEXT | Timer duration in `HH:MM` format |

The table is created on startup if it does not exist.

---

## 8. Class & Method Breakdown

### 8.1 `class App(customtkinter.CTk)`

* **`__init__`**: Sets up window, grid, database, and sidebar buttons, then calls `opts()` to load presets.
* **`create_table()`**: Ensures the `customer` table exists in `customer.db`.

### 8.2 Timer Methods

* **`start_timer()`**: Prompts user for `HH:MM`, calculates end time, and calls `update_timer()`.
* **`update_timer()`**: Updates countdown every second; on zero, calls `timer_ended()`.
* **`timer_ended()`**: Reverts to default format and informs the user via messagebox.

### 8.3 Registry Modification Method

* **`change(dot, com)`**: Opens registry key `HKCU\Control Panel\International` and sets:

  * `sDecimal` = `dot`
  * `sThousand` = `com`
  * Positive/negative patterns to `#,##0.00`

### 8.4 Preset Management

* **Add New Preset**:

  * `add_new_set_layout()`: Displays input form.
  * `add_new_set()`: Inserts preset into DB, applies format, reloads UI.

* **Select Preset**:

  * `change_command()`: Lists presets from DB, shows current format, and creates "Use" buttons for each.

* **Edit Preset**:

  * `edit_l()`: Lists presets with "Edit" buttons.
  * `edit_layout(name)`: Shows form pre-filled for `name`.
  * `edit()`: Updates DB entry.

* **Delete Preset**:

  * `delete_l()`: Lists presets with "Delete" buttons.
  * `delete_layout(name)`: Confirmation prompt.
  * `delete()`: Deletes DB entry.

* **Clear All UI**: `buttonw()` removes all main-panel widgets.

### 8.5 UI Navigation Methods

* **`opts()`**: Loads preset names into `self.li` for selection menus.
* **`defo()`**: Shortcut to apply default format (`,` and `.`).
* **`current()`**: Reads and displays the current system format.

---

## 9. Workflow & Data Flow

1. **Startup**: Create DB table, load presets.
2. **User Action**: Click sidebar button -> form loads in main panel.
3. **Form Submission**: Entry values read -> DB updated -> `change()` called -> UI feedback shown.
4. **Timer**: When set, countdown updates; on expiration resets to default.

---

## 10. Security & Permissions

* **Registry Access**: Requires that Python process has write access to `HKCU`.
* **DB File**: Stored in app directory; ensure proper file permissions.
* **No External Connections**: All operations local to system.

---

## 11. Customization & Extensibility

* **Change Number Pattern**: Modify `number_format` in `change()` to support more formats.
* **UI Enhancements**: Add columns to database or new sidebar actions.
* **Cross‑Platform**: Currently Windows‑only; abstract registry calls for other OS.

---

## 12. Troubleshooting & FAQs

* **Permission Denied**: Run app as user with registry write rights.
* **Preset List Not Updating**: Ensure DB file `customer.db` is in working directory.
* **Timer Not Firing**: Verify `HH:MM` format in input dialog.

---

## 13. SEO Keywords

```
Python registry editor
tkinter locale formatter
customtkinter presets
desktop number format tool
windows number format python
sqlite tkinter CRUD
auto timer locale reset
Python registry editor
tkinter locale formatter
customtkinter presets
desktop number format tool
windows number format python
sqlite tkinter CRUD
auto timer locale reset

```

---

## 14. Author & License

**Author:** Smaron Biswas
**Date:** 2024
**License:** MIT License

---
