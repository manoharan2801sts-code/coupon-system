-- ============================================================================
-- Coupon Management System - MySQL Database Schema
-- Compatible with MySQL 8.0+
-- ============================================================================

CREATE DATABASE IF NOT EXISTS `coupon_db` 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

USE `coupon_db`;

-- ----------------------------------------------------------------------------
-- 1. Table: customers
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `customers` (
    `customer_id` VARCHAR(50) NOT NULL PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `email` VARCHAR(100) NOT NULL UNIQUE,
    `phone` VARCHAR(30) DEFAULT NULL,
    `status` VARCHAR(20) NOT NULL DEFAULT 'Active',
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 2. Table: coupon_balance
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `coupon_balance` (
    `customer_id` VARCHAR(50) NOT NULL PRIMARY KEY,
    `total_earned` DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    `pending` DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    `available` DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    `redeemed` DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    `expired` DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    `cancelled` DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT `fk_balance_customer` FOREIGN KEY (`customer_id`) 
        REFERENCES `customers` (`customer_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 3. Table: coupon_rules
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `coupon_rules` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `rule_id` VARCHAR(50) NOT NULL UNIQUE,
    `supplier` VARCHAR(100) DEFAULT NULL,
    `airline` VARCHAR(100) DEFAULT NULL,
    `fare_type` VARCHAR(100) DEFAULT NULL,
    `coupon_percent` DECIMAL(5, 2) NOT NULL DEFAULT 1.00,
    `priority` INT NOT NULL DEFAULT 0,
    `status` VARCHAR(20) NOT NULL DEFAULT 'Active',
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 4. Table: bookings
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `bookings` (
    `booking_ref` VARCHAR(50) NOT NULL PRIMARY KEY,
    `customer_id` VARCHAR(50) NOT NULL,
    `supplier` VARCHAR(100) DEFAULT NULL,
    `airline` VARCHAR(100) DEFAULT NULL,
    `fare_type` VARCHAR(100) DEFAULT NULL,
    `booking_fare` DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    `booking_date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `travel_date` DATETIME NOT NULL,
    `status` VARCHAR(30) NOT NULL DEFAULT 'Completed',
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `airline_pnr` VARCHAR(50) DEFAULT NULL,
    `booking_type` VARCHAR(50) DEFAULT NULL,
    `sector` VARCHAR(150) DEFAULT NULL,
    `parent_pnr` VARCHAR(50) DEFAULT NULL,
    `pax_name` VARCHAR(150) DEFAULT NULL,
    `source_status` VARCHAR(50) DEFAULT NULL,
    `username` VARCHAR(100) DEFAULT NULL,
    CONSTRAINT `fk_booking_customer` FOREIGN KEY (`customer_id`) 
        REFERENCES `customers` (`customer_id`) ON DELETE CASCADE,
    INDEX `idx_parent_pnr` (`parent_pnr`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 5. Table: coupons
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `coupons` (
    `coupon_id` VARCHAR(50) NOT NULL PRIMARY KEY,
    `booking_ref` VARCHAR(50) NOT NULL UNIQUE,
    `customer_id` VARCHAR(50) NOT NULL,
    `coupon_percent` DECIMAL(5, 2) NOT NULL DEFAULT 0.00,
    `coupon_amount` DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    `status` VARCHAR(30) NOT NULL DEFAULT 'Pending',
    `eligibility_date` DATETIME NOT NULL,
    `expiry_date` DATETIME DEFAULT NULL,
    `remarks` VARCHAR(255) DEFAULT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT `fk_coupon_customer` FOREIGN KEY (`customer_id`) 
        REFERENCES `customers` (`customer_id`) ON DELETE CASCADE,
    INDEX `idx_coupon_booking` (`booking_ref`),
    INDEX `idx_coupon_status` (`status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 6. Table: coupon_redemptions
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `coupon_redemptions` (
    `redemption_id` VARCHAR(50) NOT NULL PRIMARY KEY,
    `txn_id` VARCHAR(50) NOT NULL UNIQUE,
    `customer_id` VARCHAR(50) NOT NULL,
    `booking_ref` VARCHAR(50) NOT NULL,
    `amount_redeemed` DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    `booking_fare` DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    `customer_payable` DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    `status` VARCHAR(30) NOT NULL DEFAULT 'Success',
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT `fk_redemption_customer` FOREIGN KEY (`customer_id`) 
        REFERENCES `customers` (`customer_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 7. Table: coupon_ledger
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `coupon_ledger` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `txn_id` VARCHAR(50) NOT NULL UNIQUE,
    `customer_id` VARCHAR(50) NOT NULL,
    `booking_ref` VARCHAR(50) NOT NULL,
    `txn_type` VARCHAR(50) NOT NULL,
    `booking_fare` DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    `coupon_percent` DECIMAL(5, 2) NOT NULL DEFAULT 0.00,
    `coupon_earned` DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    `amount` DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    `status` VARCHAR(30) NOT NULL DEFAULT 'Pending',
    `travel_date` DATETIME DEFAULT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT `fk_ledger_customer` FOREIGN KEY (`customer_id`) 
        REFERENCES `customers` (`customer_id`) ON DELETE CASCADE,
    INDEX `idx_ledger_customer` (`customer_id`),
    INDEX `idx_ledger_booking` (`booking_ref`),
    INDEX `idx_ledger_created` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 8. Table: system_settings
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `system_settings` (
    `config_key` VARCHAR(50) NOT NULL PRIMARY KEY,
    `config_value` VARCHAR(255) NOT NULL,
    `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 9. Table: admin_users (Authentication & RBAC)
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `admin_users` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `email` VARCHAR(150) NOT NULL UNIQUE,
    `password` VARCHAR(255) NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    INDEX `idx_admin_email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================================
-- SEED INITIAL SAMPLE DATA
-- ============================================================================

-- Admin Users (Default password: Admin@123)
INSERT INTO `admin_users` (`name`, `email`, `password`) VALUES
('Super Admin', 'admin@coupon.com', '5ac8c79272255741ab15b43d510b0458ed2b164d104b28a3d88d48ddb0bec0c6')
ON DUPLICATE KEY UPDATE `name` = VALUES(`name`);

-- Customers
INSERT INTO `customers` (`customer_id`, `name`, `email`, `phone`, `status`) VALUES
('CUST001', 'Rajesh Kumar', 'rajesh@email.com', '+91 9876543210', 'Active'),
('CUST002', 'Priya Sharma', 'priya@email.com', '+91 9876543211', 'Active'),
('CUST003', 'Amit Patel', 'amit@email.com', '+91 9876543212', 'Active')
ON DUPLICATE KEY UPDATE `name` = VALUES(`name`);

-- Coupon Balances
INSERT INTO `coupon_balance` (`customer_id`, `total_earned`, `pending`, `available`, `redeemed`, `expired`, `cancelled`) VALUES
('CUST001', 5000.00, 500.00, 4500.00, 1000.00, 0.00, 0.00),
('CUST002', 3000.00, 0.00, 3000.00, 0.00, 0.00, 0.00),
('CUST003', 2000.00, 200.00, 1800.00, 0.00, 0.00, 0.00)
ON DUPLICATE KEY UPDATE `available` = VALUES(`available`);

-- Coupon Rules (Hierarchical Priority Matching)
INSERT INTO `coupon_rules` (`rule_id`, `supplier`, `airline`, `fare_type`, `coupon_percent`, `priority`, `status`) VALUES
('RULE-001', 'Supplier A', 'IndiGo', 'Super 6E', 3.00, 7, 'Active'),
('RULE-002', 'Supplier A', 'IndiGo', NULL, 2.00, 6, 'Active'),
('RULE-003', 'Supplier A', 'Air India', 'Flexi', 2.50, 5, 'Active'),
('RULE-004', 'Supplier B', 'SpiceJet', NULL, 1.50, 4, 'Active'),
('RULE-005', NULL, NULL, NULL, 1.00, 0, 'Active')
ON DUPLICATE KEY UPDATE `coupon_percent` = VALUES(`coupon_percent`);

-- Sample Bookings
INSERT INTO `bookings` (`booking_ref`, `customer_id`, `supplier`, `airline`, `fare_type`, `booking_fare`, `booking_date`, `travel_date`, `status`) VALUES
('BK-2024-001', 'CUST001', 'Supplier A', 'IndiGo', 'Super 6E', 10000.00, '2024-11-20 10:00:00', '2024-12-10 14:30:00', 'Completed'),
('BK-2024-002', 'CUST001', 'Supplier A', 'Air India', 'Flexi', 12000.00, '2024-11-22 11:30:00', '2024-12-20 18:00:00', 'Completed'),
('BK-2024-003', 'CUST002', 'Supplier B', 'SpiceJet', 'Regular', 7500.00, '2024-11-25 09:15:00', '2024-12-15 12:00:00', 'Completed')
ON DUPLICATE KEY UPDATE `booking_fare` = VALUES(`booking_fare`);

-- Sample Redemptions
INSERT INTO `coupon_redemptions` (`redemption_id`, `txn_id`, `customer_id`, `booking_ref`, `amount_redeemed`, `booking_fare`, `customer_payable`, `status`, `created_at`) VALUES
('RED-001', 'RDM-1732796600.1', 'CUST001', 'BK-2024-002', 1000.00, 12000.00, 11000.00, 'Success', '2024-11-28 10:00:00')
ON DUPLICATE KEY UPDATE `amount_redeemed` = VALUES(`amount_redeemed`);

-- Sample Ledger Entries
INSERT INTO `coupon_ledger` (`txn_id`, `customer_id`, `booking_ref`, `txn_type`, `booking_fare`, `coupon_percent`, `coupon_earned`, `amount`, `status`, `travel_date`, `created_at`) VALUES
('TXN-1732796400.1', 'CUST001', 'BK-2024-001', 'Coupon Earned', 10000.00, 3.00, 300.00, 300.00, 'Eligible', '2024-12-10 14:30:00', '2024-11-20 10:00:00'),
('TXN-1732796400.2', 'CUST001', 'BK-2024-002', 'Coupon Earned', 12000.00, 2.50, 300.00, 300.00, 'Eligible', '2024-12-20 18:00:00', '2024-11-22 11:30:00'),
('RDM-1732796600.1', 'CUST001', 'BK-2024-002', 'Coupon Redeemed', 12000.00, 0.00, 0.00, -1000.00, 'Success', NULL, '2024-11-28 10:00:00'),
('TXN-1732796400.3', 'CUST001', 'BK-2024-003', 'Coupon Earned', 15000.00, 3.00, 450.00, 450.00, 'Pending', '2024-12-28 10:00:00', '2024-11-28 11:00:00')
ON DUPLICATE KEY UPDATE `amount` = VALUES(`amount`);

-- System Settings
INSERT INTO `system_settings` (`config_key`, `config_value`) VALUES
('min_redemption', '100'),
('max_redemption', '50000'),
('expiry_days', '365'),
('allow_partial_redemption', 'true'),
('allow_combined_offers', 'false')
ON DUPLICATE KEY UPDATE `config_value` = VALUES(`config_value`);
