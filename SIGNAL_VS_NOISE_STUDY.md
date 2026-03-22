# Purpose
In this section, we explore the signal vs noise for events in the M dataset. Noise represents extreme measurements in the dataset events which can occur due to corrupted hardware, inaccurate tracking, and data transmission difficulties. It is important to separate noisy events from actual physical events (signal) so that our research is based on true, significant data.

# Bz and dBz6sec Univariate Distributions
<img width="1590" height="790" alt="0d899e69-fbc5-4482-b8a8-c4185799c2ee" src="https://github.com/user-attachments/assets/1a69f2cc-1d68-41fb-ade8-48946888475e" />
The Bz distributon for the full dataset shows significant noise in the dataset. There is a steep decrease in the number of points from 0 to 500 but after this decrease, there is a consistent floor of values extending to 25000 nT. We would expect the number of points to continue decaying. Therefore, the values for Bz are most likely being filled in the dataset as placeholders. As shown later, the restricted dataset does not have this floor as the counts decay, showing that the restricted filter selects physically relevant events and implicitly rejects the noisy points.

<img width="989" height="590" alt="22ad7750-1d7a-4160-b927-ccfd79f01e01" src="https://github.com/user-attachments/assets/cfa13ee5-afb3-4c29-87fc-619f4969d40b" />
From the above visualization, we can observe that there is a long right tail which extends past 50 nT in the log scale. There are counts in the thousands past 60+ nT which is unusually high in the near-Earth plasma sheet. There are either strong magnetic field events past 60 nT or these are events which need to be closely examined. There are also a small number of negative Bz points which will be examined further with 2D Heatmaps to see if these points are unusual. 

<img width="1590" height="592" alt="94faf7fb-8add-4148-a4b0-4b1360a03484" src="https://github.com/user-attachments/assets/301775a0-6310-41c4-8419-6bb15cbfef62" />
The visualization above provides further proof for eliminating the large Bz values which are only relevant for the near-earth dipole field. For our research, it is important to analyze events with Bz less than approximately 100 nT as we are focused on patterns near the Earth's magnetotail. The restricted filter takes care of this but there can still be noise which will be analyzed with 2D Distributions.

<img width="1189" height="590" alt="f1836839-c0b3-4882-90ce-90d96b83b323" src="https://github.com/user-attachments/assets/301dcfca-ebf5-47fa-83a2-975be26c280e" />
The dBz6sec distribution for the full dataset follows a similar pattern to that of the Bz distribution. As the dBz6sec values extend to +/- 50 nT, there is a constant floor present for the number of points rather than decaying to zero. This floor pattern provides support for non-physical events occuring at extreme values for dBz6sec.

<img width="1189" height="590" alt="69249adc-2ab6-432f-9ede-8ce17a749bcd" src="https://github.com/user-attachments/assets/b72f26c6-54ec-42dc-9075-81d337392e1b" />
The dBz6sec distributon for the restricted dataset shows a steeper decay to single digit counts as the dBz6sec values extend to +/- 30 nT. There is no flat noise floor present showing that the restricted filter selects physically relevant events and implicitily rejects noisy points. There are still extreme values of Bz which need to be analyzed with 2D Distributions. 

# 2D Distributions: Bz vs dBz6sec
<img width="1574" height="1377" alt="image" src="https://github.com/user-attachments/assets/f0c02036-7988-408c-859a-feefcb341c28" />
<img width="1566" height="1377" alt="image" src="https://github.com/user-attachments/assets/38b75d89-452e-4484-bcde-5fec5d777456" />
