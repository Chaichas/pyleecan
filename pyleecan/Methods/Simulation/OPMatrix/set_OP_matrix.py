from numpy import exp
from ....Methods.Simulation.OPMatrix import OPMatrixException


def set_OP_matrix(self, OP_matrix, *arg_list):
    """Set the OP_matrix by identifying the columns
    Ex: set_OP_matrix(OP_matrix, "N0", "Iq", "Iq", "Tem")
    set_OP_matrix(OP_matrix) calls set_OP_matrix(OP_matrix, "N0", "Id", "Iq", "Tem", "Pem")
    I0/Phi0 are converted to Id, Iq, U0/UPhi0 are converted to Ud, Uq

    Parameters
    ----------
    self : OPMatrix
        OPMatrix object to update
    OP_matrix : ndarray
        OP_matrix to set in the object
    *arg_list : list of str
        arguments to specify the OP_matrix columns name
    """

    # Clean previous data
    self._set_None()

    # Extract arg_list it the function called from another script with *arg_list
    if len(arg_list) == 1 and type(arg_list[0]) == tuple:
        arg_list = arg_list[0]

    # Setup default argument (N0, Id, Iq, Tem, Pem)
    if len(arg_list) == 0:
        N = OP_matrix.shape[1]
        if N > 0:
            arg_list.append("N0")
        if N > 1:
            arg_list.append("Id")
        if N > 2:
            arg_list.append("Iq")
        if N > 3:
            arg_list.append("Tem")
        if N > 4:
            arg_list.append("Pem")
    if len(arg_list) == 3 and OP_matrix.shape[1] >= 4:
        arg_list.append("Tem")
    if len(arg_list) == 4 and OP_matrix.shape[1] == 5:
        arg_list.append("Pem")
    if len(arg_list) != OP_matrix.shape[1]:
        raise OPMatrixException(
            "Error missing column name for OP_matrix.set_OP_matrix, "
            + str(OP_matrix.shape[1])
            + " expected "
            + str(arg_list)
        )

    arg_list_lower = [arg.lower() for arg in arg_list]
    # Convertion I0/Phi0 to Id/Iq
    if "i0" in arg_list_lower and (
        "phi0" in arg_list_lower or "iphi0" in arg_list_lower
    ):
        I0_index = arg_list_lower.index("i0")
        if "phi0" in arg_list_lower:
            Phi0_index = arg_list_lower.index("phi0")
        else:
            Phi0_index = arg_list_lower.index("iphi0")
        I0 = OP_matrix[:, I0_index]
        Phi0 = OP_matrix[:, Phi0_index]
        Z = I0 * exp(1j * Phi0)
        OP_matrix[:, I0_index] = Z.real
        OP_matrix[:, Phi0_index] = Z.imag
        arg_list[I0_index] = "Id"
        arg_list[Phi0_index] = "Iq"

    # Convertion U0/UPhi0 to Ud/Uq
    if "u0" in arg_list_lower and "uphi0" in arg_list_lower:
        U0_index, UPhi0_index = (
            arg_list_lower.index("u0"),
            arg_list_lower.index("uphi0"),
        )
        U0 = OP_matrix[:, U0_index]
        UPhi0 = OP_matrix[:, UPhi0_index]
        Z = U0 * exp(1j * UPhi0)
        OP_matrix[:, U0_index] = Z.real
        OP_matrix[:, UPhi0_index] = Z.imag
        arg_list[U0_index] = "Ud"
        arg_list[UPhi0_index] = "Uq"

    # Set column by column according to arg_list
    for ii in range(OP_matrix.shape[1]):
        if arg_list[ii].lower() in ["n0", "no", "0n", "on"]:
            self.N0 = OP_matrix[:, ii]
        elif arg_list[ii].lower() in ["id", "di", "id_ref"]:
            self.Id_ref = OP_matrix[:, ii]
        elif arg_list[ii].lower() in ["iq", "qi", "iq_ref"]:
            self.Iq_ref = OP_matrix[:, ii]
        elif arg_list[ii].lower() in ["tem", "t", "tem_av", "tem_av_ref"]:
            self.Tem_av_ref = OP_matrix[:, ii]
        elif arg_list[ii].lower() in ["pem", "p", "pem_av", "pem_av_ref"]:
            self.Pem_av_ref = OP_matrix[:, ii]
        elif arg_list[ii].lower() in ["ud", "du", "ud_ref"]:
            self.Ud_ref = OP_matrix[:, ii]
        elif arg_list[ii].lower() in ["uq", "qu", "uq_ref"]:
            self.Uq_ref = OP_matrix[:, ii]
        else:
            raise OPMatrixException(
                "Error in OP_matrix.set_OP_matrix, unknow column name for index "
                + str(ii)
                + " in "
                + str(arg_list)
            )