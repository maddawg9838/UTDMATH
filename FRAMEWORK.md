# TEAM ACTION PLAN
For this semester, our project will focus on: Identifying physically meaningful magnetic and plasma patterns that precede large directional fluctuations in elementary particle fluxes in the restricted dataset.

**Phase 1. Re-establish the foundation***
	1. Lock the dataset and scope:
	Use the restricted dataset as the main working dataset.
	Tasks:
	- confirm the exact time range being analyzed,
	- confirm the exact restriction criteria,
	- list all variables currently in the working matrix,
	- document all derived quantities already created.
	
  2. Define variables:
	Look at TERMINOLOGY_INFORMATION.md

**Phase 2. Separate real structure from garbage-data**
	3. Benchmark only on the restricted dataset
	Use the restricted dataset first because it is the best-understood subset.
	Tasks:
	- reproduce the main 1D and 2D plots only for the restricted data,
	- interpreting the full dataset when restricted-data behavior is better understood.

  4. Use histograms and 2D count maps to identify repeatable behavior
	Focus on plots such as:
	- Bz histogram
	- dBz6sec histogram
	- Bz vs dBz6sec 2D count map
	- Bz vs flux change
	- dBz6sec vs flux change
	- Vx vs dBz6sec
	- density vs flux change
  Purpose:
	- identify dense, repeatable regions that likely represent real physics,
	- identify sparse, isolated extremes that may be corruption, sensor error, or non-repeatable noise.

  5. Check suspicious extremes in time series
	Whenever an extreme point appears in a histogram or 2D map, inspect the corresponding time series window around it.
	Tasks:
	- select several extreme cases,
	- inspect nearby B-field, flux, position, and related variables,
	- determine whether the behavior looks physically consistent or instrument-like.

**Phase 3. Define a modest event target**
	6. Choose one event definition
	Before doing prediction or ML, define one simple, concrete target.
	Possible examples:
	- large increase in ion flux in a chosen direction,
	- large increase in electron flux,
	- large fluctuation in dBz6sec accompanied by supporting behavior,
	- dipolarization-like interval in the restricted dataset.
	Important: the event definition should be mathematical and reproducible, not just visual.
	For example, define:
	- threshold,
	- time window,
	- minimum duration,
	- exclusion criteria,
	- whether neighboring points are merged into one event.

  7. Decide what are predictors and what is the response
	For every candidate variable, state whether it is:
	- a response,
	- a precursor,
	- a concurrent measurement,
	- or possibly a consequence of the event.
	This is necessary so that we do not treat the event definition itself as its own predictor.

**Phase 4. Search for precursor patterns**
	8. Study what happens before the defined event
	Once an event is defined, examine preceding behavior.
	Tasks:
	- build fixed windows before each event,
	- compare event windows vs non-event windows,
	- examine averages, distributions, and 2D maps of preceding conditions.
	
  9. Use aggregated statistics first, then time series confirmation
	Workflow:
	- first find robust patterns in binned or averaged data,
	- then verify those patterns in raw time series around selected cases.
	This follows the guidance that integrated quantities are more robust than noisy time series alone.

**Phase 5. External data only if physically justified**
	10. Postpone external datasets until mapping is clear
	DSCOVR, SOPHIE, AE, and other sources can be considered later, but only if the team can explain:
	- what quantity they provide,
	- how it relates physically to the current THA observations,
	- whether the timescales and event definitions match,
	- whether they are measured in comparable regions or contexts.
  Immediate rule: do not add an external dataset unless there is a justification.

**Phase 6. Machine learning only after labels are credible**
	11. Delay ML until event labels and noise filtering are ready
	Machine learning is allowed, but only after:
	- event definition is fixed,
	- bad-data screening is in place,
	- predictor/response roles are clear,
	- benchmark plots support that the target is physically meaningful.

  12. Start simple when ML begins
	Recommended order:
		1.	logistic regression
		2.	random forest
		3.	LSTM only later, if the sequential structure is well defined

