# coding: "utf-8"
# author: bcynuaa
# date: 2023/05/18

###################################################################################################
# This file is used to contain things in matplotlib

TIMEDOMAIN_XLABEL: str = r"$t$ (s)"
TIMEDOMAIN_YLABEL: str = r"$q(t)$"
TIMEDOMAIN_TITLE: str = r"Time Domain"

def getTimeDomainYlabel(i: int) -> str:
    """get the ylabel of time domain

    Args:
        i (int): the index of the ylabel

    Returns:
        str: the ylabel of time domain
    """
    if i == -1:
        return TIMEDOMAIN_YLABEL
        pass
    else:
        return r"$q_" + str(i+1) + r"(t)$"
        pass
    pass

FREQUENCYDOMAIN_XLABEL: str = r"$f$ (Hz)"
FREQUENCYDOMAIN_YLABEL: str = r"$q(f)$"
FREQUENCYDOMAIN_TITLE: str = r"Frequency Domain"

def getFrequencyDomainYlabel(i: int) -> str:
    """get the ylabel of frequency domain

    Args:
        i (int): the index of the ylabel

    Returns:
        str: the ylabel of frequency domain
    """
    if i == -1:
        return FREQUENCYDOMAIN_YLABEL
        pass
    else:
        return r"$q_" + str(i+1) + r"(f)$"
        pass
    pass

print("Things in matplotlib have been loaded.")

###################################################################################################