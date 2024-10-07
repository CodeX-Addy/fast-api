# SQL Query Runner

A simple web-based application to execute SQL queries on a MySQL database. The app has a FastAPI backend and a JavaScript-based frontend, allowing users to input and run SQL queries directly from the frontend interface.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)


## Overview
This project provides a simple SQL query runner, allowing users to interact with a MySQL database via a web interface. You can use it to run `SELECT`, `INSERT`, `UPDATE`, and `DELETE` queries and see results directly on the webpage. The application is designed with a FastAPI backend and a basic JavaScript and HTML frontend with built-in CSS styling for a clean, responsive interface.

## Features
- Connects to a MySQL database.
- Supports SQL query execution from the frontend interface.
- Displays query results in a clean, tabular format for `SELECT` queries.
- Displays success or error messages for non-`SELECT` queries.
- Simple and clean user interface with responsive design.

## Technologies Used
- **Backend**: FastAPI
- **Database**: MySQL
- **Frontend**: HTML, JavaScript, CSS

## Prerequisites
- Python 3.8+
- MySQL Server
- Node.js (for development environment, if needed)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/CodeX-Addy/fast-api.git
cd fast-api
```
### 2. Install required packages
```bash
pip install -r requirements.txt
```

### 3. Run the server
```bash
uvicorn app:app --reload

```
