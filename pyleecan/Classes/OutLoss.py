# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutLoss.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutLoss
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Output.OutLoss.get_loss import get_loss
except ImportError as error:
    get_loss = error

try:
    from ..Methods.Output.OutLoss.get_loss_lam import get_loss_lam
except ImportError as error:
    get_loss_lam = error

try:
    from ..Methods.Output.OutLoss.get_loss_winding import get_loss_winding
except ImportError as error:
    get_loss_winding = error

try:
    from ..Methods.Output.OutLoss.get_loss_magnet import get_loss_magnet
except ImportError as error:
    get_loss_magnet = error

try:
    from ..Methods.Output.OutLoss.get_loss_dist import get_loss_dist
except ImportError as error:
    get_loss_dist = error


from ._check import InitUnKnowClassError


class OutLoss(FrozenClass):
    """Gather the loss module outputs"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Output.OutLoss.get_loss
    if isinstance(get_loss, ImportError):
        get_loss = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutLoss method get_loss: " + str(get_loss))
            )
        )
    else:
        get_loss = get_loss
    # cf Methods.Output.OutLoss.get_loss_lam
    if isinstance(get_loss_lam, ImportError):
        get_loss_lam = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLoss method get_loss_lam: " + str(get_loss_lam)
                )
            )
        )
    else:
        get_loss_lam = get_loss_lam
    # cf Methods.Output.OutLoss.get_loss_winding
    if isinstance(get_loss_winding, ImportError):
        get_loss_winding = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLoss method get_loss_winding: "
                    + str(get_loss_winding)
                )
            )
        )
    else:
        get_loss_winding = get_loss_winding
    # cf Methods.Output.OutLoss.get_loss_magnet
    if isinstance(get_loss_magnet, ImportError):
        get_loss_magnet = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLoss method get_loss_magnet: " + str(get_loss_magnet)
                )
            )
        )
    else:
        get_loss_magnet = get_loss_magnet
    # cf Methods.Output.OutLoss.get_loss_dist
    if isinstance(get_loss_dist, ImportError):
        get_loss_dist = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLoss method get_loss_dist: " + str(get_loss_dist)
                )
            )
        )
    else:
        get_loss_dist = get_loss_dist
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        lamination=-1,
        winding=-1,
        magnet=-1,
        meshsolution=-1,
        logger_name="Pyleecan.OutLoss",
        mech=-1,
        misc=-1,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "lamination" in list(init_dict.keys()):
                lamination = init_dict["lamination"]
            if "winding" in list(init_dict.keys()):
                winding = init_dict["winding"]
            if "magnet" in list(init_dict.keys()):
                magnet = init_dict["magnet"]
            if "meshsolution" in list(init_dict.keys()):
                meshsolution = init_dict["meshsolution"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "mech" in list(init_dict.keys()):
                mech = init_dict["mech"]
            if "misc" in list(init_dict.keys()):
                misc = init_dict["misc"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.lamination = lamination
        self.winding = winding
        self.magnet = magnet
        self.meshsolution = meshsolution
        self.logger_name = logger_name
        self.mech = mech
        self.misc = misc

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutLoss_str = ""
        if self.parent is None:
            OutLoss_str += "parent = None " + linesep
        else:
            OutLoss_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutLoss_str += (
            "lamination = "
            + linesep
            + str(self.lamination).replace(linesep, linesep + "\t")
            + linesep
        )
        OutLoss_str += (
            "winding = "
            + linesep
            + str(self.winding).replace(linesep, linesep + "\t")
            + linesep
        )
        OutLoss_str += (
            "magnet = "
            + linesep
            + str(self.magnet).replace(linesep, linesep + "\t")
            + linesep
        )
        OutLoss_str += (
            "meshsolution = "
            + linesep
            + str(self.meshsolution).replace(linesep, linesep + "\t")
            + linesep
        )
        OutLoss_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        OutLoss_str += (
            "mech = "
            + linesep
            + str(self.mech).replace(linesep, linesep + "\t")
            + linesep
        )
        OutLoss_str += (
            "misc = "
            + linesep
            + str(self.misc).replace(linesep, linesep + "\t")
            + linesep
        )
        return OutLoss_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.lamination != self.lamination:
            return False
        if other.winding != self.winding:
            return False
        if other.magnet != self.magnet:
            return False
        if other.meshsolution != self.meshsolution:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.mech != self.mech:
            return False
        if other.misc != self.misc:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        OutLoss_dict = dict()
        OutLoss_dict["lamination"] = (
            self.lamination.copy() if self.lamination is not None else None
        )
        OutLoss_dict["winding"] = (
            self.winding.copy() if self.winding is not None else None
        )
        OutLoss_dict["magnet"] = self.magnet.copy() if self.magnet is not None else None
        OutLoss_dict["meshsolution"] = (
            self.meshsolution.copy() if self.meshsolution is not None else None
        )
        OutLoss_dict["logger_name"] = self.logger_name
        OutLoss_dict["mech"] = self.mech.copy() if self.mech is not None else None
        OutLoss_dict["misc"] = self.misc.copy() if self.misc is not None else None
        # The class name is added to the dict for deserialisation purpose
        OutLoss_dict["__class__"] = "OutLoss"
        return OutLoss_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.lamination = None
        self.winding = None
        self.magnet = None
        self.meshsolution = None
        self.logger_name = None
        self.mech = None
        self.misc = None

    def _get_lamination(self):
        """getter of lamination"""
        return self._lamination

    def _set_lamination(self, value):
        """setter of lamination"""
        if type(value) is int and value == -1:
            value = list()
        check_var("lamination", value, "list")
        self._lamination = value

    lamination = property(
        fget=_get_lamination,
        fset=_set_lamination,
        doc=u"""List of the computed lamination losses

        :Type: list
        """,
    )

    def _get_winding(self):
        """getter of winding"""
        return self._winding

    def _set_winding(self, value):
        """setter of winding"""
        if type(value) is int and value == -1:
            value = list()
        check_var("winding", value, "list")
        self._winding = value

    winding = property(
        fget=_get_winding,
        fset=_set_winding,
        doc=u"""List of the computed winding losses

        :Type: list
        """,
    )

    def _get_magnet(self):
        """getter of magnet"""
        return self._magnet

    def _set_magnet(self, value):
        """setter of magnet"""
        if type(value) is int and value == -1:
            value = list()
        check_var("magnet", value, "list")
        self._magnet = value

    magnet = property(
        fget=_get_magnet,
        fset=_set_magnet,
        doc=u"""List of the computed magnet losses

        :Type: list
        """,
    )

    def _get_meshsolution(self):
        """getter of meshsolution"""
        return self._meshsolution

    def _set_meshsolution(self, value):
        """setter of meshsolution"""
        if type(value) is int and value == -1:
            value = list()
        check_var("meshsolution", value, "list")
        self._meshsolution = value

    meshsolution = property(
        fget=_get_meshsolution,
        fset=_set_meshsolution,
        doc=u"""list of FEA software mesh and post processing results

        :Type: list
        """,
    )

    def _get_logger_name(self):
        """getter of logger_name"""
        return self._logger_name

    def _set_logger_name(self, value):
        """setter of logger_name"""
        check_var("logger_name", value, "str")
        self._logger_name = value

    logger_name = property(
        fget=_get_logger_name,
        fset=_set_logger_name,
        doc=u"""Name of the logger to use

        :Type: str
        """,
    )

    def _get_mech(self):
        """getter of mech"""
        return self._mech

    def _set_mech(self, value):
        """setter of mech"""
        if type(value) is int and value == -1:
            value = list()
        check_var("mech", value, "list")
        self._mech = value

    mech = property(
        fget=_get_mech,
        fset=_set_mech,
        doc=u"""List of the mechanical losses

        :Type: list
        """,
    )

    def _get_misc(self):
        """getter of misc"""
        return self._misc

    def _set_misc(self, value):
        """setter of misc"""
        if type(value) is int and value == -1:
            value = list()
        check_var("misc", value, "list")
        self._misc = value

    misc = property(
        fget=_get_misc,
        fset=_set_misc,
        doc=u"""List of the miscellaneous losses

        :Type: list
        """,
    )
