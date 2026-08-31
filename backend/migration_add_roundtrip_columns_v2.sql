-- ============================================================================
-- MIGRATION: Add Roundtrip_COUPON.xlsx format columns to existing bookings table
-- Run this ONCE against your existing coupon_db database.
-- Compatible with MySQL 8.0.x (no IF NOT EXISTS needed on ADD COLUMN).
-- If a column already exists you'll get "Duplicate column name" — that's fine,
-- just remove that one line and re-run the rest.
-- ============================================================================

ALTER TABLE `bookings`
    ADD COLUMN `airline_pnr`   VARCHAR(50)  DEFAULT NULL,
    ADD COLUMN `booking_type`  VARCHAR(50)  DEFAULT NULL,
    ADD COLUMN `sector`        VARCHAR(150) DEFAULT NULL,
    ADD COLUMN `parent_pnr`    VARCHAR(50)  DEFAULT NULL,
    ADD COLUMN `pax_name`      VARCHAR(150) DEFAULT NULL,
    ADD COLUMN `source_status` VARCHAR(50)  DEFAULT NULL,
    ADD COLUMN `username`      VARCHAR(100) DEFAULT NULL;

ALTER TABLE `bookings`
    ADD INDEX `idx_parent_pnr` (`parent_pnr`);
