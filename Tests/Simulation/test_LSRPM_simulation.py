# Load the machine
from os.path import join
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
import matplotlib.pyplot as plt

from pyleecan.Functions.Plot import dict_2D

from os.path import join

from numpy import ones, pi, array, linspace, cos, sqrt, zeros, exp

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.EEC_PMSM import EEC_PMSM
from pyleecan.Classes.FluxLinkFEMM import FluxLinkFEMM
from pyleecan.Classes.IndMagFEMM import IndMagFEMM
#%run -m pip install plotly # Uncomment this line to install plotly
import plotly.graph_objects as go
from plotly.offline import init_notebook_mode


def test_LSRPM_simulation():
    # Create the Simulation

    LSRPM = load(join(DATA_DIR, "Machine", "LSRPM_004.json"))
    LSRPM.plot()

    # Create a simultion
    simu_femm = Simu1(name="FEMM_simulation", machine=LSRPM)

    p = simu_femm.machine.stator.winding.p
    qs = simu_femm.machine.stator.winding.qs

    # Defining Simulation Input
    simu_femm.input = InputCurrent()

    # Rotor speed [rpm]
    simu_femm.input.N0 = 750

    # time discretization [s]
    time = linspace(
        start=0, stop=60 / simu_femm.input.N0, num=32 * p, endpoint=False
    )  # 32*p timesteps
    simu_femm.input.time = time

    # Angular discretization along the airgap circonference for flux density calculation
    simu_femm.input.angle = linspace(
        start=0, stop=2 * pi, num=2048, endpoint=False
    )  # 2048 steps

    # Stator currents as a function of time, each column correspond to one phase [A] triphase
    #I0_rms = 6.85
    felec = p * simu_femm.input.N0 / 60  # [Hz]
    rot_dir = simu_femm.machine.stator.comp_rot_dir()

    # Phi0 = 0  # Maximum Torque Per Amp

    # Ia = (

    #     I0_rms
    #     * sqrt(2)
    #     * cos(2 * pi * felec * time + 0 * rot_dir * 2 * pi / qs + Phi0)
    # )
    # Ib = (
    #     I0_rms
    #     * sqrt(2)
    #     * cos(2 * pi * felec * time + 1 * rot_dir * 2 * pi / qs + Phi0)
    # )
    # Ic = (
    #     I0_rms
    #     * sqrt(2)
    #     * cos(2 * pi * felec * time + 2 * rot_dir * 2 * pi / qs + Phi0)
    # )
    #Auxiliary
    # Id = zeros(time.shape)
    # Ie = zeros(time.shape)
    # If = zeros(time.shape)
    # simu_femm.input.Is = array([Ia, Ib, Ic, Id, Ie, If]).transpose()
    # simu_femm.input.Is = array([Ia, Ib, Ic]).transpose()

    simu_femm.mag = MagFEMM(
        type_BH_stator=0,  # 0 to use the material B(H) curve,
        # 1 to use linear B(H) curve according to mur_lin,
        # 2 to enforce infinite permeability (mur_lin =100000)
        type_BH_rotor=0,  # 0 to use the material B(H) curve,
        # 1 to use linear B(H) curve according to mur_lin,
        # 2 to enforce infinite permeability (mur_lin =100000)
        file_name="",  # Name of the file to save the FEMM model
    )

    # Definition of a sinusoidal current
 
    #I0, Phi0 to set
    I0_rms = 6.85# Maximum current [Arms]
    Phi0 = -pi/2  # MATP 
    # Compute corresponding Id/Iq
    Id_ref = (I0_rms*exp(1j*(Phi0))).real
    Iq_ref = (I0_rms*exp(1j*(Phi0))).imag
 

    # Setting the values
    simu_femm.input.Id_ref = Id_ref # [Arms]
    simu_femm.input.Iq_ref = Iq_ref # [Arms]

    print(Id_ref,Iq_ref)

    simu_femm.input.Nt_tot = 128*3 # Number of time step
    simu_femm.input.Na_tot = 2048 # Spatial discretization
    simu_femm.input.N0 = 750 # Rotor speed [rpm]

    # Only the magnetic module is defined
    # simu_femm.elec = None
    simu_femm.force = None
    simu_femm.struct = None
    simu_femm.mag.is_periodicity_a = False
    simu_femm.mag.is_periodicity_t = True
    simu_femm.mag.nb_worker = (
        16  # Number of FEMM instances to run at the same time (1 by default)
    )
    simu_femm.mag.is_get_meshsolution = (
        True  # To get FEA mesh for latter post-procesing
    )
    simu_femm.mag.is_save_meshsolution_as_file = (
        False  # To save FEA results in a dat file
    )
    out_femm = simu_femm.run()
    # Radial magnetic flux

    out_femm.mag.B.plot_2D_Data("angle", "time[0]", component_list=["radial"])
    out_femm.mag.B.plot_2D_Data("wavenumber=[0,76]", "time[0]", component_list=["radial"])
    # Tangential magnetic flux
    out_femm.mag.B.plot_2D_Data("angle","time[0]",component_list=["tangential"])
    out_femm.mag.B.plot_2D_Data("wavenumber=[0,76]","time[0]",component_list=["tangential"])
    out_femm.mag.Tem.plot_2D_Data("time")

    print(out_femm.mag.Tem.values.shape)
    print(simu_femm.input.Nt_tot)

    out_femm.mag.meshsolution.plot_contour(label="B", group_names="stator core")
    out_femm.elec.get_Is().plot_2D_Data("time", "phase", **dict_2D)
    print(out_femm.simu.machine.stator.comp_resistance_wind())




    #########################################################################################
    ##Electrical module
    # Definition of the magnetic simulation (FEMM with symmetry and sliding band)
    # simu_femm.elec = Electrical(
    # eec=EEC_PMSM(
    #     indmag=IndMagFEMM(is_periodicity_a=None, Nt_tot=50),
    #     fluxlink=FluxLinkFEMM(is_periodicity_a=None, Nt_tot=50),
    #     )
    # )
    # # Run only Electrical module

    # simu_femm.force = None
    # simu_femm.struct = None

    # out = simu_femm.run()
    # out.elec.Us.plot_2D_Data("time", "phase", **dict_2D)

    plt.show()

if __name__ == "__main__":
    test_LSRPM_simulation()
