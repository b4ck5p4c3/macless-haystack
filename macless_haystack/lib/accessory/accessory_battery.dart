enum AccessoryBatteryStatus {
  ok,     // Battery is currently charging
  medium,  // Battery is currently discharging
  low,         // Battery is fully charged
  criticalLow,          // Battery level is low
  unknown       // Battery status is unknown or not applicable
}