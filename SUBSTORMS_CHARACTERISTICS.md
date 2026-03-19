# Expected Substorm Signatures in the Data
These observables represent measurable signatures in satellite and ground-based data that indicate the onset and evolution of magnetospheric substorms, and will be used to guide both statistical analysis and machine learning feature selection.

**Substorm Onset**: The time marking the beginning of the expansion phase
- **Observable Signature**: Sudden auroral brightening and rapid changes in magnetic and plasma parameters

**Dipolarization**: A rapid transition of the magnetic field from a stretched (tail-like) to a more dipole-like configuration
- **Observable Signature**: Sharp increase in Bz (northward turning) and spikes in dBz

**dBz Spikes (Magnetic Field Variability)**: Rapid temporal changes in the north-south magnetic field component
- **Observable Signature**: Large values in dBz6sec, often coinciding with substorm onset and dipolarization

**Busrty Bulk Flows (BBFs)**: Short-duration, high-speed plasma flows moving earthward in the plasma sheet
- **Observable Signature**: Sudden increase in earthward velocity (Vx), often correlated with dipolarization

**Flow Braking**: The deceleration of BBFs closer to Earth, leading to energy conversion and magnetic field reconfiguration
- **Observable Signature**: Decrease in Vx with simultaneous increase in Bz and particle energization

**Plasma Sheet Thinning**: Reduction in the vertical thickness of the plasma sheet during the growth phase
- **Observable Signature**: Decrease in particle flux and density at a fixed satellite location

**Energetic Particle Injection**: Rapid increase in energetic electron and ion fluxes during substorm expansion
- **Observable Signature**: Spikes in dF/PSEF (electrons) and dF/PSIF (ions)

**Auroral Electrojet Intensification (AE/SML Increase)**: Strengthening of ionospheric currents during substorms
- **Observable Signature**: Sharp increase in AE or decrease (more negative) in SML index

**Southward IMF (Bz < 0)**: Condition that enhances magnetic reconnection and energy loading into the magnetotail
- **Observable Signature**: Sustained negative Bz prior to substorm onset

**Magnetic Reconnection (Near-Earth Neutral Line)**: Process where magnetic field lines break and reconnect, releasing stored energy
- **Observable Signature**: Associated with BBFs, dipolarization, and energetic particle injections
