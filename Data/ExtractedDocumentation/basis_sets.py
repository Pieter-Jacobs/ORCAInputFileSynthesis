# ------------------- BASIS SETS and related keywords -------------------------# 
basis_set_contraction = """DecontractBas@Decontract the basis set (removes duplicate primitives)
NoDecontractBas@Do not decontract the basis set
DecontractAuxJ@Decontract the AuxJ basis set
DecontractAux@Decontract the AuxJ basis set
NoDecontractAuxJ@Do not decontract the AuxJ basis set
DecontractAuxJK@Decontract the AuxJK basis set
NoDecontractAuxJK@Do not decontract the AuxJK basis set
DecontractAuxC@Decontract the AuxC basis set
NoDecontractAuxC@Do not decontract the AuxC basis set
Decontract@Decontract all (orbital and auxiliary) basis sets
AutoAux@Automatic construction of a general purpose auxiliary basis for simultaneously fitting Coulomb, exchange and correlation calculations."""

basis_set_coulomb_fitting = """SARC/J@General-purpose Coulomb-fitting auxiliary for all SARC orbital basis sets.
Def2/J@Weigend’s “universal” Coulomb fitting basis that is suitable for all def2 type basis sets. Assumes the use of ECPs beyond Kr (do not use with DKH/ZORA).
SARC/J@General-purpose Coulomb fitting basis set for all-electron calculations. Consists of the decontracted def2/J up to Kr and of our own auxiliary basis sets for the rest of the periodic table. Appropriate for use in DKH or ZORA calculations with the recontracted versions of the all-electron def2 basis sets (up to Kr) and the SARC basis sets for the heavier elements.
x2c/J@Weigend’s Coulomb fitting basis for the all-electron x2c-XVPall basis sets."""

basis_set_correlation_fitting="""Def2-SVP/C@Correlation fitting for the def2-SVP orbital basis
Def2-TZVP/C@Correlation fitting for the def2-TZVP orbital basis
Def2-TZVPP/C@Correlation fitting for the def2-TZVPP orbital basis
Def2-QZVPP/C@Correlation fitting for the def2-QZVPP orbital basis
Def2-SVPD/C@Correlation fitting for the def2-SVPD orbital basis
Def2-TZVPD/C@Correlation fitting for the def2-TZVPD orbital basis
Def2-TZVPPD/C@Correlation fitting for the def2-TZVPPD orbital basis
Def2-QZVPPD/C@Correlation fitting for the def2-QZVPPD orbital basis
cc-pVDZ/C@Correlation fitting for the cc-pVDZ orbital basis
cc-pVTZ/C@Correlation fitting for the cc-pVTZ orbital basis
cc-pVQZ/C@Correlation fitting for the cc-pVQZ orbital basis
cc-pV5Z/C@Correlation fitting for the cc-pV5Z orbital basis
cc-pV6Z/C@Correlation fitting for the cc-pV6Z orbital basis
aug-cc-pVDZ/C@Correlation fitting for the aug-cc-pVDZ orbital basis
aug-cc-pVTZ/C@Correlation fitting for the aug-cc-pVTZ orbital basis
aug-cc-pVQZ/C@Correlation fitting for the aug-cc-pVQZ orbital basis
aug-cc-pV5Z/C@Correlation fitting for the aug-cc-pV5Z orbital basis
aug-cc-pV6Z/C@Correlation fitting for the aug-cc-pV6Z orbital basis
cc-pwCVDZ/C@Correlation fitting for the cc-pwCVDZ orbital basis
cc-pwCVTZ/C@Correlation fitting for the cc-pwCVTZ orbital basis
cc-pwCVQZ/C@Correlation fitting for the cc-pwCVQZ orbital basis
cc-pwCV5Z/C@Correlation fitting for the cc-pwCV5Z orbital basis
aug-cc-pwCVDZ/C@Correlation fitting for the aug-cc-pwCVDZ orbital basis
aug-cc-pwCVTZ/C@Correlation fitting for the aug-cc-pwCVTZ orbital basis
aug-cc-pwCVQZ/C@Correlation fitting for the aug-cc-pwCVQZ orbital basis
aug-cc-pwCV5Z/C@Correlation fitting for the aug-cc-pwCV5Z orbital basis
cc-pVDZ-PP/C@Correlation fitting for the respective cc-pVDZ-PP orbital basis
cc-pVTZ-PP/C@Correlation fitting for the respective cc-pVTZ-PP orbital basis
cc-pVQZ-PP/C@Correlation fitting for the respective cc-pVQZ-PP orbital basis
aug-cc-pVDZ-PP/C@Correlation fitting for the respective aug-cc-pVDZ-PP orbital basis
aug-cc-pVTZ-PP/C@Correlation fitting for the respective aug-cc-pVTZ-PP orbital basis
aug-cc-pVQZ-PP/C@Correlation fitting for the respective aug-cc-pVQZ-PP orbital basis
cc-pwCVDZ-PP/C@Correlation fitting for the respective cc-pwCVDZ-PP orbital basis
cc-pwCVTZ-PP/C@Correlation fitting for the respective cc-pwCVTZ-PP orbital basis
cc-pwCVQZ-PP/C@Correlation fitting for the respective cc-pwCVQZ-PP orbital basis
aug-cc-pwCVDZ-PP/C@Correlation fitting for the respective aug-cc-pwCVDZ-PP orbital basis
aug-cc-pwCVTZ-PP/C@Correlation fitting for the respective aug-cc-pwCVTZ-PP orbital basis
aug-cc-pwCVQZ-PP/C@Correlation fitting for the respective aug-cc-pwCVQZ-PP orbital basis
cc-pVDZ-F12-MP2fit@Correlation fitting for the respective cc-pVDZ-F12 orbital basis
cc-pVTZ-F12-MP2fit@Correlation fitting for the respective cc-pVTZ-F12 orbital basis
cc-pVQZ-F12-MP2fit@Correlation fitting for the respective cc-pVQZ-F12 orbital basis
cc-pCVDZ-F12-MP2fit@Correlation fitting for the respective cc-pCVDZ-F12 orbital basis
cc-pCVTZ-F12-MP2fit@Correlation fitting for the respective cc-pCVTZ-F12 orbital basis
cc-pCVQZ-F12-MP2fit@Correlation fitting for the respective cc-pCVQZ-F12 orbital basis
cc-pVDZ-PP-F12-MP2fit@Correlation fitting for the respective cc-pVDZ-PP-F12 orbital basis
cc-pVTZ-PP-F12-MP2fit@Correlation fitting for the respective cc-pVTZ-PP-F12 orbital basis
cc-pVQZ-PP-F12-MP2fit@Correlation fitting for the respective cc-pVQZ-PP-F12 orbital basis"""

basis_set_coulomb_exchange_fitting = """SARC2-DKH-QZVP/JK@Simultaneous exchange and coulomb fitting for the SARC2-DKH-QZVP basis set.
SARC2-DKH-QZV/JK@Simultaneous exchange and coulomb fitting for the SARC2-DKH-QZV basis set.
SARC2-ZORA-QZVP/JK@Simultaneous exchange and coulomb fitting for the SARC2-ZORA-QZVP basis set.
SARC2-ZORA-QZV/JK@Simultaneous exchange and coulomb fitting for the SARC2-ZORA-QZV basis set.
Def2/JK@Coulomb+Exchange fitting for all def2 basis sets
Def2/JKsmall@reduced version of Coulomb+Exchange fitting for all def2 basis sets
cc-pVTZ/JK@Coulomb+Exchange fitting for the respective cc-pVTZ orbital basis
cc-pVQZ/JK@Coulomb+Exchange fitting for the respective cc-pVQZ orbital basis
cc-pV5Z/JK@Coulomb+Exchange fitting for the respective cc-pV5Z orbital basis
aug-cc-pVTZ/JK@Coulomb+Exchange fitting for the aug-cc-pVTZ orbital basis
aug-cc-pVQZ/JK@Coulomb+Exchange fitting for the aug-cc-pVQZ orbital basis
aug-cc-pV5Z/JK@Coulomb+Exchange fitting for the aug-cc-pV5Z orbital basis"""

basis_set_pople = """STO-3G@Minimal basis set(H–I)
3-21G@Pople 3-21G (H–Cs)
3-21GSP@Buenker 3-21GSP (H–Ar)
4-22GSP@Buenker 4-22GSP (H–Ar)
6-31G@Pople 6-31G and its modifications (H–Zn)
6-31G*@Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H
6-31G(d)@Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H
6-31G(2d)@Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except H
6-31G**@Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms
6-31G(d,p)@Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms 
6-31G(2d, p)@Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except for H, where one set is applied
6-31G(2d, 2p)@Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms
6-31G*@Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H
6-31+G*@Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H. Include diffuse functions on all atoms except H
6-31++G*@Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H. Include diffuse functions on all atoms
6-31G(d)@Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H
6-31+G(d)@Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H. Include diffuse functions on all atoms except H
6-31+G(d)@Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H. Include diffuse functions on all atoms
6-31G(2d)@Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except H
6-31+G(2d)@Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except H. Include diffuse functions on all atoms except H
6-31++G(2d)@Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except H. Include diffuse functions on all atoms
6-31G**@Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms
6-31+G**@Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms. Include diffuse functions on all atoms except H
6-31++G**@Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms. Include diffuse functions on all atoms
6-31G(d,p)@Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms 
6-31+G(d,p)@Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms. Include diffuse functions on all atoms except H
6-31++G(d,p)@Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms. Include diffuse functions on all atoms 
6-31G(2d, p)@Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except for H, where one set is applied
6-31+G(2d, p)@Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except for H, where one set is applied. Include diffuse functions on all atoms except H
6-31++G(2d, p)@Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except for H, where one set is applied. Include diffuse functions on all atoms 
6-31G(2d, 2p)@Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms
6-31+G(2d, 2p)@Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms. Include diffuse functions on all atoms except H
6-31++G(2d, 2p)@Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms. Include diffuse functions on all atoms 
m6-31G@Modified Pople 6-31G and its modifications (H–Zn)
m6-31G*@Modified Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H
m6-31G(d)@Modified Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H
m6-31G(2d)@Modified Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except H
m6-31G**@Modified Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms
m6-31G(d,p)@Modified Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms 
m6-31G(2d, p)@Modified Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except for H, where one set is applied
m6-31G(2d, 2p)@Modified Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms
m6-31+G@Modified Pople 6-31G and its modifications (H–Zn). Include diffuse functions on all atoms except H
m6-31++G@Modified Pople 6-31G and its modifications (H–Zn). Include diffuse functions on all atoms
m6-31G*@Modified Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H
m6-31+G*@Modified Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H. Include diffuse functions on all atoms except H
m6-31++G*@Modified Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H. Include diffuse functions on all atoms
m6-31G(d)@Modified Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H
m6-31+G(d)@Modified Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H. Include diffuse functions on all atoms except H
m6-31+G(d)@Modified Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H. Include diffuse functions on all atoms
m6-31G(2d)@Modified Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except H
m6-31+G(2d)@Modified Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except H. Include diffuse functions on all atoms except H
m6-31++G(2d)@Modified Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except H. Include diffuse functions on all atoms
m6-31G**@Modified Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms
m6-31+G**@Modified Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms. Include diffuse functions on all atoms except H
m6-31++G**@Modified Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms. Include diffuse functions on all atoms
m6-31G(d,p)@Modified Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms 
m6-31+G(d,p)@Modified Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms. Include diffuse functions on all atoms except H
m6-31++G(d,p)@Modified Pople 6-31G and its modifications (H–Zn) with one set of first polarization functions on all atoms. Include diffuse functions on all atoms 
m6-31G(2d, p)@Modified Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except for H, where one set is applied
m6-31+G(2d, p)@Modified Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except for H, where one set is applied. Include diffuse functions on all atoms except H
m6-31++G(2d, p)@Modified Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except for H, where one set is applied. Include diffuse functions on all atoms 
m6-31G(2d, 2p)@Modified Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms
m6-31+G(2d, 2p)@Modified Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms. Include diffuse functions on all atoms except H
m6-31++G(2d, 2p)@Modified Pople 6-31G and its modifications (H–Zn) with two sets of first polarization functions on all atoms. Include diffuse functions on all atoms 
6-311G@Pople 6-311G and its modifications (H–Zn)
6-311G*@Pople 6-311G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H
6-311G(d)@Pople 6-311G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H
6-311G(2d)@Pople 6-311G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except H
6-311G**@Pople 6-311G and its modifications (H–Zn) with one set of first polarization functions on all atoms
6-311G(d,p)@Pople 6-311G and its modifications (H–Zn) with one set of first polarization functions on all atoms 
6-311G(2d, p)@Pople 6-311G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except for H, where one set is applied
6-311G(2d, 2p)@Pople 6-311G and its modifications (H–Zn) with two sets of first polarization functions on all atoms
6-311+G@Pople 6-311G and its modifications (H–Zn). Include diffuse functions on all atoms except H
6-311++G@Pople 6-311G and its modifications (H–Zn). Include diffuse functions on all atoms
6-311G*@Pople 6-311G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H
6-311+G*@Pople 6-311G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H. Include diffuse functions on all atoms except H
6-311G(d)@Pople 6-311G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H
6-311+G(d)@Pople 6-311G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H. Include diffuse functions on all atoms except H
6-311+G(d)@Pople 6-311G and its modifications (H–Zn) with one set of first polarization functions on all atoms except H. Include diffuse functions on all atoms
6-311G(2d)@Pople 6-311G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except H
6-311+G(2d)@Pople 6-311G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except H. Include diffuse functions on all atoms except H
6-311++G(2d)@Pople 6-311G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except H. Include diffuse functions on all atoms
6-311G**@Pople 6-311G and its modifications (H–Zn) with one set of first polarization functions on all atoms
6-311+G**@Pople 6-311G and its modifications (H–Zn) with one set of first polarization functions on all atoms. Include diffuse functions on all atoms except H
6-311++G**@Pople 6-311G and its modifications (H–Zn) with one set of first polarization functions on all atoms. Include diffuse functions on all atoms
6-311G(d,p)@Pople 6-311G and its modifications (H–Zn) with one set of first polarization functions on all atoms 
6-311+G(d,p)@Pople 6-311G and its modifications (H–Zn) with one set of first polarization functions on all atoms. Include diffuse functions on all atoms except H
6-311++G(d,p)@Pople 6-311G and its modifications (H–Zn) with one set of first polarization functions on all atoms. Include diffuse functions on all atoms 
6-311G(2d, p)@Pople 6-311G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except for H, where one set is applied
6-311+G(2d, p)@Pople 6-311G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except for H, where one set is applied. Include diffuse functions on all atoms except H
6-311++G(2d, p)@Pople 6-311G and its modifications (H–Zn) with two sets of first polarization functions on all atoms except for H, where one set is applied. Include diffuse functions on all atoms 
6-311G(2d, 2p)@Pople 6-311G and its modifications (H–Zn) with two sets of first polarization functions on all atoms
6-311+G(2d, 2p)@Pople 6-311G and its modifications (H–Zn) with two sets of first polarization functions on all atoms. Include diffuse functions on all atoms except H
6-311++G(2d, 2p)@Pople 6-311G and its modifications (H–Zn) with two sets of first polarization functions on all atoms. Include diffuse functions on all atoms"""

# All-electron basis sets for elements H–Kr.
basis_set_kahrlsruhe = """def2-SVP@Valence double-zeta basis set with “new” polarization functions.
def2-SV(P)@Valence double-zeta basis set with “new” polarization functions with slightly reduced polarization.
def2-TZVP@Valence triple-zeta basis set with “new” polarization functions. Note that this is quite similar to the older (“def”) TZVPP for the main group elements and TZVP for hydrogen.
def2-TZVP(-f)@TZVP with f polarization removed from main group elements.
def2-TZVPP@TZVPP basis set with “new” polarization functions.
def2-QZVP@Polarized quadruple-zeta basis.
def2-QZVPP@Accurate doubly polarized quadruple-zeta basis."""

# 5s, 6s, 4d, and 5d elements and iodine.
basis_set_kahrlsruhe_dirac_firoc = """dhf-SV(P)@based on def2-SV(P)
dhf-SVP@based on def2-SVP
dhf-TZVP@based on def2-TZVP
dhf-TZVPP@based on def2-TZVPP
dhf-QZVP@based on def2-QZVP
dhf-QZVPP@based on def2-QZVPP"""

# All-electron basis sets for elements H–Kr.
basis_set_ahrlsrichs = """SV@Valence double-zeta basis set.
SV(P)@Valence double-zeta with polarization only on heavy elements.
SVP@Polarized valence double-zeta basis set.
TZV@Valence triple-zeta basis set.
TZV(P)@Valence triple-zeta with polarization on heavy elements.
TZVP@Polarized valence triple-zeta basis set.
TZVPP@Doubly polarized triple-zeta basis set.
QZVP@Polarized valence quadruple-zeta basis set.
QZVPP@Doubly polarized quadruple-zeta basis set."""

# All-electron basis sets for elements H–Kr.
basis_set_def2_minimally_augmented = """ma-def2-SVP@Minimally augmented def2-SVP basis set.
ma-def2-SV(P)@Minimally augmented def2-SV(P) basis set.
ma-def2-TZVP@Minimally augmented def2-TZVP basis set.
ma-def2-TZVP(-f)@Minimally augmented def2-TZVP(-f) basis set.
ma-def2-TZVPP@Minimally augmented def2-TZVPP basis set.
ma-def2-QZVPP@Minimally augmented def2-QZVPP basis set."""


# All-electron basis sets for elements H–Kr.
basis_set_def2_karlsruhe_def2_diffused = """def2-SVPD@Diffuse def2-SVP basis set for property calculations
def2-TZVPD@Diffuse def2-TZVP basis set for property calculations
def2-TZVPPD@Diffuse def2-TZVPP basis set for property calculations
def2-QZVPD@Diffuse def2-QZVP basis set for property calculations
def2-QZVPPD@Diffuse def2-QZVPP basis set for property calculations"""


basis_set_def_karlsruhe_recontracted_dkh = """DKH-SVP@DKH adapted Valence double-zeta basis set with “new” polarization functions. Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
DKH-SV(P)@DKH adapted valence double-zeta basis set with “new” polarization functions with slightly reduced polarization. Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
DKH-TZVP@DKH adapted valence triple-zeta basis set with “new” polarization functions. Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
DKH-TZVP(-f)@DKH adapted valence triple-zeta basis set with “new” polarization functions and f polarization removed from main group elements. Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
DKH-TZVPP@DKH adapted TZVPP basis set with “new” polarization functions. Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
DKH-QZVPP@DKH adapted accurate doubly polarized quadruple-zeta basis. Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
"""

basis_set_def_karlsruhe_recontracted_zora = """ZORA-SVP@ZORA adapted valence double-zeta basis set with polarization functions. Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ZORA-SV(P)@ZORA adapted valence double-zeta basis set with “new” polarization functions with slightly reduced polarization. Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ZORA-TZVP@ZORA adapted valence triple-zeta basis set with “new” polarization functions.  Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ZORA-TZVP(-f)@ZORA adapted valence triple-zeta basis set with “new” polarization functions and f polarization removed from main group elements.  Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ZORA-TZVPP@ZORA adapted TZVPP basis set with “new” polarization functions.  Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ZORA-QZVPP@ZORA adapted ccurate doubly polarized quadruple-zeta basis.  Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
"""

# karlsruhe fpr dkh hamiltonian
basis_set_def2_karlsruhe_recontracted_dkh = """DKH-def2-SVP@DKH adapted Valence double-zeta basis set with “new” polarization functions. Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
DKH-def2-SV(P)@DKH adapted valence double-zeta basis set with “new” polarization functions with slightly reduced polarization. Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
DKH-def2-TZVP@DKH adapted valence triple-zeta basis set with “new” polarization functions. Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
DKH-def2-TZVP(-f)@DKH adapted valence triple-zeta basis set with “new” polarization functions and f polarization removed from main group elements. Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
DKH-def2-TZVPP@DKH adapted TZVPP basis set with “new” polarization functions.. Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
DKH-def2-QZVPP@DKH adapted accurate doubly polarized quadruple-zeta basis. Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian."""

# karlsruhe for zora hamiltonian
basis_set_recontracted_zora = """ZORA-def2-SVP@ZORA adapted valence double-zeta basis set with “new” polarization functions. Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ZORA-def2-SV(P)@ZORA adapted valence double-zeta basis set with “new” polarization functions with slightly reduced polarization. Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ZORA-def2-TZVP@ZORA adapted valence triple-zeta basis set with “new” polarization functions.  Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ZORA-def2-TZVP(-f)@ZORA adapted valence triple-zeta basis set with “new” polarization functions and f polarization removed from main group elements..  Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ZORA-def2-TZVPP@ZORA adapted TZVPP basis set with “new” polarization functions.  Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ZORA-def2-QZVPP@ZORA adapted ccurate doubly polarized quadruple-zeta basis.  Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian."""

basis_set_def_karlsruhe_recontracted_dkh_minimally_augmented = """ma-DKH-SVP@Minimally augmented DKH adapted Valence double-zeta basis set with “new” polarization functions. Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
ma-DKH-SV(P)@Minimally augmented DKH adapted valence double-zeta basis set with “new” polarization functions with slightly reduced polarization. Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
ma-DKH-TZVP@Minimally augmented DKH adapted valence triple-zeta basis set with “new” polarization functions. Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
ma-DKH-TZVP(-f)@Minimally augmented DKH adapted valence triple-zeta basis set with “new” polarization functions and f polarization removed from main group elements. Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
ma-DKH-TZVPP@Minimally augmented DKH adapted TZVPP basis set with “new” polarization functions. Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
ma-DKH-QZVPP@Minimally augmented DKH adapted accurate doubly polarized quadruple-zeta basis. Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian."""

basis_set_def_karlsruhe_recontracted_zora_minimally_augmented = """ma-ZORA-SVP@Minimally augmented ZORA adapted valence double-zeta basis set with polarization functions. Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ma-ZORA-SV(P)@Minimally augmented ZORA adapted valence double-zeta basis set with “new” polarization functions with slightly reduced polarization. Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ma-ZORA-TZVP@Minimally augmented ZORA adapted valence triple-zeta basis set with “new” polarization functions.  Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ma-ZORA-TZVP(-f)@Minimally augmented ZORA adapted valence triple-zeta basis set with “new” polarization functions and f polarization removed from main group elements.  Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ma-ZORA-TZVPP@Minimally augmented ZORA adapted TZVPP basis set with “new” polarization functions.  Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ma-ZORA-QZVPP@Minimally augmented ZORA adapted ccurate doubly polarized quadruple-zeta basis.  Retains the original def exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
"""

# karlsruhe fpr dkh hamiltonian
basis_set_def2_karlsruhe_recontracted_dkh_minimally_augmented = """ma-DKH-def2-SVP@Minimally augmented DKH adapted Valence double-zeta basis set with “new” polarization functions. Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
ma-DKH-def2-SV(P)@Minimally augmented DKH adapted valence double-zeta basis set with “new” polarization functions with slightly reduced polarization. Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
ma-DKH-def2-TZVP@Minimally augmented DKH adapted valence triple-zeta basis set with “new” polarization functions. Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
ma-DKH-def2-TZVP(-f)@Minimally augmented DKH adapted valence triple-zeta basis set with “new” polarization functions and f polarization removed from main group elements. Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
ma-DKH-def2-TZVPP@Minimally augmented DKH adapted TZVPP basis set with “new” polarization functions.. Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian.
ma-DKH-def2-QZVPP@Minimally augmented DKH adapted accurate doubly polarized quadruple-zeta basis. Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the DKH Hamiltonian."""

# karlsruhe for zora hamiltonian
basis_set_recontracted_zora_minimally_augmented = """ma-ZORA-def2-SVP@Minimally augmented ZORA adapted valence double-zeta basis set with “new” polarization functions. Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ma-ZORA-def2-SV(P)@Minimally augmented ZORA adapted valence double-zeta basis set with “new” polarization functions with slightly reduced polarization. Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ma-ZORA-def2-TZVP@Minimally augmented ZORA adapted valence triple-zeta basis set with “new” polarization functions.  Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ma-ZORA-def2-TZVP(-f)@Minimally augmented ZORA adapted valence triple-zeta basis set with “new” polarization functions and f polarization removed from main group elements..  Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ma-ZORA-def2-TZVPP@Minimally augmented ZORA adapted TZVPP basis set with “new” polarization functions.  Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian.
ma-ZORA-def2-QZVPP@Minimally augmented ZORA adapted ccurate doubly polarized quadruple-zeta basis.  Retains the original def2 exponents but has only one contracted function per angular momentum, with contraction coefficients suitable for the ZORA Hamiltonian."""

# Karlsruhe for two component calculations (not implemented in orca so not going to use)
basis_set_karlsruhe_two_component = """x2c-SV(P)all@SV(P) all-electron Karlsruhe basis sets up to Rn for exact two-component methods (X2C).
x2c-SV(P)all-2c@SV(P) all-electron Karlsruhe basis set up to Rn for exact two-component methods (X2C), 2c version.
x2c-SV(P)all-s@SV(P) all-electron Karlsruhe basis set up to Rn for exact two-component methods (X2C), NMR version.
x2c-SVPall@SVP all-electron Karlsruhe basis sets up to Rn for exact two-component methods (X2C).
x2c-SVPall-2c@SVP all-electron Karlsruhe basis set up to Rn for exact two-component methods (X2C), 2c version.
x2c-SVPall-s@SVP all-electron Karlsruhe basis set up to Rn for exact two-component methods (X2C), NMR version.
x2c-TZVPall@TZVP all-electron Karlsruhe basis sets up to Rn for exact two-component methods (X2C).
x2c-TZVPall-2c@TZVP all-electron Karlsruhe basis set up to Rn for exact two-component methods (X2C), 2c version.
x2c-TZVPall-s@TZVP all-electron Karlsruhe basis set up to Rn for exact two-component methods (X2C), NMR version.
x2c-TZVPPall@TZVPP all-electron Karlsruhe basis sets up to Rn for exact two-component methods (X2C).
x2c-TZVPPall-2c@TZVPP all-electron Karlsruhe basis set up to Rn for exact two-component methods (X2C), 2c version.
x2c-TZVPPall-s@TZVPP all-electron Karlsruhe basis set up to Rn for exact two-component methods (X2C), NMR version.
x2c-QZVPall@QZVP all-electron Karlsruhe basis sets up to Rn for exact two-component methods (X2C).
x2c-QZVPall-2c@QZVP all-electron Karlsruhe basis set up to Rn for exact two-component methods (X2C), 2c version.
x2c-QZVPall-s@QZVP all-electron Karlsruhe basis set up to Rn for exact two-component methods (X2C), NMR version.        
x2c-QZVPPall@QZVPP all-electron Karlsruhe basis sets up to Rn for exact two-component methods (X2C).
x2c-QZVPPall-2c@QZVPP all-electron Karlsruhe basis set up to Rn for exact two-component methods (X2C), 2c version.
x2c-QZVPPall-s@QZVPP all-electron Karlsruhe basis set up to Rn for exact two-component methods (X2C), NMR version.""" 

# For use for all elements beyond krypton
basis_set_sarc_contracted_DKH = """SARC-DKH-TZVP@TZVP Segmented all-electron relativistically contracted basis sets for use with the DKH2 Hamiltonian.
SARC-DKH-TZVPP@TZVPP Segmented all-electron relativistically contracted basis sets for use with the DKH2 Hamiltonian.
SARC2-DKH-QZVP@SARC basis set of valence quadruple-zeta quality for lanthanides, with NEVPT2-optimized (3g2h) polarization functions. Suitable for accurate calculations using DKH2 wavefunction methods"""

basis_set_sarc_contracted_ZORA = """SARC-ZORA-TZVP@TZVP Segmented all-electron relativistically contracted basis sets for use with the ZORA Hamiltonian.
SARC-ZORA-TZVPP@TZVPP Segmented all-electron relativistically contracted basis sets for use with the ZORA Hamiltonian.
SARC2-ZORA-QZVP@SARC basis set of valence quadruple-zeta quality for lanthanides, with NEVPT2-optimized (3g2h) polarization functions. Suitable for accurate calculations using ZORA wavefunction methods"""

basis_set_sarc2_contracted_DKH = """SARC2-DKH-QZVP@SARC basis sets of valence quadruple-zeta quality for lanthanides, with NEVPT2-optimized (3g2h) polarization functions. Suitable for accurate calculations using DKH wavefunction method.
SARC2-DKH-QZV@SARC basis sets of valence quadruple-zeta quality for lanthanides. Suitable for accurate calculations using ZORA wavefunction method."""

basis_set_sarc2_contracted_ZORA = """SARC2-ZORA-QZVP@SARC basis sets of valence quadruple-zeta quality for lanthanides, with NEVPT2-optimized (3g2h) polarization functions. Suitable for accurate calculations using ZORA wavefunction method.
SARC2-ZORA-QZV@SARC2-ZORA-QZVP@SARC basis sets of valence quadruple-zeta quality for lanthanides. Suitable for accurate calculations using ZORA wavefunction method."""


basis_set_jensen_scf = """pc-0@“Polarization-consistent” generally contracted basis sets (H–Kr) of 0-zeta quality, optimized for SCF calculations
pc-1@“Polarization-consistent” generally contracted basis sets (H–Kr) of 1-zeta quality, optimized for SCF calculations
pc-2@“Polarization-consistent” generally contracted basis sets (H–Kr) of 2-zeta quality, optimized for SCF calculations
pc-3@“Polarization-consistent” generally contracted basis sets (H–Kr) of 3-zeta quality, optimized for SCF calculations
pc-4@“Polarization-consistent” generally contracted basis sets (H–Kr) of 4-zeta quality, optimized for SCF calculations
aug-pc-0@“Polarization-consistent” generally contracted basis sets (H–Kr) of 0-zeta quality, optimized for SCF calculations, augmented by diffuse functions
aug-pc-1@“Polarization-consistent” generally contracted basis sets (H–Kr) of 1-zeta quality, optimized for SCF calculations, augmented by diffuse functions
aug-pc-2@“Polarization-consistent” generally contracted basis sets (H–Kr) of 2-zeta quality, optimized for SCF calculations, augmented by diffuse functions
aug-pc-3@“Polarization-consistent” generally contracted basis sets (H–Kr) of 3-zeta quality, optimized for SCF calculations, augmented by diffuse functions, augmented by diffuse functions
aug-pc-4@“Polarization-consistent” generally contracted basis sets (H–Kr) of 4-zeta quality, optimized for SCF calculations, augmented by diffuse functions"""

basis_set_jensen_dft = """pcseg-0@Segmented PC basis sets (H–Kr) of 0-zeta quality, DFT-optimized
pcseg-1@Segmented PC basis sets (H–Kr) of 1-zeta quality, DFT-optimized
pcseg-2@Segmented PC basis sets (H–Kr) of 2-zeta quality, DFT-optimized
pcseg-3@Segmented PC basis sets (H–Kr) of 3-zeta quality, DFT-optimized
pcseg-4@Segmented PC basis sets (H–Kr) of 4-zeta quality, DFT-optimized
aug-pcseg-0@Segmented PC basis sets (H–Kr) of 0-zeta quality, DFT-optimized and augmented by diffuse functions
aug-pcseg-1@Segmented PC basis sets (H–Kr) of 1-zeta quality, DFT-optimized and augmented by diffuse functions
aug-pcseg-2@Segmented PC basis sets (H–Kr) of 2-zeta quality, DFT-optimized and augmented by diffuse functions
aug-pcseg-3@Segmented PC basis sets (H–Kr) of 3-zeta quality, DFT-optimized and augmented by diffuse functions
aug-pcseg-4@Segmented PC basis sets (H–Kr) of 4-zeta quality, DFT-optimized and augmented by diffuse functions"""

basis_set_jensen_shielding = """pcSseg-0@Segmented contracted basis sets (H–Kr)  of 0-zeta quality optimized for nuclear magnetic shielding
pcSseg-1@Segmented contracted basis sets (H–Kr)  of 1-zeta quality optimized for nuclear magnetic shielding
pcSseg-2@Segmented contracted basis sets (H–Kr)  of 2-zeta quality optimized for nuclear magnetic shielding
pcSseg-3@Segmented contracted basis sets (H–Kr)  of 3-zeta quality optimized for nuclear magnetic shielding
pcSseg-4@Segmented contracted basis sets (H–Kr)  of 4-zeta quality optimized for nuclear magnetic shielding
aug-pcSseg-0@Segmented contracted basis sets (H–Kr)  of 0-zeta quality optimized for nuclear magnetic shielding, augmented by diffuse functions
aug-pcSseg-1@Segmented contracted basis sets (H–Kr)  of 1-zeta quality optimized for nuclear magnetic shielding, augmented by diffuse functions
aug-pcSseg-2@Segmented contracted basis sets (H–Kr)  of 2-zeta quality optimized for nuclear magnetic shielding, augmented by diffuse functions
aug-pcSseg-3@Segmented contracted basis sets (H–Kr)  of 3-zeta quality optimized for nuclear magnetic shielding, augmented by diffuse functions
aug-pcSseg-4@Segmented contracted basis sets (H–Kr)  of 4-zeta quality optimized for nuclear magnetic shielding, augmented by diffuse functions"""


basis_set_jensen_spin_orbital = """pcJ-0@Segmented contracted basis sets (H–Ar) of 0-zeta quality optimized for spin-spin coupling constants
pcJ-1@Segmented contracted basis sets (H–Ar) of 1-zeta quality optimized for spin-spin coupling constants
pcJ-2@Segmented contracted basis sets (H–Ar) of 2-zeta quality optimized for spin-spin coupling constants
pcJ-3@Segmented contracted basis sets (H–Ar) of 3-zeta quality optimized for spin-spin coupling constants
pcJ-4@Segmented contracted basis sets (H–Ar) of 4-zeta quality optimized for spin-spin coupling constants
aug-pcJ-0@Segmented contracted basis sets (H–Ar) of 0-zeta quality optimized for spin-spin coupling constants,augmented by diffuse functions
aug-pcJ-1@Segmented contracted basis sets (H–Ar) of 1-zeta quality optimized for spin-spin coupling constants,augmented by diffuse functions
aug-pcJ-2@Segmented contracted basis sets (H–Ar) of 2-zeta quality optimized for spin-spin coupling constants,augmented by diffuse functions
aug-pcJ-3@Segmented contracted basis sets (H–Ar) of 3-zeta quality optimized for spin-spin coupling constants,augmented by diffuse functions
aug-pcJ-4@Segmented contracted basis sets (H–Ar) of 4-zeta quality optimized for spin-spin coupling constants,augmented by diffuse functions"""

basis_set_sapporo = """Sapporo-DZP-2012@DZP all-electron generally contracted non-relativistic basis sets (H–Xe)
Sapporo-TZP-2012@TZP all-electron generally contracted non-relativistic basis sets (H–Xe)
Sapporo-QZP-2012@QZP all-electron generally contracted non-relativistic basis sets (H–Xe)
Sapporo-DKH3-DZP-2012@DZP all-electron basis sets optimized for the DKH3Hamiltonian and finite nucleus (K–Rn)
Sapporo-DKH3-TZP-2012@TZP all-electron basis sets optimized for the DKH3Hamiltonian and finite nucleus (K–Rn)
Sapporo-DKH3-QZP-2012@QZP all-electron basis sets optimized for the DKH3Hamiltonian and finite nucleus (K–Rn)"""

basis_set_dunning = """cc-pVDZ@Dunning correlation-consistent polarized double-zeta
cc-pVTZ@Dunning correlation-consistent polarized triple-zeta
cc-pVQZ@Dunning correlation-consistent polarized quadruple-zeta
cc-pV5Z@Dunning correlation-consistent polarized quintuple-zeta
cc-pV6Z@Dunning correlation-consistent polarized sextuple-zeta
aug-cc-pVDZ@Dunning correlation-consistent polarized double-zeta, augmented with diffuse functions
aug-cc-pVTZ@Dunning correlation-consistent polarized triple-zeta, augmented with diffuse functions
aug-cc-pVQZ@Dunning correlation-consistent polarized quadruple-zeta, augmented with diffuse functions
aug-cc-pV5Z@Dunning correlation-consistent polarized quintuple-zeta, augmented with diffuse functions
aug-cc-pV6Z@Dunning correlation-consistent polarized sextuple-zeta, augmented with diffuse functions
cc-pCDTZ@Dunning correlation-consistent core polarized double-zeta
cc-pCVTZ@Dunning correlation-consistent core polarized triple-zeta
cc-pCVQZ@Dunning correlation-consistent core polarized quadruple-zeta
cc-pCV5Z@Dunning correlation-consistent core polarized quintuple-zeta
cc-pCV6Z@Dunning correlation-consistent core polarized sextuple-zeta
aug-cc-pCDTZ@Dunning correlation-consistent core polarized double-zeta, augmented with diffuse functions
aug-cc-pCVTZ@Dunning correlation-consistent core polarized triple-zeta, augmented with diffuse functions
aug-cc-pCVQZ@Dunning correlation-consistent core polarized quadruple-zeta, augmented with diffuse functions
aug-cc-pCV5Z@Dunning correlation-consistent core polarized quintuple-zeta, augmented with diffuse functions
aug-cc-pCV6Z@Dunning correlation-consistent core polarized sextuple-zeta, augmented with diffuse functions
cc-pwCDTZ@Dunning correlation-consistent core polarized double-zeta with weighted core functions
cc-pwCVTZ@Dunning correlation-consistent core polarized triple-zeta with weighted core functions
cc-pwCVQZ@Dunning correlation-consistent core polarized quadruple-zeta with weighted core functions
cc-pwCV5Z@Dunning correlation-consistent core polarized quintuple-zeta with weighted core functions
cc-pwCV6Z@Dunning correlation-consistent core polarized sextuple-zeta with weighted core functions
aug-cc-pwCDTZ@Dunning correlation-consistent core polarized double-zeta with weighted core functions, augmented with diffuse functions
aug-cc-pwCVTZ@Dunning correlation-consistent core polarized triple-zeta with weighted core functions, augmented with diffuse functions
aug-cc-pwCVQZ@Dunning correlation-consistent core polarized quadruple-zeta with weighted core functions, augmented with diffuse functions
aug-cc-pwCV5Z@Dunning correlation-consistent core polarized quintuple-zeta with weighted core functions, augmented with diffuse functions
aug-cc-pwCV6Z@Dunning correlation-consistent core polarized sextuple-zeta with weighted core functions, augmented with diffuse functions
cc-pVD(+d)Z@Dunning correlation-consistent polarized double-zeta with tight d functions
cc-pVT(+d)Z@Dunning correlation-consistent polarized triple-zeta with tight d functions
cc-pVQ(+dZ@Dunning correlation-consistent polarized quadruple-zeta with tight d functions
cc-pV5(+d)Z@Dunning correlation-consistent polarized quintuple-zeta with tight d functions
cc-pV6(+d)Z@Dunning correlation-consistent polarized sextuple-zeta with tight d functions"""

# TODO, change n 
basis_set_partially_augmented = """apr-cc-pV(Q+d)Z@Augmented with sp diffuse functions on Li–Ca
may-cc-pV(T+d)Z@sp diffuse functions on Li–Ca
may-cc-pV(Q+d)Z@spd diffuse functions on Li–Ca
jun-cc-pV(D+d)Z@sp diffuse functions on Li–Ca
jun-cc-pV(T+d)Z@spd diffuse functions on Li–Ca
jun-cc-pV(Q+d)Z@spdf diffuse functions on Li–Ca
jul-cc-pV(D+d)Z@spd diffuse functions on Li–Ca
jul-cc-pV(T+d)Z@spdf diffuse functions on Li–Ca
jul-cc-pV(Q+d)Z@spdfg diffuse functions on Li–Ca
maug-cc-pV(D+d)Z@sp diffuse functions on Li–Ca 
maug-cc-pV(T+d)Z@sp diffuse functions on Li–Ca
maug-cc-pV(Q+d)Z@ Augmented with sp diffuse functions on Li–Ca"""


# Only for use with DKH
basis_set_cc_dkh = """cc-pVDZ-DK@Correlation-consistent all-electron basis sets for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian. Polarized double-zeta
cc-pVTZ-DK@Correlation-consistent all-electron basis sets for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian. Polarized triple-zeta
cc-pVQZ-DK@Correlation-consistent all-electron basis sets for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian. Polarized quadruple-zeta
cc-pV5Z-DK@Correlation-consistent all-electron basis sets for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian. polarized quintuple-zeta
aug-cc-pVDZ-DK@Correlation-consistent all-electron basis sets for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian. Polarized double-zeta augmented with diffuse functions
aug-cc-pVTZ-DK@Correlation-consistent all-electron basis sets for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian. Polarized triple-zeta augmented with diffuse functions
aug-cc-pVQZ-DK@Correlation-consistent all-electron basis sets for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian. Polarized quadruple-zeta augmented with diffuse functions
aug-cc-pV5Z-DK@Correlation-consistent all-electron basis sets for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian. polarized quintuple-zeta augmented with diffuse functions
cc-pwCVDZ-DK@Correlation-consistent all-electron basis sets for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian. Polarized double-zeta and using weighted core correlation
cc-pwCVTZ-DK@Correlation-consistent all-electron basis sets for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian. Polarized triple-zeta and using weighted core correlation
cc-pwCVQZ-DK@Correlation-consistent all-electron basis sets for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian. Polarized quadruple-zeta and using weighted core correlation
cc-pwCV5Z-DK@Correlation-consistent all-electron basis sets for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian. polarized quintuple-zeta and using weighted core correlation
aug-cc-pwCVDZ-DK@Correlation-consistent all-electron basis sets for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian. Polarized double-zeta and using weighted core correlation and augmented with diffuse functions
aug=cc-pwCVTZ-DK@Correlation-consistent all-electron basis sets for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian. Polarized triple-zeta and using weighted core correlation and augmented with diffuse functions 
aug-cc-pwCVQZ-DK@Correlation-consistent all-electron basis sets for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian. Polarized quadruple-zeta and using weighted core correlation and augmented with diffuse functions
aug-cc-pwCV5Z-DK@Correlation-consistent all-electron basis sets for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian. polarized quintuple-zeta and using weighted core correlation and augmented with diffuse functions
cc-pVDZ-DK3@Correlation-consistent all-electron basis sets for lanthanides and actinides with the 3rd-order Douglas-KrollHess Hamiltonian using polarized double zeta
cc-pVTZ-DK3@Correlation-consistent all-electron basis sets for lanthanides and actinides with the 3rd-order Douglas-KrollHess Hamiltonian using polarized triple zeta
cc-pVQZ-DK3@Correlation-consistent all-electron basis sets for lanthanides and actinides with the 3rd-order Douglas-KrollHess Hamiltonian using polarized quadruple zeta 
cc-pwCVDZ-DK3@Correlation-consistent all-electron basis sets for lanthanides and actinides with the 3rd-order Douglas-KrollHess Hamiltonian using polarized double zeta using weighted core correlation
cc-pwCVTZ-DK3@Correlation-consistent all-electron basis sets for lanthanides and actinides with the 3rd-order Douglas-KrollHess Hamiltonian using polarized triple zeta using weighted core correlation
cc-pwCVQZ-DK3@Correlation-consistent all-electron basis sets for lanthanides and actinides with the 3rd-order Douglas-KrollHess Hamiltonian using polarized quadruple zeta using weighted core correlation"""

basis_set_ecp = """cc-pVDZ-PP@Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using double polarized zeta
cc-pVTZ-PP@Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using triple polarized zeta
cc-pVQZ-PP@Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using quadruple polarized zeta
cc-pV5Z-PP@Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using quintuple polarized zeta
aug-cc-pVDZ-PP@Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using double polarized zeta, augmented with diffuse functions
aug-cc-pVTZ-PP@Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using triple polarized zeta, augmented with diffuse functions
aug-cc-pVQZ-PP@Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using quadruple polarized zeta, augmented with diffuse functions
aug-cc-pV5Z-PP@Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using quintuple polarized zeta, augmented with diffuse functions
cc-pVDZ-PP@Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using double polarized zeta and weighted core functions
cc-pVTZ-PP@Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using triple polarized zeta and weighted core functions
cc-pVQZ-PP@Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using quadruple polarized zeta and weighted core functions
cc-pV5Z-PP@Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using quintuple polarized zeta and weighted core functions
aug-cc-pVDZ-PP@Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using double polarized zeta and weighted core functions and augmented with diffuse functions
aug-cc-pVTZ-PP@Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using triple polarized zeta and weighted core functions and augmented with diffuse functions
aug-cc-pVQZ-PP@Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using quadruple polarized zeta and weighted core functions and augmented with diffuse functions
aug-cc-pV5Z-PP@Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using quintuple polarized zeta and weighted core functions and augmented with diffuse functions"""

# For F12 calculations
basis_set_f12 = """cc-pVDZ-F12@Special orbital basis sets for F12 calculations using double polarized zeta
cc-pVTZ-F12@Special orbital basis sets for F12 calculations using triple polarized zeta
cc-pVQZ-F12@Special orbital basis sets for F12 calculations using quadruple polarized zeta
cc-pCVDZ-F12@Special orbital basis sets for F12 calculations using double polarized zeta with core polarization functions
cc-pCVTZ-F12@Special orbital basis sets for F12 calculations using triple polarized zeta with core polarization functions
cc-pCVQZ-F12@Special orbital basis sets for F12 calculations using quadruple polarized zeta with core polarization functions
cc-pVDZ-PP-F12@ECP-based version of a special orbital basis sets for F12 calculations using double polarized zeta
cc-pVTZ-PP-F12@ECP-based version of a special orbital basis sets for F12 calculations using triple polarized zeta
cc-pVQZ-PP-F12@ECP-based version of a special orbital basis sets for F12 calculations using quadruple polarized zeta"""

basis_set_auxilary_cabs= """cc-pVDZ-F12-CABS@Near-complete auxiliary basis sets for F12 calculations with double polarized zeta
cc-pVTZ-F12-CABS@Near-complete auxiliary basis sets for F12 calculations with triple polarized zeta
cc-pVQZ-F12-CABS@Near-complete auxiliary basis sets for F12 calculations with quadruple polarized zeta
cc-pVDZ-F12-OptRI@Near-complete auxiliary basis sets for F12 calculations with double polarized zeta
cc-pVTZ-F12-OptRI@Near-complete auxiliary basis sets for F12 calculations with triple polarized zeta
cc-pVQZ-F12-OptRI@Near-complete auxiliary basis sets for F12 calculations with quadruple polarized zeta
cc-pCVDZ-F12-OptRI@Near-complete auxiliary basis sets for F12 calculations with double polarized zeta with core polarization functions
cc-pCVTZ-F12-OptRI@Near-complete auxiliary basis sets for F12 calculations with triple polarized zeta with core polarization functions
cc-pCVQZ-F12-OptRI@Near-complete auxiliary basis sets for F12 calculations with quadruple polarized zeta with core polarization functions
cc-pVDZ-PP-F12-OptRI@ECP-based version of Near-complete auxiliary basis sets for F12 calculations with double polarized zeta
cc-pVTZ-PP-F12-OptRI@ECP-based version of Near-complete auxiliary basis sets for F12 calculations with triple polarized zeta
cc-pVQZ-PP-F12-OptRI@ECP-based version of Near-complete auxiliary basis sets for F12 calculations with quadruple polarized zeta
aug-cc-pVDZ-PP-OptRI@Near-complete auxiliary basis sets for F12 calculations. Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using double polarized zeta and core polarization functions and augmented with diffuse functions
aug-cc-pVTZ-PP-OptRI@Near-complete auxiliary basis sets for F12 calculations. Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using triple polarized zeta and core polarization functions and augmented with diffuse functions
aug-cc-pVQZ-PP-OptRI@Near-complete auxiliary basis sets for F12 calculations. Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using quadruple polarized zeta and core polarization functions and augmented with diffuse functions
aug-cc-pV5Z-PP-OptRI@Near-complete auxiliary basis sets for F12 calculations. Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using quintuple polarized zeta and core polarization functions and augmented with diffuse functions
aug-cc-pwCVDZ-PP-OptRI@Near-complete auxiliary basis sets for F12 calculations. Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using double polarized zeta and weighted core functions and augmented with diffuse functions
aug-cc-pwCVTZ-PP-OptRI@Near-complete auxiliary basis sets for F12 calculations. Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using triple polarized zeta and weighted core functions and augmented with diffuse functions
aug-cc-pwCVQZ-PP-OptRI@Near-complete auxiliary basis sets for F12 calculations. Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using quadruple polarized zeta and weighted core functions and augmented with diffuse functions
aug-cc-pwCV5Z-PP-OptRI@Near-complete auxiliary basis sets for F12 calculations. Correlation-consistent basis sets combined with SK-MCDHF-RSC effective core potentials, using quintuple polarized zeta and weighted core functions and augmented with diffuse functions"""

basis_set_atomic_natural = """ANO-pVDZ@Newly contracted ANO basis set, using double polarized Zeta on the basis of the cc-pV6Z (or pc-4 where missing) primitives. These are very accurate basis sets that are significantly better than the cc-pVnZ counterparts for the same number of basis functions (but much larger number of primitives of course).
ANO-pVTZ@Newly contracted ANO basis set, using triple polarized Zeta on the basis of the cc-pV6Z (or pc-4 where missing) primitives. These are very accurate basis sets that are significantly better than the cc-pVnZ counterparts for the same number of basis functions (but much larger number of primitives of course).
ANO-pVQZ@Newly ontracted ANO basis set, using quadruple polarized Zeta on the basis of the cc-pV6Z (or pc-4 where missing) primitives. These are very accurate basis sets that are significantly better than the cc-pVnZ counterparts for the same number of basis functions (but much larger number of primitives of course).
ANO-pV5Z@newly contracted ANO basis set, using quintuple polarized Zeta on the basis of the cc-pV6Z (or pc-4 where missing) primitives. These are very accurate basis sets that are significantly better than the cc-pVnZ counterparts for the same number of basis functions (but much larger number of primitives of course).
ANO-pV6Z@newly contracted ANO basis set, using sixtuple polarized Zeta on the basis of the cc-pV6Z (or pc-4 where missing) primitives. These are very accurate basis sets that are significantly better than the cc-pVnZ counterparts for the same number of basis functions (but much larger number of primitives of course).
saug-ANO-pVDZ@newly contracted ANO basis set, using double polarized Zeta on the basis of the cc-pV6Z (or pc-4 where missing) primitives. With augmentation with a single set of sp functions. Greatly enhances the accuracy of the SCF energies but not for correlation energies.
saug-ANO-pVTZ@newly contracted ANO basis set, using triple polarized Zeta on the basis of the cc-pV6Z (or pc-4 where missing) primitives. With augmentation with a single set of sp functions. Greatly enhances the accuracy of the SCF energies but not for correlation energies.
saug-ANO-pVQZ@newly contracted ANO basis set, using quadruple polarized Zeta on the basis of the cc-pV6Z (or pc-4 where missing) primitives. With augmentation with a single set of sp functions. Greatly enhances the accuracy of the SCF energies but not for correlation energies.
saug-ANO-pV5Z@newly contracted ANO basis set, using quintuple polarized Zeta on the basis of the cc-pV6Z (or pc-4 where missing) primitives. With augmentation with a single set of sp functions. Greatly enhances the accuracy of the SCF energies but not for correlation energies.
aug-ANO-pVDZ@newly contracted ANO basis set, using double polarized Zeta on the basis of the cc-pV6Z (or pc-4 where missing) primitives with full augmentation with spd, spdf, spdfg set of polarization functions. Almost as expensive as the next higher basis set. In fact, aug-ANO-pVnZ = ANO-pV(n + 1)Z with the highest angular momentum polarization function deleted
aug-ANO-pVTZ@newly contracted ANO basis set, using triple polarized Zeta on the basis of the cc-pV6Z (or pc-4 where missing) primitives with full augmentation with spd, spdf, spdfg set of polarization functions. Almost as expensive as the next higher basis set. In fact, aug-ANO-pVnZ = ANO-pV(n + 1)Z with the highest angular momentum polarization function deleted
aug-ANO-pVQZ@newly contracted ANO basis set, using quadtruple polarized Zeta on the basis of the cc-pV6Z (or pc-4 where missing) primitives with full augmentation with spd, spdf, spdfg set of polarization functions. Almost as expensive as the next higher basis set. In fact, aug-ANO-pVnZ = ANO-pV(n + 1)Z with the highest angular momentum polarization function deleted
aug-ANO-pV5Z@newly contracted ANO basis set, using quintuple polarized Zeta on the basis of the cc-pV6Z (or pc-4 where missing) primitives with full augmentation with spd, spdf, spdfg set of polarization functions. Almost as expensive as the next higher basis set. In fact, aug-ANO-pVnZ = ANO-pV(n + 1)Z with the highest angular momentum polarization function deleted"""

basis_set_atomic_natural_relativistic_contracted = """ANO-RCC-FULL@The complete ANO-RCC basis sets (H-Cm).
ANO-RCC-TZP@The ANO-RCC basis sets (H-Cm) contracted with TZP.
ANO-RCC-QZP@The ANO-RCC basis sets (H-Cm) contracted with QZP.
ANO-RCC-DZP@The ANO-RCC basis sets (H-Cm) contracted with DZP."""

basis_set_specialized = """D95@Dunning’s double-zeta basis set (H–Cl).
D95p@Polarized version of D95.
MINI@Huzinaga’s minimal basis set.
MINIS@Scaled version of the MINI.
MIDI@Huzinaga’s valence double-zeta basis set.
MINIX@Combination of small basis sets by Grimme (see Table 9.7). Wachters+f First-row transition metal basis set (Sc–Cu). Partridge-n (n = 1, 2, 3, 4) Uncontracted basis sets by Partridge.
LANL2DZ@Los Alamos valence double-zeta with Hay–Wadt ECPs.
LANL2TZ@Triple-zeta version.
LANL2TZ(f)@Triple-zeta plus polarization.
LANL08@Uncontracted basis set.
LANL08(f)@Uncontracted basis set + polarization.
EPR-II@Barone’s basis set (H, B–F) for EPR calculations (double-zeta).
EPR-III@Barone’s basis set for EPR calculations (triple-zeta).
IGLO-II@Kutzelnigg’s basis set (H, B–F, Al–Cl) for NMR and EPR calculations.
IGLO-III@Larger version of the above.
aug-cc-pVTZ-J@Sauer’s basis set for accurate hyperfine coupling constants.""",
