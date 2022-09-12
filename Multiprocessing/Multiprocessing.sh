#!/bin/bash
#SBATCH --mail-user=titusnyarkonde@u.boisestate.edu
#SBATCH --time=15:00:00
#SBATCH -n 48
#SBATCH -N 4
#SBATCH --job-name=Titus
#SBATCH --output=titus.o%j
#SBATCH -p gpuq

module load slurm

python3 Multiprocessing.py >>log.out