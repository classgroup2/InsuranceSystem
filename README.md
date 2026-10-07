# Insurance Policy & Claims Management System

A Python-based Object-Oriented Programming (OOP) system designed to manage clients, handle multi-category insurance policies, and track claims with built-in validation rules.

## Core Features
- **Client & Policy Management:** Register clients and bind them to Motor, Health, or Property policies.
- **Dynamic Premium Calculation:** Polymorphic premium calculations tailored by policy type (asset valuations, risk tiers, and age bands).
- **Claims Workflow:** Record, validate, and track claims against active policies and insured limits.
- **Robust Encapsulation:** Validation of inputs (dates, phone numbers, claim thresholds) handled via Python `@property` decorators.

## Architecture & OOP Highlights
- **Abstraction:** Abstract base class `InsurancePolicy` enforcing interface contracts.
- **Inheritance & Polymorphism:** Specialized subclasses (`MotorPolicy`, `HealthPolicy`, `PropertyPolicy`) overriding `calculate_premium()` and `insured_value()`.
- **System Orchestration:** Decoupled `InsuranceSystem` management engine to coordinate domain entities without procedural clutter.




## Project Overview

In production insurance platforms, business rules, underwriting logic, and loss ratios vary drastically between lines of business. This project demonstrates how clean domain-driven OOP design isolates business logic from the user interface:

- **Entity Management:** Registering clients with localized data constraints and auto-incrementing identity keys (`C001`, `C002`).
- **Specialized Underwriting:** Underwriting across Motor, Health, and Property domains using a common contractual base class.
- **Controlled Claim Settlement:** Managing the full claim lifecycle (`Pending` $\rightarrow$ `Approved` / `Rejected` $\rightarrow$ `Paid`), preventing claims on expired policies, and blocking payouts that exceed asset insured limits.
- **Reporting & Portfolio Auditing:** Providing live portfolio performance reports, loss-exposure calculations, and breakdown of premium revenues.

-