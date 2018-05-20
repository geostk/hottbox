"""
Classes that bring interoperability into tensor representations
"""


class Mode(object):
    """ This class describe mode of the Tensor

    Attributes
    ----------
    _name : str
        Placeholder for the name of the mode
    _index : list[str]
        Placeholder for the list of indices for this mode
    """
    def __init__(self, name) -> None:
        """ Constructor of the ``Mode`` class

        Parameters
        ----------
        name : str
            Name of the mode
        """
        if not isinstance(name, str):
            raise TypeError("Parameter `name` should be a string!")
        self._name = name.strip().replace("_", "-")
        self._index = None

    def __str__(self):
        self_as_string = "{}(name='{}', index={})".format(self.__class__.__name__,
                                                          self.name,
                                                          self.index)
        return self_as_string

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        """
        Returns
        -------
        bool

        Notes
        -----
        Modes are equal when everything is the same.
        """
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False

    def copy(self):
        """ Produces a copy of itself as a new object

        Returns
        -------
        new_object : Mode
        """
        name = self.name
        index = self.index
        new_object = Mode(name=name)
        new_object.set_index(index=index)
        return new_object

    @property
    def name(self):
        """ Name of the mode

        Returns
        -------
        name : str
        """
        name = self._name
        return name

    @property
    def index(self):
        """ List of indices for the mode

        Returns
        -------
        index : list[str]
        """
        index = self._index
        return index

    def set_name(self, name):
        """ Set new name of the mode

        Parameters
        ----------
        name : str
            New name of the mode

        Returns
        -------
        self : Mode
        """
        if not isinstance(name, str):
            raise TypeError("Parameter `name` should be a string!")
        self._name = name
        return self

    def set_index(self, index):
        """ Set new list of indices for the mode

        Parameters
        ----------
        index : list

        Returns
        -------
        self : Mode
        """
        if index is not None:
            if not isinstance(index, list):
                raise TypeError("Parameter `index` should be a list!")

        self._index = index
        return self

    def reset_index(self):
        """ Drop list of indices for the mode

        Returns
        -------
        self : Mode
        """
        self._index = None
        return self
