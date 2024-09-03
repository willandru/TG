# Load necessary libraries
library(dplyr)

# Parameters
radiant_intensity <- 15 # mW/sr
diameter_mm <- 5 # mm
distance_cm <- 1 # cm
wavelength_nm <- 940 # nm
view_angle_deg <- 30 # degrees

# Convert parameters to SI units
diameter_m <- diameter_mm / 1000 # meters
distance_m <- distance_cm / 100 # meters
view_angle_rad <- view_angle_deg * pi / 180 # radians

# Convert view angle to solid angle in steradians
solid_angle <- 2 * pi * (1 - cos(view_angle_rad / 2))

# Calculate radiant flux (in watts)
radiant_flux <- radiant_intensity * solid_angle * 1e-3 # convert mW to W

# Calculate irradiance
irradiance <- radiant_flux / (pi * (diameter_m / 2)^2) # W/m^2

# Define function to calculate MPE
calculate_mpe <- function(exposure_time_sec, wavelength_nm) {
  c4 <- 100.002 * (wavelength_nm - 700)
  
  # Determine alpha_min based on exposure time
  if (exposure_time_sec <= 0.7) {
    alpha_min <- 1.5 # mrad for short exposure times
  } else if (exposure_time_sec <= 10) {
    alpha_min <- 2 * exposure_time_sec^(3/4) # mrad
  } else {
    alpha_min <- 11 # mrad for longer exposure times
  }
  
  # MPE calculation
  mpe <- 7 * (10^(-4)) * c4 * (irradiance / alpha_min) # W/m^2
  return(mpe)
}

# Define exposure times
exposure_times <- c(10 * 60, 1 * 3600, 10 * 3600) # 10 min, 1 hr, 10 hrs in seconds

# Calculate MPE for each exposure time
mpe_values <- sapply(exposure_times, function(t) calculate_mpe(t, wavelength_nm))

# Print results
print(paste("Irradiance: ", round(irradiance, 2), "W/m^2"))
print("Maximum Permissible Exposure (MPE) values:")
names(mpe_values) <- c("10 minutes", "1 hour", "10 hours")
print(mpe_values)

# Check if irradiance is within safe limits
safe_check <- sapply(mpe_values, function(mpe) irradiance < mpe)
names(safe_check) <- c("10 minutes", "1 hour", "10 hours")
print("Safety Check:")
print(safe_check)
