# Plots Information

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
- Outcome: Changes in magnetic field components, especially Bz, can signal magnetic reconnection or dipolarization events.

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
- Outcome: Large dBz values indicate rapid magnetic reconfigurations that may correspond to reconnection or substorm onset.

6. Magnetic Field Relationships
- Plots: 2D Color Map Full Bz vs dBz6sec (linear & log scale), 2D Color Map Restricted Bz vs dBz6sec (linear & log scale)
- Purpose: Investigate correlations between magnetic field magnitude nd rapid magnetic fluctuations.
- Outcome: These relationships help identify magnetic conditions associated with strong field variations

7. Plasma Flux Relationships
- Plots: dF/<F> PSEF vs dF/<F> PSIF, Bz vs dBz6sec with ion flux (average & median), Bz vs dBz6sec with electron flux (average & median)
- Purpose: Determine how particle flux responds to magnetic field changes
- Outcome: Enhanced flux during strong magnetic variations may indicate particle acceleration during substorms

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
- Outcome: Fast earthward plasma flows combined with magnetic field changes are a key signature of magnetotail reconnection and substorm activity.
