##%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm
import pandas as pd

data = pd.read_csv('/home/centos/bloop/temp.csv')
print data[['m_code', 'e_hydro', 'm_hydro']].head()

m_code = data.m_code.unique()
e_hydro = data['e_hydro'].values
n_code = len(data.m_code.unique())

indiv_traces = {}
for i in m_code:
    # Select subset of data belonging to county
    c_data = data.ix[data.m_code == i]
    c_log_hydro = c_data.e_hydro
    c_floor_measure = c_data.m_code.values

    with pm.Model() as individual_model:
        # Intercept prior (variance == sd**2)
        a = pm.Normal('alpha', mu=0, sd=100**2)
        # Slope prior
        b = pm.Normal('beta', mu=0, sd=100**2)

        # Model error prior
        eps = pm.Uniform('eps', lower=0, upper=100)

        # Linear model
        radon_est = a + b * c_floor_measure
        print radon_est
        # Data likelihood
        radon_like = pm.Normal('radon_like', mu=radon_est, sd=eps, observed=c_log_hydro)
#        Inference button (TM)!
#        step = pm.NUTS()
#        trace = pm.sample(2000, step=step, progressbar=False)

    # keep trace for later analysis
#    indiv_traces[i] = trace
