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


from ._check import InitUnKnowClassError


class OutLoss(FrozenClass):
    """Gather the loss module outputs"""

    VERSION = 1

    # cf Methods.Output.OutLoss.get_loss
    if isinstance(get_loss, ImportError):
        get_loss = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutLoss method get_loss: " + str(get_loss))
            )
        )
    else:
        get_loss = get_loss
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        losses=-1,
        meshsolutions=-1,
        logger_name="Pyleecan.OutLoss",
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
            if "losses" in list(init_dict.keys()):
                losses = init_dict["losses"]
            if "meshsolutions" in list(init_dict.keys()):
                meshsolutions = init_dict["meshsolutions"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.losses = losses
        self.meshsolutions = meshsolutions
        self.logger_name = logger_name

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
            "losses = "
            + linesep
            + str(self.losses).replace(linesep, linesep + "\t")
            + linesep
        )
        OutLoss_str += (
            "meshsolutions = "
            + linesep
            + str(self.meshsolutions).replace(linesep, linesep + "\t")
            + linesep
        )
        OutLoss_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        return OutLoss_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.losses != self.losses:
            return False
        if other.meshsolutions != self.meshsolutions:
            return False
        if other.logger_name != self.logger_name:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        OutLoss_dict = dict()
        OutLoss_dict["losses"] = self.losses.copy() if self.losses is not None else None
        OutLoss_dict["meshsolutions"] = (
            self.meshsolutions.copy() if self.meshsolutions is not None else None
        )
        OutLoss_dict["logger_name"] = self.logger_name
        # The class name is added to the dict for deserialisation purpose
        OutLoss_dict["__class__"] = "OutLoss"
        return OutLoss_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.losses = None
        self.meshsolutions = None
        self.logger_name = None

    def _get_losses(self):
        """getter of losses"""
        return self._losses

    def _set_losses(self, value):
        """setter of losses"""
        if type(value) is int and value == -1:
            value = list()
        check_var("losses", value, "list")
        self._losses = value

    losses = property(
        fget=_get_losses,
        fset=_set_losses,
        doc=u"""List of the computed losses of SciDataTool's DataND type

        :Type: list
        """,
    )

    def _get_meshsolutions(self):
        """getter of meshsolutions"""
        return self._meshsolutions

    def _set_meshsolutions(self, value):
        """setter of meshsolutions"""
        if type(value) is int and value == -1:
            value = list()
        check_var("meshsolutions", value, "list")
        self._meshsolutions = value

    meshsolutions = property(
        fget=_get_meshsolutions,
        fset=_set_meshsolutions,
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
