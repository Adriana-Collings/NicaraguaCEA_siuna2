import numpy as np

np.random.seed(1)

max_age = 75.4


def lognormal(mean,sigma):
    while True:
        age = np.random.lognormal(mean=(mean), sigma=(sigma),size=None)
        if 0 <= age <= max_age:
            break
    return age


def weibull(a, lam):
    while True:
        age = np.random.weibull(a=a)
        age2 = age*lam
        if 0 <= age2 <= max_age:
            break
    return age2


def gamma(shape,rate):
    while True:
        age = np.random.gamma(shape=shape, scale=(1/rate), size=None)
        if 0 <= age <= max_age:
            break
    return age


Age_abscess = weibull(a=1.254899, lam=31.933350)
Age_appen = weibull(a=1.855648, lam=29.078622)
Age_finger_amp = weibull(a=1.515371, lam = 0.126173)
Age_burn = weibull(a=1.03563, lam = 19.95574)
Age_csection = lognormal(mean=3.1423006, sigma=0.2683582)
Age_diab = weibull(a=5.231805, lam=66.775223)
Age_disloc_seh = weibull(a=1.301287, lam = 24.647834)
Age_fx_csh = lognormal(mean=2.4666958, sigma=0.7814021)
Age_hand_fx = lognormal(mean=2.9376631, sigma=0.5508942)
Age_fx_ptf = weibull(a=2.255859, lam=29.093819)
Age_ulna_radius_fx = lognormal(mean=2.4949830, sigma=0.5504385)
Age_cerv_can = weibull(a=3.612262, lam=41.313701)
Age_mat_hem = lognormal(mean=3.1704848, sigma=0.4146018)
Age_hyst = weibull(a=3.986296, lam=57.071769)
Age_other_dis = lognormal(mean=3.0790135, sigma=0.5294391)
Age_obstrc_lab = lognormal(mean=3.1455889, sigma=0.2260368)
Age_cellu = gamma(shape=0.720004234, rate=0.03465062)
Age_hernia = gamma(shape=0.96697097, rate=29.1765679)
Age_warts = lognormal(mean=2.8019348, sigma=0.7240619)
Age_hypertrophy = weibull(a=9.052918, lam=69.899435)
Age_fx_face = lognormal(mean=3.1521040, sigma=0.4868875)
Age_fx_treated = weibull(a=1.385551, lam=15.350098)
Age_hydrocele = gamma(shape=0.62584557, rate= 0.01640809)
Age_neph = weibull(a=3.647194, lam=48.769464)
Age_tumor_others = weibull(a=1.294308, lam=26.613337)
Age_biliary = lognormal(mean=3.6188981, sigma=0.3459607)
Age_ovarian = lognormal(mean=3.1419571, sigma = 0.3132895)
Age_phimosis = lognormal (mean=1.860514, sigma=0.3491612)
Age_debrid = weibull(a=1.879095, lam=29.474877)
Age_disfig =lognormal(mean=3.5185995, sigma=0.4206365)
Age_open_wound=weibull(a=1.355499, lam=23.458189)
Age_infect = weibull(a=1.298622, lam=36.427719)
Age_breast = gamma (shape=31.76466, rate=1.22169)
Age_other_inj = weibull(a=1.358377, lam=24.925249)
Age_paralytic_il = weibull(a=1.494522, lam=41.658403)
Age_mat_abor = lognormal(mean=3.3212253, sigma=0.1274309)
Age_blad_can = weibull(a=2.188844, lam=50.878135)
Age_rect_fist = gamma(shape=3.6821937, rate=0.1375658)
Age_contra = weibull(a=6.145127, lam=34.857291)
Age_abdom_pelv = gamma(shape=7.127964, rate=0.225643)


#print("Abscess, weibull", Age_abscess)
#print("Appendicitis, gamma", Age_appen)
#print("Diabetes, gamma", Age_diab)
#print("Hand fx, Lognormal", Age_hand_fx)
#print("Ulna/Radius Fx, Lognormal", Age_ulna_radius_fx)
#print("Hernia, weibull", Age_hernia)
#print("Warts, lognormal",Age_warts)
#print("fx treated", Age_fx_treated)
#print("hydrocele", Age_hydrocele)
#print("tumor", Age_tumor_others)
#print("biliary", Age_biliary)
#print(Age_ovarian)
#print(Age_phimosis)
#print(Age_debrid)
#print(Age_disfig)
#print(Age_open_wound)
#print(Age_breast)
#print(Age_injury_tendon)
#print(Age_contra)