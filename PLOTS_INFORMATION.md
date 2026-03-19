# Plots Information
The collection of plots is designed to identify key physical signatures of magnetospheric substorms, including magnetic field dipolarization (Bz), rapid field variability (dBz6sec), enhanced plasma flows (Vx), and particle energization (flux). By combining these observables, we can move beyond simple visualization and begin defining quantitative criteria for substorm detection and model development.

**Timeline**: 7/1/2014 - 12/31/2014
<br>

1. Spacecraft Location in the Magnetosphere
- Plots: Plot GSM Coordinates as a function of time
- Purpose: Determine when the spacecraft is located within the magnetotail, plasma sheet, or other magnetospheric region where substorm activity occurs.
- Origin: Center of Earth (geocentric)
- X-axis: Points from Earth to the Sun
- Z-axis: Lies in the plane containing Earth's magnetic dipole and X-axis, positive northward
- Y-axis: Completes a right-handed system (roughly duskward)

2. Magnetic Field Evolution
- Plots: Magnetic Field Components (Bx, By, Bz) vs time, Energy flux vs time
- Purpose: Identify temporal variations in the magnetic field and energetic particle transport that may indicate substorm activity.
- Outcome: Variations in the magnetic field, particularly rapid increases in Bz, are indicative of dipolarization events associated with substorm expansion phase onset. These signatures will be used as key indicators for identifying substorm intervals.

3. Magnetic Field Distribution
- Plots: Histogram of full Bz (linear scale), Histogram of full Bz (log scale)
- Purpose: Understand the statistical distribution of magnetic field values throughout the observation period.
- Outcome: These distributions reveal the most common magnetic configurations and help identify extreme events.

4. Magnetotail Selection (Restricted Bz):
To isolate the magnetotail plasma sheet conditions, the dataset was restricted using the following criteria:
  1) X_GSM < -6 RE
  2) |Y_GSM|<|X_GSM|/2
  3) sqrt {Bx^2+By^2} < 15nT
- Plots: Histogram of restricted Bz (linear scale), Histogram of restricted Bz (log scale)
- Purpose: Filter the dataset to focus on regions of the magnetotail where reconnection and substorm activity are most likely to occur.
- The restricted dataset highlights magnetic field distributions specifically within the plasma sheet.

5. Magnetic Field Variability
- Plots: Histogram of dBz6sec (linear scale), Histogram of dBz6sec (log scale), dBz vs time
- Purpose: Examine how rapidly the magnetic field changes
- Outcome: Large values of dBz6sec indicate rapid magnetic field reconfigurations, which are characteristic of dipolarization fronts and substorm onset. These spikes will be used as a primary feature for detecting transient substorm activity and may serve as an input feature for machine learning models.

6. Magnetic Field Relationships
- Plots: 2D Color Map Full Bz vs dBz6sec (linear & log scale), 2D Color Map Restricted Bz vs dBz6sec (linear & log scale)
- Purpose: Investigate correlations between magnetic field magnitude nd rapid magnetic fluctuations.
- Outcome: These distributions reveal how frequently strong magnetic fluctuations occur under different background magnetic field conditions. This helps determine whether extreme dBz events are rare outliers or occur within specific Bz regimes, guiding threshold selection and feature engineering for substorm detection.

7. Plasma Flux Relationships
- Plots: dF/<F> PSEF vs dF/<F> PSIF, Bz vs dBz6sec with ion flux (average & median), Bz vs dBz6sec with electron flux (average & median)
- Purpose: Determine how particle flux responds to magnetic field changes
- Outcome: Enhanced particle flux during periods of strong magnetic field variation indicates particle acceleration associated with reconnection and dipolarization. These relationships help link magnetic field dynamics to plasma energization, providing additional confirmation of substorm activity.

8. Magnetic Field Geometry Effects
- Plots: By vs Bz with ion flux, d|B| vs |B| with ion flux
- Purpose: Examine how magnetic field geometry influences particle energization
- Outcome: These plots help determine whether particle flux increases during strong magnetic field gradients.

9. Plasma Properties
- Plots: Ion density histogram (linear & log scale), Electron density histogram (linear & log scale), Ion temperature anisotropy histogram (linear & log), Electron temperature anisotropy histogram (linear & log scale)
- Purpose: Characterize plasma conditions during the observation period.
- Outcome: Changes in density or temperature anisotropy may indicate plasma sheet dynamics associated with substorms.

10. Plasma Flow vs Magnetic Field
- Plots: Bz vs Vx
- Purpose: Examine how plasma flow velocity relates to the magnetic field configuration.
- Outcome: Fast earthward plasma flows (negative Vx) occurring simultaneously with increases in Bz are a hallmark of bursty bulk flows (BBFs) and flow braking. These combined signatures are strong indicators of magnetotail reconnection and will be used to identify substorm-related energy transport.
