import pickle

from typing import Any, Final


# define constants
atw_title: Final = 'Around The World in Eighty Days'
cor_title: Final = 'Corpus'
ttl_title: Final = 'Twenty Thousand Leagues Under the Sea'
SENT_BEG: Final = '<s>'
SENT_END: Final = '</s>'

class General():
    def __init__(self) -> None:
        pass

    def read_from_pickle(self, filepath) -> Any:
        """Read an object from a pickle file
        Parameters:
            filepath (str): path to the pickle file
        Returns:
            Any: the object in the file"""
        
        obj = None
        
        with open(filepath, 'rb') as pckl:
            obj = pickle.load(pckl)
            
        return obj