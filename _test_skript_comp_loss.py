# --- Load Machine ------------------------------------------------------------------- #
# Change of directory to have pyleecan in the path
# from os import chdir
# chdir('..')

from pyleecan.Functions.load import load
from pyleecan.Classes.SolutionData import SolutionData
from numpy import abs, cos, pi, linspace, array

from SciDataTool import Data1D, DataTime
from SciDataTool.Functions.parser import read_input_strings

# Import the results
myResults = load("MyResults.json")

mySimu = myResults.simu
machine = mySimu.machine

print("Results loaded")

# --- Setup the Loss Model ----------------------------------------------------------- #
from pyleecan.Classes.Loss1 import Loss1
from pyleecan.Classes.LossModel import LossModel
from pyleecan.Classes.LossModelBertotti import LossModelBertotti
from pyleecan.Classes.ImportMatrixXls import ImportMatrixXls


myLossModel = LossModelBertotti()
mySimu.loss = Loss1()
mySimu.loss.lam_stator = myLossModel

myLossModel.k_hy = None
myLossModel.alpha_hy = 2
myLossModel.k_ed = None
myLossModel.alpha_ed = 2
myLossModel.k_ex = 0
myLossModel.alpha_ex = 1.5

LossData = ImportMatrixXls()
# LossData.file_path = "pyleecan\\pyleecan\\Data\\Material\\M400-50A.xlsx"
LossData.file_path = "pyleecan\\Data\\Material\\M400-50A.xlsx"
LossData.is_transpose = False
LossData.sheet = "LossData"
LossData.skiprows = 2
LossData.usecols = None

machine.stator.mat_type.mag.LossData = LossData

# --- Run the Loss Simulation -------------------------------------------------------- #
myLoss = mySimu.loss
myLoss.run()

myResults.mag.meshsolution.plot_contour(label='B', group_names='stator', itime=0, clim=[0, 1.5])
myResults.mag.meshsolution.plot_contour(label='LossDens', group_names='stator', itime=7,)

print(f"stator loss = {myResults.loss.Plam_stator[0]} W")