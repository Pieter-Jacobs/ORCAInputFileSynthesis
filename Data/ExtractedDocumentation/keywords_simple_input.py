
# TODO EXTRAPOLATION KEYWORDS
# Extrapolate (n/m, bas)@Extrapolation of the basis set family "bas" (bas=cc,aug-cc, cc-core, ano, sang-ano, aug-ano, def2; if omitted "cc-pVnZ" is used) for cardinal numbers n.m (n<m=2,3,4,5), e.g. Extrapolate(2/3,cc) extrapolates the SCF, MP2 and MDCI energies to the basis set limit. "core" refers to basis sets with core correlation function. In this case the frozen core approximation is by default turned off. This setting can be overridden in the "methods" block if one just wants to use the basis set with core correlation functions (steep primitives) but without unfreezing the core electrons.
# Extrapolate (n, bas)@Calculate the first n-energies for member of the basis set family basis, e.g. Extrapolate (3) is doing calculations with cr-pVDZ, ce-pVTZ and ex-pVQZ. Similar: performs SCF, MP2 and MDCI calculations. The higher basis set can only be done with DLPNO-CCSD(T) or MP2 methods and then used to extrapolate the MDCI calculation to the basis set limit.
# Extrapolate EP2 (n/m, bas, [method, method-details])s@Similar to EP2: for the high basis set method we go one cardinal number higher.

# --------------------------GRID input block keywords----------------------------------- #
dft_grid_keywords = """DefGrid1@First default grid points for Numerical Integration
DefGrid2@second default grid points for Numerical Integration
DefGrid3@heavier, higher-quality grid or Numerical Integration, that is close to the limit if one considers an enormous grid as a reference.
NOCOSX@turn off COSX approximation
NOFINALGRIDX@Turns off the final grid in COSX"""

# --------------------------METHOD input block keywords----------------------------------- #
general_computational_methods = """HF@Selects the Hartree–Fock method
DFT@Selects the DFT method
FOD@FOD analysis employing default settings (TPSS/def2-TZVP, TightSCF, SmearTemp = 5000 K)"""

# Type of runtype when already having selected a method
runtype_computation = """ENERGY@Selects a single point calculation
SP@Selects a single point calculation
OPT@Selects a geometry optimization calculation (using internal redundant coordinates)
CI-OPT@Selects a CI optimization calculation (using internal redundant coordinates)
COPT@Optimization in Cartesian coordinates
ZOPT@Optimization in Z-matrix coordinates
GDIIS-COPT@Optimization in Cartesian coordinates using GDIIS
GDIIS-ZOPT@Optimization in Z-matrix coordinates using GDIIS
GDIIS-OPT@Normal optimization using GDIIS
ENGRAD@Selects an energy and gradient calculation
NUMGRAD@Calculate numerical gradient
NUMFREQ@Calculate a numerical frequency calculation
ANFREQ@Run an analytical harmonic frequency calculation
NUMNACME@Numerical non-adiabatic coplings
MD@Molecular dynamic simulation 
CIM@Cluster-In-Molecule calculation"""

method_extra_options = """Mass2016@ Use the latest atomic masses of the most abundant or most stable isotopes instead of atomic weights.
NoPropFile@Turns writing to property file off (default is on for everything except MD and L-Opt calculations)"""

# Frozen core is used by default in MP2
frozen_core = """FROZENCORE@Use a frozen core. By default this is done by counting the number of chemical core 
FC_NONE@Use a frozen core with an orbital energy window
NOFROZENCORE@Do not use a frozen core"""

# Use ri approximation in DFT (so only usable with a DFT method). RI needs to be used with Correlation fitting
ri_computation_for_dft = """RI@Sets RI=true to use the RI approximation in DFT calculations. Default to Split-RI-J
Split-RI-J@Sets RI=true to use the RI approximation in DFT calculations.
RIJONX@RI-J for the Coulomb integrals only and no approximation applied to HF Exchange
NORI@Sets RI=false for using RI approximation 
RIJCOSX@Sets the flag for the efficient RIJCOSXalgorithm (treat the Coulomb term via RI and the Exchange term via seminumerical integration)
"""

# Can also be used with HF, aside from dft. Can only be used with /J or /K in combination with a /C basis set
ri_computation_for_hf_and_dft="""RI-JK@Sets the flag for the efficient RI algorithm for Coulomb and Exchange. Works for SCF (HF/DFT) energies and gradients. Works direct or conventional.
RIJK@Sets the flag for the efficient RI algorithm for Coulomb and Exchange. Works for SCF (HF/DFT) energies and gradients. Works direct or conventional.
RIJCOSX@Sets the flag for the efficient RIJCOSXalgorithm (treat the Coulomb term via RI and the Exchange term via seminumerical integration).
RIJDX@RI-J for the Coulomb integrals only and no approximation applied to HF Exchange
RIJONX@RI-J for the Coulomb integrals only and no approximation applied to HF Exchange"""

# ----------------- Symmetry input block keywords -------------------- #
symmetry_handling = """UseSym@Turns on the use of molecular symmetry. 
NoUseSym@Turns the use of molecular symmetry of"""

# ------------------- MP2 input block keywords ---------------------------#
# Recommended to use RI-SCS-MP2 instead of normal SCS-MP2. Same foor OO-RI
# Dont use linearly dependent basis sets with MP2
# When using orbital optimization, use NOITER as well
basic_mp2_methods = """MP2@Selects Method=HF and DoMP2=true
MP2RI@Select the MP2-RI method
RI-MP2@Select the MP2-RI method
SCS-MP2@Spin-component scaled MP2
RI-SCS-MP2@Spin-component scaled RI-MP2
SCS-RI-MP2@Spin-component scaled RI-MP2 
OO-RI-MP2@Orbital optimized RI-MP2
OO-RI-SCS-MP2@Orbital optimized and spin-component scaled RI-MP2
MP2-F12@MP2 with F12 correction 
F12-MP2@MP2 with F12 correction 
MP2-F12-RI@MP2-RI with RI-F12 correction
MP2-F12D-RI@MP2-RI with RI-F12 correction employing the D approximation 
F12-RI-MP2@MP2-RI with RI-F12 correction employing the D approximation 
RI-MP2-F12@MP2-RI with RI-F12 correction employing the D approximation"""

local_correlation_mp2_methods = """DLPNO-MP2@Local MP2
DLPNO-SCS-MP2@Spin-component scaled Local (DLPNO) MP2
SCS-DLPNO-MP2@Spin-component scaled Local (DLPNO) MP2
DLPNO-MP2-F12@Local (DLPNO) MP2 with F12 correction employing an efficient form of the Cap approximation
DLPNO-MP2-F12/D@Local (DLPNO) MP2 with F12 correction employing an efficient form of the Cap approximation with approach D (less expensive than the C approximation)
DLPNO-CCSD-F12@DLPNO-CCSD with F12 correction employing an efficient form of the Cap approximation
DLPNO-CCSD-F12/D@DLPNO-CCSD-F12 with approach D (less expensive than the C approximation)
DLPNO-CCSD(T)-F12@DLPNO-CCSD(T) with F12 correction employing an efficient form of the C approximation
DLPNO-CCSD(T)-F12/D@DLPNO-CCSD(T)-F12 with approach D (less expensive than the C approximation)
DLPNO-CCSD(T1)-F12@DLPNO-CCSD(T1) with F12 correction employing an efficient form of the C approximation
DLPNO-CCSD(T)-F12/D@DLPNO-CCSD(T)-F12 with approach D (less expensive than the C approximation)
DLPNO-NEVPT2@DLPNO-NEVPT2 requires a CASSCF block
DLPNO-B2PLYP@Domain Localized Pair Natural Orbital - Second-order Perturbation Theory using B2PLYP functional"""

# Accuracy control for PNO (DPLNO in MP2 and DPLNO in MCDI)
accuracy_control = """LoosePNO@Selects loose DLPNO thresholds
NormalPNO@Selects default DLPNO thresholds
TightPNO@Selects tight DLPNO thresholds
DLPNO-HFC1@Tightened truncation setting for DLPNO-CCSD hyperfine coupling constants calculation.
DLPNO-HFC2@Tighter truncation setting than for DLPNO-HFC1"""

# ------------------- MDCI (single reference correlation) input block keywords ---------------------------# 
ci_type = """CCSD@Coupled-cluster singles and doubles. Perform a full four index transformation
MO-CCSD@Coupled-cluster singles and doubles. Perform a full four index transformation
AOX-CCSD@Coupled-cluster singles and doubles. Compute the 3- and 4-external contributions from stored AO integrals.
AO-CCSD@Coupled-cluster singles and doubles. Compute the 3- and 4-external contributions on the fly.
RI-CCSD@Coupled-cluster singles and doubles. Make the density fitting approximation operative
RI34-CCSD@Coupled-cluster singles and doubles. Make the density fitting approximation operative for 3rd and 4th integrals
CCSD(T)@Coupled-cluster singles and doubles with perturbative triples correction. Perform a full four index transformation
MO-CCSD(T)@Coupled-cluster singles and doubles with perturbative triples correction. Perform a full four index transformation
AOX-CCSD(T)@Coupled-cluster singles and doubles with perturbative triples correction. Compute the 3- and 4-external contributions from stored AO integrals.
AO-CCSD(T)@Coupled-cluster singles and doubles with perturbative triples correction. Compute the 3- and 4-external contributions on the fly.
RI-CCSD(T)@Coupled-cluster singles and doubles with perturbative triples correction. Make the density fitting approximation operative
RI34-CCSD(T)@Coupled-cluster singles and doubles with perturbative triples correction. Make the density fitting approximation operative for 3rd and 4th integrals
CCSD-F12@Coupled-cluster singles and doubles with F12 correction
CCSD(T)-F12@Coupled-cluster singles and doubles with perturbative triples correction with F12 correction
CCSD-F12/RI@Coupled-cluster singles and doubles with F12 correction with RI-F12 correction
CCSD-F12D/RI@Coupled-cluster singles and doubles with RI-F12 correction employing the D approximation (less expensive)
CCSD(T)-F12/RI@Coupled-cluster singles and doubles with perturbative triples correction with RI-F12 correction
CCSD(T)-F12D/RI@Coupled-cluster singles and doubles with perturbative triples correction with RI-F12 correction employing the D approximation (less expensive)
CISD@Configuration interaction. Perform a full four index transformation
MO-CISD@Configuration interaction. Perform a full four index transformation
AOX-CISD@Configuration interaction. Compute the 3- and 4-external contributions from stored AO integrals.
AO-CISD@Configuration . Compute the 3- and 4-external contributions on the fly.
RI-CISD@Configuration interaction. Make the density fitting approximation operative
RI34-CISD@Configuration interaction. Make the density fitting approximation operative for 3rd and 4th integrals
QCISD@Quadratic Configuration interaction. Perform a full four index transformation
MO-QCISD@Quadratic Configuration interaction. Perform a full four index transformation
AOX-QCISD@Quadratic Configuration interaction. Compute the 3- and 4-external contributions from stored AO integrals.
AO-QCISD@Quadratic Configuration interaction. Compute the 3- and 4-external contributions on the fly.
RI-QCISD@Quadratic Configuration interaction. Make the density fitting approximation operative
RI34-QCISD@Quadratic Configuration interaction. Make the density fitting approximation operative for 3rd and 4th integrals
QCISD(T)@Quadratic Configuration interaction with perturbative triples correction
MO-QCISD(T)@Quadratic Configuration interaction with perturbative triples correction. Perform a full four index transformation
AOX-QCISD(T)@Quadratic Configuration interaction with perturbative triples correction. Compute the 3- and 4-external contributions from stored AO integrals.
AO-QCISD(T)@Quadratic Configuration interaction with perturbative triples correction. Compute the 3- and 4-external contributions on the fly.
RI-QCISD(T)@Quadratic Configuration interaction with perturbative triples correction. Make the density fitting approximation operative
RI34-QCISD(T)@Quadratic Configuration interaction with perturbative triples correction. Make the density fitting approximation operative for 3rd and 4th integrals
QCISD-F12@Quadratic Configuration interaction with F12 correction
QCISD(T)-F12@Quadratic Configuration interaction with F12 correction with F12 correction
QCISD-F12/RI@Quadratic Configuration interaction with RI-F12 correction
QCISD(T)-F12/RI@Quadratic Configuration interaction with perturbative triples correction and RI-F12 correction
CPF/1@Coupled-pair functional. Perform a full four index transformation
MO-CPF/1@Coupled-pair functional. Perform a full four index transformation
AOX-CPF/1@Coupled-pair functional. Compute the 3- and 4-external contributions from stored AO integrals.
AO-CPF/1@Coupled-pair functional. Compute the 3- and 4-external contributions on the fly.
RI-CPF/1@Coupled-pair functional. Make the density fitting approximation operative
RI34-CPF/1@Coupled-pair functional. Make the density fitting approximation operative for 3rd and 4th integrals
NCPF/1@A "new" modified Coupled-pair functional. Perform a full four index transformation
MO-NCPF/1@A "new" modified Coupled-pair functional. Perform a full four index transformation
AOX-NCPF/1@A "new" modified Coupled-pair functional. Compute the 3- and 4-external contributions from stored AO integrals.
AO-NCPF/1@A "new" modified Coupled-pair functional. Compute the 3- and 4-external contributions on the fly.
RI-NCPF/1@A "new" modified Coupled-pair functional. Make the density fitting approximation operative
RI34-NCPF/1@A "new" modified Coupled-pair functional. Make the density fitting approximation operative for 3rd and 4th integrals
CEPA/1@Coupled-electron-pair approximation. Perform a full four index transformation
MO-CEPA/1@Coupled-electron-pair approximation. Perform a full four index transformation
AOX-CEPA/1@Coupled-electron-pair approximation. Compute the 3- and 4-external contributions from stored AO integrals.
AO-CEPA/1@Coupled-electron-pair approximation. Compute the 3- and 4-external contributions on the fly.
RI-CEPA/1@Coupled-electron-pair approximation. Make the density fitting approximation operative
RI34-CEPA/1@Coupled-electron-pair approximation. Make the density fitting approximation operative for 3rd and 4th integrals
NCEPA/1@A "new" modified Coupled-pair functional.Coupled-electron-pair approximation. Perform a full four index transformation
MO-NCEPA/1@A "new" modified Coupled-pair functional. Coupled-electron-pair approximation. Perform a full four index transformation
AOX-NCEPA/1@A "new" modified Coupled-pair functional. Coupled-electron-pair approximation. Compute the 3- and 4-external contributions from stored AO integrals.
AO-NCEPA/1@A "new" modified Coupled-pair functional. Coupled-electron-pair approximation. Compute the 3- and 4-external contributions on the fly.
RI-NCEPA/1@A "new" modified Coupled-pair functional. Coupled-electron-pair approximation. Make the density fitting approximation operative
RI34-NCEPA/1@A "new" modified Coupled-pair functional. Coupled-electron-pair approximation. Make the density fitting approximation operative for 3rd and 4th integrals
RI-CEPA/1-F12@RI-CEPA with F12 correction
MP3@MP3 energies
SCS-MP3@Grimme's refined version of MP3"""
# RI-METHOD@Make the density fitting approximation operative
# RI34-METHOD@Make the density fitting approximation operative for 3rd and 4th integrals
# MO-METHOD@Perform a full four index transformation
# AO-METHOD@Compute the 3- and 4-external contributions on the fly 
# AOX-METHOD@Compute the 3- and 4-external contributions from stored AO integrals.

# These must be used together with auxiliary correlation fitting basis sets
local_correlation_mcdi_methods = """LPNO-CEPA/1@Local pair natural orbital CEPA methods
LPNO-CPF/1@Local pair natural orbital CEPA methods coupled-pair functionals
LPNO-NCEPA/1@Local pair natural orbital CEPA methods modified versions
LPNO-NCPF/1@Various Local pair natural orbital CEPA methods for modified versions
LPNO-QCISD@Local pair natural orbital CEPA methods for quadratic CI with singles and doubles
LPNO-CCSD@Local pair natural orbital for coupled-cluster theory with single and double excitations
DLPNO-CCSD@Domain based local pair natural orbital coupled-cluster method with single and double excitations (closed-shell only)
DLPNO-CCSD(T)@Domain based local pair natural orbital coupled-cluster method with perturbative triple excitations
DLPNO-CCSD(T1)@Domain based local pair natural orbital coupled-cluster method with iterative perturbative triple excitations CCSD(T1)"""

# There needs to be an input block with the number of roots
mdci_methods_for_excited_states = """EOM-CCSD@Equation of Motion CCSD
bt-PNO-EOM-CCSD@back-transformed PNO approximation
STEOM-CCSD@Similarity Transformed Equation of Motion CCSD
bt-PNO-STEOM-CCSD@back-transformed PNO approximation
STEOM-DLPNO-CCSD@The STEOM-DLPNO-CCSD method uses the full potential of DLPNO to reduce the computational scaling while keeping the accuracy of STEOM-CCSD.
IP-EOM-DLPNO-CCSD@IP version of the STEOM-DLPNO-CCSD method uses the full potential of DLPNO to reduce the computational scaling while keeping the accuracy of STEOM-CCSD.
EA-EOM-DLPNO-CCSD@EA version of the STEOM-DLPNO-CCSD method uses the full potential of DLPNO to reduce the computational scaling while keeping the accuracy of STEOM-CCSD.
DIJCOSX-EOM-Lential of DLPNO to reduce the computational scaling while keeping the accuracy of STEOM-CCSD.
IH-FSMR-CCSD@Fock-Space CCPNO-CCSD@IJ Chain Of Spheres version of the STEOM-DLPNO-CCSD method uses the full potSD using an intermediate Hamiltonian
bt-PNO-IH-FSMR-CCSD@back-transformed PNO approximation"""

# Fully internally contracted methods that assume a lot of parameters (AUTOCI)
autoci_methods = """FIC-MRCI@Fully internally contracted MRCI
FIC-DDCI3@Fully internally contracted DDC13
FIC-CEPA0@Fully internally contracted CEPAO
FIC-ACPF@Fully internally contracted ACPF
FIC-AQCC@Fully internally contracted AQCC
FIC-MRCC@Fully internally contracted CCSD"""

# ------------------- CASSCF input block keywords ---------------------------# 
casscf_step_option = """DMRG@DMRG as "CIStep" in CASSCF"""
casscf_PT_methods = """NEVPT2@SC NEVPT2
SC-NEVPT2@SC-NEVPT2 same as NEVPT2
RI-NEVPT2@SC-NEVPT2 with the RI approximation
FIC-NEVPT2@FIC-NEVPT2 aka PC-NEVPT2
DLPNO-NEVPT2@FIC-NEVPT2 in the framework of DLPNO
CASPT2@FIC-CASPT2
RI-CASPT2@FIC-CASPT2 with the RI approximation"""
casscf_dynamic_correlation = """DCD-CAS(2)@2nd order Dynamic Correlation Dressed CAS
RI-DCD-CAS(2)@2nd order Dynamic Correlation DressedCAS with RI approximation"""


# ------------------- MRCI input block keywords -------------------------# 
# These are mainly for expert users, because there are a lot of flags
mrci_calculation_types = """MRCI@Multireference configuration interaction calculation with single and double excitations
MRCI+Q@Same with multireference Davidson correction for unlinked quadruples
MRACPF@Average coupled-pair functional
MRAQCC@Average quadratic coupled-cluster
MRDDCII@Difference dedicated CI with one degree of freedom
MRDDC12@Same with two degrees of freedom
MRDDC13@Same with three degrees of freedom MRDDCI with Davidson correction
MRDDCIn+Q@MRDDCI with Davidson correction
SORCI@Spectroscopy oriented CI"""


# ------------------- Semiemprical methods -------------------------# 
semiemperical_methods= """ZINDO/S@Selects the ZINDO/S method
ZINDO/1@Selects the ZINDO/1 method
ZINDO/2@Selects the ZINDO/2 method
NDDO/1@Selects the NDDO/1 method
NDDO/2@Selects the NDDO/2 method
MNDO@Selects the MNDO method
AM1@Selects the AM1 method
PM3@Selects the PM3 method"""

# ------------------- SCF input block keywords -------------------------# 
scf_hartree_fock_type = """RHF@Selects closed-shell SCF
RKS@Selects closed-shell SCF
UHF@Selects spin unrestricted SCF
UKS@Selects spin unrestricted SCF
ROHF@Selects open-shell spin restricted SCF
ROKS@Selects open-shell spin restricted SCF"""

# Can only be used when RI is used
scf_coulomb_matrix_calculation_for_ri = """SPLITJ@Select the efficient Split-J procedure for the calculation of the Coulomb matrix in non-hybrid DFT (rarely used)
SPLIT-RI-J@Select the efficient Split-RI-J procedure for the improved evaluation of the RI approximation to the Coulomb-matrix
NoSplit-RI-J@Turns the Split-RI-J feature off (but does not set the RI flag to false!)
RI-J-XC@Turn on RI for the Coulomb term and the XC terms. This saves time when the XC integration is significant but introduces another basis set incompleteness error. (rarely used)"""

scf_extra_options="""UNO@Produce UHF natural orbitals
UCO@Calculate and plot the unrestricted corresponding orbitals
AllowRHF@Allow a RHF calculation even if the system is open-shell (Mult>1). Default is to switch to UHF then
NOITER@Sets the number of SCF iterations to 0. This works together with MOREAD and means that the program will work with the provided starting orbitals
FRACOCC@Turns the fractional occupation option on (FOD is always calculated)
SCFConvergenceForced@Lets the user insist on a fully converged SCF for a geometry optimization"""

scf_integral_calculation="""DIRECT@Selects an integral direct calculation
CONV@Selects an integral conventional calculation"""

scf_use_smear = """SMEAR@Sets temperature for occupation number smearing (default 5000 K; FOD is always calculated)
NOSMEAR@Turns occupation number smearing off"""

scf_keep_ints = """KEEPINTS@Keeps two-electron integrals on disk
NOKEEPINTS@Does not keep two-electron integrals on disk"""

scf_read_ints = """READINTS@Reads two-electron integrals from disk
NOREADINTS@Does not read two-electron integrals from disk"""

scf_keep_dens = """KEEPDENS@Keeps the density  DLPNO-STEOM-CCSDmatrix on disk
NOKEEPDENS@Does not keep the density matrix on disk"""

scf_use_cheap_ints = """CHEAPINTS@Uses the cheap integral feature in direct SCF calculations
NOCHEAPINTS@Turns the cheap integral feature off"""

scf_val_format = """FLOAT@Sets storage format for numbers to single precision (SCF, RI-MP2, CIS, CIS(D), MDCI)
DOUBLE@Sets storage format for numbers to double precision (default)
UCFLOAT@Uses float storage in matrix containers without data compression
CFLOAT@Uses float storage in matrix containers with data compression
UCDOUBLE@Uses double storage in matrix containers without data compression
CDOUBLE@Uses double storage in matrix containers with data compression"""

# Usually not necassary to do anything other then PMODEL
scf_initial_guess_strategies = """PATOM@Selects the polarized atoms guess
PMODEL@Selects the model potential guess
HUECKEL@Selects the extended Hückel guess
HCORE@Selects the one-electron matrix guess
MOREAD@Reads MOs from a previous calculation
AUTOSTART@Tries to start from the existing GBW file of the same name (only for single-point calculations)
NOAUTOSTART@Doesn't try to start from the existing GBW file"""

# Type of convergence for scf  
scf_convergence_type = """EasyConv@Assumes no convergence problems
NormalConv@Normal convergence criteria
SlowConv@Selects appropriate SCF convergence criteria for difficult cases (e.g., transition metal complexes)
VerySlowConv@Selects appropriate SCF convergence criteria for very difficult cases
ForceConv@Force convergence: do not continue with the calculation if SCF did not fully converge
IgnoreConv@Ignore convergence: continue with the calculation even if the SCF wavefunction is far from convergence"""

solvent_types = """CPCM@Invokes the conductor-like polarizable continuum model (CPCM) without specified solvent so infinity is assumed
CPCM(Acetonitrile)@Invokes the conductor-like polarizable continuum model (CPCM) with a Acetonitrile solvent.
CPCM(Acetone)@Invokes the conductor-like polarizable continuum model (CPCM) with a Acetone solvent.
CPCM(Ammonia)@Invokes the conductor-like polarizable continuum model (CPCM) with a Ammonia solvent.
CPCM(Water)@Invokes the conductor-like polarizable continuum model (CPCM) with a Water solvent.
CPCM(Benzene)@Invokes the conductor-like polarizable continuum model (CPCM) with a Benzene solvent.
CPCM(CCl4)@Invokes the conductor-like polarizable continuum model (CPCM) with a CCl4 solvent.
CPCM(CH2Cl2)@Invokes the conductor-like polarizable continuum model (CPCM) with a CH2Cl2 solvent.
CPCM(Chloroform)@Invokes the conductor-like polarizable continuum model (CPCM) with a Chloroform solvent.
CPCM(Cyclohexane)@Invokes the conductor-like polarizable continuum model (CPCM) with a Cyclohexane solvent.
CPCM(DMF)@Invokes the conductor-like polarizable continuum model (CPCM) with a DMF solvent.
CPCM(DMSO)@Invokes the conductor-like polarizable continuum model (CPCM) with a DMSO solvent.
CPCM(Ethanol)@Invokes the conductor-like polarizable continuum model (CPCM) with a Ethanol solvent.
CPCM(Hexane)@Invokes the conductor-like polarizable continuum model (CPCM) with a Hexane solvent.
CPCM(Methanol)@Invokes the conductor-like polarizable continuum model (CPCM) with a Methanol solvent.
CPCM(Octanol)@Invokes the conductor-like polarizable continuum model (CPCM) with a Octanol solvent.
CPCM(Pyridine)@Invokes the conductor-like polarizable continuum model (CPCM) with a Pyridine solvent.
CPCM(THF)@Invokes the conductor-like polarizable continuum model (CPCM) with a THF solvent.
CPCM(Toluene)@Invokes the conductor-like polarizable continuum model (CPCM) with a Toluene solvent."""

# How tightly to converge scf
scf_convergence_thesholds = """NORMALSCF@@Selects normal SCF convergence criteria
LOOSESCF@Selects loose SCF convergence criteria (less stringent than normal)
SLOPPYSCF@Selects sloppy SCF convergence criteria (even less stringent)
STRONGSCF@Selects strong SCF convergence criteria (more stringent than normal)
TIGHTSCF@Selects tight SCF convergence criteria (very stringent)
VERYTIGHTSCF@Selects very tight SCF convergence criteria (extremely stringent)
EXTREMESCF@Selects "extreme" SCF convergence (practically only usable for benchmarking)
SCFCONV6@Sets energy convergence check and sets energy tolerance (ETol) to 10^-6
SCFCONV7@Sets energy convergence check and sets energy tolerance (ETol) to 10^-7
SCFCONV8@Sets energy convergence check and sets energy tolerance (ETol) to 10^-8
SCFCONV9@Sets energy convergence check and sets energy tolerance (ETol) to 10^-9
SCFCONV10@Sets energy convergence check and sets energy tolerance (ETol) to 10^-10"""

scf_convergence_accelaration = """DIIS@Turns Direct Inversion in the Iterative Subspace (DIIS) on for SCF convergence acceleration
NODIIS@Turns DIIS off
KDIIS@Turns Kollmar's DIIS on for SCF convergence acceleration
TRAH@Turns Trust-Region Augmented Hessian (TRAH) on for SCF convergence
NOTRAH@Turns TRAH off
SOSCF@Turns Size-Optimization and Stabilization (SOSCF) on for SCF convergence
NOSOSCF@Turns SOSCF off
DAMP@Turns damping on for SCF convergence
NODAMP@Turns damping off
LSHIFT@Turns level shifting on for SCF convergence
NOLSHIFT@Turns level shifting off"""

# ------------------- REL input block keywords -------------------------# 
relativistic_hamiltonians = """DKH@Selects the scalar relativistic Douglas-Kroll-Hess Hamiltonian of 2nd order
DKH2@Selects the scalar relativistic Douglas-Kroll-Hess Hamiltonian of 2nd order
ZORA@Selects the scalar relativistic ZORA Hamiltonian
ZORA/RI@Selects the scalar relativistic ZORA Hamiltonian in RI approximation
IORA/RI@Selects the scalar relativistic IORA Hamiltonian in RI approximation
IORAmm/RI@Selects the scalar relativistic IORA mm (modified metric) Hamiltonian in RI approximation""" 

spin_orbit_type = """SOMF(1X)@Invokes the SOMF(1X) treatment of the spin-orbit coupling operator
RI-SOMF(1X)@Invokes the RI-SOMF(1X) treatment of the spin-orbit coupling operator (RI for Coulomb part)
VEFF-SOC@Invokes the VEFF-SOC treatment of the spin-orbit coupling operator
VEFF(-2X)-SOC@Invokes the VEFF(-2X)-SOC treatment of the spin-orbit coupling operator
AMFI@Invokes the AMFI treatment of the spin-orbit coupling operator
AMFI-A@Invokes the AMFI-A treatment of the spin-orbit coupling operator
ZEFF-SOC@Uses effective nuclear charges for the spin-orbit coupling operator"""

# ------------------- Geom input block keywords -------------------------# 
# How tightly to converge geometry calculation
geometry_convergence = """VERYTIGHTOPT@Selects very tight optimization convergence (specifies tolerances for energy and root-mean-square gradient)
TIGHTOPT@Selects tight optimization convergence (specifies tolerance for maximum gradient component)
NORMALOPT@Selects default optimization convergence (uses tolerances for root-mean-square displacement and maximum displacement)
LOOSEOPT@Selects loose optimization convergence (less stringent criteria than normal)
OptTS@Saddlepoint ("TS") optimization via relaxed scan"""

# ------------------- OUTPUT input block keywords -------------------------# 
# Defines output size
print_level = """NORMALPRINT@Selects the normal output
NoMOPrint@Dont print any of the MOs
MINIPRINT@Selects the minimal output
SMALLPRINT@Selects the small output
LARGEPRINT@Selects the large output"""

# Turns on/off certain prints
general_print_options = """PRINTMOS@Prints MO coefficients
NOPRINTMOS@Suppress printing of MO coefficients
PRINTBASIS@Print the basis set in input format
PRINTGAP@Prints the HOMO/LUMO gap in each SCF iteration. This may help to detect convergence problems
ALLPOP@Turns on all population analysis
NOPOP@Turns off all populaton analysis
MULLIKEN@Turns on the Mulliken analysis
NOMULLIKEN@Turns off the Mulliken analysis
LOEWDIN@Turns on the Loewdin analysis
NOLOEWDIN@Turns off the Loewdin analysis
MAYER@Turns on the Mayer analysis
NOMAYER@Turns off the Mayer analysis
NPA@Turns on interface for the NPA analysis using the GENNBO program
NBO@Turns on the interface for the NPA plus NBO analysis with the GENNBO program
NONPA@Turns off NPA analysis
NONBO@Turns of NBO analysis
REDUCEDPOP@Prints Loewdin reduced orb.pop per MO
NOREDUCEDPOP@Turns printing Loewdin reduced orb.pop per MO of
AIM@Produce a WFN file
XYZFILE@Produce an XYZ coordinate file
PDBFILE@Produce a PDB file"""

# -------------------------- COORDINATES keywords ---------------------------- #
coordinate_units ="""ANGS@Select angstrom units
BOHRS@Select input coordinates in atomic units"""


