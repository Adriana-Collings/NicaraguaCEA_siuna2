import numpy as np

#change the maximum age!!!

def lognormal(mean,sigma):
    while True:
        age = np.random.lognormal(mean=(mean), sigma=(sigma),size=None)
        if 0 <= age <= 100:
            break
    return age

def weibull(a, lam):
    while True:
        age = np.random.weibull(a=a)
        age2 = age*lam
        if 0 <= age <= 100:
            break
    return age2

def gamma(shape,rate):
    while True:
        age = np.random.gamma(shape=shape, scale=(1/rate), size=None)
        if 0 <= age <= 100:
            break
    return age


#weibull, a = shape
# need to fix Weibull and Gamma
Age_abscess = weibull(a=1.556657, lam=34.006317)
Age_appen = gamma(shape=3.23739, rate=0.126173)
Age_finger_amp = weibull(a=1.515371, lam = 0.126173)
Age_burn = gamma(shape=0.92747608, rate = 0.0317023)
Age_csection = gamma(shape=12.5258328, rate = 0.5276385)
Age_diab = weibull(a=4.599732, lam = 61.886372)
Age_disloc_seh = weibull(a=1.301287, lam = 24.647834)
Age_fx_csh = lognormal(mean=2.4666958, sigma=0.7814021)
Age_hand_fx = lognormal(mean=3.0166143, sigma=0.5539478)
Age_fx_ptf = weibull(a=1.677329, lam=30.757564)
Age_ulna_radius_fx = lognormal(mean=2.3597845, sigma=0.7367141)
Age_cerv_can = gamma(shape=10.1563492, rate=0.2688349)
Age_mat_hem = lognormal(mean=3.1704848, sigma=0.4146018)
Age_hyst = weibull(a=3.445038, lam=53.670295)
Age_other_dis = lognormal(mean=3.0790135, sigma=0.5294391)
Age_obstrc_lab = lognormal(mean=3.1455889, sigma=0.2260368)
Age_cellu = gamma(shape=0.720004234, rate=0.03465062)
Age_hernia = weibull(a=1.043705, lam=27.520765)
Age_warts = lognormal(mean=2.8019348, sigma=0.7240619)
Age_hypertrophy = weibull(a=9.052918, lam=69.899435)
Age_fx_face = lognormal(mean=3.1521040, sigma=0.4868875)
Age_fx_treated = weibull(a=1.256805, lam=25.3880747)
Age_hydrocele = gamma(shape=0.61440163, rate=0.212111)
Age_neph = weibull(a=3.50575, lam=47.92219)
Age_tumor_others = weibull(a=1.556175, lam=28.081127)
Age_biliary = lognormal(mean=3.5894991, sigma=0.3491612)
Age_ovarian = lognormal(mean=3.047458, sigma=0.3500424)
Age_phimosis = lognormal (mean=1.860514, sigma=0.3491612)
Age_debrid = weibull(a=1.417915, lam=26.355934)
Age_disfig =lognormal(mean=3.5185995, sigma=0.4206365)
Age_open_wound=weibull(a=1.606495, lam=28.202406)
Age_infect = weibull(a=1.298622, lam=36.427719)
Age_breast = gamma (shape=31.76466, rate=1.22169)
Age_other_inj = weibull(a=1.441696, lam=27.036828)
Age_paralytic_il = weibull(a=1.494522, lam=41.658403)
Age_mat_abor = gamma(shape=17.2149750, rate=0.6221902)
Age_blad_can = weibull(a=2.188844, lam=50.878135)
Age_rect_fist = gamma(shape=3.6821937, rate=0.1375658)
Age_contra = weibull(a=5.749082, lam=34.418543)
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