
import os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

def get_modelpath(envid):
    """
    to create a path to save the data from the network that we will analize.
    """
    # Make a local file directories
    path = Path('.') / 'files'
    os.makedirs(path, exist_ok=True)
    path = path / envid
    os.makedirs(path, exist_ok=True)
    
    return path

def plot_trials_timestep(inputs, actions, gt, perf, env_kwargs, reward=None):
    inputs = np.array(inputs)
    actions = np.array(actions)
    gt = np.array(gt)
    perf = np.array(perf)
    reward = np.array(reward)   
    # Plot first 40 steps
    num_steps = 20
    f, ax = plt.subplots(ncols=1, nrows=3, figsize=(8, 4), dpi=150, sharex=True)

    ax[0].plot(np.arange(1, num_steps+1)*env_kwargs['dt'], inputs[:num_steps, 0], label='Fixation')
    ax[0].plot(np.arange(1, num_steps+1)*env_kwargs['dt'], inputs[:num_steps, 1], label='Stim. L.')
    ax[0].plot(np.arange(1, num_steps+1)*env_kwargs['dt'], inputs[:num_steps, 2], label='Stim. R.')
    ax[0].set_ylabel('Inputs')
    ax[0].legend()
    ax[1].plot(np.arange(1, num_steps+1)*env_kwargs['dt'], gt[:num_steps], label='Targets', color='k')
    ax[1].plot(np.arange(1, num_steps+1)*env_kwargs['dt'], actions[:num_steps], label='Choice', linestyle='--')
    ax[1].set_ylabel('Actions / Targets')
    ax[1].legend()
    ax[2].plot(np.arange(1, num_steps+1)*env_kwargs['dt'], perf[:num_steps], label='Accuracy')
    if reward is not None:
        ax[2].plot(np.arange(1, num_steps+1)*env_kwargs['dt'], reward[:num_steps], label='reward')
    ax[2].set_ylabel('Performance')
    ax[1].legend()
    ax[2].set_xlabel('Time (ms)')

def plot_trial_sequence(correct_choice, block):
    
    # Plot correct choice
    f = plt.figure(figsize=(8, 4), dpi=150)
    plt.plot(np.arange(1, len(correct_choice)+1), correct_choice, label='Correct choice')
    plt.plot(np.arange(1, len(correct_choice)+1), np.array(block)+1, '--', label='Block')
    plt.xlabel('Trial')
    plt.ylabel('Correct choice')
    plt.legend()    