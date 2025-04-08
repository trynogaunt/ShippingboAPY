from abc import ABC
import difflib

class AbstractModel(ABC):
    """Abstract base class for models in the ShippingBo API."""

    def __init__(self, response , wrapper_key=None):
        """Initialize the model with keyword arguments."""
        self.__attributes = []

        data = response.get(wrapper_key) if response.get(wrapper_key) else response
        if data:
            for key, value in data.items():
                attr_name = f"__{key}"
                if not hasattr(self, attr_name):
                    # If the attribute doesn't exist, create it dynamically
                    setattr(self, attr_name, value)
                    # Store the attribute name for later reference
                    self.__attributes.append(key)
        
    def __getattr__(self, name):
        if name in self.__attributes:
            return getattr(self, f"__{name}")
        # Generate an error message if the attribute doesn't exist
        # and suggest similar attributes using difflib
        
        error_msg = f"{self.__class__.__name__} has no attribute '{name}'"
        similar_attr = difflib.get_close_matches(name, self.__attributes, n=3, cutoff=0.6)
        if similar_attr:
            suggestions = ', '.join(similar_attr)
            error_msg += f". Did you mean: {suggestions}?"
        raise AttributeError(error_msg)

    def get_attributes(self):
        """Return the list of attributes."""
        return list(self.__attributes)
    
    def to_dict(self):
        """Convert the model to a dictionary."""
        return {attr: getattr(self, f"__{attr}") for attr in self.__attributes}
        
    def __repr__(self):
        """Return a string representation of the model."""
        return f"{self.__class__.__name__}({self.__dict__})"
    
    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.__class__.__name__}({self.__dict__})"