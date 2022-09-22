#!/bin/bash
#Account and Email Information
#SBATCH -A tnde  ## User ID
#SBATCH --mail-type=end
#SBATCH --mail-user=titusnyarkonde@u.boisestate.edu
# Specify parition (queue)
#SBATCH --partition=gpuq
# Join output and errors into output.
#SBATCH -o titus.o%j
#SBATCH -e titus.e%j
# Specify job not to be rerunable.
#SBATCH --no-requeue
# Job Name.
#SBATCH --job-name="DK14_mse"
# Specify walltime.
###SBATCH --time=48:00:00
# Specify number of requested nodes.
#SBATCH -N 4
# Specify the total number of requested procs:
#SBATCH -n 48
# Number of GPUs per node.
#SBATCH --gres=gpu:1
# load all necessary modules.
module load slurm
module load anaconda/anaconda3/5.1.0
# conda activate mass_cal2
# Echo commands to stdout (standard output).
set -x
# Copy your code & data to your R2 Home directory using
# the SFTP (secure file transfer protocol).
# Go to the directory where the actual BATCH file is present.
cd /home/tnde/P1_Density_Calibration/Density3D
# The �python� command runs your python code.
# All output is dumped into titus.o%j with �%j� replaced by the Job ID.
## The file Multiprocessing.py must also 
## be in $/home/tnde/P1_Density_Calibration/Density3D
python3 Multiprocessing.py >>log.out


