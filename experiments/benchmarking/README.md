# Benchmark RL Agents on CARL
Framework: coax.

## Runcommands
Local debugging
```bash
 python experiments/benchmarking/run_training.py max_num_frames=25000 '+environments/classic_control=pendulum' '+context_visibility=hidden' 'wandb.debug=true'
```

Example for slurm
```bash
 python experiments/benchmarking/run_training.py max_num_frames=25000 '+environments/classic_control=pendulum' '+context_visibility=hidden' 'wandb.debug=true' 'seed=range(1,11)' '+slurm=cpushort' -m
```

## Command Pieces

### Context Feature Args
Pendulum
```bash
'context_sampler.context_feature_names=[],[m, l, g, dt, max_speed],[m],[g],[l],[dt],[max_speed]'
```

### Context Sampling
Relative standard deviation
```bash
'context_sampler.sigma_rel=0.1,0.25,0.5'
```

### Context Visibility
```bash
'+context_visibility=hidden,cgate,visible_all,visible_changing'
```


## Experiment Plan
- [ ] SAC hidden, visible full, visible change only, SAC cGate, on CARLPendulum with 0.1, 0.25, 0.5 for all single context features + all context features at once
```bash
python experiments/benchmarking/run_training.py '+environments/classic_control=pendulum' 'seed=range(1,11)' '+context_visibility=hidden,cgate,visible_all,visible_changing' 'context_sampler.context_feature_names=[],[m, l, g, dt, max_speed],[m],[g],[l],[dt],[max_speed]' 'context_sampler.sigma_rel=0.1,0.25,0.5' '+slurm=cpushort' 'hydra.launcher.timeout_min=240' -m
```
280 combinations
Status: running

- [ ] SAC hidden, SAC cGate on LunarLander planet contexts
```bash
'environments/box2d=lunarlander' '+context_visibility=hidden,cgate'
```
- [ ] SAC hidden, SAC cGate on walker 0.1 for all context features + all context features at once
- [ ] SAC hidden, SAC cGate on quadruped 0.1 for all context features + whichever combination is manageable
- [ ] SAC hidden, SAC cGate on fish 0.1 for all context features + all context features at once
- [ ] SAC hidden, SAC cGate on CartPole with train and test dists for the Kirk experiment (gravity + pole_length)
- [ ] SAC hidden, SAC cGate Mario with only one context dist
- [ ] Some brax env?
- [ ] LSTM baseline for whatever makes sense


## Experiment Preparations
Find HPs for
- [x] Pendulum (SAC)
```bash
 python experiments/benchmarking/run_training.py max_num_frames=25000 '+environments/classic_control=pendulum' '+context_visibility=hidden' 'wandb.debug=true' 
```
- [ ] LunarLander
```bash
 python experiments/benchmarking/run_training.py max_num_frames=25000 '+environments/box2d=lunarlander' '+context_visibility=hidden' 'wandb.debug=true' '+algorithm=c51'
```
- [ ] Walker
```bash
 python experiments/benchmarking/run_training.py max_num_frames=25000 '+environments/dmc=walker' '+context_visibility=hidden' 'wandb.debug=true'
```
- [ ] Quadruped
```bash
 python experiments/benchmarking/run_training.py max_num_frames=25000 '+environments/dmc=quadruped' '+context_visibility=hidden' 'wandb.debug=true'
```
- [ ] Fish
```bash
 python experiments/benchmarking/run_training.py max_num_frames=25000 '+environments/dmc=fish' '+context_visibility=hidden' 'wandb.debug=true'
```
- [ ] Mario
```bash
 python experiments/benchmarking/run_training.py max_num_frames=25000 '+environments/misc=mario' '+context_visibility=hidden' 'wandb.debug=true'
```


- [ ] Kirk distr.
- [ ] LunarLander contexts --> Option to read contexts from file