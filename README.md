# COVID Spike TA Experiment

Historical exploratory data-analysis project from the COVID-19 pandemic.

The core experiment in `cov.py` applies technical-analysis-inspired transforms — especially rolling moving averages and RSI-like normalization — to public COVID time series in an attempt to visualize recurring patterns and possible spikes in cases, hospitalizations, and deaths.

This was an experimental pattern-finding exercise, not an epidemiological model, clinical tool, or validated forecasting system.

## Files

- `cov.py` — COVID-specific analysis/plotting experiment using public Tennessee and New York City data sources.
- `prpht.py` — adjacent Facebook Prophet forecasting scratchpad using S&P 500 data. Preserved because it appears to be part of the same period of forecasting experimentation, but it is not itself a COVID model.
- `verifi.py` — adjacent moving-average analysis experiment using a separate call-volume / transfer dataset. It reuses much of the same analysis structure and is archived as supporting development history rather than COVID-specific code.

## Historical notes

The scripts reflect their original exploratory state and reference APIs, datasets, and older package names that may have changed since they were written. The archive has been lightly cleaned for publication without rewriting the original approach into a modern production project.

## Dependencies

See `requirements.txt`. The Prophet script uses the historical `fbprophet` package name used at the time; current Prophet installations use the `prophet` package name and may require code changes.