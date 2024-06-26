
# ------------------- DENSITY FUNCTIONALS, always make use of the DFT method -------------------------# 
dft_local_and_gradient_corrected = """HFS@Selects the Hartree-Fock-Slater exchange-only functional
LDA@Selects the local density approximation (LDA) functional (defaults to VWN5 parameterization)
VWN@Selects the Vosko-Wilk-Nusair local density approximation (LDA) functional, version 5 parameterization
VWN3@Selects the Vosko-Wilk-Nusair local density approximation (LDA) functional, version 3 parameterization
PWLDA@Selects the Perdew-Wang parameterization of LDA functional
BP86@Selects the Becke '88 exchange functional with Perdew '86 correlation functional
BP@Selects the Becke '88 exchange functional with Perdew '86 correlation functional
BLYP@Selects the Becke '88 exchange functional with Lee-Yang-Parr correlation functional
OLYP@Selects the Handy's "optimal" exchange functional with Lee-Yang-Parr correlation functional
GLYP@Selects the Gill's '96 exchange functional with Lee-Yang-Parr correlation functional
XLYP@Selects the Xu and Goddard exchange functional with Lee-Yang-Parr correlation functional
PW91@Selects the Perdew-Wang '91 generalized gradient approximation (GGA) functional
mPWPW@Selects the modified Perdew-Wang exchange and Perdew-Wang correlation functional
mPWLYP@Selects the modified Perdew-Wang exchange and Lee-Yang-Parr correlation functional
PBE@Selects the Perdew-Burke-Erzerhof GGA functional
RPBE@Selects the "modified" PBE functional
REVPBE@Selects the "revised" PBE functional
RPW86PBE@Selects the PBE correlation functional with refitted Perdew '86 exchange functional
PWP@Selects the Perdew-Wang '91 exchange functional with Perdew '86 correlation functional"""

dft_hybrid_functionals = """B1LYP@The one-parameter hybrid functional with Becke '88 exchange and Lee-Yang-Parr correlation (25% HF exchange)
B3LYP@The popular B3LYP functional (20% HF exchange) as defined in the TurboMole program system
B3LYP/G@The popular B3LYP functional (20% HF exchange) as defined in the Gaussian program system
O3LYP@The Handy hybrid functional
PBEh-3c@A PBE hybrid density functional with small AO basis set and two corrections
X3LYP@The Xu and Goddard hybrid functional
B1P@The one-parameter hybrid version of BP86
B3P@The three-parameter hybrid version of BP86
B3PW@The three-parameter hybrid version of PW91
PW1PW@One-parameter hybrid version of PW91
mPW1PW@One-parameter hybrid version of mPWPW
mPW1LYP@One-parameter hybrid version of mPWLYP
PBE0@One-parameter hybrid version of PBE
REVPBE0@The "revised" PBE0 functional
REVPBE38@The "revised" PBE0 with 37.5% HF exchange
BHANDHLYP@Half-and-half hybrid functional by Becke"""

dft_meta_gga = """TPSS@The TPSS meta-GGA functional
M06L@The Minnesota M06-L meta-GGA functional
B97M-V@Head-Gordon's DF B97M-V with VV10 nonlocal correlation
B97M-D3BJ@Modified version of B97M-V with D3BJ correction by Najibi and Goerigk
B97M-D4@Modified version of B97M-V with DFT-D4 correction by Najibi and Goerigk
SCANfunc@Perdew's SCAN functional"""

dft_meta_gga_hybrid = """TPSSh@The hybrid version of TPSS (10% HF exchange)
TPSS0@A 25% exchange version of TPSSh that yields improved energetics
M06@The M06 hybrid meta-GGA (27% HF exchange)
M062X@The M06-2X version with 54% HF exchange
PW6B95@Hybrid functional by Truhlar"""

dft_range_seperated_hybrid = """wB97@Head-Gordon's fully variable density functional (DF)
wB97X@Head-Gordon's DF with minimal Fock exchange
wB97X-D3@Chai's refit including D3 dispersion correction in its zero-damping version
wB97X-D4@Modified version of wB97X-V with DFT-D4 dispersion correction by Najibi and Goerigk
wB97X-V@Head-Gordon's DF with VV10 nonlocal correlation
wB97X-D3BJ@Modified version of wB97X-V with D3BJ dispersion correction by Najibi and Goerigk
wB97M-V@Head-Gordon's DF with VV10 nonlocal correlation
wB97M-D3BJ@Modified version of wB97M-V with D3BJ dispersion correction by Najibi and Goerigk
wB97M-D4@Modified version of wB97M-V with DFT-D4 dispersion correction by Najibi and Goerigk
CAM-B3LYP@Handy's tau-omega functional
LC-BLYP@Hirao's original application of the LC-BLYP functional
LC-PBE@Range-separated PBE-based hybrid functional with 100% Fock exchange in the long-range regime"""

# You can add RI and DLPNO prefixes to these
dft_perturbatively_corrected_double_hybrid = """B2PLYP@Grimme's mixture of B88 exchange, LYP correlation, and MP2
mPW2PLYP@MPW exchange instead of B88 exchange in B2PLYP, which is supposed to improve weak interactions
B2GP-PLYP@Gershom Martin's "general purpose" reparameterization of B2PLYP
B2K-PLYP@Gershom Martin's "kinetic" reparameterization of B2PLYP
B2T-PLYP@Gershom Martin's "thermochemistry" reparameterization of B2PLYP
PWPB95@Goerigk and Grimme's mixture of modified PW91, modified B95, and SOS-MP2
PBE-QIDH@Adamo and co-workers' "quadratic integrand" double hybrid with PBE exchange and correlation
PBE0-DH@Adamo and co-workers' PBE-based double hybrid
DSD-BLYP@Gershom Martin's "general purpose" double-hybrid with B88 exchange, LYP correlation and SCS-MP2 mixing (without D3BJ correction)
DSD-PBEP86@Gershom Martin's "general purpose" double-hybrid with PBE exchange, P86 correlation and SCS-MP2 mixing (without D3BJ correction)
DSD-PBEB95@Gershom Martin's "general purpose" double-hybrid with PBE exchange, B95 correlation and SCS-MP2 mixing (without D3BJ correction)"""

dft_perturbatively_corrected_double_hybrid_with_ri = """RI-B2PLYP@Grimme's mixture of B88 exchange, LYP correlation, and MP2 with RI approximation
RI-mPW2PLYP@MPW exchange instead of B88 exchange in B2PLYP, which is supposed to improve weak interactions. Use RI approximation 
RI-B2GP-PLYP@Gershom Martin's "general purpose" reparameterization of B2PLYP. Use RI approximation 
RI-B2K-PLYP@Gershom Martin's "kinetic" reparameterization of B2PLYP. Use RI approximation 
RI-B2T-PLYP@Gershom Martin's "thermochemistry" reparameterization of B2PLYP. Use RI approximation 
RI-PWPB95@Goerigk and Grimme's mixture of modified PW91, modified B95, and SOS-MP2. Use RI approximation 
RI-PBE-QIDH@Adamo and co-workers' "quadratic integrand" double hybrid with PBE exchange and correlation. Use RI approximation 
RI-PBE0-DH@Adamo and co-workers' PBE-based double hybrid. Use RI approximation 
RI-DSD-BLYP@Gershom Martin's "general purpose" double-hybrid with B88 exchange, LYP correlation and SCS-MP2 mixing (without D3BJ correction). Use RI approximation 
RI-DSD-PBEP86@Gershom Martin's "general purpose" double-hybrid with PBE exchange, P86 correlation and SCS-MP2 mixing (without D3BJ correction). Use RI approximation 
RI-DSD-PBEB95@Gershom Martin's "general purpose" double-hybrid with PBE exchange, B95 correlation and SCS-MP2 mixing (without D3BJ correction). Use RI approximation"""

dft_perturbatively_corrected_double_hybrid_with_dlpno = """DLPNO-B2PLYP@Grimme's mixture of B88 exchange, LYP correlation, and MP2 with DLPNO approximation
DLPNO-mPW2PLYP@MPW exchange instead of B88 exchange in B2PLYP, which is supposed to improve weak interactions. Use DLPNO approximation 
DLPNO-B2GP-PLYP@Gershom Martin's "general purpose" reparameterization of B2PLYP. Use DLPNO approximation 
DLPNO-B2K-PLYP@Gershom Martin's "kinetic" reparameterization of B2PLYP. Use DLPNO approximation 
DLPNO-B2T-PLYP@Gershom Martin's "thermochemistry" reparameterization of B2PLYP. Use DLPNO approximation 
DLPNO-PWPB95@Goerigk and Grimme's mixture of modified PW91, modified B95, and SOS-MP2. Use DLPNO approximation 
DLPNO-PBE-QIDH@Adamo and co-workers' "quadratic integrand" double hybrid with PBE exchange and correlation. Use DLPNO approximation 
DLPNO-PBE0-DH@Adamo and co-workers' PBE-based double hybrid. Use DLPNO approximation 
DLPNO-DSD-BLYP@Gershom Martin's "general purpose" double-hybrid with B88 exchange, LYP correlation and SCS-MP2 mixing (without D3BJ correction). Use DLPNO approximation 
DLPNO-DSD-PBEP86@Gershom Martin's "general purpose" double-hybrid with PBE exchange, P86 correlation and SCS-MP2 mixing (without D3BJ correction). Use DLPNO approximation 
DLPNO-DSD-PBEB95@Gershom Martin's "general purpose" double-hybrid with PBE exchange, B95 correlation and SCS-MP2 mixing (without D3BJ correction). Use DLPNO approximation"""

# Once again can use RI and DLPNO
dft_range_seperated_double_hybrid = """wB2PLYP@Goerigk and Casanova-Páez's range-separated double-hybrid density functional (DHDF) with B2PLYP correlation, optimized for excitation energies.
wB2GP-PLYP@Goerigk and Casanova-Páez's range-separated DHDF with B2GP-PLYP correlation, optimized for excitation energies.
RSX-QIDH@Range-separated version of the PBE-QIDH double-hybrid by Adamo and co-workers.
RSX-0DH@Range-separated version of the PBE-0DH double-hybrid by Adamo and co-workers.
wB88PP86@Casanova-Páez and Goerigk's range-separated DHDF based on Becke88 exchange and P86 correlation, optimized for excitation energies.
wPBEPP86@Casanova-Páez and Goerigk's range-separated DHDF based on PBE exchange and P86 correlation, optimized for excitation energies."""

dft_range_seperated_double_hybrid_with_ri = """RI-wB2PLYP@Goerigk and Casanova-Páez's range-separated double-hybrid density functional (DHDF) with B2PLYP correlation, optimized for excitation energies. Use RI approximation 
RI-wB2GP-PLYP@Goerigk and Casanova-Páez's range-separated DHDF with B2GP-PLYP correlation, optimized for excitation energies. Use RI approximation 
RI-RSX-QIDH@Range-separated version of the PBE-QIDH double-hybrid by Adamo and co-workers. Use RI approximation 
RI-RSX-0DH@Range-separated version of the PBE-0DH double-hybrid by Adamo and co-workers. Use RI approximation 
RI-wB88PP86@Casanova-Páez and Goerigk's range-separated DHDF based on Becke88 exchange and P86 correlation, optimized for excitation energies. Use RI approximation 
RI-wPBEPP86@Casanova-Páez and Goerigk's range-separated DHDF based on PBE exchange and P86 correlation, optimized for excitation energies. Use RI approximation"""

dft_range_seperated_double_hybrid_with_dlpno = """DLPNO-wB2PLYP@Goerigk and Casanova-Páez's range-separated double-hybrid density functional (DHDF) with B2PLYP correlation, optimized for excitation energies. Use DLPNO approximation 
DLPNO-wB2GP-PLYP@Goerigk and Casanova-Páez's range-separated DHDF with B2GP-PLYP correlation, optimized for excitation energies. Use DLPNO approximation 
DLPNO-RSX-QIDH@Range-separated version of the PBE-QIDH double-hybrid by Adamo and co-workers. Use DLPNO approximation 
DLPNO-RSX-0DH@Range-separated version of the PBE-0DH double-hybrid by Adamo and co-workers. Use DLPNO approximation 
DLPNO-wB88PP86@Casanova-Páez and Goerigk's range-separated DHDF based on Becke88 exchange and P86 correlation, optimized for excitation energies. Use DLPNO approximation 
DLPNO-wPBEPP86@Casanova-Páez and Goerigk's range-separated DHDF based on PBE exchange and P86 correlation, optimized for excitation energies. Use DLPNO approximation"""


# Once again RI and DLPNO
dft_global_range_separated_double_hybrid_spin_component_spin_opposite_scaling = """wB97X-2@Chai and Head-Gordon's range-separated GGA-based double-hybrid density functional (DHDF) with spin-component scaling.
SCS/SOS-B2PLYP21@Spin-component scaled and spin-opposite scaled versions of B2PLYP optimized for excited states by Casanova-Páez and Goerigk (SCS/SOS applies to the CIS(D) component).
SCS-PBE-QIDH@Spin-component scaled version of PBE-QIDH optimized for excited states by Casanova-Páez and Goerigk (SCS applies to the CIS(D) component).
SOS-PBE-QIDH@Spin-opposite scaled version of PBE-QIDH optimized for excited states by Casanova-Páez and Goerigk (SOS applies to the CIS(D) component).
SCS-B2GP-PLYP21@Spin-component scaled version of B2GP-PLYP optimized for excited states by Casanova-Páez and Goerigk (SCS applies to the CIS(D) component).
SOS-B2GP-PLYP21@Spin-opposite scaled version of B2GP-PLYP optimized for excited states by Casanova-Páez and Goerigk (SOS applies to the CIS(D) component).
SCS/SOS-wB2PLYP@Spin-component scaled and spin-opposite scaled versions of B2PLYP optimized for excited states by Casanova-Páez and Goerigk (SCS/SOS applies to the CIS(D) component).
SCS-wB2GP-PLYP@Spin-component scaled version of B2GP-PLYP optimized for excited states by Casanova-Páez and Goerigk (SCS applies to the CIS(D) component).
SOS-wB2GP-PLYP@Spin-opposite scaled version of B2GP-PLYP optimized for excited states by Casanova-Páez and Goerigk (SOS applies to the CIS(D) component).
SCS-RSX-QIDH@Spin-component scaled version of RSX-QIDH optimized for excited states by Casanova-Páez and Goerigk (SCS applies to the CIS(D) component)
SOS-RSX-QIDH@Spin-opposite scaled version of RSX-QIDH optimized for excited states by Casanova-Páez and Goerigk (SOS applies to the CIS(D) component)
SCS-wB88PP86@Spin-component scaled version of B88PP86 optimized for excited states by Casanova-Páez and Goerigk (SCS applies to the CIS(D) component)"""

dft_global_range_separated_double_hybrid_spin_component_spin_opposite_scaling_with_ri = """RI-wB97X-2@Chai and Head-Gordon's range-separated GGA-based double-hybrid density functional (DHDF) with spin-component scaling. Use RI approximation 
RI-SCS/SOS-B2PLYP21@Spin-component scaled and spin-opposite scaled versions of B2PLYP optimized for excited states by Casanova-Páez and Goerigk (SCS/SOS applies to the CIS(D) component). Use RI approximation 
RI-SCS-PBE-QIDH@Spin-component scaled version of PBE-QIDH optimized for excited states by Casanova-Páez and Goerigk (SCS applies to the CIS(D) component). Use RI approximation 
RI-SOS-PBE-QIDH@Spin-opposite scaled version of PBE-QIDH optimized for excited states by Casanova-Páez and Goerigk (SOS applies to the CIS(D) component). Use RI approximation 
RI-SCS-B2GP-PLYP21@Spin-component scaled version of B2GP-PLYP optimized for excited states by Casanova-Páez and Goerigk (SCS applies to the CIS(D) component). Use RI approximation 
RI-SOS-B2GP-PLYP21@Spin-opposite scaled version of B2GP-PLYP optimized for excited states by Casanova-Páez and Goerigk (SOS applies to the CIS(D) component). Use RI approximation 
RI-SCS/SOS-wB2PLYP@Spin-component scaled and spin-opposite scaled versions of B2PLYP optimized for excited states by Casanova-Páez and Goerigk (SCS/SOS applies to the CIS(D) component). Use RI approximation 
RI-SCS-wB2GP-PLYP@Spin-component scaled version of B2GP-PLYP optimized for excited states by Casanova-Páez and Goerigk (SCS applies to the CIS(D) component). Use RI approximation 
RI-SOS-wB2GP-PLYP@Spin-opposite scaled version of B2GP-PLYP optimized for excited states by Casanova-Páez and Goerigk (SOS applies to the CIS(D) component). Use RI approximation 
RI-SCS-RSX-QIDH@Spin-component scaled version of RSX-QIDH optimized for excited states by Casanova-Páez and Goerigk (SCS applies to the CIS(D) component). Use RI approximation 
RI-SOS-RSX-QIDH@Spin-opposite scaled version of RSX-QIDH optimized for excited states by Casanova-Páez and Goerigk (SOS applies to the CIS(D) component). Use RI approximation 
RI-SCS-wB88PP86@Spin-component scaled version of B88PP86 optimized for excited states by Casanova-Páez and Goerigk (SCS applies to the CIS(D) component). Use RI approximation """

dft_global_range_separated_double_hybrid_spin_component_spin_opposite_scaling_with_dlpno = """DLPNO-wB97X-2@Chai and Head-Gordon's range-separated GGA-based double-hybrid density functional (DHDF) with spin-component scaling. Use RI approximation 
DLPNO-SCS/SOS-B2PLYP21@Spin-component scaled and spin-opposite scaled versions of B2PLYP optimized for excited states by Casanova-Páez and Goerigk (SCS/SOS applies to the CIS(D) component). Use RI approximation 
DLPNO-SCS-PBE-QIDH@Spin-component scaled version of PBE-QIDH optimized for excited states by Casanova-Páez and Goerigk (SCS applies to the CIS(D) component). Use RI approximation 
DLPNO-SOS-PBE-QIDH@Spin-opposite scaled version of PBE-QIDH optimized for excited states by Casanova-Páez and Goerigk (SOS applies to the CIS(D) component). Use RI approximation 
DLPNO-SCS-B2GP-PLYP21@Spin-component scaled version of B2GP-PLYP optimized for excited states by Casanova-Páez and Goerigk (SCS applies to the CIS(D) component). Use RI approximation 
DLPNO-SOS-B2GP-PLYP21@Spin-opposite scaled version of B2GP-PLYP optimized for excited states by Casanova-Páez and Goerigk (SOS applies to the CIS(D) component). Use RI approximation 
DLPNO-SCS/SOS-wB2PLYP@Spin-component scaled and spin-opposite scaled versions of B2PLYP optimized for excited states by Casanova-Páez and Goerigk (SCS/SOS applies to the CIS(D) component). Use RI approximation 
DLPNO-SCS-wB2GP-PLYP@Spin-component scaled version of B2GP-PLYP optimized for excited states by Casanova-Páez and Goerigk (SCS applies to the CIS(D) component). Use RI approximation 
DLPNO-SOS-wB2GP-PLYP@Spin-opposite scaled version of B2GP-PLYP optimized for excited states by Casanova-Páez and Goerigk (SOS applies to the CIS(D) component). Use RI approximation 
DLPNO-SCS-RSX-QIDH@Spin-component scaled version of RSX-QIDH optimized for excited states by Casanova-Páez and Goerigk (SCS applies to the CIS(D) component). Use RI approximation 
DLPNO-SOS-RSX-QIDH@Spin-opposite scaled version of RSX-QIDH optimized for excited states by Casanova-Páez and Goerigk (SOS applies to the CIS(D) component). Use RI approximation 
DLPNO-SCS-wB88PP86@Spin-component scaled version of B88PP86 optimized for excited states by Casanova-Páez and Goerigk (SCS applies to the CIS(D) component). Use RI approximation """

dft_dispersion_correction = """D4@Density dependent atom-pairwise dispersion correction with Becke-Johnson damping and ATM
D3BJ@Atom-pairwise dispersion correction to the DFT energy with Becke-Johnson damping
D3@Atom-pairwise dispersion correction to the DFT energy with Becke-Johnson damping
D3ZERO@Atom-pairwise dispersion correction with zero damping
D2@Empirical dispersion correction from 2006 (not recommended)"""

dft_non_local_correlation = """NL@Does a post-SCF correction on the energy only
SCNL@Fully self-consistent approach, adding the VV10 correlation to the KS Hamiltonian"""

