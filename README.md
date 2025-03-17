# 🏪 Vendor and Shop Management System

## 📌 Introduction
This is a **Django-based Vendor and Shop Management System** that provides APIs for:
- **Vendor Registration & Authentication (JWT)**
- **Shop Management (CRUD Operations)**
- **Finding Nearby Shops Using Geolocation**

## 🛠️ Tech Stack
- **Backend**: Django, Django REST Framework (DRF), Django Simple JWT
- **Database**: SQLite
- **Authentication**: JWT (Access & Refresh Tokens)

---

## 🚀 API Endpoints

### 1️⃣ Authentication & User Management

#### 🔹 Register a New Vendor
- **Endpoint**: `POST /register/`
- **Request Body**:
  ```json
  {
    "full_name": "Heisenberg",
    "username": "vendor1",
    "password": "securepassword123"
  }
- **Response**:
```json
{
  "message": "Vendor registered successfully!"
}
```
---

#### 🔹Login (Obtain JWT Access & Refresh Tokens)[POST]
- **Endpoint**: `POST /login/`
- **Description**: Authenticates the vendor and returns JWT access & refresh tokens.
- **Request**:
```json
{
  "username": "vendor1",
  "password": "securepassword123"
}
```
- **Response**:
```json
{
  "access": "eyJhbGciOiJIUzI1...",
  "refresh": "eyJhbGciOiJIUzI1..."
}
```
- **Usage**:
    - The access token is used in Authorization headers for protected requests.
    - The refresh token is used to obtain a new access token, usually before expiry of access token.

---
#### 🔹 Refresh JWT Access Token[POST]
- **Endpoint**: `POST /login/refresh/`
- **Description**: Generates a new access token using the refresh token.
- **Request**:
```json
{
  "refresh": "eyJhbGciOiJIUzI1..."
}
```
- **Response**:
```json
{
  "access": "new_access_token_here",
  "refresh": "new_refresh_token_here"
}
```

### 2️⃣ Shop Management
#### 🔹 Create a New Shop[POST]
- **Endpoint**: `POST /shops/`
- **Description**: Adds a new shop for an authenticated vendor.
- **Headers**: Bearer/Access Token required
- **Request Body**:
```json
{
  "name": "FurnishingHome",
  "type_of_business": "Furniture",
  "latitude": 0.11,
  "longitude": 8.11
}
```
- **Response**:
```json
{
  "id": 1,
  "name": "FurnishingHome",
  "owner": "vendor1",
  "type_of_business": "Furniture",
  "latitude": 0.11,
  "longitude": 8.11
}
```

#### 🔹 Get All Shops by logged-in vendor [GET]
- **Endpoint**: `GET /shops/`
- **Description**: Retrieves all shops owned by the logged-in vendor.
- **Headers**: Access Token required
- **Response**:
```json
[
  {
    "id": 1,
    "name": "FurnishingHome",
    "owner": "vendor1",
    "type_of_business": "Furniture",
    "latitude": 0.11,
    "longitude": 8.11
  },
  {
    "id": 2,
    "name": "TechWorld",
    "owner": "vendor1",
    "type_of_business": "Electronics",
    "latitude": 12.34,
    "longitude": 56.78
  }
]
```
#### 🔹 Get Shop Details [GET]
- **Endpoint**: GET /shops/{id}/
- **Description**: Retrieves details of a specific shop by ID.
- **Headers**:
Access token required
- **Response**:
```json
{
  "id": 1,
  "name": "FurnishingHome",
  "owner": "vendor1",
  "type_of_business": "Furniture",
  "latitude": 0.11,
  "longitude": 8.11
}
```
#### 🔹 Update Shop Details [PUT]
- **Endpoint**: PUT /shops/{id}/
- **Description**: Updates a shop's details.
- **Headers**: Access Token Required
- **Request Body**:
```json
{
  "name": "FurnishingHome Updated",
  "type_of_business": "Home Decor",
  "latitude": 1.23,
  "longitude": 4.56
}
```
- **Response**:
```json
{
  "id": 1,
  "name": "FurnishingHome Updated",
  "owner": "vendor1",
  "type_of_business": "Home Decor",
  "latitude": 1.23,
  "longitude": 4.56
}
```

#### 🔹 Delete a Shop[DELETE]
- **Endpoint**: DELETE /shops/{id}/
- **Description**: Deletes a shop.
- **Headers**: Access Token required
- **Response**:
```json
{
  "message": "Shop deleted successfully."
}
```

## 3️⃣ Find Nearby Shops
- **Endpoint**: GET /shops/nearby/?lat=<value>&lon=<value>&radius=<value>
- **Description**: Finds shops within a given radius (in km) from a given latitude & longitude.
- **Request**:
```GET /shops/nearby/?lat=37.7749&lon=-122.4194&radius=5```
- **Response**:
```json
[
  {
    "id": 2,
    "name": "TechWorld",
    "owner": "vendor1",
    "type_of_business": "Electronics",
    "latitude": 37.7750,
    "longitude": -122.4180
  },
  {
    "id": 5,
    "name": "FashionStore",
    "owner": "vendor2",
    "type_of_business": "Clothing",
    "latitude": 37.7800,
    "longitude": -122.4100
  }
]
```

---
## 🔒 Security Considerations
### 1️⃣ 🔐 Secured Storage of Sensitive Data

- Passwords are hashed using Django's built-in authentication system.
- Tokens are stored securely in HTTP-Only Cookies.

### 2️⃣ 🛑 Role-Based Access Control

- Only authenticated vendors can create/update/delete their own shops.
- Nearby shops API is public, but other actions require authentication.
  
### 3️⃣ 🚀 Token Expiry & Auto-Refresh

- Access Token expires quickly but can be refreshed using the refresh token.

---
# 📌 API Endpoints (TL;DR):

## ***Requires Authentication***
### 🔹 Auth & Vendor Management
  - **Register a Vendor** → `POST /register/`  
    - Create a new vendor account.  

  - **Login** → `POST /login/`  
    - Get access & refresh tokens.  

  - **Refresh Token** → `POST /login/refresh/`  
    - Get a new access token using the refresh token.  

### 🔹 Shop Management
  - **List All Shops** → `GET /shops/`  
    - Retrieve all shops of the authenticated vendor.  

  - **Create Shop** → `POST /shops/`  
    - Add a new shop.  

  - **Get Shop Details** → `GET /shops/{id}/`  
    - Retrieve details of a specific shop.  

  - **Update Shop** → `PUT /shops/{id}/`  
    - Modify shop details.  

  - **Delete Shop** → `DELETE /shops/{id}/`  
    - Remove a shop.  

---

## ***Available openly as the name suggests***
### 🔹 Public API
- **Find Nearby Shops** → `GET /shops/nearby/?lat={value}&lon={value}&radius={value}`  
- Search shops within a specified radius.  
