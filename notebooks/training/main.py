import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import matplotlib.ticker as mticker
import pyspedas

# Defined time range
start = '2014-7-01'
end = '2015-1-01'

# Magnetic field (Bz)
themis.fgm(trange=[start, end], probe='a', level='l2', coord='gsm', get_support_data=False)

# Step 1: Build Matrix M with Magnetic field Base
fgm_var = get_data('tha_fgs_gsm')

times_fgm = fgm_var[0]
B = fgm_var[1]

matrix_M = pd.DataFrame({
    'time': pd.to_datetime(times_fgm, unit='s'),
    'Bx': B[:,0],
    'By': B[:,1],
    'Bz': B[:,2]
})

# Download Spacecraft Position (STATE) Data
state_files = themis.state(
    trange=[start, end],
    level='l1',
    probe='a',
    varnames=['tha_pos_gsm']
)

# Step 2: Get spacecraft position
pos_var = get_data('tha_pos_gsm')

# Access the tuple
times_pos = pos_var[0]  # timestamps
pos = pos_var[1]        # Nx3 array: X, Y, Z in GSM

# Convert position times to seconds since epoch
times_pos_sec = times_pos  # already in seconds, like FGM timestamps
times_fgm_sec = matrix_M['time'].astype(np.int64) / 1e9  # convert ns -> s

# Step 3: Interpolate the Location data to the Magnetic field TIMESTAMPS
# Create arrays for X, Y, Z at FGM timestamps
X_interp = np.interp(times_fgm_sec, times_pos_sec, pos[:,0])
Y_interp = np.interp(times_fgm_sec, times_pos_sec, pos[:,1])
Z_interp = np.interp(times_fgm_sec, times_pos_sec, pos[:,2])

# Add to your DataFrame
matrix_M['X'] = X_interp
matrix_M['Y'] = Y_interp
matrix_M['Z'] = Z_interp

# Step 4: Compute dBz6sec
Bz = matrix_M['Bz'].values
dBz6sec = np.full_like(Bz, np.nan)
dBz6sec[1:-1] = Bz[2:] - Bz[:-2]

matrix_M['dBz6sec'] = dBz6sec

# Ion flux (SST)
themis.sst(trange=[start, end], probe='a', level='l2', varnames=['tha_psif_en_eflux', 'tha_psef_en_eflux'], get_support_data=False)

# Step 5: Get Flux changes for Ions and Electrons
# Get PSIF data
psif_var = get_data('tha_psif_en_eflux')

# Get PSEF data
psef_var = get_data('tha_psef_en_eflux')

# Step 6: Interpolate F and dF onto matrix_M time base
t_M = matrix_M['time'].astype(np.int64) / 1e9

# Get Channel #5 = index 4
F_psif = psif_var[1][:, 4]
t_psif = psif_var[0]

F_psef = psef_var[1][:, 4]
t_psef = psef_var[0]

# Interpolate both onto t_M
matrix_M['PSIF_ch5'] = np.interp(t_M, t_psif, F_psif)
matrix_M['PSEF_ch5'] = np.interp(t_M, t_psef, F_psef)

# Step 7: Calculate dF/<F> Relative Flux Change
# PSIF
dF_psif = np.full_like(F_psif, np.nan)
dF_psif[1:-1] = F_psif[2:] - F_psif[:-2]
matrix_M['dPSIF_ch5'] = np.interp(t_M, t_psif, dF_psif)

matrix_M['PSIF_mean'] = np.nan
matrix_M.iloc[1:-1, matrix_M.columns.get_loc('PSIF_mean')] = (
    matrix_M['PSIF_ch5'].iloc[2:].values +
    matrix_M['PSIF_ch5'].iloc[:-2].values
) / 2
matrix_M['rel_PSIF'] = matrix_M['dPSIF_ch5'] / matrix_M['PSIF_mean']

# PSEF
dF_psef = np.full_like(F_psef, np.nan)
dF_psef[1:-1] = F_psef[2:] - F_psef[:-2]
matrix_M['dPSEF_ch5'] = np.interp(t_M, t_psef, dF_psef)

matrix_M['PSEF_mean'] = np.nan
matrix_M.iloc[1:-1, matrix_M.columns.get_loc('PSEF_mean')] = (
    matrix_M['PSEF_ch5'].iloc[2:].values +
    matrix_M['PSEF_ch5'].iloc[:-2].values
) / 2
matrix_M['rel_PSEF'] = matrix_M['dPSEF_ch5'] / matrix_M['PSEF_mean']

# Download Plasma Data (ESA)
themis.esa(trange=[start, end], probe='a', level='l2',
           varnames=['tha_peir_density', 'tha_peir_velocity_gsm',
                     'tha_peir_t3', 'tha_peir_magf', 'tha_peir_epoch',
                     'tha_peer_density', 'tha_peer_velocity_gsm',
                     'tha_peer_t3', 'tha_peer_magf', 'tha_peer_epoch'],
           get_support_data=False)

# Ions
ion_density_var = get_data('tha_peir_density')
ion_velocity_var = get_data('tha_peir_velocity_gsm')
ion_T3_var = get_data('tha_peir_t3')
ion_B_var = get_data('tha_peir_magf')

ion_time = ion_density_var.times
ion_density = ion_density_var.y

ion_velocity = ion_velocity_var.y
ion_T3 = ion_T3_var.y
ion_B = ion_B_var.y

# Electrons
elec_density_var = get_data('tha_peer_density')
elec_velocity_var = get_data('tha_peer_velocity_gsm')
elec_T3_var = get_data('tha_peer_t3')
elec_B_var = get_data('tha_peer_magf')

elec_time = elec_density_var.times
elec_density = elec_density_var.y

elec_velocity = elec_velocity_var.y
elec_T3 = elec_T3_var.y
elec_B = elec_B_var.y

ion_Tpar, ion_Tperp = compute_Tpar_Tperp_diag(ion_T3, ion_B)
elec_Tpar, elec_Tperp = compute_Tpar_Tperp_diag(elec_T3, elec_B)

ion_Ae = (ion_Tperp / ion_Tpar) - 1
elec_Ae = (elec_Tperp / elec_Tpar) - 1

# Task 2: Add downloaded and processes plasma data to Matrix M
# Convert matrix_M times to seconds
t_M_sec = matrix_M['time'].astype(np.int64) / 1e9

# Ions
matrix_M['Ion_density'] = np.interp(t_M_sec, ion_time, ion_density)
matrix_M['Ion_Vx'] = np.interp(t_M_sec, ion_time, ion_velocity[:,0])
matrix_M['Ion_Vy'] = np.interp(t_M_sec, ion_time, ion_velocity[:,1])
matrix_M['Ion_Vz'] = np.interp(t_M_sec, ion_time, ion_velocity[:,2])
matrix_M['Ion_Tpar'] = np.interp(t_M_sec, ion_time, ion_Tpar)
matrix_M['Ion_Tperp'] = np.interp(t_M_sec, ion_time, ion_Tperp)
matrix_M['Ion_Ae'] = np.interp(t_M_sec, ion_time, ion_Ae)

# Electrons
matrix_M['Elec_density'] = np.interp(t_M_sec, elec_time, elec_density)
matrix_M['Elec_Vx'] = np.interp(t_M_sec, elec_time, elec_velocity[:,0])
matrix_M['Elec_Vy'] = np.interp(t_M_sec, elec_time, elec_velocity[:,1])
matrix_M['Elec_Vz'] = np.interp(t_M_sec, elec_time, elec_velocity[:,2])
matrix_M['Elec_Tpar'] = np.interp(t_M_sec, elec_time, elec_Tpar)
matrix_M['Elec_Tperp'] = np.interp(t_M_sec, elec_time, elec_Tperp)
matrix_M['Elec_Ae'] = np.interp(t_M_sec, elec_time, elec_Ae)

# OMNI AE index
load(trange=[start, end], level='hro', varnames=['AE_INDEX'], get_support_data=False)

# Task 5: Add AE Index to Matrix M
ae = get_data('AE_INDEX')

ae_time = ae[0]
ae_values = ae[1]

matrix_M['AE'] = np.interp(
    t_M_sec,
    ae_time,
    ae_values
)


